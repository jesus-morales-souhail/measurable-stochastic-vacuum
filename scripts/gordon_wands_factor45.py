#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arithmetic of Gordon & Wands (2005), arXiv:astro-ph/0504132, Eqs. (25)–(27).

Uses the *paper's own* 2005-era numbers (not modern tensor updates):
  V_inf^{1/4} needed (frozen) > 7e-2 M_p   [Eq. 25]
  V_inf^{1/4} GW bound         < 1e-2 M_p   [Eq. 26]
  ⇒ δQ_f/δQ_i > 45              [Eq. 27]

Why ~45 not ~7: δQ ~ H/(2π) and H ∝ V^{1/2} ∝ (V^{1/4})^2,
so the field-perturbation ratio scales as (energy-scale ratio)^2.

This is NOT the Sorkin gap 10^56. Different seed, different target.
See papers/inflation-spectator-seed-gordon-wands.md
"""

from __future__ import annotations

import math

# Paper numbers (Gordon & Wands 2005)
V14_NEEDED = 7e-2  # M_p units, Eq. (25)
V14_GW_BOUND = 1e-2  # M_p units, Eq. (26)
PAPER_FACTOR = 45.0  # Eq. (27)


def energy_scale_ratio(v_needed: float = V14_NEEDED, v_bound: float = V14_GW_BOUND) -> float:
    return v_needed / v_bound


def field_perturbation_ratio_from_scales(v_needed: float = V14_NEEDED, v_bound: float = V14_GW_BOUND) -> float:
    """
    If δQ ∝ H ∝ V^{1/2} ∝ (V^{1/4})^2, then
    δQ_needed/δQ_max_GW = (V14_needed/V14_bound)^2.
    """
    r = energy_scale_ratio(v_needed, v_bound)
    return r * r


def main() -> None:
    r_E = energy_scale_ratio()
    r_Q = field_perturbation_ratio_from_scales()
    print("Gordon & Wands (2005) — factor >45 arithmetic")
    print(f"  V_inf^{{1/4}} needed (frozen light field) > {V14_NEEDED} M_p   [Eq. 25]")
    print(f"  V_inf^{{1/4}} GW bound (paper)            < {V14_GW_BOUND} M_p   [Eq. 26]")
    print(f"  Energy-scale ratio R_E = {r_E:.3f}")
    print(f"  Field-pert. ratio R_Q ≈ R_E^2 = {r_Q:.3f}  (paper states > {PAPER_FACTOR:.0f})")
    print(f"  Relative match |R_Q - 45|/45 = {abs(r_Q - PAPER_FACTOR)/PAPER_FACTOR:.3f}")
    print()
    print("Seed: P_Q^{1/2} = H_inf/(2π)  [Eq. 12]  — NOT Sorkin sigma_0 ~ 1e-61")
    print("Target in paper: large DE isocurvature for CMB quadrupole — NOT DESI sigma_X kernel")
    print("Amplification proposed: Mexican-hat radial roll  phi_f/phi_i > 45  [Eq. 32]")
    print()
    print("Illegal: equate this 'tachyonic' roll with excluded BAO GPE residual")
    print("Illegal: say Gordon-Wands 'hits the same 10^56 wall' as Sorkin soft maps")
    print("Legal: open number is H_inf + O(10-100) derived growth, category ≠ free 1e56")
    print("See papers/inflation-spectator-seed-gordon-wands.md")


if __name__ == "__main__":
    main()
