#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full DESI DR2 Gaussian BAO likelihood (13 observables, full 13×13 covariance)
for residual coupling lambda with fixed R_nl / sigma_free.

Data: public DESI DR2 BAO ALL_GCcomb mean + cov
  (DV, DM, DH)/rd at 7 effective redshifts → 13 numbers
  (BGS: DV only; Lya: DH,DM order).

Model (fractional / α-like residual — removes fixed-rd absolute offset):
  r_i = data_i / theory_i − 1
  C_frac_ij = C_data_ij / (theory_i * theory_j)
  C_total = C_frac + C_signal
  C_signal_ij = S_i S_j * sigma_res^2 * exp(−theta |x_i − x_j|)
  S_i = d ln O_i / d Omega_Lambda  (numerical, flat LCDM)
  sigma_res(lambda) = sqrt(sigma_free^2 + lambda^2)
  x_i = ln(1+z_i)

R_nl / ell_* NOT floated.

Why fractional: absolute residual (data−theory) with fixed rd inherits a
theory–data mean offset that dominates χ² and thrashs the λ profile
(grid-edge formal limits). Fractional residuals match the α≡D/D_fid
construction used in the sister OU-BAO pipeline.

See papers/r1-bounding-g-plan.md · results/r1_lambda_fullcov/
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.linalg import cho_factor, cho_solve
from scipy.optimize import minimize_scalar

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
OUT = ROOT / "results" / "r1_lambda_fullcov"
OUT.mkdir(parents=True, exist_ok=True)
DATA = ROOT / "data"

# Sister zenodo cache (absolute fallback)
SISTER_BAO = Path(
    "/home/ashpokemon/Proyectos/01_Fisica_y_Cosmologia/stochastic-dark-energy-ou"
    "/data/desi_dr2_local/dr2_data/dr2-bao-zenodo/cosmology_chains/bao_data/desi_bao_dr2"
)
# Alternate public copies
ALT_BAO = Path(
    "/home/ashpokemon/Proyectos/01_Fisica_y_Cosmologia/proyecto_unificacion"
    "/data/desi/bao_dr2"
)

from lib_verified import hubble_radius_mpc, sigma_from_count  # noqa: E402
from r1_sigma_R_full import H as H_FID, SIGMA8, find_R_nl, make_Pk_unnorm, normalize_A  # noqa: E402

# Cosmology for theory + S_i
OM0 = 0.315
OL0 = 1.0 - OM0
H0 = 67.4  # km/s/Mpc
C_KMS = 299792.458
RD = 147.09  # Mpc, DESI/Planck-class sound horizon (fixed convention; cancels in frac)
DESI_WORKING = 1.5e-4  # programme working 95% ceiling (sister paper)


def E(z: float, Om: float = OM0, Ol: float = OL0) -> float:
    return math.sqrt(Om * (1 + z) ** 3 + Ol)


def comoving_chi_mpc(z: float, Om: float = OM0, Ol: float = OL0, H0: float = H0) -> float:
    if z <= 0:
        return 0.0
    val, _ = quad(lambda zp: 1.0 / E(zp, Om, Ol), 0.0, z, epsabs=1e-10)
    return (C_KMS / H0) * val


def DH_over_rd(z: float, Om: float = OM0, Ol: float = OL0, H0: float = H0, rd: float = RD) -> float:
    return (C_KMS / (H0 * E(z, Om, Ol))) / rd


def DM_over_rd(z: float, Om: float = OM0, Ol: float = OL0, H0: float = H0, rd: float = RD) -> float:
    return comoving_chi_mpc(z, Om, Ol, H0) / rd


def DV_over_rd(z: float, Om: float = OM0, Ol: float = OL0, H0: float = H0, rd: float = RD) -> float:
    dm = DM_over_rd(z, Om, Ol, H0, rd) * rd
    dh = DH_over_rd(z, Om, Ol, H0, rd) * rd
    return ((z * dm**2 * dh) ** (1.0 / 3.0)) / rd


