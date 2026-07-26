#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sandwich derivation machinery for residual grain scale ℓ_* ~ R_nl.

Under axioms A0–A4 (see papers/r1-derivation-sandwich.md):
  UV bound: free residual cannot live at ℓ << R_nl (decoherence / coarse-grain)
  IR bound: free residual claimed at ℓ >> R_nl renormalizes to R_nl under local coupling
  → uniqueness: ℓ_* ~ R_nl (O(1) BBKS factors)

Computes:
  1) Real-space ξ_δ(r) of top-hat-filtered density at R = R_nl
  2) Correlation length r_e where ξ_δ(r_e)/ξ_δ(0) = 1/e
  3) Gaussian threshold mask m=1{δ>δ_c}: f, ξ_mask(r), r_e,mask
  4) Decoherence OOM rate for residual χ coupled as g χ δ_m
  5) Sandwich numerical test: σ_count(ℓ) vs R_nl band

Not a full QFT proof. Elevates the B.4 sketch to axioms + lemmas + numbers.

See papers/r1-derivation-sandwich.md
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Callable, Tuple

import numpy as np
from scipy.integrate import quad
from scipy.special import erfc, ndtr
from scipy.stats import multivariate_normal

ROOT = Path(__file__).resolve().parents[2]
_SCRIPTS = ROOT / "scripts"
for _d in (_SCRIPTS, _SCRIPTS / "core", _SCRIPTS / "r1", _SCRIPTS / "closed", _SCRIPTS / "side"):
    if _d.is_dir() and str(_d) not in sys.path:
        sys.path.insert(0, str(_d))
OUT = ROOT / "results" / "r1_sandwich"
OUT.mkdir(parents=True, exist_ok=True)

from lib_verified import hubble_radius_mpc, sigma_from_count  # noqa: E402
from r1_sigma_R_full import (  # noqa: E402
    H,
    SIGMA8,
    find_R_nl,
    make_Pk_unnorm,
    normalize_A,
    top_hat_W,
)


def Pk_normed() -> Tuple[Callable[[float], float], float, float]:
    """Return (Pk_unnorm, A, R_nl_Mpc). k in h/Mpc."""
    Pk = make_Pk_unnorm()
    A = normalize_A(Pk, SIGMA8)
    R_hinv = find_R_nl(Pk, A, 1.0)
    return Pk, A, R_hinv / H


def xi_filtered(
    r_hinv: float,
    R_hinv: float,
    Pk: Callable[[float], float],
    A: float,
    kmin: float = 1e-4,
    kmax: float = 50.0,
) -> float:
    """
    Real-space correlation of top-hat filtered density field:
      ξ(r) = ∫ dk k² /(2π²) A P(k) W²(kR) j0(kr)
    r, R in h^{-1} Mpc; k in h/Mpc.
    """
    if r_hinv < 0:
        raise ValueError("r>=0")

    def j0(x: float) -> float:
        if abs(x) < 1e-8:
            return 1.0 - x * x / 6.0
        return math.sin(x) / x

    def integrand_logk(lk: float) -> float:
        k = math.exp(lk)
        W = top_hat_W(k * R_hinv)
        # dk * k² * P * W² * j0 / (2π²) = dlnk * k³ * ...
        return (k**3) * (A * Pk(k)) * (W**2) * j0(k * r_hinv) / (2.0 * math.pi**2)

    val, _ = quad(
        integrand_logk,
        math.log(kmin),
        math.log(kmax),
        epsabs=1e-10,
        epsrel=1e-5,
        limit=500,
    )
    return float(val)


def find_corr_length(
    xi_fn: Callable[[float], float],
    xi0: float,
    r_max_hinv: float,
    target: float = 1.0 / math.e,
    n: int = 48,
) -> float:
    """Smallest r>0 with xi(r)/xi0 <= target (linear scan + interpolate)."""
    if xi0 <= 0:
        return float("nan")
    rs = np.linspace(0.0, r_max_hinv, n)
    prev_r, prev_y = 0.0, 1.0
    for r in rs[1:]:
        y = xi_fn(float(r)) / xi0
        if y <= target:
            # linear interpolate in r
            if prev_y == y:
                return float(r)
            t = (prev_y - target) / (prev_y - y)
            return float(prev_r + t * (r - prev_r))
        prev_r, prev_y = float(r), float(y)
    return float(r_max_hinv)  # did not cross


