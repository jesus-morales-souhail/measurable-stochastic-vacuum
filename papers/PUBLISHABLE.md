# What is publishable here (and what is not)

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)  
July 2026 · independent work · not peer reviewed

I wrote this so the repo has one place that says, in plain language, **what could go into a paper draft**, what is only a lab note, and what I already closed on purpose.  
Tone: human desk work. No sales pitch.

If you just landed: [`../START_HERE.md`](../START_HERE.md) · full list: [`INDEX.md`](INDEX.md) · fence: [`../BOUNDARY.md`](../BOUNDARY.md).

---

## Three layers

| Layer | Meaning | Where it lives |
|:------|:--------|:---------------|
| **A — Hard / shippable** | identities + numbers I re-run with `pytest` or a named script; I would defend them as written | `core/`, key `results/`, sister DESI bound |
| **B — Conditional science** | true *if* stated axioms hold; falsifiers written; not a detection | `r1_kernel/` sandwich + T2 + $g$ proxy |
| **C — Context / closed / pedagogy** | dead routes, analogies, longer WPs — keep for honesty, not as main claims | `closed_walls/`, `side_threads/`, `work_packages/` |

A draft paper should be mostly **A + a short B**.  
C goes to appendices or “routes I closed,” not the abstract.

---

## A — Hard package (could be §Results / Methods)

| Claim | Note / code | Status |
|:------|:------------|:-------|
| Kinematic identities (slip, path RMS bookkeeping) | [`core/VERIFIED_RESULTS.md`](core/VERIFIED_RESULTS.md) · `pytest -q` | green |
| Soft maps do not freely create $10^{56}$ | sister repo amplification gap + this repo soft bounds | closed under audited maps |
| Residual does not fix $\sim 8\%\,H_0$ at DESI-safe amplitude | closed walls + FOR_REFEREES | closed |
| $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ from $\sigma(R)=1$ | [`r1-principle-nonlinear-matter.md`](r1_kernel/r1-principle-nonlinear-matter.md) · `r1_sigma_R_full.py` | geometry (ΛCDM shape stated) |
| DESI residual ceiling $\sigma_X<1.5\times 10^{-4}$ (95% CL) | sister [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou) | empirical (cite sister) |
| CF4 block-net $\eta(L)$ | [`r1-real-velocity-block-net.md`](r1_kernel/r1-real-velocity-block-net.md) | **matter kinematics only** |
| CF4 collapse peaks + velocity relief | [`r1-collapse-relief.md`](r1_kernel/r1-collapse-relief.md) | **matter kinematics only** |

**CF4 notes are publishable as local-structure kinematics.**  
They are **not** a dark-energy residual detection and do not measure $g$ or $\sigma_X$.

Reproduce hard bits:

```bash
pytest -q
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_real_velocity_block_net.py
python scripts/r1/r1_collapse_relief_cf4.py
```

---

## B — Conditional package (could be §Model / §Predictions)

Only under axioms A0–A4 (or the named hypothesis P$_{\mathrm{nl}}$). I say that out loud every time.

| Piece | Note | One-line honesty |
|:------|:-----|:-----------------|
| Free residual cell $\ell_{\ast}\sim R_{\mathrm{nl}}$ | [`NOTE_uniqueness_residual_grain.md`](r1_kernel/NOTE_uniqueness_residual_grain.md), [`r1-derivation-sandwich.md`](r1_kernel/r1-derivation-sandwich.md) | uniqueness **if** local coupling to nonlinear matter |
| How it dies | [`r1-sandwich-falsifiers.md`](r1_kernel/r1-sandwich-falsifiers.md) | required in any draft |
| $\sigma_{\mathrm{free}}\sim 8.5\times 10^{-5}$ | sandwich numbers | under $d=3$ counting, not a fit to DESI |
| $\lvert g\rvert\lesssim 1.45$ working bound | DESI residual + $\sigma_{\mathrm{free}}$ | a posteriori ceiling, not a measurement of $g$ |
| $g_{\mathrm{eff}}\sim\mathcal{O}(1)$ from averaging proxy | [`r1-lineA-g-from-averaging.md`](r1_kernel/r1-lineA-g-from-averaging.md) | order-of-magnitude, not microphysics |
| Residual × structure protocol | [`r1-T2-preregistration.md`](r1_kernel/r1-T2-preregistration.md) + mock | protocol + synthetic recovery; **no real residual map yet** |
| Minimal public model | [`core/SIMPLE_AS_LAMBDA.md`](core/SIMPLE_AS_LAMBDA.md) | $\Lambda$ + one grain $\sigma$ |