def dlnO_dOl(kind: str, z: float, eps: float = 1e-4) -> float:
    """Numerical d ln O / d Omega_Lambda; flat Om+Ol=1."""
    ol1, ol2 = OL0 - eps, OL0 + eps
    om1, om2 = 1.0 - ol1, 1.0 - ol2

    def O(om, ol):
        if kind == "DV":
            return DV_over_rd(z, om, ol)
        if kind == "DM":
            return DM_over_rd(z, om, ol)
        if kind == "DH":
            return DH_over_rd(z, om, ol)
        raise ValueError(kind)

    o1, o2 = O(om1, ol1), O(om2, ol2)
    return (math.log(o2) - math.log(o1)) / (2 * eps)


def _find_mean_cov() -> tuple[Path, Path]:
    candidates = [
        (SISTER_BAO / "desi_gaussian_bao_ALL_GCcomb_mean.txt",
         SISTER_BAO / "desi_gaussian_bao_ALL_GCcomb_cov.txt"),
        (ALT_BAO / "desi_gaussian_bao_ALL_GCcomb_mean.txt",
         ALT_BAO / "desi_gaussian_bao_ALL_GCcomb_cov.txt"),
        (DATA / "desi_gaussian_bao_ALL_GCcomb_mean.txt",
         DATA / "desi_gaussian_bao_ALL_GCcomb_cov.txt"),
    ]
    for m, c in candidates:
        if m.exists() and c.exists():
            return m, c
    raise FileNotFoundError(
        "DESI ALL_GCcomb mean/cov not found. Checked sister zenodo, "
        "proyecto_unificacion, and local data/."
    )


def load_desi_all() -> tuple[np.ndarray, np.ndarray, np.ndarray, list[str]]:
    """Return z, data vector (13,), cov (13,13), kinds list.

    Prefer text source (full provenance); fall back to local npy copies.
    """
    npy_mean = DATA / "desi_dr2_mean_all_13.npy"
    npy_z = DATA / "desi_dr2_z_all_13.npy"
    npy_cov = DATA / "desi_dr2_cov_all_13.npy"
    npy_kinds = DATA / "desi_dr2_kinds_13.txt"

    try:
        mean_path, cov_path = _find_mean_cov()
        rows = []
        with open(mean_path) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split()
                z = float(parts[0])
                val = float(parts[1])
                kind = parts[2].split("_")[0]  # DV, DM, DH
                rows.append((z, val, kind))
        z = np.array([r[0] for r in rows])
        data = np.array([r[1] for r in rows])
        kinds = [r[2] for r in rows]
        cov = np.loadtxt(cov_path)
        assert cov.shape == (len(data), len(data))
        DATA.mkdir(exist_ok=True)
        np.save(npy_mean, data)
        np.save(npy_z, z)
        np.save(npy_cov, cov)
        with open(npy_kinds, "w") as f:
            f.write("\n".join(kinds) + "\n")
        return z, data, cov, kinds
    except FileNotFoundError:
        if npy_mean.exists() and npy_z.exists() and npy_cov.exists() and npy_kinds.exists():
            data = np.load(npy_mean)
            z = np.load(npy_z)
            cov = np.load(npy_cov)
            kinds = npy_kinds.read_text().strip().split()
            assert len(kinds) == len(data)
            return z, data, cov, kinds
        raise


def theory_vector(z: np.ndarray, kinds: list[str]) -> np.ndarray:
    th = []
    for zi, k in zip(z, kinds):
        if k == "DV":
            th.append(DV_over_rd(float(zi)))
        elif k == "DM":
            th.append(DM_over_rd(float(zi)))
        elif k == "DH":
            th.append(DH_over_rd(float(zi)))
        else:
            raise ValueError(k)
    return np.array(th)


def sensitivity_vector(z: np.ndarray, kinds: list[str]) -> np.ndarray:
    return np.array([dlnO_dOl(k, float(zi)) for zi, k in zip(z, kinds)])


def sigma_free_Rnl() -> tuple[float, float]:
    Pk = make_Pk_unnorm()
    A = normalize_A(Pk, SIGMA8)
    R_nl = find_R_nl(Pk, A, 1.0) / H_FID
    sf = sigma_from_count(R_nl, hubble_radius_mpc(), 3)
    return R_nl, float(sf)


