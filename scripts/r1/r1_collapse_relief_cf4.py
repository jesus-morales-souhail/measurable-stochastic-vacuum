#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Collapse peaks + velocity relief + gravity/expansion impact on Cosmicflows-4.

Sources:
  Tully et al. 2023, ApJ 944, 94  — Cosmicflows-4
  CDS J/ApJ/944/94
    table2.dat  galaxies (membership via 1PGC)
    table4.dat  groups with published Dist, Vpec (CF4 formulas)

Literature context (cited, not recomputed here):
  Whitford et al. 2023, MNRAS 526, 3051 — bulk flow estimators on CF4
  Courtois et al. 2023, A&A 670, L15 — CF4 density/velocity grids
  Tully et al. 2008, ApJ 676, 184 — Local Void outflow
  Shaya et al. 2017, ApJ 850, 207 — Local Supercluster action dynamics

WHAT WE MEASURE (data only):
  1) Collapse proxies: N_mem (table2 membership), n_gal(<10 Mpc)
  2) Peak classes: multi-member & high density (p75 / p90)
  3) Velocity relief (topography of matter kinematics):
       - internal: rms(member Vcmb) about group V3k
       - external: catalog Vpec scatter by environment
       - density-binned Vpec / internal-vrms profile (relief curve)
  4) Gravity vs expansion diagnostics at collapse points:
       - eta_int = internal_vrms / (H0 * R_char)   [R_char ~ R_nl = 8.61 Mpc]
       - eta_pec = |Vpec| / (H0 * Dist) for each group
       - peak vs void contrast of both
  5) Top multi-member collapse list + distance shells
  6) Cross-link to block-net eta(L) from prior CF4 run (if present)

NO: DE residual map, Omega fit, free H0, work origin, numerology.
T2 residual×structure is NOT run here (needs residual map; see r1-T2-preregistration).
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "real_velocity_net"
OUT = ROOT / "results" / "r1_collapse_relief"
OUT.mkdir(parents=True, exist_ok=True)

H0_CF = 75.0  # only for eta diagnostic; CF4 Vpec is catalog-published
# Sandwich / matter nonlinear scale from this repo (r1_sigma_R_full.py): geometry only
R_NL_MPC = 8.61
# Neighbor sphere for local density — deliberately near R_nl decade (not fitted)
R_NEI_MPC = 10.0

SOURCE = {
    "catalog": "Cosmicflows-4",
    "paper": "Tully et al. 2023, ApJ 944, 94",
    "cds": "J/ApJ/944/94",
    "files": ["table2.dat", "table4.dat"],
    "urls": {
        "table2": "https://cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/table2.dat.gz",
        "table4": "https://cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/table4.dat.gz",
        "readme": "https://cdsarc.cds.unistra.fr/ftp/J/ApJ/944/94/ReadMe",
    },
    "literature": [
        "Whitford et al. 2023, MNRAS 526, 3051 (CF4 bulk-flow estimators)",
        "Courtois et al. 2023, A&A 670, L15 (CF4 density/velocity grids)",
        "Tully et al. 2008, ApJ 676, 184 (Local Void outflow)",
        "Shaya et al. 2017, ApJ 850, 207 (Local Supercluster action dynamics)",
    ],
    "repo_geometry": {
        "R_nl_Mpc": R_NL_MPC,
        "note": "from results of r1_sigma_R_full.py under stated LCDM shape; not refit here",
    },
}


def parse_table2(path: Path):
    pgc, g1, vcmb, dm, edm = [], [], [], [], []
    sgl, sgb = [], []
    with open(path) as f:
        for line in f:
            if len(line) < 190:
                continue
            try:
                pgc.append(int(line[0:7]))
                g1.append(int(line[8:15]))
                vcmb.append(float(line[22:27]))
                dm.append(float(line[28:34]))
                edm.append(float(line[35:40]))
                sgl.append(float(line[173:181]))
                sgb.append(float(line[182:190]))
            except ValueError:
                continue
    return {
        "pgc": np.asarray(pgc, int),
        "g1": np.asarray(g1, int),
        "vcmb": np.asarray(vcmb, float),
        "dm": np.asarray(dm, float),
        "edm": np.asarray(edm, float),
        "sgl": np.asarray(sgl, float),
        "sgb": np.asarray(sgb, float),
    }


