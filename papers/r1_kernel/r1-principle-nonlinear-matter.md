# Blind R1 candidate: DE residual cell = matter nonlinear scale $R_{\mathrm{nl}}$

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail) · July 2026

*Physical hypothesis + refined length calculation. Not a derivation from an action.*

Code: [`scripts/r1/r1_sigma_R_full.py`](../../scripts/r1/r1_sigma_R_full.py) (full $\sigma(R)$) · [`scripts/r1/r1_principle_Rnl.py`](../../scripts/r1/r1_principle_Rnl.py) (power-law shortcut only)
Steering: [`r1-scale-decade-8-12.md`](r1-scale-decade-8-12.md) · [`r1-open-kernel.md`](r1-open-kernel.md)

---

## Abstract

I state a blind candidate hypothesis (not an action principle) for the open R1 kernel:

> **(P $_\mathrm{nl}$)** The effective counting / correlation cell $\ell_{\ast}$ of the stochastic DE residual sector is the scale at which matter density fluctuations become order unity, $\sigma(R_{\mathrm{nl}})=1$, *if* residual grain / decoherence is sourced where structure collapses.

Two layers, kept separate:

1. **Hypothesis (unproven):** vacuum residual grain $\leftrightarrow$ matter nonlinear patch. This is a physical conjecture, not derived from a Lagrangian or open-system calculation of decoherence.
2. **Geometry of $R_{\mathrm{nl}}$:** once P $_\mathrm{nl}$ is *assumed*, $R_{\mathrm{nl}}$ is a standard matter observable. The evaluation I prefer is the full integral


\sigma^2(R)=\int_0^\infty\frac{\mathrm{d}k}{k}\,\Delta^2(k)\,W_{\mathrm{TH}}^2(kR),


 with a $\Lambda$CDM-like $ P(k)$ normalized to $\sigma_8$, not only a single-index power-law shortcut $\sigma(R)\propto R^{-(n_{\mathrm{eff}}+3)/2}$.

Full integral (this repo): $R_{\mathrm{nl}}\approx 5.80\,h^{-1}\mathrm{Mpc}\approx 8.61\,\mathrm{Mpc}$ ($\sigma_8=0.81$, $h=0.674$).
Power-law shortcut: $\sim 7.8$–$9.6\,\mathrm{Mpc}$ (same decade; coarser).
A posteriori: near $r_0(L_*)$; same decade as $R_8$ and DESI-ceiling $d=3$ cell.
Not claimed: derivation of decoherence; $\ell_{\ast}=R_{\mathrm{nl}}$ proven; $H_0$ tension solved.

---

## 1. Principle (stated before the a posteriori table)

### 1.1 Physical content

1. Matter clustering becomes nonlinear on a characteristic comoving scale $R_{\mathrm{nl}}$ defined by the variance of the linear density field in a top-hat (or equivalent) filter: $\sigma(R_{\mathrm{nl}})=1$.
2. That scale is fixed by the observed $\sigma_8$ (amplitude at $8\,h^{-1}\mathrm{Mpc}$) and the shape of $P(k)$ near that pivot — both are matter / growth data, not DE residual likelihoods.
3. **Hypothesis (not derived):** the DE residual sector does not count Planck cells; it inherits a grain set by the matter nonlinear patch, *if* residual isotropy / SDiff leakage / decoherence is tied to collapsed structure.
 **Missing step:** an explicit decoherence or effective-action calculation that *forces* $\ell_{\ast}=R_{\mathrm{nl}}$ rather than merely allowing it.

Once P $_\mathrm{nl}$ is *assumed*, $R_{\mathrm{nl}}$ is fixed by $\sigma_8$ and $P(k)$ — that part is geometry, not a free dial. The *identification* $\ell_{\ast}=R_{\mathrm{nl}}$ remains the open physical claim.

### 1.2 What is not input

| Forbidden as input to the prediction | Why |
|:-------------------------------------|:----|
| DESI $\sigma_X$ ceiling | A posteriori only |
| Target $\ell_{\ast}=12.56\,\mathrm{Mpc}$ | That is the comparison target |
| Hand-tuned $\theta$ or $r$ | Amplifier walls |
| NP-A $2.06\,\mathrm{Mpc}$ | Different $\sigma$ row; not the lead |

---

## 2. A priori calculation of $R_{\mathrm{nl}}$ (geometry only)

### 2.1 Full integral (primary)


\sigma^2(R)=\int_0^\infty\frac{\mathrm{d}k}{k}\,\Delta^2(k)\,W_{\mathrm{TH}}^2(kR),\qquad \Delta^2(k)=\frac{k^3 P(k)}{2\pi^2},\qquad W_{\mathrm{TH}}(x)=\frac{3(\sin x-x\cos x)}{x^3}.


$P(k)=A\,k^{n_s}T^2(k)$ with Eisenstein–Hu–style transfer (shape $\Gamma_{\mathrm{eff}}$), $n_s=0.965$, $\Omega_m=0.315$, $\Omega_b=0.049$, $h=0.674$, normalized so $\sigma(8\,h^{-1}\mathrm{Mpc})=\sigma_8=0.81$. Solve $\sigma(R_{\mathrm{nl}})=1$.

| Result | Value |
|:-------|:------|
| $R_{\mathrm{nl}}$ | $5.803\,h^{-1}\mathrm{Mpc}=8.610\,\mathrm{Mpc}$ |
| Downstream $\sigma=(\ell_{\ast}/L_H)^{3/2}$ if $\ell_{\ast}=R_{\mathrm{nl}}$, $d=3$ | $\approx 8.5\times 10^{-5}$ (under DESI ceiling $1.5\times 10^{-4}$) |