**I do not claim:** SM realises $\chi$; residual detected; $\ell_{\ast}$ fitted to DESI after looking.

---

## C — Keep, but do not lead with

| Folder | Why keep | How to cite in a draft |
|:-------|:---------|:-----------------------|
| [`closed_walls/`](closed_walls/) | I already killed free $H_0$ bridges, wrong $\ell_{\ast}$ matches | “Routes closed” appendix |
| [`side_threads/`](side_threads/) | inflation spectator, lensing floors, edge analogy | related work / pedagogy |
| [`work_packages/`](work_packages/) | longer slip / falsification maps | internal; compress if needed |
| Sister exploratory notes | wrong-scale optics | **never** as cosmology claims |

---

## Suggested draft skeleton (one paper, not three repos)

1. **Question** — can residual DE noise sit near $10^{-5}$–$10^{-4}$ without free $10^{56}$?  
2. **Data bound** — sister DESI $\sigma_X$ ceiling (cite, do not re-MCMC here).  
3. **Minimal model** — SIMPLE_AS_LAMBDA equations.  
4. **Scale** — $R_{\mathrm{nl}}$ geometry + sandwich under A0–A4 + falsifiers.  
5. **What residual cannot do** — not 8% $H_0$.  
6. **Matter context (optional short section)** — CF4 block-net + collapse relief: where gravity / peculiar motions live relative to expansion near $R_{\mathrm{nl}}$; explicit non-claims.  
7. **Next test** — T2 when residual maps exist; better $g$ from averaging / open system.  
8. **Closed routes** — short table pointing to closed_walls.

That is the cohesion I want: **one story**, three repos only for hygiene of claims.

---

## Numbers I am willing to put in an abstract (with caveats)

| Symbol | Value | Caveat in the same breath |
|:-------|:------|:--------------------------|
| $\sigma_X$ ceiling | $<1.5\times 10^{-4}$ (95% CL) | sister analysis, kernel stated there |
| $R_{\mathrm{nl}}$ | $\approx 8.61\,\mathrm{Mpc}$ | EH-style $P(k)$, $\sigma_8=0.81$, $h=0.674$ |
| $\sigma_{\mathrm{free}}$ if $\ell_{\ast}=R_{\mathrm{nl}}$ | $\approx 8.5\times 10^{-5}$ | $d=3$ counting |
| $\lvert g\rvert$ working | $\lesssim 1.45$ | from ceiling / $\sigma_{\mathrm{free}}$, not a detection |
| CF4 $\eta(L)$ | $>1$ at $L\sim 5$–$15\,\mathrm{Mpc}$; $<1$ at $L\gtrsim 30$ | $H_0=75$ CF convention; distance noise included |
| CF4 peak / void rms$(V_{\mathrm{pec}})$ | $\sim 0.37$ | catalog scatter; peaks multi-member + dense |

---

## Rules I keep when I say “publishable”

1. Every display equation uses proper `$` / `$$` so GitHub and the draft render.  
2. First person is fine; marketing is not.  
3. Public catalog + my script → say so ([`HONEST_ASSETS.md`](r1_kernel/HONEST_ASSETS.md)).  
4. Matter kinematics and DE residual never share a sentence that blurs them.  
5. Closed walls stay closed: no free soft gain, no residual-as-$H_0$-fix.

---

## Where I am still open (honest)

- Microphysics of $\chi$ and $g$ (postulated / OOM).  
- Real residual × structure (T2) on survey residual maps.  
- CF4: LOS only; optional Courtois grids; named cross-match of top `1PGC`.  
- CAMB-normalized $R_{\mathrm{nl}}$ refinement (same decade expected).

That open list is not a weakness in the hard package. It is the boundary of the draft.