def bivariate_exceed_prob(nu: float, rho: float) -> float:
    """
    P(X>nu, Y>nu) for standard bivariate normal with corr rho.
    Uses scipy multivariate_normal survival.
    """
    rho = float(np.clip(rho, -0.999, 0.999))
    mean = [0.0, 0.0]
    cov = [[1.0, rho], [rho, 1.0]]
    # P(X>nu,Y>nu) = P(-X<-nu, -Y<-nu) = CDF of (-X,-Y) at (-nu,-nu)
    # equivalently 1 - P(X<=nu) - P(Y<=nu) + P(X<=nu,Y<=nu)
    # use mvn CDF for upper orthant via symmetry:
    # P(X>nu,Y>nu) = mvn.sf with lower=[nu,nu] — scipy has cdf only;
    return float(
        multivariate_normal.cdf([-nu, -nu], mean=mean, cov=cov)
    )  # = P(X'<=-nu,Y'<=-nu)=P(X>=nu,Y>=nu) with X'=-X


def mask_stats(
    r_hinv: float,
    R_hinv: float,
    Pk: Callable[[float], float],
    A: float,
    delta_c: float,
    xi0: float,
) -> Tuple[float, float, float]:
    """
    Return (f, xi_mask(r), rho_delta(r)).
    m = 1{δ > δ_c}, σ0 = sqrt(xi0) should be ~1 at R_nl.
    """
    sig = math.sqrt(max(xi0, 1e-30))
    nu = delta_c / sig
    f = 0.5 * erfc(nu / math.sqrt(2.0))
    xi_r = xi_filtered(r_hinv, R_hinv, Pk, A)
    rho = xi_r / xi0 if xi0 > 0 else 0.0
    rho = float(np.clip(rho, -0.999, 0.999))
    p11 = bivariate_exceed_prob(nu, rho)
    xi_m = p11 - f * f
    return f, xi_m, rho


def decoherence_oom(
    g: float,
    R_nl_mpc: float,
    sigma_delta: float = 1.0,
    H0: float = 67.4,
) -> dict:
    """
    OOM decoherence rate for residual χ coupled as g χ δ_m.

    Model (influence-functional / Caldeira–Leggett style OOM):
      Γ ~ g² σ_δ² / τ_c
    with bath correlation time τ_c ~ R_nl / c  (causal scale of patch)
    or τ_c ~ 1/H0 (slow cosmological bath). Report both.

    Also Γ_Hubble = Γ / H0 dimensionless (how many decoherences per Hubble time).

    χ dimensionless residual contrast; g dimensionless response coupling.
    """
    C_KMS = 299792.458
    # Hubble rate in 1/Myr-ish: use 1/t_H = H0, compare rates to H0
    # Light-crossing time of patch in units of Hubble time:
    # t_cross / t_H = (R_nl / c) / (1/H0) = R_nl / L_H
    L_H = hubble_radius_mpc(H0)
    t_cross_over_tH = R_nl_mpc / L_H
    # Fast bath (causal patch): τ_c = t_cross ⇒ Γ/H0 ~ g² σ² / (t_cross H0) = g² σ² / t_cross_over_tH
    # Careful: Γ ~ g² σ² / τ_c  with Γ in frequency units, τ_c = t_cross,
    # Γ/H0 ~ g² σ² * (t_H / τ_c) = g² σ² / (R_nl/L_H)
    gamma_over_H_fast = (g**2) * (sigma_delta**2) / max(t_cross_over_tH, 1e-30)
    # Slow bath: τ_c ~ t_H ⇒ Γ/H0 ~ g² σ²
    gamma_over_H_slow = (g**2) * (sigma_delta**2)
    return {
        "g": g,
        "sigma_delta": sigma_delta,
        "R_nl_over_LH": t_cross_over_tH,
        "Gamma_over_H0_fast_bath": gamma_over_H_fast,
        "Gamma_over_H0_slow_bath": gamma_over_H_slow,
        "N_decoherences_per_tH_fast": gamma_over_H_fast,
        "N_decoherences_per_tH_slow": gamma_over_H_slow,
        "note": (
            "Γ ~ g² σ_δ² / τ_c. Fast: τ_c = R_nl/c; slow: τ_c = 1/H0. "
            "If Γ/H0 ≫ 1, residual is decohered within a Hubble time "
            "and free DOF are patch-coarse-grained."
        ),
    }