def build_C_total(
    C_frac: np.ndarray, S: np.ndarray, x: np.ndarray, theta: float, s_res: float
) -> np.ndarray:
    C = C_frac.copy()
    s2 = s_res**2
    n = len(S)
    for i in range(n):
        for j in range(n):
            dx = abs(x[i] - x[j])
            C[i, j] += S[i] * S[j] * s2 * math.exp(-theta * dx)
    return C


def logL(C: np.ndarray, residual: np.ndarray) -> float:
    try:
        c, lower = cho_factor(C, lower=True, check_finite=False)
        y = cho_solve((c, lower), residual, check_finite=False)
        logdet = 2.0 * np.sum(np.log(np.diag(c)))
        n = len(residual)
        return float(-0.5 * (residual @ y + logdet + n * math.log(2 * math.pi)))
    except Exception:
        return -1e30


def max_over_theta(
    C_frac: np.ndarray, S: np.ndarray, x: np.ndarray, residual: np.ndarray, s_res: float
) -> tuple[float, float]:
    def neg(th: float) -> float:
        return -logL(build_C_total(C_frac, S, x, th, s_res), residual)

    best_ll, best_th = -1e30, 1.0
    for bracket in ((1e-3, 0.5), (0.1, 3.0), (1.0, 25.0)):
        try:
            res = minimize_scalar(neg, bounds=bracket, method="bounded", options={"xatol": 1e-5})
            ll = -res.fun
            if ll > best_ll:
                best_ll, best_th = ll, float(res.x)
        except Exception:
            pass
    for th in np.geomspace(1e-3, 25, 60):
        ll = logL(build_C_total(C_frac, S, x, float(th), s_res), residual)
        if ll > best_ll:
            best_ll, best_th = ll, float(th)
    return best_ll, best_th


def profile_upper_95(profile: list[dict], key: str, ll_field: str = "logL") -> float:
    """Largest |param| still within Delta lnL = 1.92 of profile max."""
    ll_max = max(p[ll_field] for p in profile)
    thr = ll_max - 1.92
    ok = [p for p in profile if p[ll_field] >= thr]
    if not ok:
        return float("nan")
    return max(p[key] for p in ok)


