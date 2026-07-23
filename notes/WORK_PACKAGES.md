# Work packages (live status)

**Language:** English 
**Last update:** July 2026 

**Primary results note:** [`papers/VERIFIED_RESULTS.md`](../papers/VERIFIED_RESULTS.md) + `pytest -q` green. 
WP notes are expansions, not independent hard-claim sources.

---

## Overview

| WP | Rule | Status | Main document |
|:---|:-----|:-------|:--------------|
| WP0 | Empirical boundary | **Done** (sister repo) | [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) |
| WP1 | R1 counting seed | **Partial** | [`r1-counting-principle.md`](../papers/r1-counting-principle.md) · [`r1-open-kernel.md`](../papers/r1-open-kernel.md) |
| WP2 | R3 soft open map | **Soft theorems done** | [`r3-open-horizon-map.md`](../papers/r3-open-horizon-map.md) |
| WP3 | R2 slip + path | **Partial** | [`r2-slip-from-same-sector.md`](../papers/r2-slip-from-same-sector.md) |
| WP4 | Joint table + zeros | **Done** | [`wp4-joint-predictions-and-zeros.md`](../papers/wp4-joint-predictions-and-zeros.md) |
| WP5 | Falsification | **Done** | [`wp5-falsification.md`](../papers/wp5-falsification.md) |
| — | Narrow path (NP-A/B) | **Done** | [`NARROW_PATH.md`](../papers/NARROW_PATH.md) |
| — | Lensing RMS vs real data | **Done (OOM gate)** | [`lensing-rms-forecast-real-data.md`](../papers/lensing-rms-forecast-real-data.md) |
| — | Inflation spectator seed (G&W 2005) | **Revalidated (literature door)** | [`inflation-spectator-seed-gordon-wands.md`](../papers/inflation-spectator-seed-gordon-wands.md) |

---

## WP0 — Sister empirical corpus

Null OU/QNM, $\sigma_X<1.5\times 10^{-4}$ (95% CL), tachyonic exclusion, amplifier audit, slip starvation. 
**Do not re-run DESI MCMC here.**

---

## WP1 — Counting seed (partial)

**Delivered:** $\sigma_{0,\mathrm{eff}}=(\ell_*/L)^{d/2}$; Sorkin zero; mesoscopic landscape for $\sigma=10^{-5}$; **open-kernel note** (walls vs kernel; R1d scale class; falsifiers).  
**Open:** principle fixing $\ell_*$ (R1a/b/c/**d**).  
**Code:** `scripts/r1_counting_landscape.py`, `scripts/r1_open_kernel_scales.py`, `lib_verified.py`.  
**Publishable status note:** [`papers/r1-open-kernel.md`](../papers/r1-open-kernel.md).

---

## WP2 — Soft open map (done for soft regime)

**Delivered:** $G_O=e^{2r}$; soft no-gain for Sorkin; $r\sim 64$ required to lift Sorkin (algebra). 
**Open:** hard horizon bath. 
**Code:** `scripts/r3_open_horizon_map.py`.

---

## WP3 — Slip and light path (partial)

**Delivered:** local $|\gamma-1|$; path $\mathrm{RMS}=s\sqrt{N}$; Sorkin path null; meso path OOM. 
**Open:** $\varepsilon$ from symmetry. 
**Code:** `scripts/r2_light_path_accumulation.py`.

---

## WP4 — Joint predictions and zeros (done)

Single table linking seed → soft residual → slip → path RMS; structural zeros Z1–Z6.

---

## WP5 — Falsification (done)

L0–L4 failure levels; decision tree; checklist before any positive paper.

---

## Recommended order going forward

```
Verified core (pytest) ──► R1a/b/c/d candidate (only real missing physics)
 ──► optional hard-R3 only if derived, not dialed
 ──► then Boltzmann if amplitude+ε fixed
```

Do **not** re-open soft amplification of Sorkin (measured walls).  
Do **not** fit $\ell_*$ to DESI or $R_8$/S$_8$.

---

## Run everything

```bash
pip install -r requirements.txt
pytest -q
python scripts/lib_verified.py
python scripts/r1_counting_landscape.py
python scripts/r1_open_kernel_scales.py
python scripts/lensing_rms_real_data_compare.py
python scripts/r3_open_horizon_map.py
python scripts/r2_light_path_accumulation.py
```