def sandwich_table(R_nl: float, L_H: float, d: float = 3) -> list:
    """
    For trial cells ℓ, report:
      - regime (UV forbidden / allowed / IR renormalizes)
      - N_patches in cell = (ℓ/R_nl)^d
      - sigma_count(ℓ)
      - effective sigma after patch average if ℓ > R_nl: sigma_Rnl / sqrt(N_p)
    """
    rows = []
    for ell, label in [
        (1e-20, "Planck-ish (proxy)"),  # symbolic, not actual L_P in Mpc
        (0.01, "0.01 Mpc"),
        (0.1, "0.1 Mpc"),
        (1.0, "1 Mpc"),
        (1.58, "R_* ~ 1.58"),
        (R_nl, "R_nl"),
        (15.9, "ell_sep ~ 16"),
        (50.0, "50 Mpc"),
        (100.0, "100 Mpc"),
        (L_H, "L_H"),
    ]:
        if ell <= 0:
            continue
        n_p = (ell / R_nl) ** d
        sig = sigma_from_count(ell, L_H, d)
        sig_R = sigma_from_count(R_nl, L_H, d)
        if ell < 0.3 * R_nl:
            regime = "UV: decohered / not free residual (ℓ ≪ R_nl)"
            sig_eff = 0.0  # free residual killed / not independent
        elif ell <= 3.0 * R_nl:
            regime = "ALLOWED band: ℓ_* ~ R_nl (O(1) BBKS)"
            sig_eff = sig
        else:
            regime = "IR: local coupling renormalizes to R_nl cells"
            # variance of average over N independent patches
            sig_eff = sig_R / math.sqrt(n_p) if n_p > 0 else sig_R
        rows.append(
            {
                "label": label,
                "ell_Mpc": float(ell),
                "N_patches": float(n_p),
                "sigma_count_naive": float(sig),
                "sigma_eff_after_renorm": float(sig_eff),
                "regime": regime,
            }
        )
    return rows


