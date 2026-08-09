# Index of notes

Jesús Morales Souhail · July 2026
[github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)

If you just landed: [`../START_HERE.md`](../START_HERE.md).
If I wrote a short paper: [`what-i-would-put-in-a-paper.md`](what-i-would-put-in-a-paper.md).

| Other repo | Role |
|:-----------|:-----|
| [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) | DESI residual analysis |
| [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes) | method notes only |

```bash
pytest -q
```

---

## Folders

| Folder | What is in it |
|:-------|:--------------|
| [`core/`](core/) | stable claims and formulae |
| [`r1_kernel/`](r1_kernel/) | residual scale, coupling, survey tests, CF4 kinematics |
| [`closed_walls/`](closed_walls/) | routes I closed |
| [`side_threads/`](side_threads/) | side work |
| [`work_packages/`](work_packages/) | longer WP notes |

---

## 1. Core

| File | Why it exists |
|:-----|:--------------|
| [`core/FOR_REFEREES.md`](core/FOR_REFEREES.md) | claim list and formula sheet |
| [`core/VERIFIED_RESULTS.md`](core/VERIFIED_RESULTS.md) | only what tests cover |
| [`core/SIMPLE_AS_LAMBDA.md`](core/SIMPLE_AS_LAMBDA.md) | minimal model |
| [`core/OBSERVABLE_WALL.md`](core/OBSERVABLE_WALL.md) | slip wall |
| [`core/PAST_LIGHT_CONE_INTEGRATION.md`](core/PAST_LIGHT_CONE_INTEGRATION.md) | path RMS |
| [`core/NARROW_PATH.md`](core/NARROW_PATH.md) | NP-A / NP-B windows |
| [`core/SELF_SHIELDING_AXIOMS.md`](core/SELF_SHIELDING_AXIOMS.md) | method rules I try to keep |
| [`../BOUNDARY.md`](../BOUNDARY.md) | repo fence |

---

## 2. Residual scale (read roughly in this order)

| | File | Content |
|:--|:-----|:--------|
| 1 | [`r1_kernel/NOTE_uniqueness_residual_grain.md`](r1_kernel/NOTE_uniqueness_residual_grain.md) | main draft |
| 2 | [`r1_kernel/r1-derivation-sandwich.md`](r1_kernel/r1-derivation-sandwich.md) | uniqueness + numbers |
| 3 | [`r1_kernel/r1-sandwich-falsifiers.md`](r1_kernel/r1-sandwich-falsifiers.md) | how it dies |
| 4 | [`r1_kernel/r1-T2-preregistration.md`](r1_kernel/r1-T2-preregistration.md) | residual × structure protocol |
| 5 | [`r1_kernel/r1-lineA-g-from-averaging.md`](r1_kernel/r1-lineA-g-from-averaging.md) | $g$ from averaging proxy |
| 6 | [`r1_kernel/r1-a1-microphysics.md`](r1_kernel/r1-a1-microphysics.md) | where $g\chi\delta_m$ could come from |
| 7 | [`r1_kernel/r1-principle-nonlinear-matter.md`](r1_kernel/r1-principle-nonlinear-matter.md) | full $\sigma(R)$ |
| 8 | [`r1_kernel/r1-open-kernel.md`](r1_kernel/r1-open-kernel.md) | walls vs open kernel |
| 9 | [`r1_kernel/r1-scale-decade-8-12.md`](r1_kernel/r1-scale-decade-8-12.md) | 8–12 Mpc decade |
| 10 | [`r1_kernel/r1-bounding-g-plan.md`](r1_kernel/r1-bounding-g-plan.md) | plan for $\lambda$, $g$ |
| 11 | [`r1_kernel/r1-t1-mechanisms-compute.md`](r1_kernel/r1-t1-mechanisms-compute.md) | domain / mask numbers |
| 12 | [`r1_kernel/r1-t12-bbks-and-derivation.md`](r1_kernel/r1-t12-bbks-and-derivation.md) | BBKS peaks |
| 13 | [`r1_kernel/r1-mechanism-candidates.md`](r1_kernel/r1-mechanism-candidates.md) | literature ranking |
| 14 | [`r1_kernel/r1-counting-principle.md`](r1_kernel/r1-counting-principle.md) | counting landscape |
| 15 | [`r1_kernel/FRONTIER_INQUIRY.md`](r1_kernel/FRONTIER_INQUIRY.md) | what I work on next |
| 16 | [`r1_kernel/HONEST_ASSETS.md`](r1_kernel/HONEST_ASSETS.md) | public data vs my analysis |

### 2b. Local matter kinematics (Cosmicflows-4 — not DE residual)

