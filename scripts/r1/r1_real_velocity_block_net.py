#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Block-net analysis of real galaxy peculiar velocities (Cosmicflows-4).

SOURCE (public, CDS):
  Tully et al. 2023, ApJ 944, 94
  CDS catalog J/ApJ/944/94  table2.dat  (galaxy sample)
  ReadMe: https://cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/ReadMe

WHAT THIS DOES (data only — no residual-DE model, no free dials):
  1) Parse CF4 distance moduli + Vcmb
  2) Convert DM -> distance (Mpc)
  3) Line-of-sight peculiar velocity vs pure Hubble flow at fixed H0
       v_pec = Vcmb - H0 * d
     H0=75 km/s/Mpc is the conventional CF scale for residual velocities
     (stated explicitly; not fitted here).
  4) Place galaxies in supergalactic Cartesian coordinates
  5) Bin into cubic blocks of side L
  6) Per block: mean v_pec, n_gal, rms
  7) Empirical block-block correlation of mean v_pec vs separation
  8) Report correlation scale where C(r)/C(0) ~ 1/e and velocity rms

WHAT THIS DOES NOT DO:
  - invent dark-energy residual work
  - fit ell_* to DESI residual
  - numerology / free 1e56 / H0 tension solution

Outputs: results/r1_real_velocity_net/
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "real_velocity_net"
OUT = ROOT / "results" / "r1_real_velocity_net"
OUT.mkdir(parents=True, exist_ok=True)

# Fixed conversion convention for CF residual velocities (not fitted)
H0_CF_KMS = 75.0  # km/s/Mpc — Cosmicflows conventional residual scale
C_KMS = 299792.458

SOURCE = {
    "catalog": "Cosmicflows-4",
    "reference": "Tully et al. 2023, ApJ 944, 94",
    "cds": "J/ApJ/944/94",
    "file": "table2.dat",
    "url_readme": "https://cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/ReadMe",
    "url_table2": "https://cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/table2.dat.gz",
    "H0_convention_km_s_Mpc": H0_CF_KMS,
    "H0_note": (
        "H0 enters only as the conversion v_pec = Vcmb - H0*d. "
        "Value 75 km/s/Mpc is the conventional Cosmicflows residual scale, "
        "not fitted to these data in this script."
    ),
}


def parse_table2(path: Path) -> dict:
    """Fixed-width parse of CF4 table2 (galaxy catalog)."""
    pgc, vcmb, dm, edm = [], [], [], []
    ra, dec, sgl, sgb = [], [], [], []
    with open(path) as f:
        for line in f:
            if len(line) < 190:
                continue
            try:
                # bytes are 1-indexed in ReadMe
                pgc_i = int(line[0:7])
                v_i = int(line[22:27])
                dm_i = float(line[28:34])
                edm_i = float(line[35:40])
                ra_i = float(line[137:145])
                de_i = float(line[146:154])
                sgl_i = float(line[173:181])
                sgb_i = float(line[182:190])
            except ValueError:
                continue
            pgc.append(pgc_i)
            vcmb.append(v_i)
            dm.append(dm_i)
            edm.append(edm_i)
            ra.append(ra_i)
            dec.append(de_i)
            sgl.append(sgl_i)
            sgb.append(sgb_i)
    return {
        "pgc": np.array(pgc, dtype=int),
        "vcmb": np.array(vcmb, dtype=float),
        "dm": np.array(dm, dtype=float),
        "edm": np.array(edm, dtype=float),
        "ra": np.array(ra, dtype=float),
        "dec": np.array(dec, dtype=float),
        "sgl": np.array(sgl, dtype=float),
        "sgb": np.array(sgb, dtype=float),
    }


def dm_to_distance_mpc(dm: np.ndarray) -> np.ndarray:
    """Luminosity distance from distance modulus: d = 10**((DM-25)/5) Mpc."""
    return 10.0 ** ((dm - 25.0) / 5.0)


def supergalactic_xyz(d_mpc: np.ndarray, sgl_deg: np.ndarray, sgb_deg: np.ndarray):
    """Supergalactic Cartesian coordinates (Mpc)."""
    sgl = np.deg2rad(sgl_deg)
    sgb = np.deg2rad(sgb_deg)
    x = d_mpc * np.cos(sgb) * np.cos(sgl)
    y = d_mpc * np.cos(sgb) * np.sin(sgl)
    z = d_mpc * np.sin(sgb)
    return x, y, z


