# As simple as $\Lambda$: the minimal model

**Author:** Jesús Morales Souhail · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Date:** July 2026  
**Status:** Pedagogical + verified reduction of the full programme  
**Gate:** `pytest -q` · library `scripts/lib_verified.py` · details in `VERIFIED_RESULTS.md`  

---

## 1. Why $\Lambda$ wins (and how to match it)

| | Cosmological constant $\Lambda$ | This programme (reduced) |
|:--|:--------------------------------|:-------------------------|
| Background expansion | **One** number ($\Lambda$ or $\Omega_\Lambda$) | **Same** — keep $\Lambda$CDM |
| Einstein equation | $G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}$ | **Unchanged** for the mean |
| Extra physics | None | **One** grain parameter $\sigma$ |
| Extra prediction | None | One light-path number $\mathrm{RMS}$ |
| Free lunch $10^{-61}\to 10^{-5}$ | Not needed | **Forbidden** (already killed) |

**How we “beat” $\Lambda$ is not by more maths.**  
$\Lambda$ already describes the **mean** vacuum.  
We keep that mean and add the **simplest possible correction** that $\Lambda$ cannot make: a small, countable grain that light can see.

---

## 2. Folder-by-folder reduction (what survives)

| Folder / repo | Role after simplification |
|:--------------|:--------------------------|
| `stochastic-dark-energy-ou` | **Data:** null residual $\Rightarrow$ mean is $\Lambda$-like; $\sigma_X<1.5\times 10^{-4}$ |
| `measurable-stochastic-vacuum` | **Theory:** only the equations below |
| `stochastic-de-exploratory-notes` | **Ignore** for the minimal model (hygiene only) |
| `proyecto_unificacion` | Separate pipeline; not required here |
| Desqueezing / tesseract / GPE / Euclid MCMC demos | Optional; **not** in the minimal set |

Everything else is commentary, audits, or open research.

---

## 3. The model in three lines (same simplicity class as $\Lambda$)

### Line A — Background (identical to $\Lambda$CDM)

$$
H^2(z) = H_0^2\Bigl[\Omega_m(1+z)^3 + \Omega_\Lambda\Bigr].
$$

No new expansion history. DESI residual analysis prefers this smoothness.

### Line B — One grain parameter (replaces Planck mythology)

$$
\sigma = \left(\frac{\ell_*}{L_H}\right)^{3/2}
\quad\Leftrightarrow\quad
\ell_* = L_H\,\sigma^{2/3}.
$$

- $\sigma$: dimensionless noise amplitude of the dark-energy sector (our only extra constant, like $\Omega_\Lambda$ is the only vacuum constant in flat $\Lambda$CDM).  
- $\ell_*$: correlation / counting length (derived from $\sigma$, not free).  
- $L_H=c/H_0$: Hubble length.  
- Exponent $3/2$: spatial 3D counting ($d=3$).  

**Drop** Sorkin $\sigma\sim 10^{-61}$ as a target for telescopes.  
If you measure something, $\sigma$ is mesoscopic: $\sigma\sim 10^{-6}$–$10^{-5}$ $\Rightarrow$ $\ell_*\sim$ Mpc.

### Line C — What light sees (one prediction)

$$
\mathrm{RMS}
=
\sigma\sqrt{\frac{L_H}{\ell_*}}
=
\sigma^{2/3}
\qquad\text{(order of magnitude; }d=3\text{)}.
$$

More carefully (same content, one prefactor $\mathcal{O}(1)$):

$$
\mathrm{RMS}(|\gamma-1|)
\;\approx\;
\alpha\,\sigma\sqrt{\frac{\chi}{\ell_*}},
\qquad
\alpha \equiv 2\varepsilon\frac{\rho_X}{\rho_m|\delta_m|}\sim\mathcal{O}(1).
$$

With $\ell_*=L_H\sigma^{2/3}$ and $\chi\sim L_H$:

$$
\mathrm{RMS}
\;\sim\;
\alpha\,\sigma^{2/3}.
$$

**That is the whole theory** at $\Lambda$-level simplicity:

| Symbol | Meaning | Analogue in $\Lambda$CDM |
|:-------|:--------|:-------------------------|
| $\Omega_\Lambda$ | Mean vacuum | Same, kept |
| $\sigma$ | Grain of vacuum | **New**, single extra constant |
| $\mathrm{RMS}\sim\sigma^{2/3}$ | Light-path slip signal | New observable |

---

## 4. Side-by-side “textbook” form

### Cosmological constant

$$
\boxed{G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}}
$$

Parameters: $\Lambda$ (or $\Omega_\Lambda$).  
Prediction: $H(z)$ as above.

### Grainy vacuum (minimal)

$$
\boxed{
\begin{aligned}
&\text{mean: same }\Lambda\text{CDM}\\
&\sigma=\text{one grain amplitude}\\
&\mathrm{RMS}(|\gamma-1|)\sim \sigma^{2/3}
\end{aligned}
}
$$

Parameters: $\sigma$ (plus shared $\Omega_m,H_0$).  
Prediction: small gravitational slip along the line of sight; **not** a new $H(z)$.

Optional soft open factor (still simple):

$$
\sigma_{\mathrm{res}} = G\,\sigma,
\qquad G\sim 1\text{–}20
\quad(r=\mathcal{O}(1)),
$$

with **constraint** from data:

$$
\sigma_{\mathrm{res}} < 1.5\times 10^{-4}
\quad\text{(DESI residual ceiling)}.
$$

