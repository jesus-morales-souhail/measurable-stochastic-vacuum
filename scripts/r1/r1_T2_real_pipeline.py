#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
T2 protocol on real public data (no synthetic mock fields).

Data used:
  1) DESI DR2 BAO multipoles (data + theory) from the local Zenodo DR2 pack
     under stochastic-dark-energy-ou/data/desi_dr2_local/...
  2) Cosmicflows-4 galaxy distances/velocities (CDS table2) for a real
     peculiar-velocity structure scale.

Residual on multipoles: r(s) = xi_data(s) - xi_theory(s).
Structure proxy: xi_data itself (built only from LSS multipoles, not residual).
CF4: correlation scale of block-mean v_pec in real 3D positions.

Not a Stage-IV residual-map detection. Reports chi2 of multipole residuals,
correlation length of residual auto, residual×structure cross vs shuffled null,
and CF4 velocity correlation scale vs R_nl band.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "results" / "r1_T2_real"
OUT.mkdir(parents=True, exist_ok=True)

# DESI DR2 multipoles live in the data repo (sibling or env)
CANDIDATE_DESI = [
    ROOT.parent
    / "stochastic-dark-energy-ou"
    / "data"
    / "desi_dr2_local"
    / "dr2_data"
    / "dr2-bao-zenodo"
    / "figure5",
]
CF4 = ROOT / "data" / "real_velocity_net" / "table2.dat"

R_NL = 8.61  # Mpc, programme value
ALLOWED = (0.5 * R_NL, 3.0 * R_NL)  # Mpc

sys.path.insert(0, str(ROOT / "scripts" / "r1"))
from r1_real_velocity_block_net import (  # noqa: E402
    H0_CF_KMS,
    dm_to_distance_mpc,
    parse_table2,
    quality_mask,
    supergalactic_xyz,
)


def find_multipole_dir() -> Path:
    import os
    env = os.environ.get("DESI_MULTIPOLE_DIR")
    if env and Path(env).is_dir():
        return Path(env)
    for p in CANDIDATE_DESI:
        if p.is_dir():
            return p
    raise FileNotFoundError(
        "DESI multipole directory not found. Set DESI_MULTIPOLE_DIR or keep the "
        "stochastic-dark-energy-ou data pack next to this repo."
    )


def load_pair(data_path: Path, theory_path: Path) -> dict:
    d = np.loadtxt(data_path, comments="#")
    t = np.loadtxt(theory_path, comments="#")
    # data: s, xi0, xi0_err, xi2, xi2_err
    # theory: s, xi0, xi2
    s = d[:, 0]
    # interpolate theory onto data s if needed
    if t.shape[0] != d.shape[0] or not np.allclose(t[:, 0], s, rtol=0, atol=1e-6):
        xi0_th = np.interp(s, t[:, 0], t[:, 1])
        xi2_th = np.interp(s, t[:, 0], t[:, 2])
    else:
        xi0_th = t[:, 1]
        xi2_th = t[:, 2]
    xi0 = d[:, 1]
    e0 = d[:, 2]
    xi2 = d[:, 3]
    e2 = d[:, 4]
    r0 = xi0 - xi0_th
    r2 = xi2 - xi2_th
    chi2_0 = float(np.sum((r0 / np.maximum(e0, 1e-30)) ** 2))
    chi2_2 = float(np.sum((r2 / np.maximum(e2, 1e-30)) ** 2))
    return {
        "name": data_path.name.replace("multipoles_", "").replace("_data.txt", ""),
        "s": s,
        "xi0": xi0,
        "e0": e0,
        "xi2": xi2,
        "e2": e2,
        "r0": r0,
        "r2": r2,
        "chi2_0": chi2_0,
        "chi2_2": chi2_2,
        "n_bins": int(len(s)),
    }


def corr_length_1e(s: np.ndarray, y: np.ndarray) -> float | None:
    """Scale where |y| drops to |y|_max / e (first crossing after peak)."""
    y = np.asarray(y, dtype=float)
    s = np.asarray(s, dtype=float)
    if len(y) < 3:
        return None
    a = np.abs(y)
    imax = int(np.argmax(a))
    peak = a[imax]
    if peak <= 0:
        return None
    thr = peak / math.e
    for i in range(imax, len(a) - 1):
        if a[i] >= thr >= a[i + 1]:
            # linear in s
            if a[i] == a[i + 1]:
                return float(s[i])
            f = (a[i] - thr) / (a[i] - a[i + 1])
            return float(s[i] + f * (s[i + 1] - s[i]))
    return float(s[-1])


def residual_structure_cross(r: np.ndarray, struct: np.ndarray) -> float:
    """Pearson correlation residual vs structure proxy (same s bins)."""
    r = r - r.mean()
    s = struct - struct.mean()
    den = float(np.sqrt(np.sum(r**2) * np.sum(s**2)))
    if den <= 0:
        return 0.0
    return float(np.sum(r * s) / den)