def quality_mask(cat: dict, d: np.ndarray) -> np.ndarray:
    """
    Data-quality cuts (documented, not tuned to a target scale):
      - finite DM, e_DM
      - e_DM <= 0.5 mag (reject poorly constrained distances)
      - 1 < d < 200 Mpc (CF4 useful volume for local flows; avoids extreme far end)
      - |Vcmb| < 30000 km/s
    """
    m = np.ones(len(d), dtype=bool)
    m &= np.isfinite(cat["dm"]) & np.isfinite(cat["edm"]) & np.isfinite(cat["vcmb"])
    m &= cat["edm"] <= 0.5
    m &= (d > 1.0) & (d < 200.0)
    m &= np.abs(cat["vcmb"]) < 30000.0
    return m


def block_means(
    x, y, z, vpec, L: float, min_n: int = 3
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Cubic blocks of side L (Mpc) in SG coordinates.
    Returns block centers (N,3), mean v_pec, n_gal, rms v_pec.
    """
    # integer block indices
    ix = np.floor(x / L).astype(int)
    iy = np.floor(y / L).astype(int)
    iz = np.floor(z / L).astype(int)
    # pack keys
    # shift to non-negative for unique
    keys = np.stack([ix, iy, iz], axis=1)
    # unique blocks
    # use dict for accumulation
    acc_sum = {}
    acc_sum2 = {}
    acc_n = {}
    for i in range(len(vpec)):
        k = (int(keys[i, 0]), int(keys[i, 1]), int(keys[i, 2]))
        acc_sum[k] = acc_sum.get(k, 0.0) + float(vpec[i])
        acc_sum2[k] = acc_sum2.get(k, 0.0) + float(vpec[i]) ** 2
        acc_n[k] = acc_n.get(k, 0) + 1

    centers, means, ns, rms = [], [], [], []
    for k, n in acc_n.items():
        if n < min_n:
            continue
        mu = acc_sum[k] / n
        var = max(acc_sum2[k] / n - mu * mu, 0.0)
        centers.append([(k[0] + 0.5) * L, (k[1] + 0.5) * L, (k[2] + 0.5) * L])
        means.append(mu)
        ns.append(n)
        rms.append(math.sqrt(var))
    if not centers:
        return (
            np.zeros((0, 3)),
            np.zeros(0),
            np.zeros(0, dtype=int),
            np.zeros(0),
        )
    return (
        np.array(centers),
        np.array(means),
        np.array(ns, dtype=int),
        np.array(rms),
    )


def pair_correlation(
    centers: np.ndarray, means: np.ndarray, r_max: float, n_bins: int = 12
) -> dict:
    """
    Empirical correlation of block-mean peculiar velocities vs separation.
    C(r) = < v_i v_j > for pairs in radial bins (means already demeaned).
    """
    v = means - means.mean()
    n = len(v)
    if n < 10:
        return {"r": [], "C": [], "n_pairs": [], "C0": float(np.mean(v**2))}
    # pair separations (upper triangle)
    # for large n this is O(n^2); CF4 blocks are manageable
    r_edges = np.linspace(0.0, r_max, n_bins + 1)
    sum_c = np.zeros(n_bins)
    n_pairs = np.zeros(n_bins, dtype=int)
    for i in range(n):
        dvec = centers[i + 1 :] - centers[i]
        r = np.sqrt(np.sum(dvec**2, axis=1))
        prod = v[i] * v[i + 1 :]
        for b in range(n_bins):
            m = (r >= r_edges[b]) & (r < r_edges[b + 1])
            if np.any(m):
                sum_c[b] += float(np.sum(prod[m]))
                n_pairs[b] += int(np.sum(m))
    C = np.full(n_bins, np.nan)
    for b in range(n_bins):
        if n_pairs[b] > 0:
            C[b] = sum_c[b] / n_pairs[b]
    r_c = 0.5 * (r_edges[:-1] + r_edges[1:])
    C0 = float(np.mean(v**2))
    # correlation length: first r where C/C0 <= 1/e
    r_e = float("nan")
    if C0 > 0:
        thr = C0 / math.e
        prev_r, prev_c = 0.0, C0
        for ri, ci in zip(r_c, C):
            if not np.isfinite(ci):
                continue
            if ci <= thr:
                if prev_c == ci:
                    r_e = float(ri)
                else:
                    t = (prev_c - thr) / (prev_c - ci + 1e-30)
                    r_e = float(prev_r + t * (ri - prev_r))
                break
            prev_r, prev_c = float(ri), float(ci)
    return {
        "r_Mpc": r_c.tolist(),
        "C": [None if not np.isfinite(c) else float(c) for c in C],
        "n_pairs": n_pairs.tolist(),
        "C0": C0,
        "r_e_1over_e_Mpc": r_e,
    }


def main() -> None:
    table2 = DATA / "table2.dat"
    if not table2.exists():
        raise FileNotFoundError(
            f"Missing {table2}. Download Cosmicflows-4 table2 from CDS J/ApJ/944/94."
        )

    print("=== Real velocity block net (Cosmicflows-4) ===")
    print(f"Source: {SOURCE['reference']}  ({SOURCE['cds']})")
    print(f"H0 convention for v_pec: {H0_CF_KMS} km/s/Mpc (not fitted)\n")

    cat = parse_table2(table2)
    d = dm_to_distance_mpc(cat["dm"])
    m = quality_mask(cat, d)
    d, vcmb = d[m], cat["vcmb"][m]
    sgl, sgb = cat["sgl"][m], cat["sgb"][m]
    edm = cat["edm"][m]

    v_hubble = H0_CF_KMS * d
    v_pec = vcmb - v_hubble

    x, y, z = supergalactic_xyz(d, sgl, sgb)

    print(f"Galaxies after cuts: {len(d)}")
    print(f"Distance range: {d.min():.2f} – {d.max():.2f} Mpc")
    print(f"Vcmb range: {vcmb.min():.0f} – {vcmb.max():.0f} km/s")
    print(f"v_pec global: mean={v_pec.mean():.1f}  rms={v_pec.std():.1f} km/s")
    print(f"median e_DM = {np.median(edm):.3f} mag\n")

    # Block sides to scan (Mpc) — fixed grid, not tuned to a theory target
    L_list = [5.0, 10.0, 15.0, 20.0, 30.0, 40.0]
    results_L = {}

    for L in L_list:
        centers, means, ns, rms = block_means(x, y, z, v_pec, L, min_n=3)
        n_blocks = len(means)
        if n_blocks < 20:
            print(f"L={L:5.1f} Mpc: only {n_blocks} blocks — skip correlation")
            results_L[str(L)] = {"n_blocks": n_blocks, "skipped": True}
            continue
        # correlation out to ~4 L or 120 Mpc
        r_max = min(120.0, 4.0 * L + 40.0)
        corr = pair_correlation(centers, means, r_max=r_max, n_bins=12)
        v_h_L = H0_CF_KMS * L
        sigma_v_block = float(np.std(means))
        eta = sigma_v_block / v_h_L if v_h_L > 0 else float("nan")
        row = {
            "L_block_Mpc": L,
            "n_blocks": int(n_blocks),
            "n_gal_median": float(np.median(ns)),
            "n_gal_total_in_blocks": int(np.sum(ns)),
            "mean_vpec_block_mean": float(np.mean(means)),
            "sigma_v_block_means_km_s": sigma_v_block,
            "median_rms_inside_block_km_s": float(np.median(rms)),
            "v_Hubble_at_L_km_s": v_h_L,
            "eta_sigma_v_over_vH": eta,
            "correlation": corr,
        }
        results_L[str(L)] = row
        print(
            f"L={L:5.1f} Mpc | blocks={n_blocks:4d} | "
            f"σ(v_block)={sigma_v_block:6.1f} km/s | "
            f"v_H(L)={v_h_L:6.1f} | η={eta:5.2f} | "
            f"r_e≈{corr['r_e_1over_e_Mpc']:.1f} Mpc"
        )

    # Jackknife crude error on global rms (leave-one-out on random 200 subsamples of galaxies)
    rng = np.random.default_rng(0)
    n_jk = 50
    jk_rms = []
    idx = np.arange(len(v_pec))
    for _ in range(n_jk):
        # 90% subsample
        sel = rng.choice(idx, size=int(0.9 * len(idx)), replace=False)
        jk_rms.append(float(np.std(v_pec[sel])))
    jk_rms = np.array(jk_rms)

    out = {
        "source": SOURCE,
        "cuts": {
            "e_DM_max_mag": 0.5,
            "d_min_Mpc": 1.0,
            "d_max_Mpc": 200.0,
            "abs_Vcmb_max_km_s": 30000.0,
            "min_gal_per_block": 3,
        },
        "sample": {
            "n_galaxies": int(len(d)),
            "d_min_Mpc": float(d.min()),
            "d_max_Mpc": float(d.max()),
            "v_pec_mean_km_s": float(v_pec.mean()),
            "v_pec_rms_km_s": float(v_pec.std()),
            "v_pec_rms_jk_mean": float(jk_rms.mean()),
            "v_pec_rms_jk_std": float(jk_rms.std()),
            "median_e_DM_mag": float(np.median(edm)),
        },
        "block_scan": results_L,
        "definitions": {
            "distance_Mpc": "10**((DM-25)/5) from CF4 MCMC distance modulus",
            "v_pec_km_s": "Vcmb - H0 * d",
            "coordinates": "supergalactic Cartesian from CF4 SGL,SGB",
            "eta": "std(block-mean v_pec) / (H0 * L_block)",
            "r_e": "pair separation where C(r)/C(0) first drops to 1/e",
        },
        "non_claims": [
            "Not a dark-energy residual detection",
            "Not a measurement of Omega_Lambda",
            "Not a solution of H0 tension",
            "H0=75 is CF residual convention, not fitted here",
            "Block scale L is scanned; not tuned to a theory target",
        ],
    }

    (OUT / "cf4_block_net.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    # human summary
    lines = [
        "REAL DATA: Cosmicflows-4 block-net (matter peculiar velocities)",
        f"Source: {SOURCE['reference']}  CDS {SOURCE['cds']} table2.dat",
        f"H0 for v_pec = Vcmb - H0*d : {H0_CF_KMS} km/s/Mpc (CF convention, not fitted)",
        f"N galaxies (cuts): {len(d)}",
        f"v_pec rms (global): {v_pec.std():.1f} km/s  "
        f"(jackknife subsample rms std {jk_rms.std():.1f})",
        "",
        "Block side L | N_blocks | sigma(v_block) | v_H(L)=H0*L | eta=sig/vH | r_e (1/e)",
    ]
    for L in L_list:
        row = results_L.get(str(L), {})
        if row.get("skipped"):
            lines.append(f"{L:6.1f} | skipped (few blocks)")
            continue
        lines.append(
            f"{L:6.1f} | {row['n_blocks']:5d} | {row['sigma_v_block_means_km_s']:8.1f} | "
            f"{row['v_Hubble_at_L_km_s']:8.1f} | {row['eta_sigma_v_over_vH']:5.2f} | "
            f"{row['correlation']['r_e_1over_e_Mpc']:6.1f}"
        )
    lines += [
        "",
        "Definitions:",
        "  v_pec = Vcmb - H0*d   (line-of-sight residual vs pure Hubble at fixed H0)",
        "  eta = rms(block-mean v_pec) / (H0*L)  — gravity/peculiar vs expansion at scale L",
        "  r_e = separation where block-mean velocity correlation falls to 1/e",
        "",
        "Non-claims: not DE residual; not Omega; not H0 solution; no free dials.",
        f"Wrote {OUT / 'cf4_block_net.json'}",
    ]
    text = "\n".join(lines) + "\n"
    (OUT / "cf4_block_net.txt").write_text(text, encoding="utf-8")
    print()
    print(text)

    # provenance copy
    prov = (
        "DATA PROVENANCE\n"
        f"Catalog: {SOURCE['catalog']}\n"
        f"Paper: {SOURCE['reference']}\n"
        f"CDS: {SOURCE['cds']}\n"
        f"Files: {SOURCE['url_table2']}\n"
        f"ReadMe: {SOURCE['url_readme']}\n"
        f"Data file in repo: data/real_velocity_net/{Path(table2).name}
"
        f"H0 convention: {H0_CF_KMS} km/s/Mpc for v_pec only\n"
    )
    (OUT / "PROVENANCE.txt").write_text(prov, encoding="utf-8")


if __name__ == "__main__":
    main()
