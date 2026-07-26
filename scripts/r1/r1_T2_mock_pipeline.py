#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T2 end-to-end mock validation pipeline (Line B).

Validates the pre-registered T2 protocol on synthetic fields:
  1) Gaussian matter field δ with correlation scale ~ R_nl (σ_δ=1)
  2) Nonlinear mask m = 1{δ > δ_c}
  3) Inject residual r correlated with matter/mask at that scale
  4) Recover correlation length r_e of residual auto
  5) Measure residual×mask cross vs random-mask null
  6) Report PASS/FAIL against pre-registered ALLOWED band

This does NOT use real DESI maps. It proves the *pipeline* recovers the
injected scale when the sandwich hypothesis is true in the mock.

See papers/r1_kernel/r1-T2-preregistration.md
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
_SCRIPTS = ROOT / "scripts"
for _d in (_SCRIPTS, _SCRIPTS / "core", _SCRIPTS / "r1", _SCRIPTS / "closed", _SCRIPTS / "side"):
    if _d.is_dir() and str(_d) not in sys.path:
        sys.path.insert(0, str(_d))
OUT = ROOT / "results" / "r1_T2_mock"
OUT.mkdir(parents=True, exist_ok=True)

from lib_verified import hubble_radius_mpc, sigma_from_count  # noqa: E402
from r1_sigma_R_full import H as H_FID, SIGMA8, find_R_nl, make_Pk_unnorm, normalize_A  # noqa: E402

RNG = np.random.default_rng(20260726)


def make_gaussian_field_2d(
    n: int,
    box_mpc: float,
    corr_length_mpc: float,
    sigma_target: float = 1.0,
) -> tuple[np.ndarray, float]:
    """
    2D Gaussian random field with approx correlation length R via
    P(k) ∝ exp(−(k R)^2), normalized to rms = sigma_target.
    Returns (field, pixel_size_mpc).
    """
    dx = box_mpc / n
    # white noise in Fourier space
    white = RNG.normal(0.0, 1.0, size=(n, n)) + 1j * RNG.normal(0.0, 1.0, size=(n, n))
    white = white / math.sqrt(2.0)
    # wave numbers
    kx = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)
    ky = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)
    KX, KY = np.meshgrid(kx, ky, indexing="ij")
    k = np.sqrt(KX**2 + KY**2)
    # Gaussian power → corr length ~ R
    Pk = np.exp(-((k * corr_length_mpc) ** 2))
    Pk[0, 0] = 0.0  # zero mean mode
    field_k = white * np.sqrt(Pk)
    field = np.fft.ifft2(field_k).real
    field = field - field.mean()
    rms = field.std()
    if rms > 0:
        field = field * (sigma_target / rms)
    return field.astype(np.float64), dx


