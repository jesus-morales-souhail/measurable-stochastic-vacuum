#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Profile likelihood for dimensionless coupling lambda on DESI DR2 BAO (diagonal).

Same public BAO arrays as sister profile_sigma_x_desi.py / ou_bao_likelihood.py.
Model:
  sigma_res(lambda) = sqrt(sigma_free^2 + lambda^2)
  C_ij = diag(sigma_obs^2) + S_i S_j sigma_res^2 exp(-theta |x_i-x_j|)

sigma_free fixed from R_nl counting (P_nl, d=3). ell_* / R_nl NOT floated.

Reports:
  - formal profile 95% CL on |lambda| (Delta lnL = -1.92, 1 dof)
  - working ceiling map from sigma_X < 1.5e-4 (programme working limit)
  - g under convention lambda = g * sigma_free

See papers/r1-bounding-g-plan.md · results/r1_lambda_profile/
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.linalg import cho_factor, cho_solve
from scipy.optimize import minimize_scalar

ROOT = Path(__file__).resolve().parents[2]
_SCRIPTS = ROOT / "scripts"
for _d in (_SCRIPTS, _SCRIPTS / "core", _SCRIPTS / "r1", _SCRIPTS / "closed", _SCRIPTS / "side"):
    if _d.is_dir() and str(_d) not in sys.path:
        sys.path.insert(0, str(_d))
OUT = ROOT / "results" / "r1_lambda_profile"
OUT.mkdir(parents=True, exist_ok=True)

from lib_verified import hubble_radius_mpc, sigma_from_count  # noqa: E402
from r1_sigma_R_full import H, SIGMA8, find_R_nl, make_Pk_unnorm, normalize_A  # noqa: E402
def _load_desi_alpha():
    """Load real DESI DR2 alpha from sibling data pack if present."""
    cand = [
        ROOT.parent / "stochastic-dark-energy-ou" / "scripts" / "desi_dr2_data.py",
    ]
    for c in cand:
        if c.is_file():
            import importlib.util
            spec = importlib.util.spec_from_file_location("desi_dr2_data", c)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            d = mod.load_alpha_dv(prefer_file=True)
            print("r1_profile_lambda data:", d["source"])
            return d["z"], d["alpha"], d["sigma"], d["S_z"]
    # published table fallback (real DESI numbers, not mock draws)
    z = np.array([0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330])
    a = np.array([1.0030, 0.9947, 1.0016, 0.9960, 1.0020, 0.9963, 1.0008])
    s = np.array([0.0097, 0.0072, 0.0057, 0.0049, 0.0063, 0.0088, 0.0120])
    sz = np.array([-0.284, -0.462, -0.595, -0.719, -0.870, -0.917, -1.070])
    print("r1_profile_lambda data: published DR2 table fallback")
    return z, a, s, sz



Z_EFF, ALPHA, SIGMA_OBS, S_Z = _load_desi_alpha()
RES = ALPHA - 1.0
X = np.log(1.0 + Z_EFF)
N = len(Z_EFF)

DESI_WORKING = 1.5e-4  # programme working 95% ceiling (paper)




def sigma_free_from_Rnl() -> tuple[float, float]:
    Pk = make_Pk_unnorm()
    A = normalize_A(Pk, SIGMA8)
    R_nl = find_R_nl(Pk, A, 1.0) / H
    sf = sigma_from_count(R_nl, hubble_radius_mpc(), 3)
    return R_nl, float(sf)


def sigma_res(lam: float, sigma_free: float) -> float:
    return math.sqrt(sigma_free**2 + abs(lam) ** 2)


def build_C(theta: float, s_res: float) -> np.ndarray:
    C = np.diag(SIGMA_OBS**2)
    s2 = s_res**2
    for i in range(N):
        for j in range(N):
            dx = abs(X[i] - X[j])
            C[i, j] += S_Z[i] * S_Z[j] * s2 * np.exp(-theta * dx)
    return C


def logL(theta: float, s_res: float) -> float:
    if theta <= 0 or s_res < 0:
        return -1e30
    C = build_C(theta, s_res)
    try:
        c, lower = cho_factor(C, lower=True, check_finite=False)
        y = cho_solve((c, lower), RES, check_finite=False)
        logdet = 2.0 * np.sum(np.log(np.diag(c)))
        return float(-0.5 * (RES @ y + logdet + N * np.log(2 * np.pi)))
    except Exception:
        return -1e30


