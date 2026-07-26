# Collapse peaks, velocity relief, and gravity vs expansion (Cosmicflows-4)

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)  
July 2026 · data note · not peer reviewed

**Code:** [`scripts/r1/r1_collapse_relief_cf4.py`](../../scripts/r1/r1_collapse_relief_cf4.py)  
**Results:** [`results/r1_collapse_relief/`](../../results/r1_collapse_relief/)  
**Companion (volume net):** [`r1-real-velocity-block-net.md`](r1-real-velocity-block-net.md)

---

## What this is

The previous note cast a cubic “net” over Cosmicflows-4 and measured block-mean residual velocities.  
Here I ask a sharper question on the **same public catalog**:

> Where does **matter collapse most**, what is the **velocity relief** (topography) at those points, and how does that kinematic relief compare to **pure expansion** at the matter nonlinear grain?

Only real CF4 numbers. No dark-energy residual map, no $\Omega$ fit, no free $H_0$, no numerology.

---

## Data source

| Item | Value |
|:-----|:------|
| Catalog | Cosmicflows-4 |
| Paper | Tully et al. 2023, ApJ **944**, 94 |
| Archive | CDS `J/ApJ/944/94` |
| Files | `table2.dat` (galaxies + membership), `table4.dat` (group Dist, Vpec) |
| $H_0$ convention | $75\,\mathrm{km\,s^{-1}Mpc^{-1}}$ (CF residual scale; **not** fitted) |
| Neighbor radius | $R_{\mathrm{nei}}=10\,\mathrm{Mpc}$ (same decade as repo $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$) |

Published $V_{\mathrm{pec}}$ is the CF4 ramp column (their Eq. 11), not a re-fit of $H_0$.

Literature I cite but **do not recompute**: Whitford et al. 2023 (bulk flow on CF4); Courtois et al. 2023 (density/velocity grids); Tully et al. 2008 (Local Void outflow); Shaya et al. 2017 (Local Supercluster action dynamics).

---

## Collapse proxies (from the catalog only)

1. **$N_{\mathrm{mem}}$** — number of CF4 table2 galaxies sharing the group’s `1PGC` (multiplicity).  
2. **$n_{10}$** — number of CF4 galaxies within $10\,\mathrm{Mpc}$ of the group center (local density).

Classes (percentiles of the data, not theory targets):

| Class | Definition |
|:------|:-----------|
| multi | $N_{\mathrm{mem}}\ge 2$ |
| peak | multi **and** $n_{10}\ge p_{75}$ |
| peak_strong | multi **and** $n_{10}\ge p_{90}$ |
| void_proxy | $n_{10}\le p_{25}$ **and** $N_{\mathrm{mem}}\le 1$ |

On this run: $p_{75}(N_{\mathrm{mem}}|\mathrm{multi})=4$, $p_{75}(n_{10})=21$, $p_{90}(n_{10})=46$, $p_{25}(n_{10})=4$.

---

## Velocity “relief” (what I mean by that)

**Relief** here is the **topography of the kinematic field**, not a mass map:

| Layer | Estimator |
|:------|:----------|
| External | catalog $V_{\mathrm{pec}}$ mean / rms by environment |
| Internal | for multi-member groups: $\mathrm{rms}(V_{\mathrm{cmb}}^{\mathrm{members}})$ about group $V_{3k}$ |
| Relief curve | both quantities in bins of $n_{10}$ |

Internal rms is the closest thing in these tables to “matter colliding / orbiting inside a collapsed patch.”  
External $V_{\mathrm{pec}}$ mixes coherent flow **and** distance error; denser multi-member systems often **average better**, so catalog scatter can **drop** even where gravity is strong. I keep that caveat explicit.

---

## Gravity vs expansion diagnostics

Repo geometry (not refit to CF4): $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ from the sandwich / $\sigma(R)$ work.  
At CF $H_0=75$:

\[
v_H(R_{\mathrm{nl}})=H_0 R_{\mathrm{nl}}\approx 646\,\mathrm{km\,s^{-1}}.
\]

| Symbol | Definition | Meaning |
|:-------|:-----------|:--------|
| $\eta_{\mathrm{int}}$ | $\mathrm{internal\,vrms}/(H_0 R_{\mathrm{nl}})$ | internal relief vs expansion across one nonlinear grain |
| $\eta_{\mathrm{pec}}$ | $\lvert V_{\mathrm{pec}}\rvert/(H_0 d)$ | group residual vs Hubble at its distance |
| $\eta(L)$ | $\sigma(v_{\mathrm{block}})/(H_0 L)$ | volume block net (previous note) |

If $\eta_{\mathrm{int}}\sim\mathcal{O}(1)$, internal dispersion is competing with expansion across $R_{\mathrm{nl}}$.  
Median peaks sit **below** that; the **high-multiplicity** tail and individual rich groups can approach it.

---

## Results (this run)

Reproduce:

```bash
python scripts/r1/r1_collapse_relief_cf4.py
```

| Sample | $N$ | $\langle V_{\mathrm{pec}}\rangle$ | rms$(V_{\mathrm{pec}})$ | med $n_{10}$ | med internal vrms | med $\eta_{\mathrm{int}}$ | med $\eta_{\mathrm{pec}}$ |
|:-------|----:|----------------------------------:|------------------------:|-------------:|------------------:|--------------------------:|--------------------------:|
| all groups | 12337 | 91 | 640 | 9 | 108 | 0.17 | 0.050 |
| multi | 1566 | 78 | 429 | 14 | 108 | 0.17 | 0.036 |
| high multiplicity ($N_{\mathrm{mem}}\ge 4$) | 422 | 87 | 338 | 15 | **255** | **0.40** | 0.028 |
| peak (multi + dense) | 530 | 59 | **301** | 38 | 96 | 0.15 | 0.045 |
| peak_strong (multi + $p_{90}$) | 221 | 13 | **247** | 97 | 80 | 0.12 | 0.089 |
| void_proxy | 3240 | 22 | **805** | 2 | — | — | 0.046 |