def parse_table4(path: Path):
    g1, dmzp, edm, dist = [], [], [], []
    v3k, vpec, vpds, vpwf, hi = [], [], [], [], []
    sgl, sgb = [], []
    with open(path) as f:
        for line in f:
            if len(line) < 136:
                continue
            try:
                g1.append(int(line[0:7]))
                dmzp.append(float(line[8:14]))
                edm.append(float(line[15:20]))
                dist.append(float(line[21:26]))
                v3k.append(float(line[39:44]))
                # Vpds 52-57, Vpwf 59-63, Vpec 65-69
                vpds.append(float(line[51:57]))
                vpwf.append(float(line[58:63]))
                vpec.append(float(line[64:69]))
                hi.append(float(line[70:75]))
                sgl.append(float(line[119:127]))
                sgb.append(float(line[128:136]))
            except ValueError:
                continue
    return {
        "g1": np.asarray(g1, int),
        "dmzp": np.asarray(dmzp, float),
        "edm": np.asarray(edm, float),
        "dist": np.asarray(dist, float),
        "v3k": np.asarray(v3k, float),
        "vpds": np.asarray(vpds, float),
        "vpwf": np.asarray(vpwf, float),
        "vpec": np.asarray(vpec, float),
        "hi": np.asarray(hi, float),
        "sgl": np.asarray(sgl, float),
        "sgb": np.asarray(sgb, float),
    }


def sg_xyz(d, sgl_deg, sgb_deg):
    sgl = np.deg2rad(sgl_deg)
    sgb = np.deg2rad(sgb_deg)
    x = d * np.cos(sgb) * np.cos(sgl)
    y = d * np.cos(sgb) * np.sin(sgl)
    z = d * np.sin(sgb)
    return np.column_stack([x, y, z])


def neighbor_counts(xyz: np.ndarray, R: float) -> np.ndarray:
    """n_neighbors within R Mpc (excluding self). O(N^2) — N~fewe 10k ok with chunking."""
    n = len(xyz)
    counts = np.zeros(n, dtype=int)
    # brute force in chunks
    R2 = R * R
    chunk = 500
    for i0 in range(0, n, chunk):
        i1 = min(n, i0 + chunk)
        d2 = np.sum((xyz[i0:i1, None, :] - xyz[None, :, :]) ** 2, axis=2)
        counts[i0:i1] = np.sum((d2 < R2) & (d2 > 0), axis=1)
    return counts


def group_member_stats(g2, g4_index):
    """
    For each group in table4, members from table2 with same 1PGC.
    Internal relief: rms of member Vcmb about group V3k.
    """
    # map g1 -> list of vcmb
    members = defaultdict(list)
    for g, v in zip(g2["g1"], g2["vcmb"]):
        members[int(g)].append(float(v))

    n_mem = np.zeros(len(g4_index), dtype=int)
    v_rms_int = np.full(len(g4_index), np.nan)
    for i, g in enumerate(g4_index):
        vs = members.get(int(g), [])
        n_mem[i] = len(vs)
        if len(vs) >= 2:
            v_rms_int[i] = float(np.std(vs))
    return n_mem, v_rms_int


