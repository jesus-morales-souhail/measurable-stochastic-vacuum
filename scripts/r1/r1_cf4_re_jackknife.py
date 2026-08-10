#!/usr/bin/env python3
"""
Jackknife error on CF4 peculiar-velocity correlation scale r_e.

Real data only: Cosmicflows-4 table2 (Tully et al. 2023).
Uses the same block-mean correlation definition as r1_real_velocity_block_net.py.

Question answered
-----------------
Is CF4 r_e(v_pec) still inside the sandwich band [0.5, 3] R_nl
after spatial jackknife uncertainty?

Non-claims: not DE residual; not a derivation of ell_*=R_nl.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "r1"))

from r1_real_velocity_block_net import (  # noqa: E402
    DATA,
    H0_CF_KMS,
    SOURCE,
    block_means,
    dm_to_distance_mpc,
    pair_correlation,
    parse_table2,
    quality_mask,
    supergalactic_xyz,
)

OUT = ROOT / "results" / "r1_cf4_jackknife"
OUT.mkdir(parents=True, exist_ok=True)

R_NL = 8.6098  # Mpc — sandwich lock
BAND = (0.5 * R_NL, 3.0 * R_NL)
# L where previous run reported r_e ~ 19–20 Mpc (near middle of sandwich band)
L_PRIMARY = 20.0
N_JK = 48  # spatial jackknife regions along primary SG axis


def load_catalog():
    table2 = DATA / "table2.dat"
    if not table2.exists():
        raise FileNotFoundError(f"Missing {table2}")
    cat = parse_table2(table2)
    d = dm_to_distance_mpc(cat["dm"])
    m = quality_mask(cat, d)
    d, vcmb = d[m], cat["vcmb"][m]
    sgl, sgb = cat["sgl"][m], cat["sgb"][m]
    v_pec = vcmb - H0_CF_KMS * d
    x, y, z = supergalactic_xyz(d, sgl, sgb)
    return {
        "x": x,
        "y": y,
        "z": z,
        "v_pec": v_pec,
        "n": len(d),
        "d_min": float(d.min()),
        "d_max": float(d.max()),
    }


def r_e_for_sample(x, y, z, v_pec, L: float) -> dict:
    centers, means, ns, rms = block_means(x, y, z, v_pec, L, min_n=3)
    if len(means) < 20:
        return {"r_e": float("nan"), "n_blocks": int(len(means)), "skipped": True}
    r_max = min(4.0 * L, 120.0)
    corr = pair_correlation(centers, means, r_max=r_max, n_bins=12)
    return {
        "r_e": float(corr["r_e_1over_e_Mpc"]),
        "n_blocks": int(len(means)),
        "C0": float(corr["C0"]),
        "skipped": False,
    }


def spatial_jackknife(cat: dict, L: float, n_jk: int = N_JK) -> dict:
    """Leave-one-region-out jackknife along supergalactic X (primary axis)."""
    x, y, z, v = cat["x"], cat["y"], cat["z"], cat["v_pec"]
    full = r_e_for_sample(x, y, z, v, L)
    # partition by x quantiles
    edges = np.quantile(x, np.linspace(0, 1, n_jk + 1))
    # ensure unique edges
    edges = np.unique(edges)
    n_reg = len(edges) - 1
    if n_reg < 8:
        n_reg = min(8, len(x) // 100)
        edges = np.quantile(x, np.linspace(0, 1, n_reg + 1))
        edges = np.unique(edges)
        n_reg = len(edges) - 1

    re_list = []
    for k in range(n_reg):
        lo, hi = edges[k], edges[k + 1]
        if k < n_reg - 1:
            keep = ~((x >= lo) & (x < hi))
        else:
            keep = ~((x >= lo) & (x <= hi))
        if keep.sum() < 500:
            continue
        res = r_e_for_sample(x[keep], y[keep], z[keep], v[keep], L)
        if not res["skipped"] and np.isfinite(res["r_e"]):
            re_list.append(res["r_e"])

    re_arr = np.array(re_list, dtype=float)
    n_eff = len(re_arr)
    if n_eff < 4 or not np.isfinite(full["r_e"]):
        return {
            "L_Mpc": L,
            "r_e_full": full.get("r_e"),
            "n_blocks_full": full.get("n_blocks"),
            "n_jk_ok": n_eff,
            "error": "insufficient jackknife samples",
        }

    # standard delete-1 jackknife variance for pseudo-values
    # theta_(.) mean of leave-one-out; var = (n-1)/n * sum (theta_i - mean)^2
    mean_loo = float(np.mean(re_arr))
    var_jk = ((n_eff - 1) / n_eff) * float(np.sum((re_arr - mean_loo) ** 2))
    err = math.sqrt(max(var_jk, 0.0))

    re0 = float(full["r_e"])
    band_lo, band_hi = BAND
    # conservative: full ± 1σ still overlaps band?
    lo = re0 - err
    hi = re0 + err
    in_band_point = band_lo <= re0 <= band_hi
    in_band_1sigma = not (hi < band_lo or lo > band_hi)
    # entire 1σ interval inside band?
    fully_inside = lo >= band_lo and hi <= band_hi

    return {
        "L_Mpc": L,
        "r_e_full_Mpc": re0,
        "r_e_jk_mean_loo_Mpc": mean_loo,
        "r_e_jk_err_Mpc": err,
        "r_e_over_R_nl": re0 / R_NL,
        "r_e_err_over_R_nl": err / R_NL,
        "n_blocks_full": full["n_blocks"],
        "n_jk_regions_used": n_eff,
        "sandwich_band_Mpc": [band_lo, band_hi],
        "R_nl_Mpc": R_NL,
        "point_in_band": in_band_point,
        "one_sigma_overlaps_band": in_band_1sigma,
        "one_sigma_fully_inside_band": fully_inside,
        "jk_r_e_list": re_arr.tolist(),
    }


def main() -> int:
    print("=== CF4 r_e jackknife (real Cosmicflows-4) ===")
    print(f"Source: {SOURCE['reference']}")
    cat = load_catalog()
    print(f"N galaxies after cuts: {cat['n']}")
    print(f"d range: {cat['d_min']:.1f}–{cat['d_max']:.1f} Mpc")
    print(f"R_nl = {R_NL:.4f} Mpc  band = [{BAND[0]:.2f}, {BAND[1]:.2f}] Mpc\n")

    # primary L + neighbors for robustness
    L_list = [15.0, 20.0, 30.0]
    results = {}
    for L in L_list:
        print(f"--- L = {L:.0f} Mpc ---")
        res = spatial_jackknife(cat, L, n_jk=N_JK)
        results[str(L)] = res
        if "error" in res:
            print("  ", res["error"])
            continue
        print(
            f"  r_e = {res['r_e_full_Mpc']:.2f} ± {res['r_e_jk_err_Mpc']:.2f} Mpc "
            f"({res['r_e_over_R_nl']:.2f} ± {res['r_e_err_over_R_nl']:.2f} R_nl)"
        )
        print(
            f"  point in band: {res['point_in_band']} | "
            f"1σ overlaps band: {res['one_sigma_overlaps_band']} | "
            f"1σ fully inside: {res['one_sigma_fully_inside_band']}"
        )
        print(f"  n_blocks={res['n_blocks_full']}  n_jk={res['n_jk_regions_used']}")

    primary = results.get(str(L_PRIMARY), {})
    gate_g2 = bool(
        primary.get("point_in_band") and primary.get("one_sigma_overlaps_band")
    )

    out = {
        "question": (
            "Is CF4 r_e(v_pec) inside [0.5,3] R_nl after jackknife error?"
        ),
        "answer": "YES_G2_HOLDS" if gate_g2 else "G2_WEAKENED_OR_FAIL",
        "gate_G2_pass": gate_g2,
        "primary_L_Mpc": L_PRIMARY,
        "primary": primary,
        "all_L": results,
        "catalog": {
            "n_galaxies": cat["n"],
            "d_min_Mpc": cat["d_min"],
            "d_max_Mpc": cat["d_max"],
            "H0_km_s_Mpc": H0_CF_KMS,
            "source": SOURCE,
        },
        "non_claims": [
            "Not a DE residual detection",
            "Not a derivation of ell_*=R_nl",
            "Jackknife is spatial along SG-X; not a full survey covariance",
        ],
    }
    (OUT / "cf4_re_jackknife.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    lines = [
        "CF4 r_e JACKKNIFE (real Cosmicflows-4 table2)",
        "=" * 50,
        f"Q: Is r_e in sandwich band after jackknife error?",
        f"A: {out['answer']}",
        f"R_nl = {R_NL:.4f} Mpc  band = [{BAND[0]:.2f}, {BAND[1]:.2f}] Mpc",
        f"N_gal = {cat['n']}",
        "",
    ]
    for L, res in results.items():
        if "error" in res:
            lines.append(f"L={L}: {res['error']}")
            continue
        lines.append(
            f"L={L} Mpc: r_e = {res['r_e_full_Mpc']:.2f} ± {res['r_e_jk_err_Mpc']:.2f} Mpc "
            f"= ({res['r_e_over_R_nl']:.2f} ± {res['r_e_err_over_R_nl']:.2f}) R_nl | "
            f"in_band={res['point_in_band']} 1σ_overlap={res['one_sigma_overlaps_band']} "
            f"fully_in={res['one_sigma_fully_inside_band']}"
        )
    lines += [
        "",
        f"Primary L={L_PRIMARY}: G2 pass = {gate_g2}",
        "Non-claims: " + "; ".join(out["non_claims"]),
        "",
    ]
    text = "\n".join(lines)
    (OUT / "cf4_re_jackknife.txt").write_text(text, encoding="utf-8")
    print("\n" + text)
    return 0 if gate_g2 else 1


if __name__ == "__main__":
    raise SystemExit(main())