def shuffled_cross(r: np.ndarray, struct: np.ndarray, n: int = 200, seed: int = 7) -> dict:
    rng = np.random.default_rng(seed)
    obs = residual_structure_cross(r, struct)
    null = []
    for _ in range(n):
        rr = rng.permutation(r)
        null.append(residual_structure_cross(rr, struct))
    null = np.array(null, dtype=float)
    # one-sided: fraction of null >= obs if obs>0
    if obs >= 0:
        p = float(np.mean(null >= obs))
    else:
        p = float(np.mean(null <= obs))
    return {
        "cross_obs": obs,
        "cross_null_mean": float(null.mean()),
        "cross_null_std": float(null.std()),
        "p_shuffle": p,
    }


def analyze_multipoles(mp_dir: Path) -> list[dict]:
    data_files = sorted(mp_dir.glob("multipoles_*_data.txt"))
    results = []
    for df in data_files:
        tf = Path(str(df).replace("_data.txt", "_theory.txt"))
        if not tf.is_file():
            continue
        pair = load_pair(df, tf)
        re0 = corr_length_1e(pair["s"], pair["r0"])
        re2 = corr_length_1e(pair["s"], pair["r2"])
        # structure proxy = data multipole (not residual)
        cross0 = shuffled_cross(pair["r0"], pair["xi0"])
        cross2 = shuffled_cross(pair["r2"], pair["xi2"])
        results.append(
            {
                "tracer": pair["name"],
                "n_bins": pair["n_bins"],
                "s_min": float(pair["s"][0]),
                "s_max": float(pair["s"][-1]),
                "chi2_xi0_residual": pair["chi2_0"],
                "chi2_xi2_residual": pair["chi2_2"],
                "r_e_residual_xi0_Mpc_h": re0,
                "r_e_residual_xi2_Mpc_h": re2,
                "cross_r0_x_xi0": cross0,
                "cross_r2_x_xi2": cross2,
                "note": (
                    "Multipole residual scale is set by BAO/clustering scales in the "
                    "file (tens of Mpc/h), not the R_nl galaxy-density sandwich band."
                ),
            }
        )
    return results


def cf4_velocity_corr_scale(max_gal: int = 12000) -> dict:
    """Real CF4 block v_pec correlation length (Mpc)."""
    if not CF4.is_file():
        return {"error": f"missing {CF4.as_posix()}"}
    cat = parse_table2(CF4)
    d = dm_to_distance_mpc(cat["dm"])
    m = quality_mask(cat, d)
    # subsample for speed if huge
    idx = np.where(m)[0]
    if len(idx) > max_gal:
        rng = np.random.default_rng(11)
        idx = rng.choice(idx, size=max_gal, replace=False)
    d = d[idx]
    vpec = cat["vcmb"][idx] - H0_CF_KMS * d
    x, y, z = supergalactic_xyz(d, cat["sgl"][idx], cat["sgb"][idx])
    # block means
    L = 20.0  # Mpc blocks
    xmin, ymin, zmin = x.min(), y.min(), z.min()
    ix = np.floor((x - xmin) / L).astype(int)
    iy = np.floor((y - ymin) / L).astype(int)
    iz = np.floor((z - zmin) / L).astype(int)
    keys = {}
    for i in range(len(x)):
        k = (ix[i], iy[i], iz[i])
        keys.setdefault(k, []).append(vpec[i])
    # keep blocks with >= 3 galaxies
    centers = []
    means = []
    for (a, b, c), vals in keys.items():
        if len(vals) < 3:
            continue
        centers.append(
            (
                xmin + (a + 0.5) * L,
                ymin + (b + 0.5) * L,
                zmin + (c + 0.5) * L,
            )
        )
        means.append(float(np.mean(vals)))
    centers = np.array(centers)
    means = np.array(means)
    if len(means) < 20:
        return {"error": "too few CF4 blocks", "n_blocks": int(len(means))}
    means = means - means.mean()
    # pair separations
    n = len(means)
    # subsample pairs if needed
    max_pairs = 80000
    seps = []
    prods = []
    rng = np.random.default_rng(3)
    trials = 0
    while len(seps) < max_pairs and trials < max_pairs * 3:
        i = int(rng.integers(0, n))
        j = int(rng.integers(0, n))
        if i >= j:
            trials += 1
            continue
        dr = float(np.linalg.norm(centers[i] - centers[j]))
        if dr < 1.0 or dr > 200.0:
            trials += 1
            continue
        seps.append(dr)
        prods.append(means[i] * means[j])
        trials += 1
    seps = np.array(seps)
    prods = np.array(prods)
    # binned correlation
    edges = np.linspace(5.0, 150.0, 16)
    rc = 0.5 * (edges[:-1] + edges[1:])
    C = np.zeros(len(rc))
    for i in range(len(rc)):
        msk = (seps >= edges[i]) & (seps < edges[i + 1])
        if msk.sum() < 5:
            C[i] = np.nan
        else:
            C[i] = float(prods[msk].mean())
    # C(0) proxy = variance of means
    C0 = float(np.var(means))
    if C0 <= 0:
        re = None
    else:
        xi = C / C0
        # first bin where xi < 1/e
        re = None
        thr = 1.0 / math.e
        for i in range(len(rc)):
            if not np.isnan(xi[i]) and xi[i] < thr:
                re = float(rc[i])
                break
    in_band = None
    if re is not None:
        in_band = bool(ALLOWED[0] <= re <= ALLOWED[1])
    return {
        "catalog": "Cosmicflows-4 table2",
        "n_galaxies_used": int(len(idx)),
        "n_blocks": int(len(means)),
        "block_side_Mpc": L,
        "H0_km_s_Mpc": H0_CF_KMS,
        "vpec_rms_km_s": float(np.std(vpec)),
        "r_e_vpec_block_Mpc": re,
        "R_nl_Mpc": R_NL,
        "allowed_band_Mpc": list(ALLOWED),
        "r_e_in_allowed_band": in_band,
        "C_of_r_centers_Mpc": rc.tolist(),
        "C_over_C0": [None if np.isnan(x) else float(x) for x in (C / C0 if C0 > 0 else C)],
    }


