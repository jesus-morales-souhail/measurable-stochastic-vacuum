#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Operational falsifiers for the sandwich uniqueness theorem (A0–A4).

Predictions at the programme working point:
  ell_* = R_nl ≈ 8.61 Mpc
  sigma_free = (R_nl/L_H)^{3/2} ≈ 8.5e-5
  |lambda| ≲ 1.24e-4, |g| ≲ 1.45  (working DESI map)

Compares to published / forecast floors (Maus, Sakr, DESI residual, Stage-IV).
Does NOT claim Stage-IV detects path-RMS; states what would kill / confirm.

See papers/r1-sandwich-falsifiers.md
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_SCRIPTS = ROOT / "scripts"
for _d in (_SCRIPTS, _SCRIPTS / "core", _SCRIPTS / "r1", _SCRIPTS / "closed", _SCRIPTS / "side"):
    if _d.is_dir() and str(_d) not in sys.path:
        sys.path.insert(0, str(_d))
OUT = ROOT / "results" / "r1_falsifiers"
OUT.mkdir(parents=True, exist_ok=True)

from lib_verified import (  # noqa: E402
    comoving_distance_mpc,
    hubble_radius_mpc,
    n_patches,
    rms_incoherent,
    sigma_from_count,
    slip_deviation,
)
from r1_sigma_R_full import H as H_FID, SIGMA8, find_R_nl, make_Pk_unnorm, normalize_A  # noqa: E402

# External floors (named papers; same as lensing_rms_real_data_compare)
MAUS_SIGMA_GAMMA = 0.11  # arXiv:2505.20656
SAKR_ETA_CONST = 0.05  # arXiv:2501.07477 optimistic constant η
SAKR_ETA_FREE = 0.30  # free (z,k) OOM
DESI_SIGMA_X = 2.5e-2  # sister OU/QNM residual 95%
STAGE4_M_BIAS = 2e-3  # calibration requirement, wrong operator for path-RMS
EUCLID_RESIDUAL_TARGET = 1e-5  # programme telescope-band reference


def R_nl_and_sigma() -> tuple[float, float]:
    Pk = make_Pk_unnorm()
    A = normalize_A(Pk, SIGMA8)
    R_nl = find_R_nl(Pk, A, 1.0) / H_FID
    sf = sigma_from_count(R_nl, hubble_radius_mpc(), 3)
    return R_nl, float(sf)


def predictions(
    R_nl: float,
    sigma_free: float,
    eps: float = 1.0,
    z_slip: float = 0.8,
    z_src: float = 1.5,
    delta_m: float = 1.0,
) -> dict:
    """Sandwich-point observables (a priori under A0–A4 + counting)."""
    # Working lambda from DESI ceiling
    if sigma_free < DESI_SIGMA_X:
        lam_work = math.sqrt(DESI_SIGMA_X**2 - sigma_free**2)
    else:
        lam_work = 0.0
    g_work = lam_work / sigma_free if sigma_free > 0 else float("nan")
    # Residual amplitude: free grain only, or free+induced at working ceiling
    s_free = sigma_free
    s_work = DESI_SIGMA_X
    s_res = math.sqrt(s_free**2 + lam_work**2)  # = DESI ceiling by construction

    slip_loc_free = slip_deviation(eps, s_free, z_slip, delta_m)
    slip_loc_work = slip_deviation(eps, s_work, z_slip, delta_m)

    chi = comoving_distance_mpc(z_src)
    n_pat = n_patches(chi, R_nl)
    rms_free = rms_incoherent(slip_loc_free, n_pat)
    rms_work = rms_incoherent(slip_loc_work, n_pat)

    return {
        "R_nl_Mpc": R_nl,
        "sigma_free": s_free,
        "lambda_working": lam_work,
        "g_working": g_work,
        "sigma_res_working_ceiling": s_res,
        "eps": eps,
        "z_slip": z_slip,
        "z_src": z_src,
        "chi_Mpc": chi,
        "N_patches_path": n_pat,
        "slip_local_free": slip_loc_free,
        "slip_local_working": slip_loc_work,
        "RMS_path_free": rms_free,
        "RMS_path_working": rms_work,
        "ell_star_band_lo_Mpc": 0.5 * R_nl,
        "ell_star_band_hi_Mpc": 3.0 * R_nl,
    }


