# What I would put in a paper (and what I would leave out)

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)  
July 2026 · not peer reviewed

I keep too many notes. This page is only for me when I sit down to write something short:  
what I would defend, what needs the axioms said out loud, and what stays in the drawer.

Landing page: [`../START_HERE.md`](../START_HERE.md) · full list: [`INDEX.md`](INDEX.md).

---

## Three piles on the desk

**1. Numbers I re-run**  
If `pytest` or a named script still prints them, they can go in Methods / Results.

- kinematics locked by tests — [`core/VERIFIED_RESULTS.md`](core/VERIFIED_RESULTS.md)  
- $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ — `r1_sigma_R_full.py`  
- residual does not fix $\sim 8\%\,H_0$ at the DESI-safe amplitude  
- soft maps do not hand me free $10^{56}$  
- DESI ceiling $\sigma_X<1.5\times 10^{-4}$ (95% CL) — sister repo, cite it  
- Cosmicflows-4 block net and collapse relief — **matter velocities only**, not dark-energy residual  

```bash
pytest -q
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_real_velocity_block_net.py
python scripts/r1/r1_collapse_relief_cf4.py
```

**2. Claims that are true only under the axioms**  
Sandwich $\ell_{\ast}\sim R_{\mathrm{nl}}$, falsifiers, $g$ order-of-magnitude, T2 protocol.  
I write the *if* in the same sentence. I do not call this a detection.

Main thread: [`r1_kernel/NOTE_uniqueness_residual_grain.md`](r1_kernel/NOTE_uniqueness_residual_grain.md).

**3. Stuff I keep so I remember why I stopped**  
Closed walls, side threads, long work packages, exploratory sister notes.  
Appendix or silence — not the abstract.

---

## Outline I would actually follow

1. Question: residual near $10^{-5}$–$10^{-4}$ without free $10^{56}$?  
2. DESI bound (sister).  
3. Minimal equations ([`core/SIMPLE_AS_LAMBDA.md`](core/SIMPLE_AS_LAMBDA.md)).  
4. Scale: $R_{\mathrm{nl}}$ + sandwich under A0–A4 + how it dies.  
5. What it cannot do: not the 8% $H_0$.  
6. Optional short CF4 section: where peculiar motion sits vs expansion near that grain.  
7. What is still open: better $g$, real residual×structure when maps exist.  
8. One table of routes I already closed.

One story. Three repos only so claims do not get mixed.

---

## Numbers I would write with the caveat next to them

| Number | Caveat I would keep |
|:-------|:--------------------|
| $\sigma_X<1.5\times 10^{-4}$ | sister analysis, their kernel |
| $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ | stated $P(k)$, $\sigma_8$, $h$ |
| $\sigma_{\mathrm{free}}\approx 8.5\times 10^{-5}$ | if $\ell_{\ast}=R_{\mathrm{nl}}$, $d=3$ |
| $\lvert g\rvert\lesssim 1.45$ | from ceiling / $\sigma_{\mathrm{free}}$, not a measurement of $g$ |
| CF4 $\eta(L)$ | $H_0=75$ CF convention; distance noise is in the field |

---

## Still open (I am not hiding this)

- microphysics of $\chi$ and $g$  
- residual × structure on real residual maps  
- CF4 is line-of-sight only; grids and named clusters optional later  
- $R_{\mathrm{nl}}$ with a full Boltzmann $P(k)$ is a refinement, same decade  

---

## Habits

- equations must render (`$` / `$$`)  
- first person is fine; slogans are not  
- say when data are public and the script is mine  
- matter kinematics and DE residual stay in different sentences  
- closed walls stay closed
