#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Geometry for H0-running / mesoscopic-grain scale comparison.

Does NOT fit H0(z). Does NOT claim brachistochrone = photon path.
Does: chi(z), z_eq, N=chi/R_8, SH0ES/Planck ratio arithmetic.

See papers/h0-running-brachistochrone-bridge.md
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lib_verified import (  # noqa: E402
    H0_KM_S_MPC,
    OL0,
    OM0,
    comoving_distance_mpc,
    r8_mpc,
)

# Literature anchors (not fitted here)
H0_PLANCK = 67.4
H0_SHOES = 73.0  # OOM local ladder
H0_HOLICOW = 73.3  # Wong et al. 2020


def z_eq_matter_de(Om: float = OM0, Ol: float = OL0) -> float:
    """Redshift of matter–DE density equality for constant DE."""
    return (Ol / Om) ** (1.0 / 3.0) - 1.0


def lookback_over_tH(z: float, Om: float = OM0, Ol: float = OL0, n: int = 2000) -> float:
    """t_lb / (1/H0) = ∫_0^z dz' / [(1+z') E(z')]."""
    import numpy as np

    if z < 0:
        raise ValueError("z>=0")
    if z == 0:
        return 0.0
    zs = np.linspace(0.0, z, n)

    def E(zi: float) -> float:
        return math.sqrt(Om * (1.0 + zi) ** 3 + Ol)

    integ = np.trapezoid([1.0 / ((1.0 + float(zi)) * E(float(zi))) for zi in zs], zs)
    return float(integ)


def main() -> None:
    R8 = r8_mpc()
    L_H = 299792.458 / H0_KM_S_MPC
    zeq = z_eq_matter_de()
    ratio = H0_SHOES / H0_PLANCK

    print("=== H0 tension numbers (literature anchors, not fits) ===")
    print(f"  H0_Planck class = {H0_PLANCK}")
    print(f"  H0_SH0ES OOM    = {H0_SHOES}")
    print(f"  H0_H0LiCOW      = {H0_HOLICOW}  (Wong+2020)")
    print(f"  ratio SH0ES/Planck = {ratio:.4f}")
    print()

    print("=== Fixed gravity local regime ===")
    print("  z << 1: H(z)≈H0  (definition of local ladder, not Bernoulli g)")
    print()

    print("=== Geometry (fiducial flat LCDM) ===")
    print(f"  L_H = {L_H:.1f} Mpc")
    print(f"  R_8 = 8/h = {R8:.3f} Mpc")
    print(f"  z_eq (matter=DE) = {zeq:.3f}")
    print()
    print(f"{'z':>6} {'chi':>8} {'chi/LH':>8} {'N=chi/R8':>10} {'sqrtN':>8} {'t_lb/tH':>8}")
    for z in (0.15, 0.30, 0.50, 0.70, 1.0, 1.5):
        chi = comoving_distance_mpc(z)
        N = chi / R8
        print(
            f"{z:6.2f} {chi:8.1f} {chi/L_H:8.3f} {N:10.1f} {math.sqrt(N):8.2f} "
            f"{lookback_over_tH(z):8.3f}"
        )
    print()

    print("=== Scale-class comparison (not a derivation) ===")
    print(f"  Literature H0-running window often quoted: z ~ 0.5–0.7")
    print(f"  Matter–DE equality: z_eq ~ {zeq:.2f}  (adjacent, not identical)")
    print(f"  At z=0.5: N_patches(R8) ~ {comoving_distance_mpc(0.5)/R8:.0f}")
    print(f"  At z=0.7: N_patches(R8) ~ {comoving_distance_mpc(0.7)/R8:.0f}")
    print()
    print("Illegal: claim cycloid brachistochrone derives H0=73/67")
    print("Illegal: fit ell_* to reproduce ratio 1.083")
    print("Legal: multi-path light = time-delay; H0 running = published trend class")
    print("Legal: mesoscopic grain and H0-running share late-time depth class")
    print("See papers/h0-running-brachistochrone-bridge.md")


if __name__ == "__main__":
    main()
