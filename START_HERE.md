# START HERE — measurable-stochastic-vacuum

**Author:** Jesús Morales Souhail · July 2026 · **Not peer reviewed**

If the folder feels huge: **read this page only**, then pick one path below.

---

## The whole programme in one paragraph

We ask whether dark energy / vacuum can have a small **stochastic residual** that telescopes could see — **without** inventing free factors of \(10^{56}\) to amplify Planck-scale noise.  
Sister data (DESI BAO) already bound that residual to \(\sigma_X < 1.5\times 10^{-4}\).  
This repo develops the **theory map**: what is closed, what is open, and the current lead  
\(\ell_* \sim R_{\mathrm{nl}} \approx 8.61\,\mathrm{Mpc}\) under stated axioms.

---

## Three repositories (do not mix roles)

| Repo | Role | Start file |
|:-----|:-----|:-----------|
| **[stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)** | **Data / DESI claims** | `manuscript/PREPRINT.md` |
| **This repo** | **Theory / when measurable** | this file → `papers/INDEX.md` |
| **[stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes)** | **Pedagogy / wrong-scale quarantine** | `README.md` |

---

## Folder map (this repo)

```
START_HERE.md          ← you are here
README.md              ← short overview
BOUNDARY.md            ← what may not enter claims
papers/
  INDEX.md             ← full document index
  core/                ← stable claims (referee path)
  r1_kernel/           ← active research: grain scale uniqueness
  closed_walls/        ← closed dead ends (do not re-open)
  side_threads/        ← useful but secondary
  work_packages/       ← WP2–WP5 expansions
scripts/
  core/  r1/  closed/  side/   ← same logic as papers
tests/                 ← pytest gate (must stay green)
results/               ← numerical artefacts
data/                  ← portable DESI npy copies
```

**Nothing was deleted.** Files only moved into topic folders.

---

## Read in this order (choose one)

### Path A — “What can we claim?” (30 min)

1. [`papers/core/FOR_REFEREES.md`](papers/core/FOR_REFEREES.md)  
2. [`papers/core/VERIFIED_RESULTS.md`](papers/core/VERIFIED_RESULTS.md)  
3. [`papers/core/SIMPLE_AS_LAMBDA.md`](papers/core/SIMPLE_AS_LAMBDA.md)  
4. [`BOUNDARY.md`](BOUNDARY.md)  

### Path B — “What is the current scientific lead?” (45 min)

1. [`papers/r1_kernel/NOTE_uniqueness_residual_grain.md`](papers/r1_kernel/NOTE_uniqueness_residual_grain.md) ← short paper draft  
2. [`papers/r1_kernel/r1-derivation-sandwich.md`](papers/r1_kernel/r1-derivation-sandwich.md)  
3. [`papers/r1_kernel/r1-sandwich-falsifiers.md`](papers/r1_kernel/r1-sandwich-falsifiers.md)  
4. [`papers/r1_kernel/r1-a1-microphysics.md`](papers/r1_kernel/r1-a1-microphysics.md)  

### Path C — “What did we already kill?” (15 min)

1. Sister `amplification-gap.md`  
2. [`papers/closed_walls/`](papers/closed_walls/) — H0 from residual, Andromeda/NP-A false friends  

---

## One-line status

| Layer | Status |
|:------|:-------|
| Soft \(10^{56}\) amplifiers | **Closed** |
| \(R_{\mathrm{nl}}\) | **Computed** \(\approx 8.61\,\mathrm{Mpc}\) |
| Why grain \(=R_{\mathrm{nl}}\) | **Unique under axioms A0–A4** |
| Existence of residual sector | **Still a postulate** |
| Bound on coupling \(g\) | **Working** \(\lvert g\rvert\lesssim 1.45\) |
| \(H_0\) 9% from residual | **Excluded** |

---

## Commands

```bash
pytest -q
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_sandwich_falsifiers.py
```

Full index: [`papers/INDEX.md`](papers/INDEX.md)
