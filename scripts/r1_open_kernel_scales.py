#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
R1 open-kernel scale table (arithmetic only).

Prints the mesoscopic landscape next to the conventional R_8 = 8/h Mpc
anchor. Does NOT fit ell_* to DESI or to S8. Does NOT claim ell_* = R_8.

See papers/r1-open-kernel.md.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lib_verified import (  # noqa: E402
    H0_KM_S_MPC,
    ell_mpc_for_sigma,
    hubble_radius_mpc,
    r8_mpc,
    sigma_for_cell_mpc,
    sorkin_holographic,
)

DESI_CEILING = 1.5e-4
SIGMA_TARGET = 1e-5


def main() -> None:
    L_H = hubble_radius_mpc()
    R8 = r8_mpc()
    _, _, s0 = sorkin_holographic()

    print("R1 open-kernel scale anchors (verified arithmetic only)")
    print(f"  H0 = {H0_KM_S_MPC} km/s/Mpc")
    print(f"  L_H = {L_H:.2f} Mpc")
    print(f"  R_8 = 8/h = {R8:.4f} Mpc   (scale anchor, not a fit)")
    print(f"  Sorkin sigma_0 = {s0:.3e}")
    print()

    print(f"ell_* required for sigma = {SIGMA_TARGET:.0e} (counting inverse):")
    for d in (2, 3, 4):
        ell = ell_mpc_for_sigma(SIGMA_TARGET, d)
        print(f"  d={d}: ell_* = {ell:.4f} Mpc   |ell_*/R_8 - 1| = {abs(ell/R8 - 1):.3f}")
    print()

    print(f"ell_* required for sigma = {DESI_CEILING:.1e} (DESI residual ceiling, a posteriori scale):")
    for d in (2, 3, 4):
        ell = ell_mpc_for_sigma(DESI_CEILING, d)
        print(f"  d={d}: ell_* = {ell:.4f} Mpc   |ell_*/R_8 - 1| = {abs(ell/R8 - 1):.3f}")
    print()

    print("If ell_* were fixed to R_8 (hypothesis class R1d — NOT derived):")
    for d in (2, 3, 4):
        s = sigma_for_cell_mpc(R8, d)
        print(f"  d={d}: sigma_0,eff = {s:.4e}")
    print()

    # Near row + d-fragility (honesty: proximity is not multi-d robust)
    print("Proximity to R_8 at sigma = DESI ceiling (fragility in d):")
    for d in (2, 3, 4):
        ell = ell_mpc_for_sigma(DESI_CEILING, d)
        frac = abs(ell / R8 - 1.0)
        tag = "NEAR" if frac < 0.10 else "FAR"
        print(f"  d={d}: ell_* = {ell:.3f} Mpc  |ell_*/R_8-1| = {frac:.3f}  -> {tag}")
    print("  Honesty: near-coincidence is SPECIFIC to d=3; d=2 and d=4 do not reproduce it.")
    print()

    s_r8_d3 = sigma_for_cell_mpc(R8, 3)
    print("If ell_*=R_8 and d=3 (hypothesis class R1d — NOT derived):")
    print(f"  sigma = {s_r8_d3:.6e}  vs DESI ceiling {DESI_CEILING:.1e}  (tolerate, not prefer)")
    print()
    print("OPEN KERNEL (unchanged): principle fixing ell_* is ABSENT (declared).")
    print("Illegal: choose the row that matches DESI/S8 and call it derived.")
    print("Illegal: treat d=3 proximity as multi-d robustness.")
    print("See papers/r1-open-kernel.md")


if __name__ == "__main__":
    main()
