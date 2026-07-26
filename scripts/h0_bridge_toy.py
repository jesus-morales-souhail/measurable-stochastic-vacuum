#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Toy a priori bridge: path depth → fractional distance bias shape.

δD/D models (explicitly labelled):
  (S) stochastic / incoherent:  |δD/D| = s_loc * sqrt(χ/ℓ_*)     [path RMS]
  (C) coherent accumulation:    |δD/D| = s_loc * (χ/ℓ_*)         [usually excluded]
  (N) shape-only normalized:    f(z) = sqrt(χ(z)/χ(z_ref))       [no amplitude]

ℓ_* is FIXED a priori from R1 counting landscape (not fitted to H0):
  NP-A d=3, σ=1e-5 → ℓ_* ≈ 2.07 Mpc
  R1d-class R_8     → ℓ_* ≈ 11.87 Mpc

s_loc from Einstein+Morales wall at DESI ceiling (a posteriori ceiling, not a dial):
  s_loc = |γ-1|(σ_X=1.5e-4, ε=1, z_eval=0.5, δ_m=1)

Illegal: fit ℓ_* or s_loc to make H0_local/H0_CMB = 1.083.
Legal: predict shape f(z); report amplitude shortfall vs 9% tension.

See papers/h0-bridge-toy-map.md
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from lib_verified import (  # noqa: E402
    comoving_distance_mpc,
    ell_mpc_for_sigma,
    r8_mpc,
    slip_deviation,
)

# --- A priori fixed scales (R1 landscape) ---
ELL_NPA = ell_mpc_for_sigma(1e-5, 3)  # ~2.07 Mpc
ELL_R8 = r8_mpc()

# Local slip amplitude at DESI residual ceiling (wall formula)
S_LOC = slip_deviation(1.0, 1.5e-4, 0.5, 1.0)

# Literature anchors
H0_CMB = 67.4
H0_LOCAL = 73.0
RATIO_OBS = H0_LOCAL / H0_CMB  # ~1.083
DELTA_OBS = RATIO_OBS - 1.0  # ~0.083 if H0_inf = H0_true * (1+δ) convention below

# Redshift grid
Z_GRID = (0.05, 0.10, 0.15, 0.30, 0.50, 0.70, 1.0, 1.5, 2.0)
Z_REF = 1.5  # reference depth for shape-only


def chi(z: float) -> float:
    return comoving_distance_mpc(z)


def delta_stoch(z: float, ell: float, s_loc: float = S_LOC) -> float:
    """Incoherent path bias scale |δD/D| ~ s √(χ/ℓ)."""
    return s_loc * math.sqrt(chi(z) / ell)


def delta_coherent(z: float, ell: float, s_loc: float = S_LOC) -> float:
    """Coherent accumulation |δD/D| ~ s (χ/ℓ) — flagged as usually excluded."""
    return s_loc * (chi(z) / ell)


def shape_norm(z: float, z_ref: float = Z_REF) -> float:
    """Amplitude-free shape f(z)=√(χ/χ_ref), f(z_ref)=1."""
    return math.sqrt(chi(z) / chi(z_ref))


def h0_inferred_from_bias(h0_true: float, delta: float, sign: str = "low_z_high") -> float:
    """
    Toy: if distance is overestimated by δ, inferred H0 is lower (D∝1/H0).
    For tension: local (small δ) → high H0; deep (large δ) → low H0.

    H0_inf ≈ H0_true / (1+δ)  with δ = |δD/D| growing with depth.
    Then H0(z_low)/H0(z_deep) ≈ (1+δ_deep)/(1+δ_low) > 1.
    """
    return h0_true / (1.0 + abs(delta))


def ratio_local_to_deep(
    ell: float,
    z_local: float = 0.15,
    z_deep: float = 1.5,
    mode: str = "S",
) -> float:
    if mode == "S":
        d_lo, d_hi = delta_stoch(z_local, ell), delta_stoch(z_deep, ell)
    elif mode == "C":
        d_lo, d_hi = delta_coherent(z_local, ell), delta_coherent(z_deep, ell)
    else:
        raise ValueError("mode S or C")
    h_lo = h0_inferred_from_bias(H0_CMB, d_lo)
    h_hi = h0_inferred_from_bias(H0_CMB, d_hi)
    return h_lo / h_hi


