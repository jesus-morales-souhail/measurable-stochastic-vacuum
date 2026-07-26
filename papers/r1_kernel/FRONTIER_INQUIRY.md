# What I work on after closing residual-$H_0$

Jesús Morales Souhail · July 2026  
[github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)

Not a detection paper. Depends on the uniqueness argument, the DESI residual ceiling, and the closed $H_0$ checks.

---

## Why residual is not the 8% $H_0$ problem

A residual at $\sigma\lesssim 10^{-4}$ cannot make an 8% jump in distance or $H_0$:

| Quantity | Value | $0.08$ / that |
|:---------|:------|:----------------|
| DESI residual ceiling | $1.5\times 10^{-4}$ | $\sim 500$ |
| free grain at $R_{\mathrm{nl}}$ | $8.5\times 10^{-5}$ | $\sim 1000$ |
| path RMS (working residual) | $\sim 2.5\times 10^{-3}$ | $\sim 30$–$50$ |

I treat the residual sector as a $10^{-5}$–$10^{-4}$ problem with a geometric scale. If the 8% is physical, it lives in early expansion, ladder systematics, or large-scale mean effects that do not inject a DESI residual above the ceiling.

---

## What can make ~8% without breaking the DESI residual bound

Any mechanism with $\Delta H/H\sim 8\%$ must not look like a stationary BAO residual $\gtrsim 10^{-4}$ on the OU/QNM kernel I used.

| Class | ~8%? | Compatible with $\sigma_X\lesssim 10^{-4}$? |
|:------|:-----|:--------------------------------------------|
| early universe / $r_d$ / $N_{\mathrm{eff}}$ | yes | yes — different epoch |
| local ladder systematics | partly | yes — not a DE residual field |
| void / bulk flow $\gtrsim 100\,\mathrm{Mpc}$ | maybe | only if it is not OU residual on BAO bins |
| mean $w(z)$ / MG | maybe | only if residual about the mean stays small |
| stochastic residual at $10^{-4}$ | no | already at ceiling |
| soft Planck $\times 10^{56}$ | only if free | closed |

I do not compete with early DE for $H_0$. I work on residual amplitude and scale.

---

## Open work on the residual sector

**Coupling $g$.** I want $g$ from physics, not only from DESI.

| Path | Status |
|:-----|:-------|
| averaging residual (Buchert-like) on $R_{\mathrm{nl}}$ | OOM + Gaussian proxy: $g_{\mathrm{eff}}\sim\mathcal{O}(1)$ — `r1-lineA-g-from-averaging.md` |
| SDiff edge residual | same order if $\varepsilon\sim\mathcal{O}(1)$ |
| influence functional with matter bath | still to formalise beyond OOM $\Gamma$ |

**Survey fingerprint.** Residual correlated with nonlinear structure near $R_{\mathrm{nl}}$ (roughly 4–26 Mpc). Protocol: `r1-T2-preregistration.md`. Synthetic mock: `scripts/r1/r1_T2_mock_pipeline.py`.

**Information on the light cone.** Path RMS $s\sqrt{N}$ is solid kinematics. Shannon / von Neumann language needs a defined ensemble; later.

---

## Priority

```
A  g from averaging / edge
B  residual × structure tests   (parallel with A)
C  information metric           (later)
```

**Matter kinematics already done (not residual detection):**  
CF4 block-net $\eta(L)$ and collapse-peak velocity relief  
([`r1-real-velocity-block-net.md`](r1-real-velocity-block-net.md), [`r1-collapse-relief.md`](r1-collapse-relief.md)).  
Where peculiar motion competes with expansion near $R_{\mathrm{nl}}$. Does not replace T2.

---

## Scope of this programme

- Residual window $\sigma\sim 10^{-5}$–$10^{-4}$, $\ell_{\ast}\sim R_{\mathrm{nl}}$ under A0–A4.  
- $H_0\sim 8\%$ is outside this residual sector.  
- No free $10^{56}$; no post-hoc $\ell_{\ast}$.  
- Each formula is either derived, order-of-magnitude, or a postulate — labelled as such.

Open work: better $g$ from averaging/SDiff, and residual–structure tests when residual maps exist.
