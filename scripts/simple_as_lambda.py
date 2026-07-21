#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimal model as simple as Λ: background ΛCDM + one grain σ + one light RMS.

  H² = H0² [Ωm(1+z)³ + ΩΛ]          # keep
  σ  = (ℓ*/L_H)^{3/2}                 # one grain parameter (d=3)
  RMS ~ σ^{2/3}                       # light-path order-of-magnitude

Also prints exact path RMS via lib_verified for comparison.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib_verified import (
    comoving_distance_mpc,
    ell_for_target_sigma,
    hubble_radius_m,
    n_patches,
    residual_soft_map,
    rms_incoherent,
    slip_deviation,
    sorkin_holographic,
)

MPC = 3.085677581e22


def simple_rms(sigma: float) -> float:
    """Blackboard formula RMS ~ sigma**(2/3) for d=3, chi ~ L_H."""
    return sigma ** (2.0 / 3.0)


def exact_path_rms(sigma_res: float, ell_mpc: float, z_src: float = 1.5, z_slip: float = 0.8) -> float:
    slip = slip_deviation(1.0, sigma_res, z_slip)
    chi = comoving_distance_mpc(z_src)
    return rms_incoherent(slip, n_patches(chi, ell_mpc))


def main() -> None:
    L_H, _, sorkin = sorkin_holographic()
    L_H_mpc = L_H / MPC

    print("=" * 64)
    print("AS SIMPLE AS Λ")
    print("=" * 64)
    print("Background:  H² = H0² [Ωm(1+z)³ + ΩΛ]     (keep ΛCDM)")
    print("Grain:       σ = (ℓ*/L_H)^{3/2}              (one number)")
    print("Light:       RMS ~ σ^{2/3}                   (one prediction)")
    print(f"L_H ≈ {L_H_mpc:.0f} Mpc")
    print()

    print(f"{'name':>14} {'sigma0':>12} {'ell*_Mpc':>12} {'s_res':>12} {'RMS~s^(2/3)':>12} {'path_RMS':>12} {'DESI':>8}")
    rows = [
        ("Sorkin d=2", sorkin, 0.0, 2),
        ("NP-A", 1e-5, 0.0, 3),
        ("NP-B", 5e-6, 1.5, 3),
    ]
    for name, sigma0, r, d in rows:
        sres = residual_soft_map(sigma0, r=r)
        ell_mpc = ell_for_target_sigma(sigma0, L_H, d) / MPC
        simple = simple_rms(sres)
        # path RMS only meaningful for mesoscopic ell; still compute
        exact = exact_path_rms(sres, max(ell_mpc, 1e-20))
        ok = "OK" if sres <= 1.5e-4 else "TENSION"
        print(
            f"{name:>14} {sigma0:12.2e} {ell_mpc:12.3e} {sres:12.2e} "
            f"{simple:12.3e} {exact:12.3e} {ok:>8}"
        )

    print()
    print("Rule: if it needs more symbols than Λ, it is an appendix.")
    print("Public model = Lines A–B–C only.")


if __name__ == "__main__":
    main()