def main() -> int:
    print("=== T2 on REAL data (DESI multipoles + CF4) ===")
    mp_dir = find_multipole_dir()
    print("multipoles:", mp_dir)
    multi = analyze_multipoles(mp_dir)
    print(f"tracers with data+theory: {len(multi)}")
    for m in multi:
        print(
            f"  {m['tracer']}: chi2_0={m['chi2_xi0_residual']:.1f} "
            f"r_e0={m['r_e_residual_xi0_Mpc_h']} "
            f"cross={m['cross_r0_x_xi0']['cross_obs']:.3f} "
            f"p_shuffle={m['cross_r0_x_xi0']['p_shuffle']:.3f}"
        )

    print("CF4 velocity structure...")
    cf4 = cf4_velocity_corr_scale()
    if "error" in cf4:
        print("  CF4:", cf4["error"])
    else:
        print(
            f"  n_blocks={cf4['n_blocks']} r_e={cf4['r_e_vpec_block_Mpc']} "
            f"in_band={cf4['r_e_in_allowed_band']}"
        )

    # aggregate multipole residual chi2
    chi2_tot = sum(m["chi2_xi0_residual"] + m["chi2_xi2_residual"] for m in multi)
    ndof = sum(2 * m["n_bins"] for m in multi)

    # honest verdict flags
    # Multipole residual scales are BAO-scale (s~60-140 Mpc/h), NOT R_nl band.
    # CF4 r_e compared to R_nl band is the real-space structure scale test.
    flags = {
        "used_synthetic_fields": False,
        "used_desi_dr2_multipoles": len(multi) > 0,
        "used_cf4_table2": "error" not in cf4,
        "multipole_residual_chi2_total": chi2_tot,
        "multipole_residual_ndof": ndof,
        "cf4_r_e_in_R_nl_band": cf4.get("r_e_in_allowed_band"),
        "note": (
            "DESI multipole residuals test data-minus-theory clustering, not a 3D "
            "residual density map at R_nl. CF4 tests real peculiar-velocity coherence."
        ),
    }

    out = {
        "protocol": "T2 real-data application",
        "R_nl_Mpc": R_NL,
        "allowed_ell_band_Mpc": list(ALLOWED),
        "desi_multipoles_dir": str(mp_dir),
        "multipole_tracers": multi,
        "cf4": cf4,
        "flags": flags,
    }
    (OUT / "T2_real_validation.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    lines = [
        "T2 REAL-DATA PIPELINE (no synthetic mock fields)",
        "=" * 55,
        f"DESI multipoles: {mp_dir}",
        f"tracers: {len(multi)}",
        f"sum chi2 residual (xi0+xi2): {chi2_tot:.1f}  (ndof~{ndof})",
        "",
        "Per tracer (xi0 residual):",
    ]
    for m in multi:
        lines.append(
            f"  {m['tracer']}: chi2_0={m['chi2_xi0_residual']:.1f} "
            f"r_e0={m['r_e_residual_xi0_Mpc_h']} "
            f"cross={m['cross_r0_x_xi0']['cross_obs']:.3f} "
            f"p_null={m['cross_r0_x_xi0']['p_shuffle']:.3f}"
        )
    lines.append("")
    lines.append("CF4 peculiar-velocity blocks:")
    if "error" in cf4:
        lines.append(f"  ERROR: {cf4['error']}")
    else:
        lines.append(f"  n_gal={cf4['n_galaxies_used']} n_blocks={cf4['n_blocks']}")
        lines.append(f"  r_e(v_pec)={cf4['r_e_vpec_block_Mpc']} Mpc")
        lines.append(f"  allowed band [{ALLOWED[0]:.1f}, {ALLOWED[1]:.1f}] Mpc")
        lines.append(f"  in_band={cf4['r_e_in_allowed_band']}")
    lines.append("")
    lines.append("FLAGS:")
    for k, v in flags.items():
        lines.append(f"  {k}: {v}")
    lines.append("")
    lines.append("This replaces the synthetic T2 mock. No injected Gaussian fields.")
    (OUT / "T2_real_validation.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote", OUT / "T2_real_validation.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