def falsifier_table(pred: dict) -> list:
    """Each row: observable, prediction, floor, ratio, verdict language."""
    rows = []

    def add(name, pred_val, floor, floor_name, kill_if, confirm_if, notes):
        ratio = floor / pred_val if pred_val > 0 else float("inf")
        rows.append(
            {
                "observable": name,
                "prediction": pred_val,
                "floor": floor,
                "floor_name": floor_name,
                "floor_over_pred": ratio,
                "kills_if": kill_if,
                "supports_if": confirm_if,
                "notes": notes,
            }
        )

    add(
        "sigma_res (BAO residual amplitude)",
        pred["sigma_free"],
        DESI_SIGMA_X,
        "DESI σ_X 95% (sister OU)",
        "Measured σ_res ≫ 2.5e-2 with no damping, at fixed ell_*=R_nl",
        "σ_res stays ≤ 2.5e-2 while ell_* locked to R_nl (compatibility)",
        "Primary empirical gate. Illegal: refit ell_* after seeing DESI.",
    )
    add(
        "sigma_res free grain only",
        pred["sigma_free"],
        EUCLID_RESIDUAL_TARGET,
        "Euclid-band OOM 1e-5",
        "Euclid residual null far below free grain with ell_*=R_nl forced",
        "Residual band 1e-5–2.5e-2 consistent with counting at R_nl",
        "Detection window if residual appears at predicted OOM without 1e56.",
    )
    add(
        "|γ−1|_local (working σ)",
        pred["slip_local_working"],
        MAUS_SIGMA_GAMMA,
        "Maus σ(γ)=0.11",
        "Mean |γ−1| required ≫ Maus if eps~1 and σ~2.5e-2 without damping",
        "Predicted local slip ≪ Maus (consistency; not a detection)",
        "Today Maus cannot test sandwich amplitude; only kills huge eps×σ.",
    )
    add(
        "RMS_path (working)",
        pred["RMS_path_working"],
        SAKR_ETA_CONST,
        "Sakr constant-η ~0.05",
        "If identified with η−1 and measured ≫ prediction without systematics",
        "RMS_path remains below mean-η floors (consistency)",
        "Operator map imperfect; do not equate RMS_path with η blindly.",
    )
    add(
        "RMS_path (free grain)",
        pred["RMS_path_free"],
        SAKR_ETA_CONST,
        "Sakr constant-η ~0.05",
        "Same as above at free-grain amplitude",
        "Free-grain path RMS deep below Stage-IV mean-η forecasts",
        "Gap ~ tens–hundreds; not Stage-IV near-term detection of free grain.",
    )
    add(
        "ell_* correlation length of residual",
        pred["R_nl_Mpc"],
        pred["ell_star_band_hi_Mpc"],
        "ALLOWED band upper ~3 R_nl",
        "Free residual ξ measured ≪ 1 Mpc or ≫ 100 Mpc at σ~1e-4",
        "Measured residual correlation length in [0.5,3]×R_nl",
        "Direct test of sandwich uniqueness (hardest observationally).",
    )
    add(
        "Stage-IV m-bias (WRONG OPERATOR)",
        pred["RMS_path_working"],
        STAGE4_M_BIAS,
        "Stage-IV m~2e-3 calibration",
        "Never use as kill of sandwich",
        "Never use as detection of residual texture",
        "Category error: shear calibration ≠ stochastic path-RMS.",
    )
    return rows


