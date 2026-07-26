# Start here

Jesús Morales Souhail · July 2026  
[github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail) · not peer reviewed

This folder is dense. You do not need to open everything.

I split the programme into three repos so claims do not get mixed:

| Repo | What I use it for |
|:-----|:------------------|
| [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) | DESI BAO residual numbers |
| **this one** | theory and kinematics |
| [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes) | analogies and wrong-scale experiments (not cosmology claims) |

The scientific question: can vacuum / dark-energy noise sit near $10^{-5}$–$10^{-4}$ without a free $10^{56}$ boost from Planck?  
On the data side I already have $\sigma_X < 1.5\times 10^{-4}$ (95% CL).  
On the theory side the working picture is $\ell_{\ast}\sim R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ under a few axioms I write down explicitly.

---

## How the folders are arranged

```
START_HERE.md      ← you are here
README.md
BOUNDARY.md         what I refuse to claim
papers/
  INDEX.md
  core/             stable notes
  r1_kernel/        residual scale work
  closed_walls/     dead ends (kept on purpose)
  side_threads/
  work_packages/
scripts/...
tests/  results/  data/
```

Nothing important was deleted when I reorganised; files only moved.

---

## Three short reading paths

**A — what can I actually claim? (~30 min)**  
1. [`papers/core/FOR_REFEREES.md`](papers/core/FOR_REFEREES.md)  
2. [`papers/core/VERIFIED_RESULTS.md`](papers/core/VERIFIED_RESULTS.md)  
3. [`papers/core/SIMPLE_AS_LAMBDA.md`](papers/core/SIMPLE_AS_LAMBDA.md)  
4. [`BOUNDARY.md`](BOUNDARY.md)

**B — residual scale argument (~45 min)**  
1. [`papers/r1_kernel/NOTE_uniqueness_residual_grain.md`](papers/r1_kernel/NOTE_uniqueness_residual_grain.md)  
2. [`papers/r1_kernel/r1-derivation-sandwich.md`](papers/r1_kernel/r1-derivation-sandwich.md)  
3. [`papers/r1_kernel/r1-sandwich-falsifiers.md`](papers/r1_kernel/r1-sandwich-falsifiers.md)  
4. [`papers/r1_kernel/r1-T2-preregistration.md`](papers/r1_kernel/r1-T2-preregistration.md)  
5. [`papers/r1_kernel/r1-lineA-g-from-averaging.md`](papers/r1_kernel/r1-lineA-g-from-averaging.md)

**C — things I already closed**  
Sister `amplification-gap.md`, plus everything under [`papers/closed_walls/`](papers/closed_walls/).

Open research lines (coupling, survey tests, and what I am not doing about $H_0$): [`papers/r1_kernel/FRONTIER_INQUIRY.md`](papers/r1_kernel/FRONTIER_INQUIRY.md).  
What is public data versus my own analysis: [`papers/r1_kernel/HONEST_ASSETS.md`](papers/r1_kernel/HONEST_ASSETS.md).

---

## Status in plain language

| Topic | Where it stands |
|:------|:----------------|
| Soft $10^{56}$ from Sorkin seed | closed under the maps I checked |
| $R_{\mathrm{nl}}$ | $\approx 8.61\,\mathrm{Mpc}$ |
| Free residual cell under axioms A0–A4 | $\ell_{\ast}\sim R_{\mathrm{nl}}$ |
| Does nature have $\chi$? | I postulate it; I do not derive it from the SM |
| Coupling $g$ | working bound $\lvert g\rvert\lesssim 1.45$ from DESI residual |
| Residual explains $\sim 8\%$ $H_0$? | no — amplitude is short by a lot |

---

## Commands I actually run

```bash
pytest -q
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_lineA_Q_variance_proxy.py
python scripts/r1/r1_T2_mock_pipeline.py
```

Full catalogue: [`papers/INDEX.md`](papers/INDEX.md).