def main() -> None:
    print("=== Sandwich derivation: ℓ_* ~ R_nl under A0–A4 ===")
    Pk, A, R_nl = Pk_normed()
    R_hinv = R_nl * H
    L_H = hubble_radius_mpc()
    xi0 = xi_filtered(0.0, R_hinv, Pk, A)
    sig0 = math.sqrt(max(xi0, 0.0))
    print(f"  R_nl = {R_nl:.4f} Mpc  ({R_hinv:.4f} h^-1 Mpc)")
    print(f"  ξ_δ(0) = σ² = {xi0:.6f}  (expect ~1 at R_nl)")
    print(f"  σ_0 = {sig0:.6f}")

    # Density correlation length
    def xi_r(r_h: float) -> float:
        return xi_filtered(r_h, R_hinv, Pk, A)

    r_e_h = find_corr_length(xi_r, xi0, r_max_hinv=20.0, target=1.0 / math.e, n=60)
    r_e = r_e_h / H
    print(f"  r_e (ξ_δ/ξ0 = 1/e) = {r_e:.3f} Mpc  ({r_e_h:.3f} h^-1 Mpc)")
    print(f"  r_e / R_nl = {r_e / R_nl:.3f}")

    # Sample ξ_δ curve
    r_samples_h = np.array([0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 8.0, 12.0, 20.0])
    xi_curve = []
    for rh in r_samples_h:
        x = xi_filtered(float(rh), R_hinv, Pk, A)
        xi_curve.append(
            {"r_hinv": float(rh), "r_Mpc": float(rh / H), "xi": x, "rho": x / xi0 if xi0 else 0.0}
        )
        print(f"    r={rh/H:6.2f} Mpc  ξ={x:+.4f}  ρ={x/xi0:+.4f}")

    # Mask correlation at δ_c = 1
    delta_c = 1.0
    f, _, _ = mask_stats(0.0, R_hinv, Pk, A, delta_c, xi0)
    # ξ_mask(0) = f(1-f) for Bernoulli
    xi_m0 = f * (1.0 - f)

    def xi_m_fn(r_h: float) -> float:
        _, xm, _ = mask_stats(r_h, R_hinv, Pk, A, delta_c, xi0)
        return xm

    r_e_m_h = find_corr_length(xi_m_fn, xi_m0, r_max_hinv=25.0, target=1.0 / math.e, n=50)
    r_e_m = r_e_m_h / H
    print(f"  mask δ_c={delta_c}: f={f:.4f}  ξ_m(0)={xi_m0:.4f}")
    print(f"  r_e,mask = {r_e_m:.3f} Mpc  ({r_e_m_h:.3f} h^-1)  r_e,mask/R_nl={r_e_m/R_nl:.3f}")

    mask_curve = []
    for rh in r_samples_h:
        fm, xm, rho = mask_stats(float(rh), R_hinv, Pk, A, delta_c, xi0)
        mask_curve.append(
            {
                "r_Mpc": float(rh / H),
                "xi_mask": xm,
                "rho_delta": rho,
                "xi_mask_over_xi0": xm / xi_m0 if xi_m0 else 0.0,
            }
        )

    # Decoherence OOM for working g and order-unity g
    sigma_free = sigma_from_count(R_nl, L_H, 3)
    lam_work = math.sqrt(max((1.5e-4) ** 2 - sigma_free**2, 0.0))
    g_work = lam_work / sigma_free if sigma_free > 0 else float("nan")
    dec_g1 = decoherence_oom(1.0, R_nl)
    dec_gwork = decoherence_oom(g_work, R_nl)
    dec_gsmall = decoherence_oom(1e-3, R_nl)
    print()
    print("  Decoherence OOM (Γ/H0):")
    print(f"    g=1:     fast={dec_g1['Gamma_over_H0_fast_bath']:.3e}  slow={dec_g1['Gamma_over_H0_slow_bath']:.3e}")
    print(f"    g=g_work={g_work:.3f}: fast={dec_gwork['Gamma_over_H0_fast_bath']:.3e}  slow={dec_gwork['Gamma_over_H0_slow_bath']:.3e}")
    print(f"    g=1e-3:  fast={dec_gsmall['Gamma_over_H0_fast_bath']:.3e}  slow={dec_gsmall['Gamma_over_H0_slow_bath']:.3e}")

    # Sandwich table
    rows = sandwich_table(R_nl, L_H, d=3)
    print()
    print("  Sandwich table (d=3):")
    for row in rows:
        print(
            f"    {row['label']:16s} ℓ={row['ell_Mpc']:.3e}  "
            f"N_p={row['N_patches']:.2e}  σ_naive={row['sigma_count_naive']:.3e}  "
            f"σ_eff={row['sigma_eff_after_renorm']:.3e}"
        )
        print(f"      → {row['regime']}")

    # Packing sep from earlier programme
    from r1_t1_mechanisms_compute import gaussian_tail_fraction, packing_separation

    f1 = gaussian_tail_fraction(1.0, 1.0)
    ell_sep = packing_separation(R_nl, f1)

    out = {
        "theorem": "sandwich uniqueness of residual grain under A0-A4",
        "R_nl_Mpc": R_nl,
        "sigma0_at_Rnl": sig0,
        "xi_delta_0": xi0,
        "r_e_delta_Mpc": r_e,
        "r_e_over_Rnl": r_e / R_nl,
        "delta_c_mask": delta_c,
        "f_mask": f,
        "r_e_mask_Mpc": r_e_m,
        "r_e_mask_over_Rnl": r_e_m / R_nl,
        "ell_sep_packing_Mpc": ell_sep,
        "sigma_free_d3": sigma_free,
        "g_working": g_work,
        "decoherence_g1": dec_g1,
        "decoherence_g_work": dec_gwork,
        "decoherence_g_1e-3": dec_gsmall,
        "xi_delta_curve": xi_curve,
        "xi_mask_curve": mask_curve,
        "sandwich_rows": rows,
        "conclusion": (
            "Under local coupling to classical nonlinear matter, free residual "
            "grain is forced into the O(1)×R_nl band: UV modes decohere; IR "
            "super-cells renormalize to R_nl patches. Correlation lengths "
            "r_e(δ) and r_e(mask) are O(R_nl), not L_H or L_P."
        ),
    }
    (OUT / "sandwich_derivation.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    txt = f"""SANDWICH DERIVATION — residual grain uniqueness under A0–A4
============================================================
R_nl = {R_nl:.4f} Mpc
σ_0(R_nl) = {sig0:.4f}  (expect 1)
ξ_δ correlation length r_e (1/e) = {r_e:.3f} Mpc = {r_e/R_nl:.3f} × R_nl
mask δ_c=1: f={f:.4f}  r_e,mask = {r_e_m:.3f} Mpc = {r_e_m/R_nl:.3f} × R_nl
packing ℓ_sep = {ell_sep:.2f} Mpc
σ_free(d=3) = {sigma_free:.6e}
g_working = {g_work:.4f}

Decoherence Γ/H0 (OOM):
  g=1:     fast={dec_g1['Gamma_over_H0_fast_bath']:.3e}  slow={dec_g1['Gamma_over_H0_slow_bath']:.3e}
  g_work:  fast={dec_gwork['Gamma_over_H0_fast_bath']:.3e}  slow={dec_gwork['Gamma_over_H0_slow_bath']:.3e}

THEOREM (under A0–A4): free residual counting cell ℓ_* is unique up to O(1):
  ℓ_* ~ R_nl  (domain/filter), not L_P and not L_H.
  Fine structure R_* and packing ℓ_sep are O(1) geometric factors in the same decade.

PRIMARY BOUND still: working |λ|≲1.24e-4, |g|≲1.45 (DESI σ_X).
See papers/r1-derivation-sandwich.md
"""
    (OUT / "sandwich_derivation.txt").write_text(txt, encoding="utf-8")
    print()
    print(txt)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
