# What I work on after closing residual-$H_0$

Jesús Morales Souhail · July 2026  
[github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)

Not a detection paper. Depends on the uniqueness argument, the DESI residual ceiling, and the closed $H_0$ checks.

---

## 0. Framing (so I stop fighting the wrong problem)

A residual at $\sigma\lesssim 10^{-4}$ cannot make an 8% jump in distance or $H_0$. Rough ratios:

| Quantity | Value | $0.08$ / that |
|:---------|:------|:----------------|
| DESI residual ceiling | $1.5\times 10^{-4}$ | $\sim 500$ |
| free grain at $R_{\mathrm{nl}}$ | $8.5\times 10^{-5}$ | $\sim 1000$ |
| path RMS (working residual) | $\sim 2.5\times 10^{-3}$ | $\sim 30$–$50$ |

So I treat the residual sector as a bounded problem in the $10^{-5}$–$10^{-4}$ window with a geometric scale, not as a failed $H_0$ model. If the 8% is physical, it lives in early expansion, ladder systematics, or large-scale mean effects that do not inject a DESI residual above the ceiling.

---

## 1. If not the grain, what can make 8% without breaking DESI residual?

Any mechanism that makes $\Delta H/H\sim 8\%$ must not look like a stationary BAO residual $\gtrsim 10^{-4}$ on the OU/QNM kernel I used.

| Class | Can give ~8%? | OK with $\sigma_X\lesssim 10^{-4}$? |
|:------|:--------------|:-------------------------------------|
| early universe / $r_d$ / $N_{\mathrm{eff}}$ | yes | yes — different epoch |
| local ladder systematics | partly, contested | yes — not a DE residual field |
| void / bulk flow $\gtrsim 100\,\mathrm{Mpc}$ | maybe | only if it is not OU residual on BAO bins |
| mean $w(z)$ / MG | maybe | only if residual about the mean stays small |
| stochastic residual at $10^{-4}$ | no | already at ceiling |
| soft Planck $\times 10^{56}$ | only if free | closed |

I do not compete with early DE for $H_0$. I work on residual amplitude and scale.

---

## 2. Where the model does live

### Coupling $g$

I want $g$ from physics, not only from DESI. Best routes for me:

| Path | Status |
|:-----|:-------|
| averaging residual (Buchert-like) on $R_{\mathrm{nl}}$ | OOM + Gaussian proxy: $g_{\mathrm{eff}}\sim\mathcal{O}(1)$ — see `r1-lineA-g-from-averaging.md` |
| SDiff edge residual | same order if $\varepsilon\sim\mathcal{O}(1)$ |
| influence functional with matter bath | still to formalise beyond OOM $\Gamma$ |

### Survey fingerprint

Not 8% in $H_0$. Residual correlated with nonlinear structure near $R_{\mathrm{nl}}$ (roughly 4–26 Mpc band). Protocol: `r1-T2-preregistration.md`. Synthetic mock recovers the injected scale: `scripts/r1/r1_T2_mock_pipeline.py`.

### Information / entropy on the light cone

Interesting, but second. Path RMS $s\sqrt{N}$ is solid kinematics. Shannon / von Neumann language needs a defined ensemble; I will not invent complex work to force $H_0$.

---

## 3. Order of work

```
A  g from averaging / edge     (foundation)
B  residual × structure tests  (falsifiability)   — parallel with A
C  information metric          (later)
```

**Done on the matter side (context, not residual detection):**  
Cosmicflows-4 block-net $\eta(L)$ and collapse-peak velocity relief  
([`r1-real-velocity-block-net.md`](r1-real-velocity-block-net.md), [`r1-collapse-relief.md`](r1-collapse-relief.md)).  
That maps where gravity / peculiar motions compete with expansion near $R_{\mathrm{nl}}$.  
It does **not** replace T2 (residual × structure still needs a residual map).

Publishable packaging of the whole programme: [`../PUBLISHABLE.md`](../PUBLISHABLE.md).

---

## 4. Rules I keep

1. Residual owns $\sigma\sim 10^{-5}$–$10^{-4}$ and $\ell_{\ast}\sim R_{\mathrm{nl}}$.  
2. $H_0\sim 8\%$ is outsourced.  
3. No free $10^{56}$, no post-hoc $\ell_{\ast}$.  
4. Every formula: derived / OOM / postulate — say which.  
5. Matter kinematics and DE residual stay in separate sentences.

---

## 5. One line

I bounded a mesoscopic residual and fixed its scale under local coupling to nonlinear matter. Local CF4 kinematics show the gravity–expansion grain in real data. The open work is better $g$ from averaging/SDiff and residual–structure tests for Stage-IV — not the 8% Hubble gap.