def summarize(name, vpec, n_mem=None, v_rms_int=None, n_nei=None, dist=None):
    out = {
        "label": name,
        "N": int(len(vpec)),
        "vpec_mean": float(np.mean(vpec)) if len(vpec) else None,
        "vpec_median": float(np.median(vpec)) if len(vpec) else None,
        "vpec_rms": float(np.std(vpec)) if len(vpec) else None,
        "vpec_p16": float(np.percentile(vpec, 16)) if len(vpec) else None,
        "vpec_p84": float(np.percentile(vpec, 84)) if len(vpec) else None,
        "abs_vpec_median": float(np.median(np.abs(vpec))) if len(vpec) else None,
    }
    if n_mem is not None and len(n_mem):
        out["n_mem_median"] = float(np.median(n_mem))
        out["n_mem_mean"] = float(np.mean(n_mem))
        out["n_mem_max"] = int(np.max(n_mem))
    if v_rms_int is not None:
        ok = np.isfinite(v_rms_int)
        if np.any(ok):
            out["internal_vrms_median"] = float(np.median(v_rms_int[ok]))
            out["internal_vrms_mean"] = float(np.mean(v_rms_int[ok]))
            out["N_with_internal"] = int(np.sum(ok))
            # gravity vs expansion: internal dispersion vs Hubble across R_nl
            v_H_Rnl = H0_CF * R_NL_MPC
            out["eta_int_median"] = float(np.median(v_rms_int[ok]) / v_H_Rnl)
            out["eta_int_mean"] = float(np.mean(v_rms_int[ok]) / v_H_Rnl)
            out["v_H_Rnl_km_s"] = float(v_H_Rnl)
    if n_nei is not None and len(n_nei):
        out["n_nei_median"] = float(np.median(n_nei))
        out["n_nei_mean"] = float(np.mean(n_nei))
    if dist is not None and len(dist) and len(vpec):
        v_H_d = H0_CF * dist
        eta_pec = np.abs(vpec) / np.maximum(v_H_d, 1.0)
        out["eta_pec_median"] = float(np.median(eta_pec))
        out["eta_pec_mean"] = float(np.mean(eta_pec))
        out["frac_eta_pec_gt_1"] = float(np.mean(eta_pec > 1.0))
    return out


def density_binned_relief(n_nei, vpec, v_rms_int, n_bins=6):
    """Relief curve: Vpec and internal vrms vs local density percentile bins."""
    order = np.argsort(n_nei)
    n = len(n_nei)
    edges = np.linspace(0, n, n_bins + 1, dtype=int)
    bins = []
    for b in range(n_bins):
        idx = order[edges[b] : edges[b + 1]]
        if len(idx) == 0:
            continue
        vi = v_rms_int[idx]
        ok = np.isfinite(vi)
        bins.append(
            {
                "bin": b + 1,
                "n_nei_lo": int(np.min(n_nei[idx])),
                "n_nei_hi": int(np.max(n_nei[idx])),
                "n_nei_median": float(np.median(n_nei[idx])),
                "N": int(len(idx)),
                "vpec_mean": float(np.mean(vpec[idx])),
                "vpec_rms": float(np.std(vpec[idx])),
                "abs_vpec_median": float(np.median(np.abs(vpec[idx]))),
                "internal_vrms_median": float(np.median(vi[ok])) if np.any(ok) else None,
                "N_with_internal": int(np.sum(ok)),
            }
        )
    return bins


def distance_shell_stats(dist, n_nei, vpec, multi, shells):
    """Collapse strength and Vpec by distance shell (selection control)."""
    rows = []
    for dlo, dhi in shells:
        m = (dist >= dlo) & (dist < dhi)
        if not np.any(m):
            continue
        rows.append(
            {
                "d_lo_Mpc": dlo,
                "d_hi_Mpc": dhi,
                "N_groups": int(np.sum(m)),
                "N_multi": int(np.sum(m & multi)),
                "n_nei_median": float(np.median(n_nei[m])),
                "n_nei_p90": float(np.percentile(n_nei[m], 90)),
                "vpec_rms": float(np.std(vpec[m])),
                "vpec_mean": float(np.mean(vpec[m])),
                "frac_multi": float(np.mean(multi[m])),
            }
        )
    return rows


def load_block_net_eta():
    """Cross-link prior block-net run if present (same repo, not re-derived)."""
    p = ROOT / "results" / "r1_real_velocity_net" / "cf4_block_net.json"
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None
    # tolerate several key layouts
    if "block_scan" in data:
        return data["block_scan"]
    if "blocks" in data:
        return data["blocks"]
    if "eta_by_L" in data:
        return data["eta_by_L"]
    # raw dump of scan rows
    for k in ("scan", "results", "L_scan"):
        if k in data:
            return data[k]
    return {"note": "json present but scan keys not recognized", "keys": list(data.keys())[:20]}