Then $\mathrm{RMS}\sim(\sigma_{\mathrm{res}})^{2/3}$ or $\mathrm{RMS}\sim\alpha\,\sigma_{\mathrm{res}}\sqrt{\chi/\ell_*}$ with $\ell_*$ from Line B using $\sigma$ (seed) or using $\sigma_{\mathrm{res}}$ if grain is read after open map — see NP-A / NP-B in `NARROW_PATH.md`.

---

## 5. Numerical postcard (no magic)

| Choice | $\sigma$ | $\ell_*$ ($d=3$) | $\mathrm{RMS}\sim\sigma^{2/3}$ | DESI residual |
|:-------|:---------|:-----------------|:-------------------------------|:--------------|
| Planck mythology | $10^{-61}$ | $L_P$ | $\sim 10^{-41}$ (invisible) | trivially OK |
| Minimal NP-A | $10^{-5}$ | $\approx 2.1\,\mathrm{Mpc}$ | $\sim 2\times 10^{-4}$ | OK |
| NP-B soft $G\approx 20$ | seed $\sim 5\times 10^{-6}$ $\to$ $\sigma_{\mathrm{res}}\sim 10^{-4}$ | $\sim$ Mpc | $\sim 10^{-3}$ | OK if $\sigma_{\mathrm{res}}\le 1.5\times 10^{-4}$ |

Exact path formula (verified library) gives the same **order**: few $\times 10^{-4}$ to few $\times 10^{-3}$ in the DESI-safe window — not $0.1$ and not $10^{-60}$.

---

## 6. How this surpasses $\Lambda$ (honestly)

| Criterion | Winner |
|:----------|:-------|
| Simplicity of **background** | **Tie** — we keep $\Lambda$ |
| Number of new constants | $\Lambda$: 0 extra; us: **1** ($\sigma$) — still minimal |
| Explains mean acceleration | **$\Lambda$** (or any DE fluid) |
| Predicts **anisotropy / light slip** from vacuum grain | **Us** (if $\sigma>0$) |
| Planck fine-tuning story | Neither solved; we **stop pretending** telescopes see $10^{-61}$ |
| Falsifiable extra | **Us:** $\mathrm{RMS}\sim\sigma^{2/3}$ vs lensing/slip surveys |

We do not replace $\Lambda$.  
We add the **smallest equation** that makes vacuum grain **testable**, with maths no heavier than $\Lambda$ itself.

---

## 7. What we delete from the mental model

| Drop | Why |
|:-----|:----|
| $r\sim 64$ | Numerology |
| $N_{\mathrm{pat}}\sim 10^{119}$ | Impossible in our universe |
| Free $10^{56}$ | Forbidden |
| Changing $H(z)$ first | Data kill large isotropic residual |
| Tesseracts, pupils, B4 | Wrong scale/operator |
| Full R1–R2–R3 jargon in public talks | Replace by Lines A–B–C |

Keep jargon only in technical appendices (`VERIFIED_RESULTS`, `NARROW_PATH`).

---

## 8. One slide / one blackboard

```text
Λ CDM:     H² = H₀² [Ω_m (1+z)³ + Ω_Λ]          ← keep  (BULK)

Grain:     σ = (ℓ*/L_H)^{3/2}                    ← one number σ  (EDGE)

Light:     RMS(γ−1) ~ σ^{2/3}                    ← one prediction  (EDGE CURRENT)

Bound:     σ ≲ 10^{-4}                           ← DESI (isotropic)
```

Hall-chip translation (see [`TOPOLOGICAL_EDGE_ANALOGY.md`](TOPOLOGICAL_EDGE_ANALOGY.md)):

```text
BULK  = Λ          (insulator / smooth mean vacuum)
EDGE  = σ          (Laughlin-like collective grain, not Planck electron)
PROTECT = no “backscatter” of free-lunch 10^{-61} into telescopes
SIGNAL  = one-way light path  (like chiral edge current)
```

**Entropy:** local *backscattering* of the protected channel is suppressed —  
**not** “entropy of the universe stops”.

That is the entire public model.

---

## 9. Reproduce

```bash
cd measurable-stochastic-vacuum
pytest -q
python - <<'PY'
import sys; sys.path.insert(0,"scripts")
from lib_verified import *
L_H,_,_ = sorkin_holographic()
MPC=3.085677581e22
for sigma in (1e-61, 1e-5, 5e-6):
    ell = ell_for_target_sigma(sigma, L_H, 3)/MPC
    # simple RMS ~ sigma**(2/3) for d=3, chi~L_H
    print(f"sigma={sigma:.1e}  ell*={ell:.3e} Mpc  sigma**(2/3)={sigma**(2/3):.3e}")
PY
```

---

## 10. Relation to the full programme

| Full programme | Minimal $\Lambda$-simple form |
|:---------------|:------------------------------|
| R1 counting | Line B: $\sigma=(\ell_*/L_H)^{3/2}$ |
| R3 soft open | Optional $G\sim 1$–$20$ with DESI clip |
| R2 slip + path | Line C: $\mathrm{RMS}\sim\sigma^{2/3}$ |
| Self-shielding zeros | Planck $\sigma$ $\Rightarrow$ RMS invisible |
| WP1–WP5 papers | Appendices |

---

*End. If it needs more symbols than $\Lambda$, it is not for the blackboard — put it in an appendix.*
