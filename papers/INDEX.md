# Document index

Jesús Morales Souhail · July 2026 · Not peer reviewed

Begin with [`../START_HERE.md`](../START_HERE.md) if this is a first visit.

| Related repository | Role |
|:-------------------|:-----|
| [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) | DESI BAO residual analysis |
| [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes) | Exploratory material only |

```bash
pytest -q
```

---

## Organisation

| Directory | Contents |
|:----------|:---------|
| [`core/`](core/) | Stable claims, formulae, referee path |
| [`r1_kernel/`](r1_kernel/) | Residual scale, coupling, survey tests |
| [`closed_walls/`](closed_walls/) | Mechanisms already excluded |
| [`side_threads/`](side_threads/) | Secondary topics |
| [`work_packages/`](work_packages/) | Longer work-package notes |

---

## 1. Core

| File | Role |
|:-----|:-----|
| [`core/FOR_REFEREES.md`](core/FOR_REFEREES.md) | Claims, non-claims, formula sheet |
| [`core/VERIFIED_RESULTS.md`](core/VERIFIED_RESULTS.md) | Unit-tested identities |
| [`core/SIMPLE_AS_LAMBDA.md`](core/SIMPLE_AS_LAMBDA.md) | Minimal model |
| [`core/OBSERVABLE_WALL.md`](core/OBSERVABLE_WALL.md) | Slip wall |
| [`core/PAST_LIGHT_CONE_INTEGRATION.md`](core/PAST_LIGHT_CONE_INTEGRATION.md) | Path accumulation |
| [`core/NARROW_PATH.md`](core/NARROW_PATH.md) | DESI-safe windows NP-A / NP-B |
| [`core/SELF_SHIELDING_AXIOMS.md`](core/SELF_SHIELDING_AXIOMS.md) | Method axioms |
| [`../BOUNDARY.md`](../BOUNDARY.md) | Claim fence |

---

## 2. Residual scale and coupling

Suggested order:

| | File | Content |
|:--|:-----|:--------|
| 1 | [`r1_kernel/NOTE_uniqueness_residual_grain.md`](r1_kernel/NOTE_uniqueness_residual_grain.md) | Main draft note |
| 2 | [`r1_kernel/r1-derivation-sandwich.md`](r1_kernel/r1-derivation-sandwich.md) | Uniqueness argument and numbers |
| 3 | [`r1_kernel/r1-sandwich-falsifiers.md`](r1_kernel/r1-sandwich-falsifiers.md) | Falsification gates |
| 4 | [`r1_kernel/r1-T2-preregistration.md`](r1_kernel/r1-T2-preregistration.md) | Residual–matter cross-correlation protocol |
| 5 | [`r1_kernel/r1-lineA-g-from-averaging.md`](r1_kernel/r1-lineA-g-from-averaging.md) | Effective coupling from averaging proxy |
| 6 | [`r1_kernel/r1-a1-microphysics.md`](r1_kernel/r1-a1-microphysics.md) | Origins of \(g\chi\delta_m\) |
| 7 | [`r1_kernel/r1-principle-nonlinear-matter.md`](r1_kernel/r1-principle-nonlinear-matter.md) | Full \(\sigma(R)\) integral |
| 8 | [`r1_kernel/r1-open-kernel.md`](r1_kernel/r1-open-kernel.md) | Walls versus open kernel |
| 9 | [`r1_kernel/r1-scale-decade-8-12.md`](r1_kernel/r1-scale-decade-8-12.md) | 8–12 Mpc decade |
| 10 | [`r1_kernel/r1-bounding-g-plan.md`](r1_kernel/r1-bounding-g-plan.md) | Plan to bound \(\lambda\), \(g\) |
| 11 | [`r1_kernel/r1-t1-mechanisms-compute.md`](r1_kernel/r1-t1-mechanisms-compute.md) | Domain and mask numbers |
| 12 | [`r1_kernel/r1-t12-bbks-and-derivation.md`](r1_kernel/r1-t12-bbks-and-derivation.md) | BBKS peaks |
| 13 | [`r1_kernel/r1-mechanism-candidates.md`](r1_kernel/r1-mechanism-candidates.md) | Mechanism ranking |
| 14 | [`r1_kernel/r1-counting-principle.md`](r1_kernel/r1-counting-principle.md) | Counting landscape |
| 15 | [`r1_kernel/FRONTIER_INQUIRY.md`](r1_kernel/FRONTIER_INQUIRY.md) | Open research lines |
| 16 | [`r1_kernel/HONEST_ASSETS.md`](r1_kernel/HONEST_ASSETS.md) | Public data versus original analysis |

