# Guide to this repository

Jesús Morales Souhail  
July 2026 · Independent research · Not peer reviewed

This repository is the theory side of a programme on whether a late-time residual in the dark-energy sector can be large enough to matter for surveys, without free amplification factors of order \(10^{56}\) from a Planck-scale seed.

A companion analysis of public DESI DR2 BAO data bounds a residual amplitude \(\sigma_X < 1.5\times 10^{-4}\) (95% CL). The working hypothesis developed here is that, under stated axioms, the residual counting scale is the matter nonlinear scale \(R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\).

---

## Related repositories

| Repository | Role |
|:-----------|:-----|
| [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) | Empirical DESI BAO residual analysis |
| This repository | Theory, kinematics, and open questions |
| [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes) | Exploratory and pedagogical material only |

---

## Directory layout

```
START_HERE.md
README.md
BOUNDARY.md
papers/
  INDEX.md           full catalogue
  core/              stable claims and formulae
  r1_kernel/         residual scale and coupling
  closed_walls/      excluded mechanisms
  side_threads/      secondary topics
  work_packages/     longer work-package notes
scripts/core|r1|closed|side
tests/
results/
data/
```

---

## Suggested reading

**For claims and notation (about 30 minutes)**  
1. [`papers/core/FOR_REFEREES.md`](papers/core/FOR_REFEREES.md)  
2. [`papers/core/VERIFIED_RESULTS.md`](papers/core/VERIFIED_RESULTS.md)  
3. [`papers/core/SIMPLE_AS_LAMBDA.md`](papers/core/SIMPLE_AS_LAMBDA.md)  
4. [`BOUNDARY.md`](BOUNDARY.md)

**For the residual-scale argument (about 45 minutes)**  
1. [`papers/r1_kernel/NOTE_uniqueness_residual_grain.md`](papers/r1_kernel/NOTE_uniqueness_residual_grain.md)  
2. [`papers/r1_kernel/r1-derivation-sandwich.md`](papers/r1_kernel/r1-derivation-sandwich.md)  
3. [`papers/r1_kernel/r1-sandwich-falsifiers.md`](papers/r1_kernel/r1-sandwich-falsifiers.md)  
4. [`papers/r1_kernel/r1-T2-preregistration.md`](papers/r1_kernel/r1-T2-preregistration.md)  
5. [`papers/r1_kernel/r1-lineA-g-from-averaging.md`](papers/r1_kernel/r1-lineA-g-from-averaging.md)

**For excluded routes**  
Sister repository `amplification-gap.md`, and notes under [`papers/closed_walls/`](papers/closed_walls/).

A broader research agenda (coupling estimates, survey tests, open problems) is summarised in [`papers/r1_kernel/FRONTIER_INQUIRY.md`](papers/r1_kernel/FRONTIER_INQUIRY.md). Scope of public data versus original analysis is stated in [`papers/r1_kernel/HONEST_ASSETS.md`](papers/r1_kernel/HONEST_ASSETS.md).

---

## Present status (summary)

| Topic | Status |
|:------|:-------|
| Soft amplification \(\sim 10^{56}\) of a Sorkin seed | Excluded under audited soft maps |
| \(R_{\mathrm{nl}}\) | \(\approx 8.61\,\mathrm{Mpc}\) from \(\sigma(R)=1\) |
| Residual scale under axioms A0–A4 | \(\ell_*\sim R_{\mathrm{nl}}\) |
| Existence of the residual sector | Postulated, not derived from the Standard Model |
| Coupling \(g\) (working bound) | \(\lvert g\rvert\lesssim 1.45\) from DESI residual ceiling |
| Residual as explanation of the \(\sim 8\%\) \(H_0\) tension | Excluded at DESI-safe amplitude |

---

## Reproduce core numbers

```bash
pytest -q
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_lineA_Q_variance_proxy.py
python scripts/r1/r1_T2_mock_pipeline.py
```

Full catalogue: [`papers/INDEX.md`](papers/INDEX.md).
