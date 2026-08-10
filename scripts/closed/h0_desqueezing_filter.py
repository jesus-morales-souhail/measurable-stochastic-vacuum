#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filter: desqueezing is real; H0(z)=H0_fid[1+ε exp(-θ x)] with θ fitted to z~0.5–0.7 is not.

Legal amplitude bound (no free θ to the 9%):
  |δH/H| ≲ σ  ≤ σ_X_DESI = 2.5e-2  <<  0.083 ≈ 73/67.4 - 1

Even θ→0 (no damping) cannot reach the Hubble tension under the residual bound.
Complex ω only phases the correlator; it does not raise the allowed σ.

Also records:
  - σ_X lives on x=ln a (temporal)
  - BAO-only (w0,wa)≈(-0.99,-0.02) from sister summary
  - 2.5σ/4.2σ are CPL dynamical-DE figures, NOT H0-running

See papers/h0-desqueezing-filter.md
"""

from __future__ import annotations

import math

SIGMA_X_DESI = 2.5e-2
H0_PLANCK = 67.4
H0_SHOES = 73.0
RATIO = H0_SHOES / H0_PLANCK
DELTA_H0 = RATIO - 1.0  # ~0.083

# Sister BAO-only CPL (eos_cpl_summary.txt) — not a fit here
W0_BAO = -0.9899
WA_BAO = -0.0159

# Programme θ anchors (a priori / measured floors — NOT tuned to H0 knee)
THETA_MLE_FLOOR = 1e-3
THETA_NESTED_EXAMPLE = 1.7339  # with σ→0 in nested BAO; not preferred


def residual_envelope(sigma: float, theta: float, dx: float) -> float:
    """|X| ≲ σ e^{-θ Δx}  (OU / desqueezing residual track)."""
    return abs(sigma) * math.exp(-abs(theta) * abs(dx))


def shortfall(max_frac: float, target: float = DELTA_H0) -> float:
    return target / max_frac if max_frac > 0 else float("inf")


def main() -> None:
    print("=== H0 / desqueezing FILTER (no free θ to the 9%) ===")
    print(f"  Observed H0 ratio SH0ES/Planck ≈ {RATIO:.4f}  (δ ≈ {DELTA_H0:.4f})")
    print(f"  DESI residual ceiling σ_X < {SIGMA_X_DESI:.1e} (95% CL)")
    print(f"  BAO-only (w0,wa) ≈ ({W0_BAO:.4f}, {WA_BAO:.4f})  [sister eos_cpl_summary]")
    print()

    print("--- Amplitude ceiling (θ → 0, most optimistic) ---")
    print(f"  max |δH/H| ≲ σ_X = {SIGMA_X_DESI:.3e}")
    print(f"  shortfall vs 8.3% tension: ×{shortfall(SIGMA_X_DESI):.0f}")
    print("  ⇒ DESI-safe residual CANNOT source ~9% H0 drift")
    print()

    print("--- Envelope examples (σ=σ_X, θ from repo anchors, not H0-fit) ---")
    print(f"{'θ':>8} {'Δx':>6} {'|X|max':>12} {'shortfall':>10}")
    for theta in (0.0, THETA_MLE_FLOOR, 1.0, THETA_NESTED_EXAMPLE):
        for dx in (0.0, 0.5, 1.0, math.log(1.5)):  # includes z~0.5 path in e-folds OOM
            env = residual_envelope(SIGMA_X_DESI, theta, dx)
            print(f"{theta:8.4f} {dx:6.3f} {env:12.3e} {shortfall(env):10.1f}")
    print()

    print("--- Illegal construction (do not publish as result) ---")
    print("  H0(z)=H0_fid[1+ε exp(-θ x)] with θ~0.47 chosen so knee is at z~0.5–0.7")
    print("  Status: REJECT (undeclared free form + post-hoc θ)")
    print()

    print("--- Label hygiene ---")
    print("  2.5σ / 4.2σ in DESI multi-probe CPL abstract = dynamical mean DE preference")
    print("  NOT an H0-running significance. Do not paste into H0-running tables.")
    print("  σ_X is defined on x=ln a (temporal e-folds), not 'spatial only'.")
    print()

    print("--- Complex ω ---")
    print("  ω = ω_R - i γ/2  and  t_1/2 = ln2/γ  are REAL (desqueezing scans).")
    print("  They do not raise σ above 2.5e-2. Phase ≠ free energy for 9% H0.")
    print()
    print("See papers/h0-desqueezing-filter.md")


if __name__ == "__main__":
    main()
