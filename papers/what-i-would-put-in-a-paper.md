# Draft outline for a short paper

Jesús Morales Souhail · July 2026  
[github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)

I keep this note so I know what belongs in a short paper and what stays in the repository only. Everything below is independent work on public data and code I can re-run.

---

## What I would include

Results I can reproduce with a script or with `pytest`:

- kinematic identities listed in [`core/VERIFIED_RESULTS.md`](core/VERIFIED_RESULTS.md)
- nonlinear scale $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ from the full $\sigma(R)$ integral (`scripts/r1/r1_sigma_R_full.py`)
- residual amplitude far below what would be needed for an $\sim 8\%$ shift in $H_0$, once the DESI residual ceiling is taken seriously
- no free soft gain of order $10^{56}$ under the amplification maps I checked
- sister DESI bound $\sigma_X < 2.5\times 10^{-2}$ (95% CL), cited as an external input to this theory map
- Cosmicflows-4 block velocities and collapse peaks as **matter** kinematics near that scale, not as a dark-energy residual detection

```bash
pytest -q
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_three_gate_lock.py
python scripts/r1/r1_real_velocity_block_net.py
python scripts/r1/r1_collapse_relief_cf4.py
```

Under axioms A0–A4 I can state a conditional result: if residual modes couple locally to nonlinear matter, then $\ell_{\ast}\sim R_{\mathrm{nl}}$. That is not a residual detection. The main write-up is [`r1_kernel/NOTE_uniqueness_residual_grain.md`](r1_kernel/NOTE_uniqueness_residual_grain.md). Plain summary of what is closed and what is open: [`r1_kernel/grain-and-microscope.md`](r1_kernel/grain-and-microscope.md).

---

## What I would leave out of the main text

Closed wrong routes (`closed_walls/`), long work packages, side analogies, and anything that belongs only in the exploratory repository. Those can sit in an appendix or stay offline.

---

## Section order I would use

1. Question: can a residual of order $10^{-5}$–$10^{-4}$ exist without a free factor $10^{56}$ from a Planck seed?
2. DESI residual bound from the sister analysis.
3. Minimal equations ([`core/SIMPLE_AS_LAMBDA.md`](core/SIMPLE_AS_LAMBDA.md)).
4. $R_{\mathrm{nl}}$, the sandwich under A0–A4, and the falsifiers.
5. Explicit statement that this does not solve the $H_0$ tension.
6. Optional: CF4 matter kinematics near $R_{\mathrm{nl}}$.
7. Open problems: microphysics of the residual sector and residual×structure on real residual maps.
8. Short table of closed amplification routes.

---

## Numbers I would quote, with caveats

| Number | Caveat |
|:-------|:-------|
| $\sigma_X < 2.5\times 10^{-2}$ (95% CL) | sister DESI analysis, their residual kernel |
| $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ | stated $P(k)$, $\sigma_8$, $h$ |
| $\sigma_{\mathrm{free}}\approx 8.5\times 10^{-5}$ | only if $\ell_{\ast}=R_{\mathrm{nl}}$ and $d=3$ |
| $\lvert g\rvert\lesssim 1.45$ | from ceiling divided by $\sigma_{\mathrm{free}}$ |
| CF4 $\eta(L)$ | CF $H_0=75$ convention; distance noise included |

---

## Still open

I do not yet have a microphysical derivation of the residual field or of the coupling $g$. Residual×structure on survey residual maps is not done. CF4 here is line-of-sight velocities only. Replacing the fitting-function $P(k)$ with a Boltzmann code would refine $R_{\mathrm{nl}}$ inside the same decade; it would not change the logic of the outline.
