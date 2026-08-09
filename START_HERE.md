# Start here

Jesús Morales Souhail · July 2026
[github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)

This folder is large; start with the table below.

I split the programme into three repos so claims do not get mixed:

| Repo | What I use it for |
|:-----|:------------------|
| [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) | DESI BAO residual numbers |
| **this one** | theory and kinematics |
| [stochastic-de-exploratory-notes](https://github.com/jesus-morales-souhail/stochastic-de-exploratory-notes) | analogies and scale checks (not cosmology claims) |

The scientific question: can vacuum / dark-energy noise sit near $10^{-5}$–$10^{-4}$ without a free $10^{56}$ boost from Planck?
On the data side I already have $\sigma_X < 1.5\times 10^{-4}$ (95% CL).
On the theory side the working picture is $\ell_{\ast}\sim R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ under a few axioms I write down explicitly.

Short-paper outline:
[`papers/what-i-would-put-in-a-paper.md`](papers/what-i-would-put-in-a-paper.md).

---

## How the folders are arranged

```
START_HERE.md
README.md
BOUNDARY.md
papers/
 what-i-would-put-in-a-paper.md
 INDEX.md
 core/
 r1_kernel/
 closed_walls/
 side_threads/
 work_packages/
scripts/...
tests/ results/ data/
```

## Reading paths

**A — what can I actually claim? (~30 min)**
1. [`papers/what-i-would-put-in-a-paper.md`](papers/what-i-would-put-in-a-paper.md)
2. [`papers/core/FOR_REFEREES.md`](papers/core/FOR_REFEREES.md)
3. [`papers/core/VERIFIED_RESULTS.md`](papers/core/VERIFIED_RESULTS.md)
4. [`papers/core/SIMPLE_AS_LAMBDA.md`](papers/core/SIMPLE_AS_LAMBDA.md)
5. [`BOUNDARY.md`](BOUNDARY.md)

**B — residual scale argument (~45 min)**
1. [`papers/r1_kernel/NOTE_uniqueness_residual_grain.md`](papers/r1_kernel/NOTE_uniqueness_residual_grain.md)
2. [`papers/r1_kernel/r1-derivation-sandwich.md`](papers/r1_kernel/r1-derivation-sandwich.md)
3. [`papers/r1_kernel/r1-sandwich-falsifiers.md`](papers/r1_kernel/r1-sandwich-falsifiers.md)
4. [`papers/r1_kernel/r1-T2-preregistration.md`](papers/r1_kernel/r1-T2-preregistration.md)
5. [`papers/r1_kernel/r1-lineA-g-from-averaging.md`](papers/r1_kernel/r1-lineA-g-from-averaging.md)

**C — things I already closed**
Sister amplification gap, plus everything under [`papers/closed_walls/`](papers/closed_walls/).

**D — local matter kinematics (CF4, not DE residual)**
1. [`papers/r1_kernel/r1-real-velocity-block-net.md`](papers/r1_kernel/r1-real-velocity-block-net.md)
2. [`papers/r1_kernel/r1-collapse-relief.md`](papers/r1_kernel/r1-collapse-relief.md)

Open lines: [`papers/r1_kernel/FRONTIER_INQUIRY.md`](papers/r1_kernel/FRONTIER_INQUIRY.md).
Public data vs my analysis: [`papers/r1_kernel/HONEST_ASSETS.md`](papers/r1_kernel/HONEST_ASSETS.md).

---

## Status

| Topic | Where it stands |
|:------|:----------------|
| Soft $10^{56}$ from Sorkin seed | closed under the maps I checked |
| $R_{\mathrm{nl}}$ | $\approx 8.61\,\mathrm{Mpc}$ |
| Free residual cell under axioms A0–A4 | $\ell_{\ast}\sim R_{\mathrm{nl}}$ |
| Does nature have $\chi$? | I postulate it; I do not derive it from the SM |
| Coupling $g$ | working bound $\lvert g\rvert\lesssim 1.45$ from DESI residual |
| Residual explains $\sim 8\%\,H_0$? | no — amplitude is short by a lot |
| CF4 block net + collapse relief | done on public catalog; matter only |

---

## Commands I actually run

```bash
pytest -q
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_lineA_Q_variance_proxy.py
python scripts/r1/r1_T2_real_pipeline.py
python scripts/r1/r1_real_velocity_block_net.py
python scripts/r1/r1_collapse_relief_cf4.py
```

Full catalogue: [`papers/INDEX.md`](papers/INDEX.md).
