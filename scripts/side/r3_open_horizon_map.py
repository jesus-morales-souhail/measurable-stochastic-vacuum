#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WP2 / R3 — open-horizon gain map (or no-gain theorem in the soft regime).

Input: sigma_0,eff from WP1 (counting principle). Not a DESI dial.
Output: residual amplitude under G = G_U * G_F * G_O with soft bounds.

Run:
  python scripts/r3_open_horizon_map.py
"""

from __future__ import annotations

import math

# --- WP1 anchors (from r1_counting_landscape.py, recomputed consistently) ---
L_P = 1.616e-35  # m
L_H = 3.0e8 / (67.4 / 3.086e19)  # m
SIGMA_SORKIN = L_P / L_H  # holographic d=2: 1/sqrt((L_H/L_P)^2)

# Soft open-system ceiling (squeeze r=1.5 -> e^{2r} ~ 20); audit of sibling repo
R_SQUEEZE = 1.5
G_O_SOFT = math.exp(2.0 * R_SQUEEZE)
G_F = 1.0  # freeze-out preserves, does not amplify (Route 2 scan)
G_U = 1.0  # late Delta x = O(1); not inflation's e^60


def sigma_res(sigma0: float, g_o: float = G_O_SOFT) -> float:
    return G_U * G_F * g_o * sigma0


def main() -> None:
    print("=" * 72)
    print("WP2 / R3 — open-horizon map (soft regime)")
    print("=" * 72)
    print(f"sigma_Sorkin (d=2 holographic) : {SIGMA_SORKIN:.3e}")
    print(f"G_U (late stretch O(1))         : {G_U:.3f}")
    print(f"G_F (freeze-out)                : {G_F:.3f}")
    print(f"G_O soft (r={R_SQUEEZE})        : {G_O_SOFT:.3f}")
    print(f"G_total soft                    : {G_U * G_F * G_O_SOFT:.3f}")
    print()

    print("--- No-gain theorem (Sorkin seed) ---")
    for g in (1.0, G_O_SOFT, 1e2, 1e6):
        s = sigma_res(SIGMA_SORKIN, g)
        print(f"  G_O={g:.1e}  ->  sigma_res={s:.3e}   (target ~1e-5? {s >= 1e-5})")
    print("  Conclusion: soft open dynamics cannot lift Sorkin to telescope band.")
    print()

    print("--- Measurable band needs WP1 mesoscopic seed ---")
    targets = [1e-6, 1e-5, 5e-5, 1.5e-4]
    print(f"{'sigma_0,eff':>14}  {'G_O=1':>12}  {'G_O=20':>12}  note")
    for s0 in targets:
        a1 = sigma_res(s0, 1.0)
        a20 = sigma_res(s0, G_O_SOFT)
        note = ""
        if a20 > 1.5e-4:
            note = "above DESI 95% ceiling (a posteriori tension if no damping)"
        elif a1 >= 1e-5:
            note = "already in Euclid-ish band at G=1"
        elif a20 >= 1e-5:
            note = "enters band only with soft open gain"
        else:
            note = "still below 1e-5"
        print(f"{s0:14.1e}  {a1:12.3e}  {a20:12.3e}  {note}")
    print()

    print("--- What r would be needed to lift Sorkin to 1e-5? (not allowed as free dial) ---")
    need = 1e-5 / SIGMA_SORKIN
    r_need = 0.5 * math.log(need)
    print(f"  required G_O ~ {need:.3e}  =>  r ~ {r_need:.1f}")
    print("  That r is a NEW scale claim; must be derived from horizon bath physics (A3,A5).")
    print()
    print("VERDICT: R3 soft = O(10) multiplier. Measurability ⇔ R1 mesoscopic seed")
    print("         (or a future derived hard-open map — not invented here).")


if __name__ == "__main__":
    main()
