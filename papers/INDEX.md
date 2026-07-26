# Document index — measurable-stochastic-vacuum

**Read this first if the folder feels crowded.**  
Author: Jesús Morales Souhail · July 2026 · **Not peer reviewed**

Sister empirical repo: [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)

---

## 1. Start here (5 minutes)

| Order | File | What you get |
|:------|:-----|:-------------|
| 1 | [`README.md`](../README.md) | One-page map + minimal model |
| 2 | [`FOR_REFEREES.md`](FOR_REFEREES.md) | Claims C* / non-claims N* + formula sheet |
| 3 | [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) | Only unit-tested identities |
| 4 | [`BOUNDARY.md`](../BOUNDARY.md) | What may / may not enter this repo |

```bash
pytest -q
```

---

## 2. Core theory (stable)

| File | Role |
|:-----|:-----|
| [`SIMPLE_AS_LAMBDA.md`](SIMPLE_AS_LAMBDA.md) | Minimal model as simple as \(\Lambda\) |
| [`OBSERVABLE_WALL.md`](OBSERVABLE_WALL.md) | Slip wall + self-shielding |
| [`PAST_LIGHT_CONE_INTEGRATION.md`](PAST_LIGHT_CONE_INTEGRATION.md) | Path \(\mathrm{RMS}=s\sqrt{N}\) |
| [`NARROW_PATH.md`](NARROW_PATH.md) | NP-A / NP-B architecture |
| [`SELF_SHIELDING_AXIOMS.md`](SELF_SHIELDING_AXIOMS.md) | Method axioms |
| [`wp4-joint-predictions-and-zeros.md`](wp4-joint-predictions-and-zeros.md) | Joint zeros table |
| [`wp5-falsification.md`](wp5-falsification.md) | Falsifiers |

---

## 3. Open R1 kernel (active research thread)

**Question:** what fixes mesoscopic \(\ell_*\)? Lead: **8–12 Mpc decade**, not NP-A 2.06 confirmation.

```
r1-open-kernel.md              ← walls vs open kernel
r1-scale-decade-8-12.md        ← steering: r0, R8, DESI-ceil cell
r1-principle-nonlinear-matter.md ← hypothesis ℓ_*=R_nl + full σ(R)
r1-t1-mechanisms-compute.md    ← T1.1/T1.2 geometry numbers
r1-t12-bbks-and-derivation.md  ← BBKS R_* + coarse-graining sketch
r1-mechanism-candidates.md     ← Tier 1–3 literature ranking
r1-bounding-g-plan.md          ← how to bound coupling λ, g
r1-counting-principle.md       ← original WP1 landscape
```

**Key numbers (locked):**

| Symbol | Value |
|:-------|:------|
| \(R_{\mathrm{nl}}\) | \(\approx 8.61\,\mathrm{Mpc}\) |
| \(R_*\) (BBKS) | \(\approx 1.58\,\mathrm{Mpc}\) |
| \(\sigma_{\mathrm{free}}\) (\(d=3\)) | \(\approx 8.5\times 10^{-5}\) |
| Working \(\lvert\lambda\rvert\) | \(\lesssim 1.2\times 10^{-4}\) (from \(\sigma_X<1.5\times 10^{-4}\)) |

**Scripts:** `r1_sigma_R_full.py`, `r1_t1_mechanisms_compute.py`, `r1_t12_bbks_peaks.py`, `r1_bound_g_oom.py`, `r1_profile_lambda_bao.py`

---

## 4. Closed walls & filters (do not re-open)

| File | Closed claim |
|:-----|:-------------|
| Sister `amplification-gap.md` | Soft \(10^{56}\) free lunch |
| [`h0-bridge-toy-map.md`](h0-bridge-toy-map.md) | Path RMS explains 9% \(H_0\) |
| [`h0-desqueezing-filter.md`](h0-desqueezing-filter.md) | Invented \(H_0(z)\) + hand-tuned \(\theta\) |
| [`ell-star-external-scales.md`](ell-star-external-scales.md) | Andromeda/Virgo confirm NP-A |
| [`ell-star-r0-peculiar-scales.md`](ell-star-r0-peculiar-scales.md) | \(r_0\equiv 2.06\,\mathrm{Mpc}\) |

---

## 5. Side threads (useful, secondary)

| File | Role |
|:-----|:-----|
| [`inflation-spectator-seed-gordon-wands.md`](inflation-spectator-seed-gordon-wands.md) | Inflation seed, factor \(\sim 45\) |
| [`inflation-spectator-residual-atlas.md`](inflation-spectator-residual-atlas.md) | Modern \(r\to\sigma_\rho\) |
| [`lensing-rms-forecast-real-data.md`](lensing-rms-forecast-real-data.md) | Path RMS vs Maus/Sakr |
| [`h0-running-brachistochrone-bridge.md`](h0-running-brachistochrone-bridge.md) | H0-running literature bridge |
| [`TOPOLOGICAL_EDGE_ANALOGY.md`](TOPOLOGICAL_EDGE_ANALOGY.md) | Pedagogy only |
| [`THEORY_REVOLUTION.md`](THEORY_REVOLUTION.md) | R1–R2–R3 manifesto |
| [`CONSISTENCY_AUDIT.md`](CONSISTENCY_AUDIT.md) | Cross-repo audit |
| `r2-*.md`, `r3-*.md` | WP2/WP3 expansions |

---

## 6. Scripts map

| Group | Scripts |
|:------|:--------|
| **Core** | `lib_verified.py`, `simple_as_lambda.py`, `light_cone_atlas.py` |
| **R1 / grain** | `r1_counting_landscape.py`, `r1_open_kernel_scales.py`, `r1_sigma_R_full.py`, `r1_principle_Rnl.py`, `ell_star_*.py` |
| **T1 mechanisms** | `r1_t1_mechanisms_compute.py`, `r1_t12_bbks_peaks.py` |
| **Bound \(g\)** | `r1_bound_g_oom.py`, `r1_profile_lambda_bao.py` |
| **H0 filters** | `h0_bridge_toy.py`, `h0_desqueezing_filter.py`, `h0_running_geometry.py` |
| **Other** | `lensing_rms_real_data_compare.py`, `gordon_wands_factor45.py`, `inflation_spectator_residual_atlas.py` |

---

## 7. Results artefacts

| Path | Content |
|:-----|:--------|
| `results/r1_landscape.txt` | Counting landscape |
| `results/r1_lambda_profile/` | \(\lambda\) profile on DESI BAO diagonal |
| `results/r2_*.txt`, `r3_*.txt` | WP scans |

---

## 8. One-page status

| Layer | Status |
|:------|:-------|
| Soft amplifiers of Sorkin | **Walls (closed)** |
| \(R_{\mathrm{nl}}\) length | **Computed** (\(\approx 8.61\,\mathrm{Mpc}\)) |
| Why vacuum grain \(=R_{\mathrm{nl}}\) | **Hypothesis + coarse-graining sketch** |
| Bound on \(\lambda,g\) | **Stage-0 OOM + BAO profile script** (formal diag profile weak; working ceiling strong) |
| \(H_0\) 9% from residual | **Excluded** at DESI-safe amplitude |

---

*End of index.*