| Quantity | Value |
|:---------|:------|
| \(R_{\mathrm{nl}}\) | \(\approx 8.61\,\mathrm{Mpc}\) |
| \(r_{e,\mathrm{mask}}\) | \(\approx 1.11\,R_{\mathrm{nl}}\) |
| \(\sigma_{\mathrm{free}}\) (\(d=3\)) | \(\approx 8.5\times 10^{-5}\) |
| Working \(\lvert\lambda\rvert\), \(\lvert g\rvert\) | \(\lesssim 1.24\times 10^{-4}\), \(\lesssim 1.45\) |

```bash
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_lineA_Q_variance_proxy.py
python scripts/r1/r1_T2_mock_pipeline.py
```

---

## 3. Closed walls

| File | Topic |
|:-----|:------|
| Sister `amplification-gap.md` | Soft \(10^{56}\) amplification |
| [`closed_walls/h0-bridge-toy-map.md`](closed_walls/h0-bridge-toy-map.md) | Path RMS and the Hubble tension |
| [`closed_walls/h0-desqueezing-filter.md`](closed_walls/h0-desqueezing-filter.md) | Ad hoc \(H_0(z)\) constructions |
| [`closed_walls/h0-running-brachistochrone-bridge.md`](closed_walls/h0-running-brachistochrone-bridge.md) | Literature bridge only |
| [`closed_walls/ell-star-external-scales.md`](closed_walls/ell-star-external-scales.md) | External galaxy scales |
| [`closed_walls/ell-star-r0-peculiar-scales.md`](closed_walls/ell-star-r0-peculiar-scales.md) | Clustering length \(r_0\) |

---

## 4. Side threads

| File | Role |
|:-----|:-----|
| [`side_threads/inflation-spectator-seed-gordon-wands.md`](side_threads/inflation-spectator-seed-gordon-wands.md) | Inflationary spectator seed |
| [`side_threads/inflation-spectator-residual-atlas.md`](side_threads/inflation-spectator-residual-atlas.md) | Residual windows from spectators |
| [`side_threads/lensing-rms-forecast-real-data.md`](side_threads/lensing-rms-forecast-real-data.md) | Path RMS versus published slip floors |
| [`side_threads/TOPOLOGICAL_EDGE_ANALOGY.md`](side_threads/TOPOLOGICAL_EDGE_ANALOGY.md) | Pedagogy |
| [`side_threads/THEORY_REVOLUTION.md`](side_threads/THEORY_REVOLUTION.md) | Programme manifesto (not hard claims) |
| [`side_threads/CONSISTENCY_AUDIT.md`](side_threads/CONSISTENCY_AUDIT.md) | Cross-repository audit |

---

## 5. Work packages

| File | Role |
|:-----|:-----|
| [`work_packages/wp4-joint-predictions-and-zeros.md`](work_packages/wp4-joint-predictions-and-zeros.md) | Joint zeros |
| [`work_packages/wp5-falsification.md`](work_packages/wp5-falsification.md) | Falsification levels |
| [`work_packages/r2-slip-from-same-sector.md`](work_packages/r2-slip-from-same-sector.md) | Slip channel |
| [`work_packages/r3-open-horizon-map.md`](work_packages/r3-open-horizon-map.md) | Soft open maps |

---

## 6. Scripts and results

| Directory | Content |
|:----------|:--------|
| `scripts/core/` | Verified kinematics, light cone, slip path |
| `scripts/r1/` | \(R_{\mathrm{nl}}\), uniqueness numbers, coupling, residual profiles, T2 mock |
| `scripts/closed/` | Excluded routes |
| `scripts/side/` | Secondary calculations |
| `results/r1_sandwich/` | Uniqueness numerics |
| `results/r1_lineA_Q/` | Coupling proxy |
| `results/r1_T2_mock/` | T2 mock validation |
| `results/r1_falsifiers/` | Working-point predictions |
| `results/r1_lambda_profile/`, `r1_lambda_fullcov/` | BAO residual profiles |

---

## 7. Status summary

| Topic | Status |
|:------|:-------|
| Soft amplification of a Sorkin seed | Excluded under audited soft maps |
| \(R_{\mathrm{nl}}\) | Computed, \(\approx 8.61\,\mathrm{Mpc}\) |
| Free residual scale under A0–A4 | \(\ell_*\sim R_{\mathrm{nl}}\) |
| Microphysics of \(\chi\) and \(g\) | Postulated; \(g_{\mathrm{eff}}\sim\mathcal{O}(1)\) from averaging proxy |
| Survey test of residual–structure correlation | Protocol and mock validation written |
| Residual as solution of the \(\sim 8\%\) \(H_0\) tension | Excluded at DESI-safe amplitude |
