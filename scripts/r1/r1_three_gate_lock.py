#!/usr/bin/env python3
"""
Three-gate lock: sandwich cell ↔ DESI residual ceiling ↔ CF4 velocity scale.

Not an OU re-run. Uses numbers already produced by:
  - r1_sandwich_derivation / r1_sigma_R_full  → R_nl, sigma_free
  - sister DESI OU pipeline                  → sigma_X ceiling
  - r1_T2_real / r1_real_velocity_block_net  → CF4 r_e(v_pec)

Question locked here
--------------------
If the free residual counting cell is the matter nonlinear scale R_nl,
is that cell (i) below the DESI residual ceiling and (ii) consistent with
the measured CF4 peculiar-velocity coherence scale?

Gates
-----
  G1  sigma_free(R_nl, d=3)  ≲  DESI working ceiling 1.5e-4
  G2  CF4 r_e(v_pec)         ∈  [0.5, 3] R_nl
  G3  CF4 block eta(L=R_nl) is O(1) (gravity ~ expansion grain), not ≫1 forever

Non-claims
----------
  - No detection of DE residual.
  - No derivation of why ell_* must equal R_nl (still open kernel).
  - Multipole residual r_e ~ 80–120 Mpc/h is BAO-scale clustering, not G2.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "results" / "r1_three_gate"
OUT.mkdir(parents=True, exist_ok=True)

# --- locked numbers from prior real runs (recomputed here where pure) ---
H0 = 67.4  # km/s/Mpc (Planck-ish; only for L_H)
C_KMS = 299792.458
L_H = C_KMS / H0  # Mpc
R_NL = 8.6098  # from r1_sandwich / r1_sigma_R_full
D = 3
SIGMA_FREE = (R_NL / L_H) ** (D / 2)
DESI_CEILING = 1.5e-4  # working 95% CL OU kernel (sister repo)
CF4_RE = 19.27  # Mpc, L=20 block-net; jk err in results/r1_cf4_jackknife
BAND = (0.5 * R_NL, 3.0 * R_NL)

# CF4 block-net eta at L near R_nl (from cf4_block_net.txt: L=10 → eta=1.39)
# Interpolate eta(L) from published run table
_L = np.array([5.0, 10.0, 15.0, 20.0, 30.0, 40.0])
_ETA = np.array([2.40, 1.39, 1.00, 0.76, 0.44, 0.35])
ETA_AT_RNL = float(np.interp(R_NL, _L, _ETA))

# Path RMS free (from falsifiers JSON if present)
FALS = ROOT / "results" / "r1_falsifiers"
RMS_PATH_FREE = None
for p in FALS.glob("*.json"):
    try:
        pred = json.loads(p.read_text()).get("predictions", {})
        if "RMS_path_free" in pred:
            RMS_PATH_FREE = float(pred["RMS_path_free"])
            break
    except Exception:
        pass
if RMS_PATH_FREE is None:
    # OOM: |γ-1|_loc ~ 2 σ_free * (ρx/ρm)/δ ~ few × 10^{-5}; RMS = local * sqrt(χ/R_nl)
    RMS_PATH_FREE = 0.00145  # matches prior falsifier freeze


def main() -> int:
    g1 = SIGMA_FREE <= DESI_CEILING
    g2 = BAND[0] <= CF4_RE <= BAND[1]
    g3 = 0.3 <= ETA_AT_RNL <= 3.0  # O(1) grain, not diverging

    ratio_ceiling = DESI_CEILING / SIGMA_FREE
    ratio_re = CF4_RE / R_NL

    gates = {
        "G1_sigma_free_below_DESI_ceiling": {
            "pass": g1,
            "sigma_free": SIGMA_FREE,
            "DESI_ceiling": DESI_CEILING,
            "ceiling_over_free": ratio_ceiling,
            "meaning": "Counting at R_nl does not overshoot the DESI residual null.",
        },
        "G2_CF4_re_in_sandwich_band": {
            "pass": g2,
            "CF4_r_e_Mpc": CF4_RE,
            "R_nl_Mpc": R_NL,
            "r_e_over_R_nl": ratio_re,
            "band_Mpc": list(BAND),
            "meaning": "Matter velocity coherence lives in the same decade as R_nl.",
        },
        "G3_eta_O1_at_R_nl": {
            "pass": g3,
            "eta_interp_at_R_nl": ETA_AT_RNL,
            "meaning": "At L~R_nl, block v_pec rms is order Hubble flow on that grain.",
        },
    }
    all_pass = all(g["pass"] for g in gates.values())

    out = {
        "question": (
            "If the free residual cell is R_nl, is it DESI-safe and "
            "CF4-scale-consistent?"
        ),
        "answer_now": "YES_ALL_THREE_GATES" if all_pass else "FAIL_SOME_GATE",
        "all_gates_pass": all_pass,
        "inputs": {
            "R_nl_Mpc": R_NL,
            "L_H_Mpc": L_H,
            "d": D,
            "sigma_free": SIGMA_FREE,
            "N_eff": (L_H / R_NL) ** D,
            "DESI_sigma_X_working_ceiling": DESI_CEILING,
            "CF4_r_e_Mpc": CF4_RE,
            "RMS_path_free_OOM": RMS_PATH_FREE,
        },
        "gates": gates,
        "next_hard_question_still_open": (
            "What principle fixes ell_* = R_nl (or any mesoscopic cell) "
            "for the DE sector? Gates only show compatibility, not derivation."
        ),
        "non_claims": [
            "No DE residual detection",
            "No proof that ell_* must equal R_nl",
            "Multipole residual r_e is not a residual-grain measurement",
        ],
    }

    (OUT / "three_gate_lock.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    lines = [
        "THREE-GATE LOCK (beyond OU null)",
        "=" * 50,
        "Q: If free residual cell = R_nl, is it DESI-safe and CF4-consistent?",
        f"A: {out['answer_now']}",
        "",
        f"R_nl          = {R_NL:.4f} Mpc",
        f"L_H           = {L_H:.1f} Mpc",
        f"sigma_free    = {SIGMA_FREE:.6e}   (d={D})",
        f"DESI ceiling  = {DESI_CEILING:.2e}",
        f"ceiling/free  = {ratio_ceiling:.3f}",
        f"CF4 r_e       = {CF4_RE:.1f} Mpc  (= {ratio_re:.3f} R_nl)",
        f"band          = [{BAND[0]:.2f}, {BAND[1]:.2f}] Mpc",
        f"eta(L~R_nl)   = {ETA_AT_RNL:.2f}",
        f"RMS_path free ≈ {RMS_PATH_FREE:.4e}  (OOM slip path)",
        "",
        "GATES:",
    ]
    for k, g in gates.items():
        flag = "PASS" if g["pass"] else "FAIL"
        lines.append(f"  [{flag}] {k}: {g['meaning']}")
    lines += [
        "",
        "STILL OPEN (not answered by this lock):",
        "  " + out["next_hard_question_still_open"],
        "",
        "Non-claims: " + "; ".join(out["non_claims"]),
        "",
    ]
    text = "\n".join(lines)
    (OUT / "three_gate_lock.txt").write_text(text, encoding="utf-8")
    print(text)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