def max_logL_over_theta(s_res: float) -> tuple[float, float]:
    def neg(th: float) -> float:
        return -logL(th, s_res)

    best_ll, best_th = -1e30, 1.0
    for bracket in ((1e-3, 0.5), (0.1, 3.0), (1.0, 20.0)):
        try:
            res = minimize_scalar(neg, bounds=bracket, method="bounded", options={"xatol": 1e-5})
            ll = -res.fun
            if ll > best_ll:
                best_ll, best_th = ll, float(res.x)
        except Exception:
            pass
    for th in np.geomspace(1e-3, 20, 40):
        ll = logL(float(th), s_res)
        if ll > best_ll:
            best_ll, best_th = ll, float(th)
    return best_ll, best_th


def main() -> None:
    R_nl, sigma_free = sigma_free_from_Rnl()
    ll_lcdm, _ = max_logL_over_theta(0.0)
    # exact LCDM check
    C0 = np.diag(SIGMA_OBS**2)
    c, lower = cho_factor(C0, lower=True)
    y = cho_solve((c, lower), RES)
    logdet = 2.0 * np.sum(np.log(np.diag(c)))
    ll0 = float(-0.5 * (RES @ y + logdet + N * np.log(2 * np.pi)))

    print("=== Profile lambda on DESI DR2 BAO (diagonal OU) ===")
    print(f"  R_nl = {R_nl:.3f} Mpc  (fixed)")
    print(f"  sigma_free = {sigma_free:.3e}  (fixed d=3 count)")
    print(f"  ll_LCDM = {ll0:.4f}")
    print()

    # profile over |lambda|
    lam_grid = np.geomspace(1e-6, 5e-2, 48)
    profile = []
    best = {"lam": 0.0, "ll": -1e30, "th": 1.0}
    for lam in lam_grid:
        sres = sigma_res(float(lam), sigma_free)
        ll, th = max_logL_over_theta(sres)
        row = {
            "lambda": float(lam),
            "sigma_res": sres,
            "theta_best": th,
            "logL": ll,
            "dlogL": ll - ll0,
        }
        profile.append(row)
        if ll > best["ll"]:
            best = {"lam": float(lam), "ll": ll, "th": th}
        print(f"  |λ|={lam:.3e}  σ_res={sres:.3e}  θ={th:.3f}  ΔlnL={ll-ll0:+.4f}")

    # 95% CL: from profile max, Delta lnL >= -1.92
    ll_max = best["ll"]
    thr = ll_max - 1.92
    # find largest |lambda| still above thr (upper limit)
    ok = [p for p in profile if p["logL"] >= thr]
    lam_95_formal = max(p["lambda"] for p in ok) if ok else float("nan")

    # Working ceiling map
    if sigma_free < DESI_WORKING:
        lam_work = math.sqrt(DESI_WORKING**2 - sigma_free**2)
    else:
        lam_work = 0.0
    g_work = lam_work / sigma_free if sigma_free > 0 else float("inf")
    g_formal = lam_95_formal / sigma_free if sigma_free > 0 else float("inf")

    print()
    print("=== Results ===")
    print(f"  Profile max near |λ|≈{best['lam']:.3e}  (ΔlnL max ≈ {best['ll']-ll0:+.4f})")
    print(f"  Formal 95% CL (diag BAO profile): |λ| ≤ {lam_95_formal:.3e}")
    print(f"  Formal |g| ≲ {g_formal:.3f}  (conv. λ=g·σ_free)")
    print(f"  Working map from σ_X<1.5e-4:     |λ| ≲ {lam_work:.3e}  |g| ≲ {g_work:.3f}")
    print()
    print("Honesty:")
    print("  Diagonal 7-bin BAO formal profile is WEAK (same as sister σ_X profile ~0.025).")
    print("  Programme working ceiling 1.5e-4 is the tighter physical working bound.")
    print("  Full covariance DESI would tighten formal limit — not re-run here.")
    print("  R_nl / ell_* NOT floated.")

    out = {
        "R_nl_Mpc": R_nl,
        "sigma_free": sigma_free,
        "ll_lcdm": ll0,
        "lambda_95_formal_profile": lam_95_formal,
        "g_95_formal": g_formal,
        "lambda_working_from_1p5e-4": lam_work,
        "g_working": g_work,
        "note": "Formal profile uses diagonal BAO only; working limit from sister paper ceiling",
        "profile": profile,
    }
    (OUT / "lambda_profile.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    lines = [
        "Profile |lambda| — DESI DR2 BAO diagonal OU",
        f"R_nl = {R_nl:.4f} Mpc (fixed)",
        f"sigma_free = {sigma_free:.6e}",
        f"Formal 95% |lambda| <= {lam_95_formal:.6e}",
        f"Working |lambda| <= {lam_work:.6e} (from sigma_X < 1.5e-4)",
        f"Working |g| <= {g_work:.4f} (lambda = g * sigma_free)",
        "See papers/r1-bounding-g-plan.md",
    ]
    (OUT / "lambda_profile.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT / 'lambda_profile.json'}")


if __name__ == "__main__":
    main()