def main():
    t2 = DATA / "table2.dat"
    t4 = DATA / "table4.dat"
    if not t2.exists() or not t4.exists():
        raise FileNotFoundError("Need CF4 table2.dat and table4.dat in data/real_velocity_net/")

    print("=== CF4 collapse peaks + velocity relief (data only) ===")
    print(f"Source: {SOURCE['paper']}  CDS {SOURCE['cds']}\n")

    g2 = parse_table2(t2)
    g4 = parse_table4(t4)

    # Group quality cuts (table4)
    d = g4["dist"]
    m = (
        np.isfinite(d)
        & np.isfinite(g4["vpec"])
        & np.isfinite(g4["edm"])
        & (g4["edm"] <= 0.5)
        & (d > 1.0)
        & (d < 200.0)
        & (np.abs(g4["v3k"]) < 30000)
    )
    for k in g4:
        g4[k] = g4[k][m]

    # Galaxy cuts for density field
    d2 = 10.0 ** ((g2["dm"] - 25.0) / 5.0)
    m2 = (
        np.isfinite(d2)
        & (g2["edm"] <= 0.5)
        & (d2 > 1.0)
        & (d2 < 200.0)
    )
    for k in g2:
        g2[k] = g2[k][m2]
    d2 = d2[m2]

    print(f"Groups after cuts: {len(g4['dist'])}")
    print(f"Galaxies after cuts: {len(d2)}")

    # Membership + internal relief
    n_mem, v_rms_int = group_member_stats(g2, g4["g1"])

    # Local density from galaxy field around group centers
    xyz_g = sg_xyz(g4["dist"], g4["sgl"], g4["sgb"])
    xyz_gal = sg_xyz(d2, g2["sgl"], g2["sgb"])
    R_nei = R_NEI_MPC
    print(f"Counting galaxies within {R_nei} Mpc of each group (near R_nl={R_NL_MPC} Mpc)...")
    n_nei = np.zeros(len(xyz_g), dtype=int)
    R2 = R_nei**2
    chunk = 200
    for i0 in range(0, len(xyz_g), chunk):
        i1 = min(len(xyz_g), i0 + chunk)
        d2m = np.sum((xyz_g[i0:i1, None, :] - xyz_gal[None, :, :]) ** 2, axis=2)
        n_nei[i0:i1] = np.sum(d2m < R2, axis=1)

    # Collapse classes from the data (not theory targets)
    multi = n_mem >= 2
    n_mem_multi = n_mem[multi]
    thr_mem = float(np.percentile(n_mem_multi, 75)) if len(n_mem_multi) else 3.0
    thr_nei_hi = float(np.percentile(n_nei, 75))
    thr_nei_lo = float(np.percentile(n_nei, 25))
    thr_nei_p90 = float(np.percentile(n_nei, 90))

    high_mem = multi & (n_mem >= thr_mem)
    high_nei = n_nei >= thr_nei_hi
    low_nei = n_nei <= thr_nei_lo
    very_high_nei = n_nei >= thr_nei_p90
    peak = multi & high_nei
    peak_strong = multi & very_high_nei
    void = low_nei & (n_mem <= 1)

    vpec = g4["vpec"]  # catalog published (ramp Eq. 11)
    vpwf = g4["vpwf"]
    vpds = g4["vpds"]
    dist = g4["dist"]

    def S(name, mask):
        return summarize(
            name,
            vpec[mask],
            n_mem[mask],
            v_rms_int[mask],
            n_nei[mask],
            dist[mask],
        )

    samples = {
        "all_groups": summarize("all_groups", vpec, n_mem, v_rms_int, n_nei, dist),
        "high_multiplicity": S("high_multiplicity", high_mem),
        "high_local_density": S("high_local_density", high_nei),
        "low_local_density": S("low_local_density", low_nei),
        "multi_member": S("multi_member", multi),
        "peak_multi_and_dense": S("peak_multi_and_dense", peak),
        "peak_strong_p90_density": S("peak_strong_p90_density", peak_strong),
        "void_proxy": S("void_proxy", void),
    }

    # Same splits for alternative CF4 PV estimators (robustness)
    alt = {}
    for name, arr in [("Vpwf", vpwf), ("Vpds", vpds)]:
        alt[name] = {
            "all_rms": float(np.std(arr)),
            "peak_rms": float(np.std(arr[peak])) if np.any(peak) else None,
            "peak_strong_rms": float(np.std(arr[peak_strong])) if np.any(peak_strong) else None,
            "void_rms": float(np.std(arr[void])) if np.any(void) else None,
            "peak_mean": float(np.mean(arr[peak])) if np.any(peak) else None,
            "void_mean": float(np.mean(arr[void])) if np.any(void) else None,
        }

    # Top collapse: (A) highest n_nei any group; (B) multi-member only (true collapse)
    def top_from_mask(mask, n_top=15):
        idx_all = np.where(mask)[0]
        if len(idx_all) == 0:
            return []
        order = idx_all[np.argsort(-n_nei[idx_all])][:n_top]
        rows = []
        for i in order:
            v_H_d = H0_CF * dist[i]
            eta_pec_i = abs(float(vpec[i])) / max(v_H_d, 1.0)
            vint = None if not np.isfinite(v_rms_int[i]) else float(v_rms_int[i])
            eta_int_i = None if vint is None else vint / (H0_CF * R_NL_MPC)
            rows.append(
                {
                    "1PGC": int(g4["g1"][i]),
                    "Dist_Mpc": float(dist[i]),
                    "V3k_km_s": float(g4["v3k"][i]),
                    "Vpec_km_s": float(vpec[i]),
                    "N_mem_in_CF4_table2": int(n_mem[i]),
                    "N_gal_within_10Mpc": int(n_nei[i]),
                    "internal_vrms_km_s": vint,
                    "eta_pec_abs_Vpec_over_H0d": float(eta_pec_i),
                    "eta_int_vrms_over_H0_Rnl": eta_int_i,
                    "SGL_deg": float(g4["sgl"][i]),
                    "SGB_deg": float(g4["sgb"][i]),
                }
            )
        return rows

    top_any = top_from_mask(np.ones(len(n_nei), dtype=bool), 15)
    top_multi = top_from_mask(multi, 20)
    top_peak = top_from_mask(peak, 15)

    # Relief curve + shells + gravity contrast
    relief_bins = density_binned_relief(n_nei, vpec, v_rms_int, n_bins=6)
    shells = distance_shell_stats(
        dist,
        n_nei,
        vpec,
        multi,
        shells=[(1, 20), (20, 40), (40, 80), (80, 120), (120, 200)],
    )

    def safe_ratio(a, b):
        if a is None or b is None or b == 0:
            return None
        return float(a / b)

    contrast = {
        "thresholds": {
            "N_mem_p75_among_multi": float(thr_mem),
            "n_nei_10Mpc_p75": float(thr_nei_hi),
            "n_nei_10Mpc_p25": float(thr_nei_lo),
            "n_nei_10Mpc_p90": float(thr_nei_p90),
            "neighbor_radius_Mpc": R_nei,
            "R_nl_Mpc_repo": R_NL_MPC,
            "H0_CF_convention": H0_CF,
        },
        "peak_minus_void_vpec_mean": (
            samples["peak_multi_and_dense"]["vpec_mean"]
            - samples["void_proxy"]["vpec_mean"]
            if samples["peak_multi_and_dense"]["N"] and samples["void_proxy"]["N"]
            else None
        ),
        "peak_over_void_vpec_rms": safe_ratio(
            samples["peak_multi_and_dense"].get("vpec_rms"),
            samples["void_proxy"].get("vpec_rms"),
        ),
        "peak_strong_over_void_vpec_rms": safe_ratio(
            samples["peak_strong_p90_density"].get("vpec_rms"),
            samples["void_proxy"].get("vpec_rms"),
        ),
        "peak_internal_vrms_median": samples["peak_multi_and_dense"].get(
            "internal_vrms_median"
        ),
        "multi_internal_vrms_median": samples["multi_member"].get("internal_vrms_median"),
        "peak_eta_int_median": samples["peak_multi_and_dense"].get("eta_int_median"),
        "peak_eta_pec_median": samples["peak_multi_and_dense"].get("eta_pec_median"),
        "void_eta_pec_median": samples["void_proxy"].get("eta_pec_median"),
        "peak_over_void_eta_pec": safe_ratio(
            samples["peak_multi_and_dense"].get("eta_pec_median"),
            samples["void_proxy"].get("eta_pec_median"),
        ),
        "interpretation": {
            "vpec_rms_lower_in_peaks": (
                "Often true in CF catalogs: dense multi-member systems have better "
                "averaged distances / shared flow, so catalog Vpec scatter drops; "
                "NOT a claim that gravity is weak in clusters."
            ),
            "internal_vrms": (
                "Member Vcmb scatter about group V3k — internal kinematic relief "
                "from orbital / infall motions inside collapsed systems."
            ),
            "eta_int": (
                "internal_vrms / (H0*R_nl): if >1, internal dispersion exceeds "
                "Hubble expansion across one R_nl cell (gravity-dominated grain)."
            ),
            "eta_pec": (
                "|Vpec|/(H0*Dist): group residual vs pure Hubble at its distance "
                "(CF H0 convention)."
            ),
        },
    }

    # Literature anchors (published, not re-derived)
    literature_bulk = {
        "Whitford_etal_2023_MNRAS": {
            "cite": "Whitford et al. 2023, MNRAS 526, 3051",
            "MLE_bulk_flow": "408 ± 165 km/s at depth ~49 Mpc/h",
            "MVE_bulk_flow": "428 ± 108 km/s at depth ~173 Mpc/h",
            "note": "Published CF4 bulk-flow estimates; direction toward Great Attractor region discussed in that paper.",
        },
        "Courtois_etal_2023_AA": {
            "cite": "Courtois et al. 2023, A&A 670, L15",
            "note": "Published CF4 density and velocity field reconstructions (grids).",
        },
        "Tully_etal_2008_ApJ": {
            "cite": "Tully et al. 2008, ApJ 676, 184",
            "note": "Local Void: galaxies move away from void (outflow) — opposite of collapse peaks.",
        },
        "Shaya_etal_2017_ApJ": {
            "cite": "Shaya et al. 2017, ApJ 850, 207",
            "note": "Action dynamics of Local Supercluster; Virgo attractor + local shear field.",
        },
    }

    # Remaining variables inventory (repo + data limits — honesty, not a claim list)
    remaining_vars = {
        "from_this_catalog": [
            "Distance errors e_DM dominate individual Vpec; group averages help but residual scatter mixes signal+noise",
            "Only line-of-sight velocity (no full 3D velocity field from CF4 tables alone)",
            "Selection: TF/FP/SN methodology mix; sky coverage not uniform (SDSS north vs south)",
            "H0=75 is CF convention for residual scale, not a cosmological fit",
            "Membership N_mem from table2 1PGC only samples CF4 galaxies, not complete group membership",
        ],
        "from_this_repo_theory_side": [
            "R_nl≈8.61 Mpc assumed as geometry for eta_int scale (sandwich); not refit to CF4",
            "g, lambda, sigma_X are DE residual parameters — NOT measured in this script",
            "T2 residual×structure needs a residual map (DESI-scale); CF4 is matter kinematics only",
            "Block-net eta(L) from r1_real_velocity_block_net is the complementary volume average",
        ],
        "from_literature_not_recomputed": [
            "Full CF4 Wiener/density grids (Courtois+2023) — would give continuous delta,v fields",
            "Whitford bulk-flow vectors — coherent large-scale flow vs local collapse",
            "Cluster masses / velocity dispersions from X-ray or caustic methods (external)",
            "Reconstruction of 3D velocity from sparse PV (malmquist, bias corrections)",
        ],
        "explicitly_not_done_here": [
            "No Omega_m / growth-rate f_sigma8 fit",
            "No DE residual detection or residual×collapse cross-correlation",
            "No free H0 solution from CF4",
            "No work-origin or vacuum-energy claim from collapse peaks",
        ],
    }

    block_net_link = load_block_net_eta()

    out = {
        "source": SOURCE,
        "cuts": {
            "groups": "e_DM<=0.5, 1<Dist<200 Mpc, |V3k|<30000",
            "galaxies": "e_DM<=0.5, 1<d<200 Mpc",
            "Vpec_column": "table4 Vpec (CF4 ramp, Eq. 11 of Tully+2023)",
            "peak_definition": "multi (N_mem>=2) AND n_nei >= p75; peak_strong: multi AND n_nei>=p90",
            "void_definition": "n_nei <= p25 AND N_mem <= 1",
        },
        "samples": samples,
        "alt_estimators": alt,
        "contrast_peak_vs_void": contrast,
        "relief_vs_density_bins": relief_bins,
        "distance_shells": shells,
        "top_collapse_any_n_nei": top_any,
        "top_collapse_multi_member": top_multi,
        "top_collapse_peak_class": top_peak,
        "literature_bulk_flow": literature_bulk,
        "block_net_crosslink": block_net_link,
        "remaining_variables": remaining_vars,
        "non_claims": [
            "Not a dark-energy residual measurement",
            "Not Omega_m / Omega_Lambda fit",
            "Not a free H0 determination",
            "Collapse proxies are N_mem and n_gal(<10 Mpc) from CF4 only",
            "Internal vrms uses member Vcmb about group V3k (table2+table4)",
            "Lower catalog Vpec rms in peaks is partly measurement/averaging, not weak gravity",
        ],
    }
    (OUT / "collapse_relief.json").write_text(json.dumps(out, indent=2), encoding="utf-8")

    def fmt(x, w=7, p=1):
        if x is None:
            return f"{'nan':>{w}}"
        return f"{x:{w}.{p}f}"

    lines = [
        "CF4 COLLAPSE PEAKS + VELOCITY RELIEF + GRAVITY/EXPANSION (data only)",
        f"Source: {SOURCE['paper']}  CDS {SOURCE['cds']}",
        f"Groups N={samples['all_groups']['N']}  Galaxies N={len(d2)}",
        f"R_nei={R_nei} Mpc  R_nl(repo)={R_NL_MPC} Mpc  H0_CF={H0_CF}",
        f"Thresholds: N_mem p75(multi)={thr_mem:.1f}  n_nei p75={thr_nei_hi:.1f} "
        f"p25={thr_nei_lo:.1f} p90={thr_nei_p90:.1f}",
        f"N multi={int(np.sum(multi))}  peak={int(np.sum(peak))}  "
        f"peak_strong={int(np.sum(peak_strong))}  void={int(np.sum(void))}",
        "",
        "Sample | N | <Vpec> | rms(Vpec) | med|V| | med Nmem | med n10 | med vrms_int | eta_int | eta_pec",
    ]
    for key in [
        "all_groups",
        "multi_member",
        "high_multiplicity",
        "high_local_density",
        "low_local_density",
        "peak_multi_and_dense",
        "peak_strong_p90_density",
        "void_proxy",
    ]:
        s = samples[key]
        lines.append(
            f"{key:24s} | {s['N']:5d} | {fmt(s.get('vpec_mean'))} | {fmt(s.get('vpec_rms'))} | "
            f"{fmt(s.get('abs_vpec_median'))} | {fmt(s.get('n_mem_median'),5,1)} | "
            f"{fmt(s.get('n_nei_median'),6,1)} | {fmt(s.get('internal_vrms_median'))} | "
            f"{fmt(s.get('eta_int_median'),6,3)} | {fmt(s.get('eta_pec_median'),6,3)}"
        )
    lines += [
        "",
        "=== Peak vs void contrast ===",
        f"peak - void <Vpec> = {contrast['peak_minus_void_vpec_mean']}",
        f"peak/void rms(Vpec) = {contrast['peak_over_void_vpec_rms']}",
        f"peak_strong/void rms(Vpec) = {contrast['peak_strong_over_void_vpec_rms']}",
        f"peak med internal vrms = {contrast['peak_internal_vrms_median']}",
        f"peak eta_int (vrms/(H0*R_nl)) = {contrast['peak_eta_int_median']}",
        f"peak eta_pec med = {contrast['peak_eta_pec_median']}  "
        f"void eta_pec med = {contrast['void_eta_pec_median']}",
        f"peak/void eta_pec = {contrast['peak_over_void_eta_pec']}",
        "",
        "=== Relief curve (Vpec vs local density bins) ===",
        "bin | n_nei range | N | <Vpec> | rms(Vpec) | med|V| | med vrms_int",
    ]
    for b in relief_bins:
        lines.append(
            f"  {b['bin']} | {b['n_nei_lo']:3d}-{b['n_nei_hi']:3d} | {b['N']:5d} | "
            f"{b['vpec_mean']:7.1f} | {b['vpec_rms']:7.1f} | {b['abs_vpec_median']:7.1f} | "
            f"{b['internal_vrms_median']}"
        )
    lines += [
        "",
        "=== Distance shells (selection control) ===",
        "d_lo-d_hi | N | N_multi | frac_multi | med n10 | p90 n10 | rms(Vpec)",
    ]
    for sh in shells:
        lines.append(
            f"  {sh['d_lo_Mpc']:3.0f}-{sh['d_hi_Mpc']:3.0f} | {sh['N_groups']:5d} | "
            f"{sh['N_multi']:5d} | {sh['frac_multi']:.3f} | {sh['n_nei_median']:6.1f} | "
            f"{sh['n_nei_p90']:6.1f} | {sh['vpec_rms']:7.1f}"
        )
    lines += [
        "",
        "=== Top MULTI-MEMBER collapse (highest n_gal within 10 Mpc) ===",
        "1PGC  d  Vpec  N_mem  n10  vrms_int  eta_pec  eta_int",
    ]
    for t in top_multi[:12]:
        lines.append(
            f"  {t['1PGC']:8d}  d={t['Dist_Mpc']:5.1f}  Vpec={t['Vpec_km_s']:+6.0f}  "
            f"Nmem={t['N_mem_in_CF4_table2']:3d}  n10={t['N_gal_within_10Mpc']:3d}  "
            f"vint={t['internal_vrms_km_s']}  "
            f"eta_pec={t['eta_pec_abs_Vpec_over_H0d']:.3f}  "
            f"eta_int={t['eta_int_vrms_over_H0_Rnl']}"
        )
    lines += [
        "",
        "=== Gravity vs expansion (definitions) ===",
        f"  v_H(R_nl) = H0*R_nl = {H0_CF * R_NL_MPC:.1f} km/s",
        "  eta_int = internal_vrms / v_H(R_nl)  — internal relief vs expansion grain",
        "  eta_pec = |Vpec| / (H0*Dist)       — group residual vs Hubble at its d",
        "  block-net eta(L) = sigma(v_block)/(H0*L) — volume average (see r1_real_velocity_net)",
        "",
        "Literature (not recomputed):",
        f"  {literature_bulk['Whitford_etal_2023_MNRAS']['cite']}: "
        f"MLE {literature_bulk['Whitford_etal_2023_MNRAS']['MLE_bulk_flow']}; "
        f"MVE {literature_bulk['Whitford_etal_2023_MNRAS']['MVE_bulk_flow']}",
        f"  {literature_bulk['Courtois_etal_2023_AA']['cite']}: CF4 density/velocity grids",
        f"  {literature_bulk['Tully_etal_2008_ApJ']['cite']}: Local Void outflow",
        f"  {literature_bulk['Shaya_etal_2017_ApJ']['cite']}: Local Supercluster action dynamics",
        "",
        "Remaining variables (honest list — see JSON remaining_variables):",
        "  LOS-only; e_DM noise; incomplete membership; no residual×structure (T2);",
        "  no Omega/f_sigma8 fit; Courtois grids not ingested; g/lambda not from CF4.",
        "",
        "Non-claims: matter kinematics only; no DE residual / Omega / H0 solution.",
        f"Wrote {OUT}",
    ]
    text = "\n".join(lines) + "\n"
    (OUT / "collapse_relief.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