def decision_tree() -> str:
    return """
DECISION TREE (sandwich package)
================================
1. Does residual sector χ couple locally to δ_m? (A0–A1)
   NO  → sandwich does not apply; scale undetermined (package narrows)
   YES → continue
2. Is ell_* forced to ~R_nl? (theorem under A0–A4)
   If data force free residual correlation ≪1 Mpc or ≫100 Mpc at σ~1e-4
   → sandwich band dies (L2 for this principle form)
3. Is σ_res ≤ 2.5e-2 at fixed ell_*=R_nl?
   NO (and no derived damping) → candidate dies vs DESI
   YES → compatible; Euclid residual can still detect or deepen null
4. Slip / path RMS
   Predicted ≪ Maus/Sakr today → consistency only
   Future stochastic path-RMS proxy at 1e-3–1e-4 → real test of anisotropic channel
5. Illegal moves (instant L4)
   - Fit ell_* to DESI after looking
   - Free 1e56 amplifier
   - Equate Stage-IV m-bias with path-RMS detection
"""


def main() -> None:
    print("=== Sandwich operational falsifiers ===")
    R_nl, sigma_free = R_nl_and_sigma()
    pred = predictions(R_nl, sigma_free)
    rows = falsifier_table(pred)

    print(f"  R_nl = {R_nl:.4f} Mpc")
    print(f"  sigma_free = {sigma_free:.6e}")
    print(f"  |lambda|_work = {pred['lambda_working']:.6e}  |g|_work = {pred['g_working']:.4f}")
    print(f"  |γ−1|_loc free/work = {pred['slip_local_free']:.3e} / {pred['slip_local_working']:.3e}")
    print(f"  RMS_path free/work  = {pred['RMS_path_free']:.3e} / {pred['RMS_path_working']:.3e}")
    print(f"  N_patches (z={pred['z_src']}) = {pred['N_patches_path']:.1f}")
    print()
    for r in rows:
        print(f"  [{r['observable']}]")
        print(f"    pred={r['prediction']:.4e}  floor={r['floor']:.4e}  "
              f"floor/pred={r['floor_over_pred']:.1f}×  ({r['floor_name']})")
        print(f"    KILLS: {r['kills_if']}")
        print(f"    SUPPORTS: {r['supports_if']}")

    tree = decision_tree()
    print(tree)

    out = {
        "predictions": pred,
        "falsifiers": rows,
        "external": {
            "Maus_sigma_gamma": MAUS_SIGMA_GAMMA,
            "Sakr_eta_const": SAKR_ETA_CONST,
            "Sakr_eta_free": SAKR_ETA_FREE,
            "DESI_sigma_X": DESI_SIGMA_X,
            "Stage4_m_bias_OOM": STAGE4_M_BIAS,
            "Euclid_residual_target": EUCLID_RESIDUAL_TARGET,
        },
        "decision_tree": tree,
    }
    (OUT / "sandwich_falsifiers.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    lines = [
        "SANDWICH OPERATIONAL FALSIFIERS",
        f"R_nl={R_nl:.4f} Mpc  sigma_free={sigma_free:.6e}",
        f"|lambda|_work={pred['lambda_working']:.6e}  |g|_work={pred['g_working']:.4f}",
        f"|γ−1|_loc free/work = {pred['slip_local_free']:.4e} / {pred['slip_local_working']:.4e}",
        f"RMS_path free/work  = {pred['RMS_path_free']:.4e} / {pred['RMS_path_working']:.4e}",
        f"N_patches(z=1.5)={pred['N_patches_path']:.2f}",
        f"ell_* ALLOWED band = [{pred['ell_star_band_lo_Mpc']:.2f}, {pred['ell_star_band_hi_Mpc']:.2f}] Mpc",
        "",
        "PRIMARY GATES:",
        "  F1 BAO: sigma_res ≤ 2.5e-2 at fixed ell_*=R_nl",
        "  F2 SCALE: residual correlation length in O(1)×R_nl if detected",
        "  F3 SLIP: local/path slip must stay below Maus/Sakr (today: automatic)",
        "  F4 ILLEGAL: no post-hoc ell_* fit, no 1e56, no m-bias rebrand",
        "",
        "See papers/r1-sandwich-falsifiers.md",
    ]
    (OUT / "sandwich_falsifiers.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
