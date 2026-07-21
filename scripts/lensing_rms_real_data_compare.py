#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compare programme path-RMS (NP-A/B kinematics) to *published* slip / MG /
Stage-IV numbers from real external studies.

Sources are hard-coded with arXiv IDs. This is NOT a likelihood forecast of
stochastic path-RMS detection — it is an OOM reality check against what the
literature actually measures or forecasts for *related* operators.

See papers/lensing-rms-forecast-real-data.md
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lib_verified import (  # noqa: E402
    comoving_distance_mpc,
    ell_mpc_for_sigma,
    n_patches,
    residual_soft_map,
    rms_incoherent,
    slip_deviation,
)

# ---------------------------------------------------------------------------
# Published external anchors (do not invent; cite in the paper note)
# ---------------------------------------------------------------------------

# Maus et al., arXiv:2505.20656v3 — DESI DR1 × CMB lensing
MAUS_GAMMA = 1.17
MAUS_GAMMA_ERR = 0.11  # 1σ on γ=Φ/Ψ
MAUS_ARXIV = "2505.20656"

# Sakr, Zheng, Casas, arXiv:2501.07477 — model-independent η forecasts
# Euclid-like photo ± DESI-like spectro (from abstract)
SAKR_ETA_CONST_FRAC = 0.05  # "finally reach 5% values in the constant case"
SAKR_ETA_ZONLY_FRAC = 0.10  # "less than 10% on average for the z dependence only"
SAKR_ETA_ZK_FRAC = 0.30  # "at least 30% if z,k independent"
SAKR_ARXIV = "2501.07477"

# DESI Collaboration / Ishak et al., arXiv:2411.12026v3
# DESI(FS+BAO)+CMB+DESY3+DESY5-SN, ΛCDM background
DESI_MG_MU0 = 0.05
DESI_MG_MU0_ERR = 0.22
DESI_MG_SIGMA0 = 0.008
DESI_MG_SIGMA0_ERR = 0.045
DESI_MG_ARXIV = "2411.12026"

# Stage-IV shear *calibration* requirements (order of magnitude from
# Euclid / LSST DESC literature). These are NOT slip-RMS sensitivities.
# Euclid prep / Stage-IV WL: multiplicative bias control ~ few × 10^{-3}.
# LSST DESC SRD arXiv:1809.01669 — Stage-IV systematic budgets for WL.
STAGE4_M_MULT_BIAS_OOM = 2e-3
STAGE4_SRD_ARXIV = "1809.01669"
EUCLID_LENSMC_NOTE = "Euclid LensMC prep (e.g. A&A 691 A319, 2024) targets Stage-IV m-bias control"

# Programme-side indicative floor used historically in wall notes
PROG_MEAN_SLIP_FLOOR = 0.03  # OOM, not a published Euclid result


def programme_path_rms(label: str, sigma0: float, r: float, d: float = 3.0) -> dict:
    """End-to-end path RMS at z_s=1.5 for a hand-placed NP corner."""
    s_res = residual_soft_map(sigma0, r=r)
    ell = ell_mpc_for_sigma(sigma0, d)  # cell from seed (counting)
    chi = comoving_distance_mpc(1.5)
    s_loc = slip_deviation(1.0, s_res, 0.8, 1.0)
    rms = rms_incoherent(s_loc, n_patches(chi, ell))
    return {
        "label": label,
        "sigma0": sigma0,
        "r": r,
        "sigma_res": s_res,
        "ell_mpc": ell,
        "slip_loc": s_loc,
        "chi": chi,
        "sqrtN": math.sqrt(chi / ell),
        "rms_path": rms,
    }


def ratio(a: float, b: float) -> float:
    return a / b if b > 0 else float("inf")


def main() -> None:
    print("=== Programme path-RMS (hand-placed NP corners; not derived) ===")
    np_a = programme_path_rms("NP-A", 1e-5, 0.0)
    np_b = programme_path_rms("NP-B", 5e-6, 1.5)
    for row in (np_a, np_b):
        print(
            f"  {row['label']}: sigma_res={row['sigma_res']:.3e}  "
            f"ell_*={row['ell_mpc']:.3f} Mpc  "
            f"|γ-1|_loc={row['slip_loc']:.3e}  "
            f"√N={row['sqrtN']:.1f}  "
            f"RMS_path={row['rms_path']:.3e}"
        )
    print()

    print("=== Published / forecast EXTERNAL anchors ===")
    print(f"  Maus γ = {MAUS_GAMMA} ± {MAUS_GAMMA_ERR}  [arXiv:{MAUS_ARXIV}]")
    print(f"    ⇒ 1σ on mean slip |γ−1| scale ~ {MAUS_GAMMA_ERR:.2f}")
    print(
        f"  Sakr η forecasts (Euclid-like ± DESI-like) [arXiv:{SAKR_ARXIV}]:"
    )
    print(f"    constant η: ~{100*SAKR_ETA_CONST_FRAC:.0f}%")
    print(f"    z-only:     <{100*SAKR_ETA_ZONLY_FRAC:.0f}% average")
    print(f"    free z,k:   ≥{100*SAKR_ETA_ZK_FRAC:.0f}%")
    print(
        f"  DESI MG Σ0 = {DESI_MG_SIGMA0} ± {DESI_MG_SIGMA0_ERR}, "
        f"μ0 = {DESI_MG_MU0} ± {DESI_MG_MU0_ERR}  [arXiv:{DESI_MG_ARXIV}]"
    )
    print(
        f"  Stage-IV multiplicative shear bias control OOM ~ "
        f"{STAGE4_M_MULT_BIAS_OOM:.0e}  [SRD arXiv:{STAGE4_SRD_ARXIV}; Euclid WL prep]"
    )
    print(f"  Programme historical mean-slip floor OOM: {PROG_MEAN_SLIP_FLOOR}")
    print()

    print("=== OOM ratios: external_error / programme_RMS  (>>1 ⇒ not yet reached) ===")
    print("  CAUTION: operators differ (mean slip / η / Σ vs stochastic path RMS).")
    print("  These ratios bound *how far* published precision sits above NP kinematics.")
    print()
    for name, err in (
        ("Maus σ(γ)", MAUS_GAMMA_ERR),
        ("Sakr 5% of η~1 (abs ~0.05)", SAKR_ETA_CONST_FRAC),
        ("Sakr free-zk ≥30% (abs ~0.30)", SAKR_ETA_ZK_FRAC),
        ("DESI MG σ(Σ0)", DESI_MG_SIGMA0_ERR),
        ("Stage-IV m-bias OOM", STAGE4_M_MULT_BIAS_OOM),
        ("Prog. mean-slip floor 0.03", PROG_MEAN_SLIP_FLOOR),
    ):
        ra = ratio(err, np_a["rms_path"])
        rb = ratio(err, np_b["rms_path"])
        print(f"  {name:32s}  / NP-A = {ra:8.1f}×   / NP-B = {rb:8.1f}×")
    print()

    print("=== Honesty locks (print every run) ===")
    print("  NP-A/B are HAND-PLACED corners, not derived open-kernel predictions.")
    print("  Published numbers constrain MEAN slip/MG parameters, not this path-RMS.")
    print("  Illegal: call Stage-IV m-bias ~1e-3 a detection of DE texture at RMS~1e-3.")
    print("  Illegal: null on mean γ kills the whole stochastic-grain programme.")
    print("  Legal: Maus O(0.1) and Sakr O(0.05–0.3) show mean-slip is still >> NP-B RMS.")
    print("See papers/lensing-rms-forecast-real-data.md")


if __name__ == "__main__":
    main()
