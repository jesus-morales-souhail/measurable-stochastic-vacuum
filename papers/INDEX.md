# Document index — measurable-stochastic-vacuum

**Lost?** Read [`../START_HERE.md`](../START_HERE.md) first (one page).  
**Author:** Jesús Morales Souhail · July 2026 · **Not peer reviewed**

Sister data repo: [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)  
Exploratory quarantine: [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes)

---

## How papers are organised

| Folder | Meaning | When to open |
|:-------|:--------|:-------------|
| [`core/`](core/) | Stable claims, formulas, referee path | Publishing / review |
| [`r1_kernel/`](r1_kernel/) | **Active lead:** grain scale uniqueness | Current research |
| [`closed_walls/`](closed_walls/) | Dead ends already measured | Only if tempted to re-open |
| [`side_threads/`](side_threads/) | Useful secondary (inflation, lensing) | After core + r1 |
| [`work_packages/`](work_packages/) | WP expansions (slip, horizon, falsification) | Deep dive |

```bash
pytest -q
```

---

## 1. Core (stable)

| File | Role |
|:-----|:-----|
| [`core/FOR_REFEREES.md`](core/FOR_REFEREES.md) | Claims C* / non-claims N* + formula sheet |
| [`core/VERIFIED_RESULTS.md`](core/VERIFIED_RESULTS.md) | Unit-tested identities only |
| [`core/SIMPLE_AS_LAMBDA.md`](core/SIMPLE_AS_LAMBDA.md) | Minimal model as simple as \(\Lambda\) |
| [`core/OBSERVABLE_WALL.md`](core/OBSERVABLE_WALL.md) | Slip wall + self-shielding |
| [`core/PAST_LIGHT_CONE_INTEGRATION.md`](core/PAST_LIGHT_CONE_INTEGRATION.md) | Path \(\mathrm{RMS}=s\sqrt{N}\) |
| [`core/NARROW_PATH.md`](core/NARROW_PATH.md) | NP-A / NP-B windows |
| [`core/SELF_SHIELDING_AXIOMS.md`](core/SELF_SHIELDING_AXIOMS.md) | Method axioms |
| [`../BOUNDARY.md`](../BOUNDARY.md) | What may / may not enter claims |

---

## 2. R1 kernel (active lead) — read in this order

| Order | File | What you get |
|:------|:-----|:-------------|
| 0 | [`r1_kernel/FRONTIER_INQUIRY.md`](r1_kernel/FRONTIER_INQUIRY.md) | **Frontier reframe** (H0 closed → Lines A/B/C) |
| 0a | [`r1_kernel/r1-lineA-g-from-averaging.md`](r1_kernel/r1-lineA-g-from-averaging.md) | **Line A:** \(g_{\mathrm{eff}}\sim\mathcal{O}(1)\) from \(Q\) proxy |
| 0b | [`r1_kernel/r1-T2-preregistration.md`](r1_kernel/r1-T2-preregistration.md) | **Line B:** T2 pre-reg + **mock PASS** |
| 0c | [`r1_kernel/HONEST_ASSETS.md`](r1_kernel/HONEST_ASSETS.md) | What we own vs public data |
| 1 | [`r1_kernel/NOTE_uniqueness_residual_grain.md`](r1_kernel/NOTE_uniqueness_residual_grain.md) | **Short paper draft** (start here for the lead) |
| 2 | [`r1_kernel/r1-derivation-sandwich.md`](r1_kernel/r1-derivation-sandwich.md) | Uniqueness theorem under A0–A4 + numbers |
| 3 | [`r1_kernel/r1-sandwich-falsifiers.md`](r1_kernel/r1-sandwich-falsifiers.md) | F1–F4 operational gates |
| 4 | [`r1_kernel/r1-a1-microphysics.md`](r1_kernel/r1-a1-microphysics.md) | Where \(g\chi\delta_m\) can come from |
| 5 | [`r1_kernel/r1-principle-nonlinear-matter.md`](r1_kernel/r1-principle-nonlinear-matter.md) | \(R_{\mathrm{nl}}\) full integral |
| 6 | [`r1_kernel/r1-open-kernel.md`](r1_kernel/r1-open-kernel.md) | Walls vs open kernel taxonomy |
| 7 | [`r1_kernel/r1-scale-decade-8-12.md`](r1_kernel/r1-scale-decade-8-12.md) | Steering: 8–12 Mpc decade |
| 8 | [`r1_kernel/r1-bounding-g-plan.md`](r1_kernel/r1-bounding-g-plan.md) | Bound \(\lambda,g\) |
| 9 | [`r1_kernel/r1-t1-mechanisms-compute.md`](r1_kernel/r1-t1-mechanisms-compute.md) | Domain + mask numbers |
| 10 | [`r1_kernel/r1-t12-bbks-and-derivation.md`](r1_kernel/r1-t12-bbks-and-derivation.md) | BBKS \(R_*\) + coarse-graining sketch |
| 11 | [`r1_kernel/r1-mechanism-candidates.md`](r1_kernel/r1-mechanism-candidates.md) | Tier 1–3 literature ranking |
| 12 | [`r1_kernel/r1-counting-principle.md`](r1_kernel/r1-counting-principle.md) | Original counting landscape |

**Locked numbers**