| | File | Content |
|:--|:-----|:--------|
| 17 | [`r1_kernel/r1-real-velocity-block-net.md`](r1_kernel/r1-real-velocity-block-net.md) | block net, $\eta(L)$, correlation scale |
| 18 | [`r1_kernel/r1-collapse-relief.md`](r1_kernel/r1-collapse-relief.md) | collapse peaks, velocity relief, gravity vs expansion |

| Number I keep quoting | Value |
|:----------------------|:------|
| $R_{\mathrm{nl}}$ | $\approx 8.61\,\mathrm{Mpc}$ |
| $r_{e,\mathrm{mask}}$ | $\approx 1.11\,R_{\mathrm{nl}}$ |
| $\sigma_{\mathrm{free}}$ ($d=3$) | $\approx 8.5\times 10^{-5}$ |
| working $\lvert\lambda\rvert$, $\lvert g\rvert$ | $\lesssim 1.24\times 10^{-4}$, $\lesssim 1.45$ |

```bash
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_lineA_Q_variance_proxy.py
python scripts/r1/r1_T2_real_pipeline.py
python scripts/r1/r1_real_velocity_block_net.py
python scripts/r1/r1_collapse_relief_cf4.py
```

---

## 3. Closed walls

| File | Topic |
|:-----|:------|
| sister amplification gap | soft $10^{56}$ |
| [`closed_walls/h0-bridge-toy-map.md`](closed_walls/h0-bridge-toy-map.md) | path RMS vs $H_0$ |
| [`closed_walls/h0-desqueezing-filter.md`](closed_walls/h0-desqueezing-filter.md) | invented $H_0(z)$ |
| [`closed_walls/h0-running-brachistochrone-bridge.md`](closed_walls/h0-running-brachistochrone-bridge.md) | literature bridge |
| [`closed_walls/ell-star-external-scales.md`](closed_walls/ell-star-external-scales.md) | Andromeda / Virgo |
| [`closed_walls/ell-star-r0-peculiar-scales.md`](closed_walls/ell-star-r0-peculiar-scales.md) | $r_0$ vs NP-A |

---

## 4. Side threads

| File | Role |
|:-----|:-----|
| [`side_threads/inflation-spectator-seed-gordon-wands.md`](side_threads/inflation-spectator-seed-gordon-wands.md) | inflation spectator |
| [`side_threads/inflation-spectator-residual-atlas.md`](side_threads/inflation-spectator-residual-atlas.md) | residual windows |
| [`side_threads/lensing-rms-forecast-real-data.md`](side_threads/lensing-rms-forecast-real-data.md) | path RMS vs Maus/Sakr |
| [`side_threads/minimal-theory-package.md`](side_threads/minimal-theory-package.md) | theory package note (not hard claims) |
| [`side_threads/CONSISTENCY_AUDIT.md`](side_threads/CONSISTENCY_AUDIT.md) | cross-repo check |

Pedagogy only (other repo): [TOPOLOGICAL_EDGE_ANALOGY](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes/blob/main/papers/TOPOLOGICAL_EDGE_ANALOGY.md)

---

## 5. Work packages

| File | Role |
|:-----|:-----|
| [`work_packages/wp4-joint-predictions-and-zeros.md`](work_packages/wp4-joint-predictions-and-zeros.md) | joint zeros |
| [`work_packages/wp5-falsification.md`](work_packages/wp5-falsification.md) | falsification levels |
| [`work_packages/r2-slip-from-same-sector.md`](work_packages/r2-slip-from-same-sector.md) | slip channel |
| [`work_packages/r3-open-horizon-map.md`](work_packages/r3-open-horizon-map.md) | soft open maps |

---

## 6. Scripts and results

| Path | Content |
|:-----|:--------|
| `scripts/core/` | kinematics library, light cone, slip path |
| `scripts/r1/` | $R_{\mathrm{nl}}$, uniqueness, $g$, residual profiles, T2 real, CF4 |
| `scripts/closed/` | closed-route checks |
| `scripts/side/` | secondary scripts |
| `results/r1_sandwich/`, `r1_lineA_Q/`, `r1_T2_real/`, `r1_real_velocity_net/`, `r1_collapse_relief/` | numerical outputs |
| `data/real_velocity_net/` | Cosmicflows-4 local copy (public CDS) |

---

## 7. Status (short)

| Topic | Status |
|:------|:-------|
| soft Sorkin amplification | closed under audited maps |
| $R_{\mathrm{nl}}$ | computed $\approx 8.61\,\mathrm{Mpc}$ |
| free residual scale under A0–A4 | $\ell_{\ast}\sim R_{\mathrm{nl}}$ |
| microphysics of $\chi$, $g$ | postulated; $g_{\mathrm{eff}}\sim\mathcal{O}(1)$ from proxy |
| residual × structure test | protocol + real DESI+CF4 written |
| residual as $H_0$ fix | excluded at DESI-safe amplitude |
| CF4 block net + collapse relief | real matter kinematics only (no DE residual) |

