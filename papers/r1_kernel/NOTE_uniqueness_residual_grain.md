# Uniqueness of the residual vacuum grain under local coupling to nonlinear structure

Jesús Morales Souhail
ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) · jmskjym@gmail.com
[github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)

July 2026 · draft note

Code for the numbers: [measurable-stochastic-vacuum](https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum)
DESI residual bound $\sigma_X<2.5\times 10^{-2}$ (95% CL) lives in [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)

---

## Abstract

Usual cosmology treats dark energy as a smooth background. I look at a residual piece $\chi$ that does not drive the mean expansion once the isotropic part is projected out, but can still have a mesoscopic correlation length $\ell_{\ast}$.

Under four axioms — residual sector, local coupling to matter contrast, classical matter on nonlinear scales, and counting free residual modes after decoherence — free residual cells much smaller than the matter nonlinear scale $R_{\mathrm{nl}}$ are not available, and cells much larger fall back to $R_{\mathrm{nl}}$ under local coupling. So $\ell_{\ast}\sim R_{\mathrm{nl}}$.

With a standard top-hat variance integral and an Eisenstein–Hu–style $P(k)$ at $\sigma_8=0.81$ I get $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$. Counting with $d=3$ then gives $\sigma\approx 8.5\times 10^{-5}$, under the DESI residual ceiling from the related analysis. The correlation length of a Gaussian mask $\delta>1$ is about $1.11\,R_{\mathrm{nl}}$. I state falsifiers and bound the dimensionless coupling by $\lvert g\rvert\lesssim\mathcal{O}(1)$. I am not claiming a Standard Model derivation of $\chi$, and I am not claiming this residual fixes the Hubble tension.

**Keywords:** dark energy residual; nonlinear scale; decoherence; gravitational slip; DESI

---

## 1. Introduction

$\Lambda$CDM does well on the mean expansion. Whether the dark-energy sector also has a residual, noisy, granular piece on megaparsec scales is a different question.

If you start from a pure Planck / Sorkin seed $\sigma_0\sim 10^{-61}$ and want $\sim 10^{-5}$ with only soft open-system maps, you need a gain around $10^{56}$. I audited that route in companion work; it is not free.

The other door is the counting cell. If residual degrees of freedom are counted on a mesoscopic length $\ell_{\ast}$ instead of $L_P$,


$$
\sigma=\Bigl(\frac{\ell_{\ast}}{L_H}\Bigr)^{d/2}
$$


can already sit near $10^{-5}$–$10^{-4}$. Then the real question is: what fixes $\ell_{\ast}$?

This note is a conditional answer. I am not saying “dark energy knows about galaxies.” I am saying: *if* a residual couples locally to classical nonlinear matter, then $\ell_{\ast}$ is forced to the matter nonlinear scale $R_{\mathrm{nl}}$ where $\sigma(R_{\mathrm{nl}})=1$. That link is not standard textbook lore. It is the working hypothesis of this programme, written as a uniqueness argument under axioms I can list.

---

## 2. Axioms

| | What I assume |
|:--|:--------------|
| A0 | There is a residual sector $\chi$. Its isotropic mean is projected out (SDiff / unimodular-type zero). Observables care about fluctuations about that mean. |
| A1 | Local coupling: $\mathcal{L}_{\mathrm{int}}=g\chi\delta_m$ (or a density form with the same locality). |
| A2 | On filters with $\sigma(R)\ge 1$, matter is effectively classical and lives in nonlinear patches of size $\sim R_{\mathrm{nl}}$. |
| A3 | After decoherence, free residual modes are counted as $N=(L_H/\ell_{\ast})^d$, $\sigma=N^{-1/2}$. |
| A4 | Soft maps do not give a free $10^{56}$ from a pure Planck seed. |

Everything below is *if A0–A4*. Existence of $\chi$ and the coupling in A1 are still postulates. Averaging residuals, edge stress, or influence functionals are possible stories for A1; they are not required for the algebra of uniqueness.

---

## 3. Uniqueness

### 3.1 Small cells

If $\chi$ couples locally to classical $\delta_m$ coherent on patches of size $R_{\mathrm{nl}}$, then configurations of $\chi$ that differ *inside* one patch share the same classical record. Open-system reasoning kills those coherences unless $g\sigma_\delta$ is tiny. What survives as free residual is the patch average


$$
\chi_{\mathrm{eff}}(p)=\frac{1}{V_p}\int_p\chi.
$$


So free residual cells with $\ell\ll R_{\mathrm{nl}}$ are not really free.

### 3.2 Large cells

If someone claims a free cell $\ell\gg R_{\mathrm{nl}}$, local coupling means that cell is a sum of $N_p=(\ell/R_{\mathrm{nl}})^d$ independent nonlinear patches. The independent modes are the patch ones. Averaging them gives


$$
\sigma_{\mathrm{eff}}(\ell)=\frac{\sigma(R_{\mathrm{nl}})}{\sqrt{N_p}},
$$


i.e. the same counting as if the cell were $R_{\mathrm{nl}}$. Big cells renormalize down.

### 3.3 Result

Under A0–A4,


$$
\ell_{\ast}\sim R_{\mathrm{nl}}
$$


up to $\mathcal{O}(1)$ factors from the same filtered matter field (density correlation length, mask correlation length, packing of $\delta>1$ regions; BBKS peak curvature $R_{\ast}$ is substructure *inside* the domain, not a separate free residual cell under the UV argument).

---

## 4. Geometry and amplitude

### 4.1 $R_{\mathrm{nl}}$\sigma^2(R)=\int_0^\infty\frac{\mathrm{d}k}{k}\,\Delta^2(k)\,W_{\mathrm{TH}}^2(kR),\qquad W_{\mathrm{TH}}(x)=\frac{3(\sin x-x\cos x)}{x^3}.