| Symbol | Value |
|:-------|:------|
| \(R_{\mathrm{nl}}\) | \(\approx 8.61\,\mathrm{Mpc}\) |
| \(r_{e,\mathrm{mask}}\) | \(\approx 1.11\,R_{\mathrm{nl}}\) |
| \(\sigma_{\mathrm{free}}\) (\(d=3\)) | \(\approx 8.5\times 10^{-5}\) |
| Working \(\lvert\lambda\rvert\) / \(\lvert g\rvert\) | \(\lesssim 1.24\times 10^{-4}\) / \(\lesssim 1.45\) |

```bash
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_sandwich_falsifiers.py
python scripts/r1/r1_bound_g_oom.py
```

---

## 3. Closed walls (do not re-open)

| File | Closed claim |
|:-----|:-------------|
| Sister `amplification-gap.md` | Soft \(10^{56}\) free lunch |
| [`closed_walls/h0-bridge-toy-map.md`](closed_walls/h0-bridge-toy-map.md) | Path RMS explains 9% \(H_0\) |
| [`closed_walls/h0-desqueezing-filter.md`](closed_walls/h0-desqueezing-filter.md) | Invented \(H_0(z)\) + hand-tuned \(\theta\) |
| [`closed_walls/h0-running-brachistochrone-bridge.md`](closed_walls/h0-running-brachistochrone-bridge.md) | Literature bridge only |
| [`closed_walls/ell-star-external-scales.md`](closed_walls/ell-star-external-scales.md) | Andromeda/Virgo confirm NP-A |
| [`closed_walls/ell-star-r0-peculiar-scales.md`](closed_walls/ell-star-r0-peculiar-scales.md) | \(r_0\equiv 2.06\,\mathrm{Mpc}\) |

---

## 4. Side threads (secondary)

| File | Role |
|:-----|:-----|
| [`side_threads/inflation-spectator-seed-gordon-wands.md`](side_threads/inflation-spectator-seed-gordon-wands.md) | Inflation seed, factor \(\sim 45\) |
| [`side_threads/inflation-spectator-residual-atlas.md`](side_threads/inflation-spectator-residual-atlas.md) | Modern \(r\to\sigma_\rho\) |
| [`side_threads/lensing-rms-forecast-real-data.md`](side_threads/lensing-rms-forecast-real-data.md) | Path RMS vs Maus/Sakr |
| [`side_threads/TOPOLOGICAL_EDGE_ANALOGY.md`](side_threads/TOPOLOGICAL_EDGE_ANALOGY.md) | Pedagogy only |
| [`side_threads/THEORY_REVOLUTION.md`](side_threads/THEORY_REVOLUTION.md) | Manifesto (not hard claims) |
| [`side_threads/CONSISTENCY_AUDIT.md`](side_threads/CONSISTENCY_AUDIT.md) | Cross-repo audit |

---

## 5. Work packages (deep dive)

| File | Role |
|:-----|:-----|
| [`work_packages/wp4-joint-predictions-and-zeros.md`](work_packages/wp4-joint-predictions-and-zeros.md) | Joint zeros |
| [`work_packages/wp5-falsification.md`](work_packages/wp5-falsification.md) | Falsification levels L0–L4 |
| [`work_packages/r2-slip-from-same-sector.md`](work_packages/r2-slip-from-same-sector.md) | Slip channel |
| [`work_packages/r3-open-horizon-map.md`](work_packages/r3-open-horizon-map.md) | Soft open map |

---

## 6. Scripts map

| Folder | Content |
|:-------|:--------|
| `scripts/core/` | `lib_verified.py`, light-cone, slip path, simple model |
| `scripts/r1/` | \(R_{\mathrm{nl}}\), sandwich, \(\lambda\) profile, mechanisms |
| `scripts/closed/` | H0 filters, external-scale audits |
| `scripts/side/` | Inflation atlas, lensing compare, R3 map |

---

## 7. Results artefacts

| Path | Content |
|:-----|:--------|
| `results/r1_sandwich/` | Uniqueness numbers |
| `results/r1_falsifiers/` | F1–F4 table |
| `results/r1_lambda_profile/` | Diagonal BAO \(\lambda\) profile |
| `results/r1_lambda_fullcov/` | Full 13×13 (formal weak; primary=working) |
| `results/r1_landscape.txt` | Counting landscape |
| `results/r2_*.txt`, `r3_*.txt` | WP scans |

---

## 8. One-page status

| Layer | Status |
|:------|:-------|
| Soft amplifiers of Sorkin | **Walls (closed)** |
| \(R_{\mathrm{nl}}\) length | **Computed** (\(\approx 8.61\,\mathrm{Mpc}\)) |
| Why vacuum grain \(=R_{\mathrm{nl}}\) | **Sandwich uniqueness under A0–A4**; A0–A1 postulates |
| A0–A1 microphysics | **Mapped** (M1–M3 preferred) |
| Falsifiers | **F1–F4 pre-registered** |
| Bound on \(\lambda,g\) | **Working** \(\lvert\lambda\rvert\lesssim 1.24\times 10^{-4}\), \(\lvert g\rvert\lesssim 1.45\) |
| Slip at working \(\lambda\) | \(\lvert\gamma-1\rvert\sim 10^{-4}\ll\) Maus; \(\mathrm{RMS}_{\mathrm{path}}\sim 2.5\times 10^{-3}\) |
| \(H_0\) 9% from residual | **Excluded** |

---

*End of index.*