def beta_needed_for_ratio(
    ell: float,
    z_local: float = 0.15,
    z_deep: float = 1.5,
    target_ratio: float = RATIO_OBS,
    mode: str = "S",
) -> float:
    """
    If |δD/D| = β * base(z), find β so that H0_lo/H0_hi = target_ratio.
    base = √(χ/ℓ) for S, χ/ℓ for C. Report β and implied s_loc = β.
    """
    if mode == "S":
        b_lo = math.sqrt(chi(z_local) / ell)
        b_hi = math.sqrt(chi(z_deep) / ell)
    else:
        b_lo = chi(z_local) / ell
        b_hi = chi(z_deep) / ell
    # (1+β b_hi)/(1+β b_lo) = R  ⇒ β (R b_lo - b_hi) = 1-R  ⇒ β = (R-1)/(b_hi - R b_lo)
    denom = b_hi - target_ratio * b_lo
    if denom <= 0:
        return float("inf")
    return (target_ratio - 1.0) / denom


def table_rows(ell: float, label: str) -> List[Dict]:
    rows = []
    for z in Z_GRID:
        rows.append(
            {
                "label": label,
                "ell": ell,
                "z": z,
                "chi": chi(z),
                "f_shape": shape_norm(z),
                "dS": delta_stoch(z, ell),
                "dC": delta_coherent(z, ell),
                "H0_S": h0_inferred_from_bias(H0_CMB, delta_stoch(z, ell)),
                "H0_C": h0_inferred_from_bias(H0_CMB, delta_coherent(z, ell)),
            }
        )
    return rows


def main() -> None:
    print("=== H0 bridge toy map (a priori ℓ_*, no H0 fit) ===")
    print(f"  ℓ_* NP-A (d=3,σ=1e-5) = {ELL_NPA:.4f} Mpc")
    print(f"  ℓ_* R8 class           = {ELL_R8:.4f} Mpc")
    print(f"  s_loc = |γ−1|(σ_X=1.5e-4,z=0.5) = {S_LOC:.6e}")
    print(f"  Observed ratio SH0ES/Planck OOM = {RATIO_OBS:.4f} (δ~{DELTA_OBS:.4f})")
    print()

    for ell, lab in ((ELL_NPA, "NP-A"), (ELL_R8, "R8")):
        print(f"--- {lab}: ℓ_*={ell:.3f} Mpc ---")
        print(f"{'z':>6} {'f_shape':>8} {'δS=s√N':>10} {'δC=sN':>10} {'H0_S':>8} {'H0_C':>8}")
        for row in table_rows(ell, lab):
            print(
                f"{row['z']:6.2f} {row['f_shape']:8.3f} {row['dS']:10.3e} {row['dC']:10.3e} "
                f"{row['H0_S']:8.2f} {row['H0_C']:8.2f}"
            )
        rS = ratio_local_to_deep(ell, mode="S")
        rC = ratio_local_to_deep(ell, mode="C")
        bS = beta_needed_for_ratio(ell, mode="S")
        bC = beta_needed_for_ratio(ell, mode="C")
        print(f"  ratio H0(0.15)/H0(1.5) stochastic = {rS:.5f}  (obs ~ {RATIO_OBS:.3f})")
        print(f"  ratio H0(0.15)/H0(1.5) coherent   = {rC:.5f}")
        print(f"  β needed for ratio=1.083 if δ=β√(χ/ℓ): β={bS:.4e}  (wall s_loc={S_LOC:.4e}, short ×{bS/S_LOC:.1f})")
        print(f"  β needed for ratio=1.083 if δ=β(χ/ℓ):  β={bC:.4e}  (wall s_loc={S_LOC:.4e}, ×{bC/S_LOC:.2f})")
        print()

    # Shape transition: where f_shape crosses 0.5 of deep reference
    print("=== Shape-only (amplitude free) ===")
    print("  f(z)=√(χ(z)/χ(1.5)); literature running window often z~0.5–0.7")
    for z in (0.3, 0.5, 0.7, 1.0):
        print(f"  f({z}) = {shape_norm(z):.3f}")
    print()
    print("Verdict:")
    print("  Stochastic DESI-safe path bias: ratio shift O(0.1%) not O(8%) — SHORT of H0 tension")
    print("  Coherent accumulation: can OOM-match ratio but is the excluded amplifier class")
    print("  Shape f(z) varies through z~0.5–0.7 — scale class only")
    print("Illegal: raise s_loc or switch to coherent after seeing 1.083")
    print("See papers/h0-bridge-toy-map.md")


if __name__ == "__main__":
    main()
