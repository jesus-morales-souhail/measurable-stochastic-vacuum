#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Atlas: inflationary spectator seed → residual-scale OOM (not a DESI fit).

Physics (standard):
  P_s = A_s ≈ 2.1e-9
  r = P_t / P_s
  P_t = 2 H^2 / (π² M_p²)  ⇒  H/M_p = π √(r A_s / 2)
  Light spectator:  δQ/M_p = H/(2π M_p) = √(r A_s / 8)   [rms order]

Fractional DE density contrast for potential-dominated quintessence:
  δρ/ρ ≈ (V'/V) δQ = √(2 ε_Q) (δQ/M_p)
  with ε_Q = (M_p²/2)(V'/V)²  (first slow-roll of DE potential)

Post-inflation field growth A = δQ_f/δQ_i (Gordon & Wands need A>45 for *their* target).

This atlas answers:
  For modern r upper bounds, what residual amplitude σ_ρ can a spectator seed
  reach *if* ε_Q and A are given — without ever using Sorkin σ_0 ~ 1e-61?

Illegal: fit ε_Q or A to DESI. Legal: show which (r, A, ε_Q) windows
hit 1e-5 / 1.5e-4 a posteriori.

See papers/inflation-spectator-residual-atlas.md
"""

from __future__ import annotations

import math
from typing import Dict, List, Tuple

# Observed scalar amplitude (Planck-class OOM)
A_S = 2.1e-9

# Modern tensor anchors (95% CL class; cite in paper note)
# BICEP/Keck + Planck combinations: r ≲ 0.036 (often quoted)
R_BK_95 = 0.036
# Slightly looser / older combinations ~0.056
R_LOOSE_95 = 0.056
# Illustrative lower scale
R_LOW = 0.001

# Programme residual anchors
SIGMA_EUCLID = 1e-5
SIGMA_DESI = 1.5e-4

# Gordon & Wands growth factor (their Eq. 27) — for *their* target; here a scan param
A_GW = 45.0


def h_over_mp(r: float) -> float:
    """H_inf / M_p from r and A_s."""
    if r <= 0:
        raise ValueError("r must be positive")
    return math.pi * math.sqrt(r * A_S / 2.0)


def delta_q_over_mp(r: float) -> float:
    """rms δQ/M_p = H/(2π M_p)."""
    return h_over_mp(r) / (2.0 * math.pi)


def sigma_rho(r: float, eps_q: float, amp: float = 1.0) -> float:
    """
    |δρ/ρ| ~ √(2 ε_Q) * A * (δQ_i/M_p)
    Requires eps_q >= 0, amp >= 0.
    """
    if eps_q < 0 or amp < 0:
        raise ValueError("eps_q and amp must be non-negative")
    return math.sqrt(2.0 * eps_q) * amp * delta_q_over_mp(r)


def gap_to_target(sigma: float, target: float) -> float:
    """How many× short of target ( >1 means below target)."""
    if sigma <= 0:
        return float("inf")
    return target / sigma


def scan_table() -> List[Dict]:
    rows = []
    for r in (R_LOW, 0.01, R_BK_95, R_LOOSE_95):
        for amp in (1.0, A_GW, 100.0):
            for eps in (1e-4, 1e-2, 0.05, 0.25, 1.0):
                s = sigma_rho(r, eps, amp)
                rows.append(
                    {
                        "r": r,
                        "A": amp,
                        "eps_Q": eps,
                        "dQ_Mp": delta_q_over_mp(r),
                        "sigma": s,
                        "G_Euclid": gap_to_target(s, SIGMA_EUCLID),
                        "G_DESI": gap_to_target(s, SIGMA_DESI),
                    }
                )
    return rows


def windows_hitting_band() -> List[Dict]:
    """(r,A,eps) that land sigma in [1e-5, 1.5e-4] without tuning claim."""
    hits = []
    for row in scan_table():
        if SIGMA_EUCLID <= row["sigma"] <= SIGMA_DESI:
            hits.append(row)
    return hits


def sorkin_compare() -> Tuple[float, float]:
    """Sorkin gaps for contrast (imported from same numbers as gap_two_targets)."""
    sigma0 = 1.1776e-61  # approx holographic
    return SIGMA_EUCLID / sigma0, SIGMA_DESI / sigma0


def main() -> None:
    print("=== Inflation spectator residual atlas (OOM) ===")
    print(f"A_s = {A_S:.2e}")
    print(f"Modern r anchors: BK-class {R_BK_95}, loose {R_LOOSE_95}, low {R_LOW}")
    print()

    print("δQ/M_p = H/(2π M_p) at horizon exit (no A, no ε):")
    for r in (R_LOW, 0.01, R_BK_95, R_LOOSE_95):
        print(
            f"  r={r:<6}  H/M_p={h_over_mp(r):.3e}  "
            f"δQ/M_p={delta_q_over_mp(r):.3e}"
        )
    print()

    print("Residual σ_ρ ≈ √(2ε_Q)·A·(δQ/M_p)  [potential-dominated OOM]")
    print(f"{'r':>6} {'A':>6} {'ε_Q':>8} {'σ_ρ':>10} {'/1e-5':>10} {'/1.5e-4':>10}  band?")
    for row in scan_table():
        # only print a readable subset
        if row["eps_Q"] not in (1e-4, 0.05, 1.0):
            continue
        if row["A"] not in (1.0, A_GW):
            continue
        band = (
            "IN"
            if SIGMA_EUCLID <= row["sigma"] <= SIGMA_DESI
            else ("low" if row["sigma"] < SIGMA_EUCLID else "high")
        )
        print(
            f"{row['r']:6.3f} {row['A']:6.1f} {row['eps_Q']:8.1e} "
            f"{row['sigma']:10.3e} {row['G_Euclid']:10.2e} {row['G_DESI']:10.2e}  {band}"
        )
    print()

    hits = windows_hitting_band()
    print(f"Scan points in [1e-5, 1.5e-4]: {len(hits)} / {len(scan_table())}")
    if hits:
        print("  Examples (not fits — a posteriori windows):")
        for row in hits[:12]:
            print(
                f"    r={row['r']}, A={row['A']}, ε_Q={row['eps_Q']:.1e} "
                f"→ σ={row['sigma']:.2e}"
            )
    print()

    gE, gD = sorkin_compare()
    print("Contrast — Sorkin holographic seed gaps (fixed σ_0):")
    print(f"  G_Euclid ~ {gE:.2e}   G_DESI ~ {gD:.2e}")
    print()

    # Key scientific punchline numbers
    r = R_BK_95
    s_frozen_flat = sigma_rho(r, 1e-4, 1.0)  # very flat DE
    s_frozen_mild = sigma_rho(r, 0.05, 1.0)
    s_A45_mild = sigma_rho(r, 0.05, A_GW)
    s_A45_eps1 = sigma_rho(r, 1.0, A_GW)
    print(f"Punchline at r={r} (BK-class upper edge):")
    print(f"  frozen, ε_Q=1e-4 (very flat): σ ~ {s_frozen_flat:.2e}  "
          f"short of 1e-5 by ×{gap_to_target(s_frozen_flat, SIGMA_EUCLID):.0f}")
    print(f"  frozen, ε_Q=0.05:             σ ~ {s_frozen_mild:.2e}  "
          f"short of 1e-5 by ×{gap_to_target(s_frozen_mild, SIGMA_EUCLID):.1f}")
    print(f"  A=45,   ε_Q=0.05:             σ ~ {s_A45_mild:.2e}  "
          f"(vs DESI ceiling {SIGMA_DESI:.1e})")
    print(f"  A=45,   ε_Q=1 (not DE-like):  σ ~ {s_A45_eps1:.2e}")
    print()
    print("Experimental door-closers / openers:")
    print("  • Measure r (or tight upper bound): lowers max δQ ∝ √r")
    print("  • Bound DE isocurvature / residual σ_X a posteriori")
    print("  • Illegal: pick ε_Q and A after seeing DESI to land in band")
    print("See papers/inflation-spectator-residual-atlas.md")


if __name__ == "__main__":
    main()