With EH-style $P(k)$, $n_s=0.965$, $\Omega_m=0.315$, $h=0.674$, $\sigma_8=0.81$:


$$
R_{\mathrm{nl}}\approx 5.80\,h^{-1}\mathrm{Mpc}\approx 8.61\,\mathrm{Mpc}.
$$


No DESI residual fit goes into this number.

### 4.2 Mask and packing

For $m=\mathbf{1}\{\delta>1\}$ at filter $R_{\mathrm{nl}}$,


$$
r_{e,\mathrm{mask}}\approx 9.53\,\mathrm{Mpc}\approx 1.11\,R_{\mathrm{nl}}.
$$


Density correlation length $\approx 14.6\,\mathrm{Mpc}\approx 1.69\,R_{\mathrm{nl}}$.
Packing separation of $\delta>1$ patches $\approx 15.9\,\mathrm{Mpc}$.

### 4.3 Counting amplitude

With $\ell_{\ast}=R_{\mathrm{nl}}$, $d=3$, $L_H=c/H_0$:


$$
\sigma_{\mathrm{free}}=\Bigl(\frac{R_{\mathrm{nl}}}{L_H}\Bigr)^{3/2}\approx 8.5\times 10^{-5},
$$


under the related DESI ceiling $\sigma_X<2.5\times 10^{-2}$ (95% CL, OU/QNM).

### 4.4 Coupling

With $\sigma_{\mathrm{res}}^2=\sigma_{\mathrm{free}}^2+\lambda^2$ and $\lambda=g\sigma_{\mathrm{free}}$,


$$
\lvert\lambda\rvert\lesssim 1.24\times 10^{-4},\qquad \lvert g\rvert\lesssim 1.45
$$


from the working DESI map. Full-covariance profiles on absolute $D/r_d$ at fixed background thrash at the $10^{-4}$ level (large $\chi^2$ gets eaten by residual variance). I keep the working ceiling as the primary bound.

---

## 5. Decoherence OOM

$\Gamma\sim g^2\sigma_\delta^2/\tau_c$ with $\sigma_\delta=1$. For $g\sim 1$, $\Gamma/H_0\sim\mathcal{O}(1)$ if $\tau_c\sim H_0^{-1}$, and larger if $\tau_c\sim R_{\mathrm{nl}}/c$. That is consistent with the UV story as an order-of-magnitude check only.

---

## 6. How this dies

| | Exclusion |
|:--|:----------|
| F1 | $\sigma_{\mathrm{res}}\gg 2.5\times 10^{-2}$ at fixed $\ell_{\ast}=R_{\mathrm{nl}}$, no damping |
| F2 | residual correlation length at $\sigma\sim 10^{-4}$ clearly $\ll 1\,\mathrm{Mpc}$ or $\gg 100\,\mathrm{Mpc}$ |
| F3 | path slip RMS forced way above published mean-slip floors without systematics |
| F4 | $\ell_{\ast}$ fitted after looking at residual data; free $10^{56}$; shear $m$-bias sold as residual texture |

A more detailed residual–structure protocol is in `r1-T2-preregistration.md`.

---

## 7. What I am not claiming

- that SM+GR must contain $\chi$
- a microscopic derivation of $g$ (only $\lvert g\rvert\lesssim\mathcal{O}(1)$ under the working ceiling)
- that this residual explains $\sim 8\%H_0$ (short by $\sim 10^{2}$–$10^{3}$)
- that present mean-slip data already test path RMS at $10^{-3}$

---

## 8. Discussion

The useful content is a narrower open problem. Without A0–A4, any mesoscopic $\ell_{\ast}$ is still in play. With local coupling to classical nonlinear matter, $\ell_{\ast}\sim R_{\mathrm{nl}}$ up to $\mathcal{O}(1)$. What remains is whether nature has that residual and coupling.

Possible non-ad-hoc routes to A1: residual about spatial averages on nonlinear domains; residual stress on nonlinear masks after isotropic projection; influence functionals with matter as bath. In those stories $\chi$ need not be a new fifth-force particle.

---

## 9. Conclusions

Under residual sector + local coupling to classical nonlinear matter + post-decoherence counting,


$$
\ell_{\ast}\sim R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc},
$$


with $\sigma\sim 8.5\times 10^{-5}$ under present DESI residual limits and $\lvert g\rvert\lesssim\mathcal{O}(1)$. Conditional, quantitative, falsifiable. No free soft Planck amplification. No $H_0$ solution.

---

## Reproduce

```bash
git clone https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum.git
cd measurable-stochastic-vacuum
pip install -r requirements.txt
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_sandwich_derivation.py
python scripts/r1/r1_sandwich_falsifiers.py
python scripts/r1/r1_bound_g_oom.py
pytest -q
```

Also useful: `r1-derivation-sandwich.md`, `r1-a1-microphysics.md`, `r1-sandwich-falsifiers.md`, `r1-T2-preregistration.md`, `r1-lineA-g-from-averaging.md`.

---

## References

1. J. M. Bardeen, J. R. Bond, N. Kaiser, A. S. Szalay, ApJ **304**, 15 (1986).
2. T. Buchert, arXiv:0707.2153.
3. D. J. Eisenstein, W. Hu, ApJ **496**, 605 (1998).
4. M. Maus et al., arXiv:2505.20656.
5. Z. Sakr, Y. Zheng, S. Casas, arXiv:2501.07477.
6. J. Morales Souhail, stochastic-dark-energy-ou and measurable-stochastic-vacuum (2026).