```bash
python scripts/r1/r1_sigma_R_full.py
```

Caveat on $P(k)$: this is a fitting-function transfer, not CAMB/CLASS Boltzmann output. Good enough to retire the single-index shortcut; a CAMB-normalized run is a further refinement, not expected to move $R_{\mathrm{nl}}$ out of the few–ten Mpc class for this cosmology.

### 2.2 Local power-law shortcut (secondary, coarser)

Near the $8\,h^{-1}\mathrm{Mpc}$ pivot only,


\sigma(R)\approx\sigma_8\left(\frac{R_8}{R}\right)^{\alpha},\qquad \alpha=\frac{n_{\mathrm{eff}}+3}{2} \quad\Rightarrow\quad R_{\mathrm{nl}}=R_8\,\sigma_8^{1/\alpha}.


| $n_{\mathrm{eff}}$ | $R_{\mathrm{nl}}$ [Mpc] |
|:---------------------|:------------------------|
| $-2.0$ | $7.79$ |
| $-1.5$ | $8.96$ |
| $-1.0$ | $9.61$ |

Agrees with the full integral at the decade level; the full integral is the preferred number ($8.61\,\mathrm{Mpc}$).

```bash
python scripts/r1/r1_principle_Rnl.py # shortcut only
```

---

## 3. A posteriori comparison (after the prediction)

| Quantity | Value [Mpc] | Relation to full $R_{\mathrm{nl}}\approx 8.61$ |
|:---------|:------------|:------------------------------------------------|
| $R_{\mathrm{nl}}$ full integral | $8.61$ | prediction (geometry under P$_\mathrm{nl}$) |
| $r_0(L_*)$(Zehavi class) | $7.4$–$8.9$ | very close; clustering length ≠ variance scale |
| $R_8=8/h$ | $11.87$ | same decade ($\sim 38\%$ larger) |
| DESI-ceiling cell $d=3$, $\sigma=1.5\times 10^{-4}$ | $12.56$ | same decade; counting inverse a posteriori |
| NP-A cell $\sigma=10^{-5}$, $d=3$ | $2.06$ | different row — not the lead |

Downstream residual if $\ell_{\ast}=R_{\mathrm{nl}}^{\mathrm{(full)}}\approx 8.61\,\mathrm{Mpc}$, $d=3$:


\sigma_{0,\mathrm{eff}}=\Bigl(\frac{\ell_{\ast}}{L_H}\Bigr)^{3/2} \approx 8.5\times 10^{-5},


under the related DESI ceiling $1.5\times 10^{-4}$ — compatibility, not a fit.

---

## 4. Falsifiers and open microphysics

| If… | Then… |
|:----|:------|
| $\sigma_8$ and $P(k)$ imply $R_{\mathrm{nl}}\ll 3\,\mathrm{Mpc}$ or $\gg 30\,\mathrm{Mpc}$ under standard growth | Principle still well-defined but leaves the 8–12 decade coincidence |
| Microphysics forces DE grain = $L_P$ | Soft null; telescope residual not from this channel |
| Derived $\ell_{\ast}=R_{\mathrm{nl}}$ but BAO residual $\gg 1.5\times 10^{-4}$ without damping | Tension with sister bound |
| Only way to hit data is to retune $R_{\mathrm{nl}}$ after seeing DESI | Excluded under BOUNDARY |

Still missing for a full theory claim: an explicit calculation — from an action, open-system master equation, or equivalent — showing *why* the vacuum residual grain must sit at $R_{\mathrm{nl}}$ rather than $L_P$, $r_0$, or another IR scale. Until that exists, P$_\mathrm{nl}$ is a motivated hypothesis with a clean length, not a derivation.

Ranked mechanism candidates (Buchert averaging, SDiff edge, IR cutoff at $R_{\mathrm{nl}}$, …):
[`r1-mechanism-candidates.md`](r1-mechanism-candidates.md).

---

## 5. Relation to programme walls

This does not re-open soft amplification of Sorkin. It changes the counting cell so the seed is already mesoscopic — the only soft-regime door left open in the kernel notes.

Scope if successful: residual $\sigma_X$ and path slip RMS $10^{-4}$–$10^{-3}$.
Not the $\sim 9\%H_0$ tension (amplitude still short under DESI-safe residual).

---

## 6. Summary

| ID | Claim | Status |
|:---|:------|:-------|
| P1 | Hypothesis P $_\mathrm{nl}$ stated without DESI $\sigma_X$ as input | this note |
| P2 | Full $\sigma(R)$ integral $\Rightarrow R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ | `scripts/r1/r1_sigma_R_full.py` |
| P3 | Power-law shortcut is same decade, coarser | `scripts/r1/r1_principle_Rnl.py` |
| P4 | A posteriori overlap with $r_0$, $R_8$, ceiling cell decade | comparison |
| P5 | $\sigma(\ell_{\ast}=R_{\mathrm{nl}},d=3)\sim 8.5\times 10^{-5}$ under ceiling | arithmetic |

| Not claimed | |
|:----------|:--|
| N-P1 | Derivation from an action / master equation that *forces* $\ell_{\ast}=R_{\mathrm{nl}}$ |
| N-P2 | $\ell_{\ast}=R_{\mathrm{nl}}$ proven |
| N-P3 | $H_0$ tension explained |
| N-P4 | EH transfer = final CAMB-precision $P(k)$ |

