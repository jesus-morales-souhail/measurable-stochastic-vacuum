# What I would put in a paper (and what I would leave out)

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)
July 2026

This is a private map of the folder. When I write something short, I use the numbers I can re-run, state the axioms when a claim needs them, and leave closed routes in an appendix or out.

[`../START_HERE.md`](../START_HERE.md) · [`INDEX.md`](INDEX.md)

---

## Content that can go in

**Reproducible numbers** (`pytest` or a named script):

- identities in [`core/VERIFIED_RESULTS.md`](core/VERIFIED_RESULTS.md)
- $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ (`r1_sigma_R_full.py`)
- residual too small for $\sim 8\%\,H_0$ at the DESI-safe amplitude
- no free soft gain of $10^{56}$ under the maps I checked
- $\sigma_X<1.5\times 10^{-4}$ (95% CL) from the related DESI analysis
- Cosmicflows-4 block net and collapse peaks: matter $v_{\mathrm{pec}}$ only

```bash
pytest -q
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_real_velocity_block_net.py
python scripts/r1/r1_collapse_relief_cf4.py
```

**Conditional on A0–A4** (say the *if*): sandwich $\ell_{\ast}\sim R_{\mathrm{nl}}$, falsifiers, $g$ at order of magnitude, T2 protocol. Not a residual detection.
Main note: [`r1_kernel/NOTE_uniqueness_residual_grain.md`](r1_kernel/NOTE_uniqueness_residual_grain.md).

**Leave for appendix or offline:** `closed_walls/`, long work packages, side analogies, exploratory related repository.

---

## Outline

1. Question: residual $\sim 10^{-5}$–$10^{-4}$ without free $10^{56}$?
2. DESI bound (sister).
3. Minimal equations — [`core/SIMPLE_AS_LAMBDA.md`](core/SIMPLE_AS_LAMBDA.md).
4. $R_{\mathrm{nl}}$, sandwich under A0–A4, falsifiers.
5. Not a solution of the $H_0$ tension.
6. Optional: CF4 matter kinematics near that scale.
7. Open: microphysics of $g$, residual×structure on real residual maps.
8. Short table of closed routes.

---

## Numbers and caveats

| Number | Caveat |
|:-------|:-------|
| $\sigma_X<1.5\times 10^{-4}$ (95% CL) | related analysis, their kernel |
| $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ | stated $P(k)$, $\sigma_8$, $h$ |
| $\sigma_{\mathrm{free}}\approx 8.5\times 10^{-5}$ | if $\ell_{\ast}=R_{\mathrm{nl}}$, $d=3$ |
| $\lvert g\rvert\lesssim 1.45$ | from ceiling / $\sigma_{\mathrm{free}}$ |
| CF4 $\eta(L)$ | $H_0=75$ CF convention; distance noise included |

---

## Still open

Microphysics of $\chi$ and $g$. Residual × structure on survey residual maps. CF4 is line-of-sight only. $R_{\mathrm{nl}}$ with a Boltzmann $P(k)$ is a refinement in the same decade.