def radial_correlation(
    field: np.ndarray,
    dx: float,
    r_max_mpc: float,
    n_bins: int = 24,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Isotropic 2-point correlation via FFT: ξ(r) from power spectrum.
    Returns (r_centers, xi).
    """
    n = field.shape[0]
    f = field - field.mean()
    fk = np.fft.fft2(f)
    power = (fk * np.conj(fk)).real / (n * n)
    xi_map = np.fft.ifft2(power).real
    # shift so zero lag at center
    xi_map = np.fft.fftshift(xi_map)
    # radial average
    cy = cx = n // 2
    yy, xx = np.indices((n, n))
    rr = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) * dx
    r_edges = np.linspace(0.0, r_max_mpc, n_bins + 1)
    r_c = 0.5 * (r_edges[:-1] + r_edges[1:])
    xi = np.zeros(n_bins)
    for i in range(n_bins):
        m = (rr >= r_edges[i]) & (rr < r_edges[i + 1])
        if np.any(m):
            xi[i] = float(xi_map[m].mean())
        else:
            xi[i] = np.nan
    # normalize so xi(0+) ~ 1 if using normalized field auto
    # actually xi_map[center] = var
    return r_c, xi


def corr_length_1e(r: np.ndarray, xi: np.ndarray) -> float:
    """Smallest r>0 with xi(r)/xi_max <= 1/e."""
    # use first bin as xi0 proxy if r~0 not exact
    valid = np.isfinite(xi) & (r > 0)
    if not np.any(valid):
        return float("nan")
    xi0 = float(np.nanmax(xi[valid]))
    if xi0 <= 0:
        # try absolute max including r~0
        xi0 = float(np.nanmax(xi))
    if xi0 <= 0:
        return float("nan")
    thr = xi0 / math.e
    prev_r, prev_x = 0.0, xi0
    for ri, xi_i in zip(r[valid], xi[valid]):
        if xi_i <= thr:
            if prev_x == xi_i:
                return float(ri)
            t = (prev_x - thr) / (prev_x - xi_i + 1e-30)
            return float(prev_r + t * (ri - prev_r))
        prev_r, prev_x = float(ri), float(xi_i)
    return float(r[valid][-1])


def cross_zero_lag(a: np.ndarray, b: np.ndarray) -> float:
    """Normalized cross correlation at zero lag: <ab> / (σa σb)."""
    a = a - a.mean()
    b = b - b.mean()
    sa, sb = a.std(), b.std()
    if sa <= 0 or sb <= 0:
        return 0.0
    return float(np.mean(a * b) / (sa * sb))


def random_mask_same_f(mask: np.ndarray) -> np.ndarray:
    """Permute mask pixels → same volume fraction, no spatial structure."""
    flat = mask.ravel().copy()
    RNG.shuffle(flat)
    return flat.reshape(mask.shape)


def run_mock(
    R_nl: float,
    sigma_free: float,
    n: int = 256,
    box_factor: float = 40.0,
    delta_c: float = 1.0,
    noise_frac: float = 0.5,
    g_inj: float = 1.0,
) -> dict:
    """
    One end-to-end mock realization.

    Residual injection (local coupling sandwich form):
      r = g_inj * sigma_free * δ + noise
    so residual tracks matter on the same correlation scale.
    """
    box = box_factor * R_nl
    delta, dx = make_gaussian_field_2d(n, box, corr_length_mpc=R_nl, sigma_target=1.0)
    mask = (delta > delta_c).astype(np.float64)
    f_vol = float(mask.mean())

    # inject residual
    signal = g_inj * sigma_free * delta
    noise_rms = noise_frac * g_inj * sigma_free
    noise = RNG.normal(0.0, noise_rms, size=delta.shape)
    residual = signal + noise

    # auto corr length of residual
    r_max = min(5.0 * R_nl, 0.45 * box)
    r_bins, xi_r = radial_correlation(residual, dx, r_max_mpc=r_max, n_bins=28)
    r_e = corr_length_1e(r_bins, xi_r)

    # also matter corr length as reference
    _, xi_d = radial_correlation(delta, dx, r_max_mpc=r_max, n_bins=28)
    r_e_delta = corr_length_1e(r_bins, xi_d)

    # cross residual × mask (and vs random)
    # use float mask
    x_rm = cross_zero_lag(residual, mask)
    mask_rand = random_mask_same_f(mask)
    x_rrand = cross_zero_lag(residual, mask_rand)
    x_rd = cross_zero_lag(residual, delta)

    band_lo, band_hi = 0.5 * R_nl, 3.0 * R_nl
    in_band = bool(np.isfinite(r_e) and band_lo <= r_e <= band_hi)
    cross_positive = bool(x_rm > 0.05)  # clear positive (mock has high S/N)
    null_ok = bool(abs(x_rrand) < abs(x_rm) * 0.5 or abs(x_rrand) < 0.05)

    # multi-realization would give significance; single mock: structure checks
    pass_T2_structure = in_band and cross_positive and null_ok

    return {
        "R_nl": R_nl,
        "box_mpc": box,
        "n_pix": n,
        "dx_mpc": dx,
        "delta_c": delta_c,
        "f_vol_mask": f_vol,
        "g_inj": g_inj,
        "sigma_free": sigma_free,
        "noise_frac": noise_frac,
        "r_e_residual_mpc": r_e,
        "r_e_delta_mpc": r_e_delta,
        "r_e_over_Rnl": r_e / R_nl if R_nl else float("nan"),
        "band_lo": band_lo,
        "band_hi": band_hi,
        "in_ALLOWED_band": in_band,
        "cross_residual_mask": x_rm,
        "cross_residual_random_mask": x_rrand,
        "cross_residual_delta": x_rd,
        "cross_positive": cross_positive,
        "null_random_weaker": null_ok,
        "PASS_T2_structure_mock": pass_T2_structure,
        "xi_r_curve": [{"r": float(a), "xi": float(b)} for a, b in zip(r_bins, xi_r) if np.isfinite(b)],
    }


def main() -> None:
    print("=== T2 end-to-end mock pipeline ===")
    print("Validates protocol recovery when sandwich injection is true.\n")

    Pk = make_Pk_unnorm()
    A = normalize_A(Pk, SIGMA8)
    R_nl = find_R_nl(Pk, A, 1.0) / H_FID
    sigma_free = sigma_from_count(R_nl, hubble_radius_mpc(), 3)

    print(f"  R_nl = {R_nl:.4f} Mpc  sigma_free = {sigma_free:.6e}")

    # baseline mock
    base = run_mock(R_nl, sigma_free, g_inj=1.0, noise_frac=0.5)
    print(f"  [baseline g=1 noise=0.5]")
    print(f"    r_e(residual) = {base['r_e_residual_mpc']:.3f} Mpc "
          f"= {base['r_e_over_Rnl']:.3f} R_nl  in_band={base['in_ALLOWED_band']}")
    print(f"    r_e(delta)    = {base['r_e_delta_mpc']:.3f} Mpc")
    print(f"    cross r×mask  = {base['cross_residual_mask']:+.4f}")
    print(f"    cross r×rand  = {base['cross_residual_random_mask']:+.4f}")
    print(f"    cross r×delta = {base['cross_residual_delta']:+.4f}")
    print(f"    PASS_T2_structure = {base['PASS_T2_structure_mock']}")

    # ensemble of realizations for robustness
    n_real = 12
    passes = 0
    r_es = []
    crosses = []
    for i in range(n_real):
        m = run_mock(R_nl, sigma_free, g_inj=1.0, noise_frac=0.5)
        r_es.append(m["r_e_residual_mpc"])
        crosses.append(m["cross_residual_mask"])
        if m["PASS_T2_structure_mock"]:
            passes += 1
    r_es = np.array(r_es)
    crosses = np.array(crosses)

    print(f"\n  Ensemble n={n_real}:")
    print(f"    r_e mean±std = {r_es.mean():.3f} ± {r_es.std():.3f} Mpc")
    print(f"    cross r×mask mean±std = {crosses.mean():+.4f} ± {crosses.std():.4f}")
    print(f"    PASS fraction = {passes}/{n_real} = {passes/n_real:.2f}")

    # negative control: residual = pure white noise (no matter coupling)
    box = 40.0 * R_nl
    n = 256
    delta, dx = make_gaussian_field_2d(n, box, R_nl, 1.0)
    mask = (delta > 1.0).astype(np.float64)
    white = RNG.normal(0.0, sigma_free, size=delta.shape)
    r_max = min(5.0 * R_nl, 0.45 * box)
    r_bins, xi_w = radial_correlation(white, dx, r_max, 28)
    r_e_white = corr_length_1e(r_bins, xi_w)
    x_wm = cross_zero_lag(white, mask)
    print(f"\n  [negative control: white residual]")
    print(f"    r_e(white) ≈ {r_e_white:.3f} Mpc  (expect tiny / unresolved)")
    print(f"    cross white×mask = {x_wm:+.4f}  (expect ~0)")

    # wrong-scale injection: residual correlated on 100 Mpc
    delta_big, dx2 = make_gaussian_field_2d(n, box, corr_length_mpc=100.0, sigma_target=1.0)
    r_wrong = 1.0 * sigma_free * delta_big
    r_bins2, xi_wrong = radial_correlation(r_wrong, dx2, min(200.0, 0.45 * box), 28)
    r_e_wrong = corr_length_1e(r_bins2, xi_wrong)
    print(f"\n  [wrong-scale injection corr=100 Mpc]")
    print(f"    r_e ≈ {r_e_wrong:.3f} Mpc  in_ALLOWED={0.5*R_nl <= r_e_wrong <= 3*R_nl}")

    ensemble_pass_rate = passes / n_real
    pipeline_ok = (
        ensemble_pass_rate >= 0.7
        and abs(x_wm) < 0.15
        and not (0.5 * R_nl <= r_e_wrong <= 3 * R_nl)
    )

    out = {
        "R_nl_Mpc": R_nl,
        "sigma_free": sigma_free,
        "baseline": base,
        "ensemble": {
            "n_real": n_real,
            "r_e_mean": float(r_es.mean()),
            "r_e_std": float(r_es.std()),
            "cross_rm_mean": float(crosses.mean()),
            "cross_rm_std": float(crosses.std()),
            "pass_fraction": ensemble_pass_rate,
        },
        "negative_control_white": {
            "r_e_mpc": r_e_white,
            "cross_mask": x_wm,
        },
        "wrong_scale_100Mpc": {
            "r_e_mpc": r_e_wrong,
            "in_ALLOWED_band": bool(0.5 * R_nl <= r_e_wrong <= 3 * R_nl),
        },
        "pipeline_validation_PASS": pipeline_ok,
        "interpretation": (
            "When residual is injected as g*σ_free*δ with corr~R_nl, pipeline recovers "
            "r_e in ALLOWED band and positive cross with mask; white residual does not; "
            "100 Mpc injection falls outside ALLOWED band. Protocol is operational."
        ),
    }
    (OUT / "T2_mock_validation.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    txt = f"""T2 END-TO-END MOCK VALIDATION
==============================
R_nl = {R_nl:.4f} Mpc  sigma_free = {sigma_free:.6e}
ALLOWED band = [{0.5*R_nl:.2f}, {3*R_nl:.2f}] Mpc

BASELINE (g=1, noise_frac=0.5):
  r_e(residual) = {base['r_e_residual_mpc']:.3f} Mpc ({base['r_e_over_Rnl']:.2f} R_nl)
  in_band = {base['in_ALLOWED_band']}
  cross r×mask = {base['cross_residual_mask']:+.4f}
  cross r×rand = {base['cross_residual_random_mask']:+.4f}
  PASS_T2_structure = {base['PASS_T2_structure_mock']}

ENSEMBLE (n={n_real}):
  r_e = {r_es.mean():.3f} ± {r_es.std():.3f} Mpc
  cross r×mask = {crosses.mean():+.4f} ± {crosses.std():.4f}
  pass fraction = {ensemble_pass_rate:.2f}

CONTROLS:
  white residual: r_e≈{r_e_white:.3f}  cross_mask={x_wm:+.4f}
  100 Mpc inject: r_e≈{r_e_wrong:.3f}  in_ALLOWED={0.5*R_nl <= r_e_wrong <= 3*R_nl}

PIPELINE VALIDATION: {'PASS' if pipeline_ok else 'FAIL'}

See papers/r1_kernel/r1-T2-preregistration.md
"""
    (OUT / "T2_mock_validation.txt").write_text(txt, encoding="utf-8")
    print()
    print(txt)
    print(f"Wrote {OUT}")
    if not pipeline_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
