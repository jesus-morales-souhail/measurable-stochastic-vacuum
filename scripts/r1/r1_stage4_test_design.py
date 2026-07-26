#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stage-IV / DESI test design for residual grain at R_nl (Line B).

Predicts working-point signatures and compares to published floors.
Unique fingerprint: residual correlated with nonlinear structure on ~R_nl,
NOT an 8% H0 jump.

See papers/r1_kernel/FRONTIER_INQUIRY.md
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
OUT = ROOT / "results" / "r1_stage4_design"
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

DESI_X = 1.5e-4
MAUS = 0.11
SAKR = 0.05
H0_TENSION = 0.08  # ~8% local vs CMB class


def main() -> None:
    Pk = make_Pk_unnorm()
    A = normalize_A(Pk, SIGMA8)
    R_nl = find_R_nl(Pk, A, 1.0) / H_FID
    sf = sigma_from_count(R_nl, hubble_radius_mpc(), 3)
    lam = math.sqrt(max(DESI_X**2 - sf**2, 0.0))
    g = lam / sf
    s_work = DESI_X

    # Observables
    slip_f = slip_deviation(1.0, sf, 0.8, 1.0)
    slip_w = slip_deviation(1.0, s_work, 0.8, 1.0)
    chi = comoving_distance_mpc(1.5)
    n_pat = n_patches(chi, R_nl)
    rms_f = rms_incoherent(slip_f, n_pat)
    rms_w = rms_incoherent(slip_w, n_pat)

    # k scale of unique fingerprint
    k_nl_h = 1.0 / (R_nl * H_FID)  # h/Mpc rough
    ell_sep = R_nl * (0.1587) ** (-1.0 / 3.0)  # packing δc=1

    # Gap to H0
    gap_sigma = H0_TENSION / sf
    gap_rms = H0_TENSION / rms_w

    tests = [
        {
            "id": "T1_BAO_residual",
            "observable": "DESI/Euclid BAO residual σ_X (OU/QNM)",
            "prediction": sf,
            "ceiling": DESI_X,
            "floor_now": DESI_X,
            "unique_fingerprint": "Amplitude only; lock ell_*=R_nl (no float)",
            "stage4_action": "Tighten σ_X with DR3/Euclid BAO; pre-register ell_*=R_nl",
            "kills_if": "σ_X >> 1.5e-4 at fixed R_nl with no damping",
            "supports_if": "σ_X stays under ceiling; optional detection near free grain",
        },
        {
            "id": "T2_scale_band",
            "observable": "Residual correlation length / preferred scale",
            "prediction_Mpc": R_nl,
            "band_Mpc": [0.5 * R_nl, 3.0 * R_nl],
            "k_nl_h_per_Mpc": k_nl_h,
            "ell_sep_Mpc": ell_sep,
            "unique_fingerprint": "Power or residual support peaks near R_nl–ell_sep, not L_H",
            "stage4_action": "Search residual×matter cross or mask-weighted slip at k~0.1 h/Mpc",
            "kills_if": "Free residual ξ << 1 Mpc or >> 100 Mpc at σ~1e-4",
            "supports_if": "Measured scale in O(1)×R_nl band",
        },
        {
            "id": "T3_slip_mean",
            "observable": "Mean gravitational slip |γ−1| or |η−1|",
            "prediction_local": slip_w,
            "floor_Maus": MAUS,
            "floor_Sakr": SAKR,
            "gap_Maus": MAUS / slip_w,
            "unique_fingerprint": "Weak alone (MG degenerate); use as consistency",
            "stage4_action": "Do NOT claim detection until σ(η) << 1e-3; combine with T2",
            "kills_if": "Data force |γ−1| >> 0.01 for eps~1 at DESI-safe σ (unexpected)",
            "supports_if": "Remains consistent with << Maus/Sakr",
        },
        {
            "id": "T4_path_RMS",
            "observable": "Path-accumulated slip RMS (stochastic proxy)",
            "prediction": rms_w,
            "floor_Sakr_mean_eta": SAKR,
            "gap": SAKR / rms_w,
            "unique_fingerprint": "Stochastic path accumulation s√N; not shear m-bias",
            "stage4_action": "Define survey proxy for path variance of slip; never use m~1e-3 as this",
            "kills_if": "Proxy measured >> few % without systematics",
            "supports_if": "Proxy upper limits approach 1e-3 from above",
        },
        {
            "id": "T5_NOT_H0",
            "observable": "H0 tension ~8%",
            "prediction_from_grain": "INSUFFICIENT",
            "gap_factor_vs_sigma": gap_sigma,
            "gap_factor_vs_path_RMS": gap_rms,
            "unique_fingerprint": "None — wrong problem for this sector",
            "stage4_action": "Outsource to early DE / ladder / large-scale mean; do not force g",
            "kills_if": "N/A (already excluded as explanation)",
            "supports_if": "N/A",
        },
    ]

    out = {
        "R_nl_Mpc": R_nl,
        "sigma_free": sf,
        "lambda_work": lam,
        "g_work": g,
        "sigma_work_ceiling": s_work,
        "slip_local_free": slip_f,
        "slip_local_work": slip_w,
        "RMS_path_free": rms_f,
        "RMS_path_work": rms_w,
        "N_patches_z1p5": n_pat,
        "k_nl_approx_h_Mpc": k_nl_h,
        "ell_sep_Mpc": ell_sep,
        "H0_8pct_over_sigma": gap_sigma,
        "H0_8pct_over_RMS": gap_rms,
        "tests": tests,
        "design_principle": (
            "Unique fingerprint = residual correlated with nonlinear structure "
            "on ~R_nl (8–16 Mpc), amplitude 1e-5–1e-4 — NOT 8% H0."
        ),
    }
    (OUT / "stage4_test_design.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    lines = [
        "STAGE-IV / DESI TEST DESIGN — residual grain (Line B)",
        f"R_nl={R_nl:.4f} Mpc  sigma_free={sf:.6e}  g_work={g:.4f}",
        f"slip_loc work={slip_w:.4e}  RMS_path work={rms_w:.4e}  N_pat={n_pat:.1f}",
        f"k_nl ~ {k_nl_h:.4f} h/Mpc  ell_sep={ell_sep:.2f} Mpc",
        f"H0 8% / sigma_free = {gap_sigma:.0f}×  |  H0 8% / RMS_path = {gap_rms:.0f}×",
        "",
        "DESIGN PRINCIPLE:",
        "  Unique signature = residual × structure at R_nl, σ ~ 1e-5–1e-4",
        "  NOT an 8% H0 jump (short by ~30–1000× depending on operator)",
        "",
        "TESTS:",
    ]
    for t in tests:
        lines.append(f"  [{t['id']}] {t['observable']}")
        lines.append(f"    action: {t['stage4_action']}")
        lines.append(f"    kills:  {t['kills_if']}")
    lines.append("")
    lines.append("See papers/r1_kernel/FRONTIER_INQUIRY.md")
    txt = "\n".join(lines) + "\n"
    (OUT / "stage4_test_design.txt").write_text(txt, encoding="utf-8")
    print(txt)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