**Peak vs void (catalog $V_{\mathrm{pec}}$):**

- peak $/$ void rms$(V_{\mathrm{pec}})\approx 0.37$  
- peak_strong $/$ void $\approx 0.31$  
- med $\eta_{\mathrm{pec}}$ is **similar** peak vs void ($\sim 0.045$); the big contrast is in **scatter**, not median residual fraction.

### Relief curve (six equal-count bins of $n_{10}$)

As local density rises, **catalog** rms$(V_{\mathrm{pec}})$ falls from $\sim 790\,\mathrm{km\,s^{-1}}$ (emptiest bin) to $\sim 390\,\mathrm{km\,s^{-1}}$ (densest).  
Internal vrms stays of order $90$–$120\,\mathrm{km\,s^{-1}}$ for systems that have members; the **high-multiplicity** cut is where internal relief jumps ($\mathrm{med}\sim 255\,\mathrm{km\,s^{-1}}$).

That pattern is consistent with: **voids / singles** → noisier individual $V_{\mathrm{pec}}$; **collapsed multi-member systems** → shared flow + real internal dispersion from gravity.

### Distance shells (selection control)

Median $n_{10}$ is huge only nearby ($d<20\,\mathrm{Mpc}$: med $n_{10}\sim 286$) and falls with distance as the CF4 galaxy sampling thins.  
rms$(V_{\mathrm{pec}})$ **rises** with distance (distance-error contribution grows with $H_0 d$).  
So the densest peaks on the top-list are **local Supercluster / Virgo-class** volume — where the catalog is densest — not a claim that collapse only happens nearby.

### Top multi-member collapse sites (highest $n_{10}$)

Examples from this run (not renamed to popular cluster names without an external ID cross-match):

| 1PGC | $d$ [Mpc] | $V_{\mathrm{pec}}$ | $N_{\mathrm{mem}}$ | $n_{10}$ | internal vrms | $\eta_{\mathrm{pec}}$ | $\eta_{\mathrm{int}}$ |
|-----:|----------:|-------------------:|-------------------:|---------:|--------------:|----------------------:|----------------------:|
| 37048 | 10.0 | +358 | 2 | 590 | 126 | 0.48 | 0.19 |
| 41066 | 8.1 | +284 | 4 | 577 | 65 | 0.47 | 0.10 |
| 32256 | 10.8 | +271 | **13** | 560 | **415** | 0.34 | **0.64** |
| 34695 | 11.4 | +267 | 5 | 539 | 144 | 0.31 | 0.22 |
| 41618 | 12.3 | +677 | 2 | 458 | 202 | 0.73 | 0.31 |

1PGC **32256** is the clearest “matter pile-up + internal relief” object in the multi-member top list: many CF4 members, large internal velocity scatter, $\eta_{\mathrm{int}}$ of order two-thirds of expansion across $R_{\mathrm{nl}}$.

---

## Gravity vs expansion in these numbers

Collapse peaks in CF4 are multi-member groups with high $n_{10}$. Expansion across one $R_{\mathrm{nl}}$ cell is $v_H\sim 650\,\mathrm{km\,s^{-1}}$. Typical peak internal rms is $\sim 100\,\mathrm{km\,s^{-1}}$; rich multi-member systems reach $\sim 0.4\,v_H$ in the median and order unity in the tail. Catalog $V_{\mathrm{pec}}$ scatter is larger in voids mostly because singles carry more distance noise, not because gravity is stronger there. The block net gives the same volume-level pattern: $\eta(L)>1$ for $L\sim 5$–$15\,\mathrm{Mpc}$ and $\eta(L)<1$ for $L\gtrsim 30\,\mathrm{Mpc}$.

---

## Limits of this run

CF4: line-of-sight only; $e_{\mathrm{DM}}$ dominates individual $V_{\mathrm{pec}}$; membership is only CF4 galaxies; sky and TF/FP/SN mix are uneven.

Not measured here: $\Omega_m$, $f\sigma_8$, DE residual $\sigma_X$, coupling $g$, free $H_0$. Residual × structure (T2) needs a residual map, not only matter kinematics. Courtois grids and Whitford bulk-flow vectors are cited, not recomputed. $R_{\mathrm{nei}}=10\,\mathrm{Mpc}$ is fixed near the $R_{\mathrm{nl}}$ decade; it is not a fit of $\ell_{\ast}$ to CF4 peaks.

If I continue: cross-match top `1PGC` to named structures (labels only); optional Courtois grids; do not retune DESI residual or sandwich numbers to CF4.

---

## References

1. R. B. Tully et al., *Cosmicflows-4*, Astrophys. J. **944**, 94 (2023).  
2. CDS [J/ApJ/944/94](https://cdsarc.cds.unistra.fr/viz-bin/cat/J/ApJ/944/94).  
3. A. M. Whitford et al., MNRAS **526**, 3051 (2023).  
4. H. M. Courtois et al., A&A **670**, L15 (2023).  
5. R. B. Tully et al., ApJ **676**, 184 (2008).  
6. E. J. Shaya et al., ApJ **850**, 207 (2017).
