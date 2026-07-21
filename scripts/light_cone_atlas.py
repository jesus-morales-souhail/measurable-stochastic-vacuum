#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Past light-cone numerical atlas for the Minimal Model.

Writes results/light_cone_integration_table.csv and prints a referee summary.

  RMS_path = |γ-1|_loc * sqrt(χ/ℓ*)     (C=1, iid patches)
"""

from __future__ import annotations

import csv
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
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "light_cone_integration_table.csv"


def main() -> None:
    L_H, _, sorkin = sorkin_holographic()
    rows = []
    scenarios = [
        ("Sorkin", sorkin, 0.0, 2, None),
        ("NP-A", 1e-5, 0.0, 3, None),
        ("NP-B", 5e-6, 1.5, 3, None),
        ("DESI_ceil", 1.5e-4, 0.0, 3, 1.5e-4),
    ]
    for z_s in (0.5, 1.0, 1.5, 2.0, 3.0):
        chi = comoving_distance_mpc(z_s)
        for name, sigma0, r, d, force_res in scenarios:
            sres = force_res if force_res is not None else residual_soft_map(sigma0, r=r)
            ell_mpc = ell_for_target_sigma(sigma0 if force_res is None else sres, L_H, d) / MPC
            for z_slip in (0.3, 0.5, 0.8, 1.0):
                if z_slip >= z_s:
                    continue
                slip = slip_deviation(1.0, sres, z_slip)
                n = n_patches(chi, max(ell_mpc, 1e-40))
                n_use = min(n, 1e12)
                rms = rms_incoherent(slip, n_use)
                rows.append(
                    {
                        "scenario": name,
                        "z_s": z_s,
                        "chi_Mpc": round(chi, 3),
                        "sigma0": sigma0,
                        "r": r,
                        "d": d,
                        "sigma_res": sres,
                        "ell_Mpc": ell_mpc,
                        "z_slip": z_slip,
                        "slip_loc": slip,
                        "N_pat": n,
                        "sqrtN": math.sqrt(n_use),
                        "RMS_path": rms,
                        "DESI_res_OK": bool(sres <= 1.5e-4 + 1e-15),
                        "boost": math.sqrt(n_use),
                    }
                )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("=" * 72)
    print("PAST LIGHT-CONE ATLAS")
    print("RMS_path = |γ-1|_loc * sqrt(χ/ℓ*)   (C=1)")
    print("=" * 72)
    print(f"Wrote {OUT}  ({len(rows)} rows)")
    print()
    print(f"{'scenario':<12} {'z_s':>4} {'chi':>8} {'s_res':>10} {'ell':>8} "
          f"{'slip':>10} {'sqrtN':>7} {'RMS':>10} DESI")
    for r in rows:
        if r["z_slip"] != 0.8:
            continue
        if r["scenario"] == "Sorkin" and r["z_s"] != 1.5:
            continue
        print(
            f"{r['scenario']:<12} {r['z_s']:4.1f} {r['chi_Mpc']:8.1f} {r['sigma_res']:10.2e} "
            f"{r['ell_Mpc']:8.3f} {r['slip_loc']:10.2e} {r['sqrtN']:7.2f} {r['RMS_path']:10.2e} "
            f"{r['DESI_res_OK']}"
        )
    print()
    print("Verdict: path boost is O(10-70) for mesoscopic cells — frontier, not free amplification.")


if __name__ == "__main__":
    main()