def main() -> None:
    print("=== FULL COV DESI DR2 BAO (13-vector) λ profile — FRACTIONAL residuals ===")
    z, data, C_data, kinds = load_desi_all()
    theory = theory_vector(z, kinds)
    # α-like fractional residual and covariance
    residual = data / theory - 1.0
    C_frac = C_data / np.outer(theory, theory)
    S = sensitivity_vector(z, kinds)
    x = np.log(1.0 + z)
    R_nl, sigma_free = sigma_free_Rnl()

    sd = np.sqrt(np.diag(C_data))
    corr = C_data / np.outer(sd, sd)
    max_off = float(np.max(np.abs(corr - np.eye(len(data)))))
    chi2_abs = float((data - theory) @ np.linalg.solve(C_data, data - theory))
    chi2_frac = float(residual @ np.linalg.solve(C_frac, residual))
    mean_ratio = float(np.mean(data / theory))
    rms_frac = float(np.sqrt(np.mean(residual**2)))

    print(f"  n_obs = {len(data)}  kinds = {kinds}")
    print(f"  max |corr| off-diag data = {max_off:.3f}")
    print(f"  R_nl = {R_nl:.3f} Mpc  sigma_free = {sigma_free:.3e}  (FIXED)")
    print(f"  mean(data/theory) = {mean_ratio:.5f}  (rd offset diagnostics)")
    print(f"  chi2_LCDM absolute = {chi2_abs:.3f}  |  fractional = {chi2_frac:.3f}  (ndata={len(data)})")
    print(f"  residual fractional RMS = {rms_frac:.4e}")
    print(f"  S range = [{S.min():.3f}, {S.max():.3f}]")
    print()

    ll0, th0 = max_over_theta(C_frac, S, x, residual, 0.0)
    print(f"  ll(s_res=0) = {ll0:.4f}  theta~{th0:.3f}")

    # Extended free sigma_res profile (must reach O(10%) for 95% upper edge)
    sig_grid = np.geomspace(1e-6, 2.0, 100)
    sig_profile = []
    best_s = {"s": 0.0, "ll": -1e30, "th": 1.0}
    for s in sig_grid:
        ll, th = max_over_theta(C_frac, S, x, residual, float(s))
        sig_profile.append(
            {"sigma_res": float(s), "logL": ll, "dlogL": ll - ll0, "theta": th}
        )
        if ll > best_s["ll"]:
            best_s = {"s": float(s), "ll": ll, "th": th}

    thr_s = best_s["ll"] - 1.92
    ok_s = [p for p in sig_profile if p["logL"] >= thr_s]
    s_lo = min(p["sigma_res"] for p in ok_s)
    s_hi = max(p["sigma_res"] for p in ok_s)
    zero_excluded = bool(ll0 < thr_s)

    # |lambda| profile (extended)
    lam_grid = np.geomspace(1e-7, 0.5, 80)
    profile = []
    best = {"lam": 0.0, "ll": -1e30, "th": 1.0, "sres": 0.0}
    report_idx = {0, len(lam_grid) // 8, len(lam_grid) // 4, len(lam_grid) // 2,
                  3 * len(lam_grid) // 4, len(lam_grid) - 1}
    for i, lam in enumerate(lam_grid):
        sres = math.sqrt(sigma_free**2 + float(lam) ** 2)
        ll, th = max_over_theta(C_frac, S, x, residual, sres)
        row = {
            "lambda": float(lam),
            "sigma_res": sres,
            "theta_best": th,
            "logL": ll,
            "dlogL": ll - ll0,
        }
        profile.append(row)
        if ll > best["ll"]:
            best = {"lam": float(lam), "ll": ll, "th": th, "sres": sres}
        if i in report_idx or abs(ll - ll0) > 0.5:
            print(f"  |λ|={lam:.3e}  σ_res={sres:.3e}  θ={th:.3f}  ΔlnL={ll-ll0:+.4f}")

    thr_l = best["ll"] - 1.92
    ok_l = [p for p in profile if p["logL"] >= thr_l]
    lam_lo = min(p["lambda"] for p in ok_l)
    lam_hi = max(p["lambda"] for p in ok_l)

    # Working ceiling from programme sigma_X < 1.5e-4
    if sigma_free < DESI_WORKING:
        lam_work = math.sqrt(DESI_WORKING**2 - sigma_free**2)
    else:
        lam_work = 0.0
    g_work = lam_work / sigma_free if sigma_free > 0 else float("nan")

    # ΔlnL at programme scales (vs LCDM)
    ll_sf, _ = max_over_theta(C_frac, S, x, residual, sigma_free)
    ll_wk, _ = max_over_theta(C_frac, S, x, residual, DESI_WORKING)

    # Formal is NOT informative for 1e-4 grain: best is O(1%), chi2 absorption
    formal_informative_for_1e4 = bool(
        best_s["s"] < 5e-4 and not zero_excluded and s_hi < 1e-3
    )

    print()
    print("=== RESULTS (full 13×13 covariance, fractional residual) ===")
    print(f"  Best σ_res ≈ {best_s['s']:.3e}  ΔlnL≈{best_s['ll']-ll0:+.4f}")
    print(f"  Formal 95% σ_res ∈ [{s_lo:.3e}, {s_hi:.3e}]  zero_excl={zero_excluded}")
    print(f"  Best |λ| ≈ {best['lam']:.3e}  95% |λ| ∈ [{lam_lo:.3e}, {lam_hi:.3e}]")
    print(f"  Working (σ_X<{DESI_WORKING:.1e}) |λ| ≲ {lam_work:.3e}  |g| ≲ {g_work:.3f}")
    print(f"  ΔlnL(σ_free)={ll_sf-ll0:+.4f}  ΔlnL(1.5e-4)={ll_wk-ll0:+.4f}")
    print(f"  formal_informative_for_1e-4_grain = {formal_informative_for_1e4}")
    print(f"  primary_bound = working")
    print()
    print("HONEST: formal ~1% preference absorbs chi2_LCDM tension, not 1e-4 grain.")
    print("        residual = data/theory−1; C_frac = C/(th⊗th); R_nl fixed.")

    out = {
        "method": "fractional residual (alpha-like) + full 13x13 DESI DR2 cov",
        "data": "DESI DR2 ALL_GCcomb 13-vector full covariance (public)",
        "n_obs": int(len(data)),
        "kinds": kinds,
        "R_nl_Mpc": R_nl,
        "sigma_free": sigma_free,
        "mean_data_over_theory": mean_ratio,
        "mean_fractional_residual": float(np.mean(residual)),
        "chi2_lcdm_absolute": chi2_abs,
        "chi2_lcdm_fractional": chi2_frac,
        "residual_frac_rms": rms_frac,
        "max_offdiag_corr": max_off,
        "ll_sres0": ll0,
        "theta_sres0": th0,
        "best_sigma_res": best_s["s"],
        "best_sigma_dlogL": best_s["ll"] - ll0,
        "sigma_res_95_lo": s_lo,
        "sigma_res_95_hi": s_hi,
        "zero_residual_excluded_95": zero_excluded,
        "best_lambda_on_grid": best["lam"],
        "best_lambda_dlogL": best["ll"] - ll0,
        "lambda_95_lo": lam_lo,
        "lambda_95_hi": lam_hi,
        "lambda_working_1p5e-4": lam_work,
        "g_working": g_work,
        "dlogL_at_sigma_free": ll_sf - ll0,
        "dlogL_at_working_1p5e-4": ll_wk - ll0,
        "formal_informative_for_1e-4_grain": formal_informative_for_1e4,
        "primary_bound": "working",
        "interpretation": (
            "Formal profile prefers sigma_res ~ O(1%) because chi2_LCDM~29 "
            "is absorbed by covariance inflation; this is NOT a detection of "
            "the microscopic free grain. Working bound from sister alpha-OU "
            "sigma_X<1.5e-4 remains the programme ceiling for lambda/g."
        ),
        "profile_lambda": profile,
        "profile_sigma_res": sig_profile,
        "theory_rd_Mpc": RD,
        "Om0": OM0,
        "H0": H0,
        "convention": "lambda = g * sigma_free  (kappa=1); sigma_res^2 = sigma_free^2 + lambda^2",
    }
    (OUT / "lambda_fullcov_profile.json").write_text(
        json.dumps(out, indent=2), encoding="utf-8"
    )
    summary = f"""FULL COV DESI DR2 BAO — lambda profile (FRACTIONAL residual)
================================================================
n_obs={len(data)}  R_nl={R_nl:.4f} Mpc  sigma_free={sigma_free:.6e}
mean(data/theory)={mean_ratio:.6f}  residual mean={float(np.mean(residual)):.4e}  rms={rms_frac:.4e}
chi2_LCDM absolute={chi2_abs:.3f}  fractional={chi2_frac:.3f}  (ndof={len(data)})  max|rho|_off={max_off:.3f}

FORMAL profile (free sigma_res; full 13x13):
  best sigma_res = {best_s['s']:.4e}   Delta lnL = {best_s['ll']-ll0:+.3f} vs LCDM
  95% CL interval sigma_res in [{s_lo:.4e}, {s_hi:.4e}]
  zero residual excluded at 95%? {zero_excluded}
  best |lambda| ~ {best['lam']:.4e}   95% |lambda| in [{lam_lo:.4e}, {lam_hi:.4e}]

WORKING (programme primary — sister sigma_X < 1.5e-4):
  |lambda| <= {lam_work:.6e}
  |g|      <= {g_work:.4f}   (convention lambda = g * sigma_free)
  Delta lnL at sigma_free  = {ll_sf-ll0:+.4f}
  Delta lnL at 1.5e-4      = {ll_wk-ll0:+.4f}

HONEST INTERPRETATION:
  Formal preference for ~1-2% residual amplitude absorbs LCDM chi2 tension
  (mean fractional offset ~1%), NOT the 1e-4 free-grain of P_nl counting.
  Full-cov does NOT tighten lambda into the 1e-4 regime.
  primary_bound = working
  formal_informative_for_1e-4_grain = {formal_informative_for_1e4}

See papers/r1-bounding-g-plan.md
"""
    (OUT / "lambda_fullcov_profile.txt").write_text(summary, encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
