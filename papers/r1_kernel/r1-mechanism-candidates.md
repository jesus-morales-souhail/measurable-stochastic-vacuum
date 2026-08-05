# Mechanism candidates for “why $\ell_{\ast}\sim R_{\mathrm{nl}}$” — ranked by seriousness

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail) · July 2026

*Literature map for the open microphysics under P$_\mathrm{nl}$. Not a derivation.*

Context: $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ is well computed ([`r1-principle-nonlinear-matter.md`](r1-principle-nonlinear-matter.md)); the missing piece is *why* a vacuum residual grain would inherit that length.

---

## 0. What a serious candidate must do

For this programme (not for “solve Dark Energy” in general):

| Requirement | Why |
|:------------|:----|
| Fix a length of order few–ten Mpc from matter / gravity without DESI $\sigma_X$ as input | Match the 8–12 Mpc decade lead |
| Connect that length to a residual / grain / IR cell of the DE or vacuum sector | Open R1 kernel, not only mean $\Lambda$ |
| Be formulable enough to write a falsifier | Same bar as WP5 |
| No free $10^{56}$ or hand-tuned $\theta$ | Walls already measured |

Below: tiers by weight. “Serious” ≠ “correct.”

---

## Tier 1 — Most coherent with this programme (pursue first)

### T1.1 Cosmological averaging / backreaction with domain $\sim R_{\mathrm{nl}}$

| | |
|:--|:--|
| Idea | Einstein equations are nonlinear; spatial averaging over a domain of size $L_{\mathrm{av}}$ produces effective sources (Buchert $Q$, averaged curvature). The natural domain is the scale of nonlinear structure, not $L_P$. |
| Why it fits | The averaging scale is an IR cell tied to structure formation — same neighbourhood as $R_{\mathrm{nl}}$, $R_8$, $r_0$. Residual fluctuations about the average could be the programme’s $\sigma$-sector. |
| Key literature | Buchert, *Dark Energy from structure* arXiv:[0707.2153](https://arxiv.org/abs/0707.2153); Räsänen on backreaction; Wiegand & Buchert, *Multiscale cosmology and structure-emerging Dark Energy* arXiv:[1002.3912](https://arxiv.org/abs/1002.3912) |
| Status | Mature, contested magnitude for *mean* acceleration; gauge / foliation issues still debated. |
| What to compute next (blind) | Choose $L_{\mathrm{av}}=R_{\mathrm{nl}}$ from $\sigma(R)=1$ only; estimate residual variance of averaged quantities on that domain; compare a posteriori to $\sigma_X$ ceiling — no fit of $L_{\mathrm{av}}$ to DESI. |
| Risk | Literature often targets mean DE, not a small residual $\sigma\sim 10^{-4}$; may overclaim acceleration. |

### T1.2 SDiff / unimodular “edge” grain locked to collapsed matter

| | |
|:--|:--|
| Idea | Isotropic vacuum stress is projected out (programme SDiff / unimodular notes); the only residual channel lives at boundaries / shear / edges of structure — hence a grain $\sim$ size of nonlinear patches. |
| Why it fits | Already the programme’s bulk–edge language ([`TOPOLOGICAL_EDGE_ANALOGY.md`](../side_threads/TOPOLOGICAL_EDGE_ANALOGY.md)); P$_\mathrm{nl}$ is the quantitative version of “edge scale = $R_{\mathrm{nl}}$.” |
| Key literature | Unimodular gravity / SDiff corpus in related DESI repo; condensed-matter edge analogy is method notes only. |
| Status | Structural zero for isotropic vacuum is a programme claim; the step “edge width = $R_{\mathrm{nl}}$” is still hypothesis. |
| What to compute next | Write the residual operator supported only on regions with $\delta_m\sim\mathcal{O}(1)$; predict $\ell_{\ast}$ from the two-point structure of that mask — a priori from $P(k)$, a posteriori vs $8.61\,\mathrm{Mpc}$. |
| Risk | Without a derived mask/width, it stays slogan-level. |

### T1.3 IR cutoff of vacuum modes at the nonlinear scale (not the Hubble scale)

| | |
|:--|:--|
| Idea | Vacuum energy / residual variance is regulated by an IR cutoff $L_{\mathrm{IR}}$. Standard holographic DE often takes $L_{\mathrm{IR}}\sim H^{-1}$ (horizon). A structure-aware choice is $L_{\mathrm{IR}}\sim R_{\mathrm{nl}}$ (modes longer than nonlinear patches are averaged / do not contribute as free residual). |
| Why it fits | Directly sets $\ell_{\ast}\sim R_{\mathrm{nl}}$ by definition of the cutoff; amplitude $\sim (L_P/L_{\mathrm{IR}})^p$ or $1/\sqrt{N_{\mathrm{cell}}}$ can be checked against $\sigma_X$. |
| Key literature | Holographic DE / IR–UV relations (e.g. CKN-type bounds for mean $\Lambda$); structure-scale cutoffs appear in averaging and coarse-graining papers more than in classic HDE. |
| Status | Choosing $L_{\mathrm{IR}}=R_{\mathrm{nl}}$ is still a postulate unless derived from coarse-graining of QFT on an inhomogeneous background. |
| What to compute next | Given $L_{\mathrm{IR}}=R_{\mathrm{nl}}$ from $\sigma(R)=1$, predict $\sigma_{0,\mathrm{eff}}$ under $d=3$ counting; require it $\le 1.5\times 10^{-4}$ a posteriori (already true at $8.61\,\mathrm{Mpc}$). The hard part remains *why* that IR cutoff. |
| Risk | Easy to reinvent free $L_{\mathrm{IR}}$ as a dial; must stay locked to matter $\sigma(R)$. |

---

## Tier 2 — Serious literature, weaker map to residual grain

### T2.1 Decoherence $\to$ effective $\Lambda$ (quantum cosmology)

| | |
|:--|:--|
| Idea | Decoherence of cosmological quantum states can induce an effective cosmological term (e.g. Kiefer et al., CQG 2011 “Cosmological constant from decoherence”; related decoherence–DE ideas). |
| Why weaker here | Usually targets mean $\Lambda$, not a mesoscopic residual cell of few Mpc; scale often set by horizon / Planck, not $R_{\mathrm{nl}}$. |
| Use for us | Borrow methods (master equation, pointer basis = structure) rather than results for $\Lambda$. |
| Ref. | Kiefer, arXiv-era CQG 28 125022 (2011) class |

### T2.2 EFT of dark energy with nonlinear $k_{\mathrm{max}}$

| | |
|:--|:--|
| Idea | Cosmological EFTs cut perturbation theory at $k\sim 0.1\,h\mathrm{Mpc}^{-1}$ (nonlinear). |
| Why weaker here | That cutoff is analysis validity, not a physical vacuum grain for $\sigma_X$. |
| Use for us | Reminds that “nonlinear scale” is already the IR of controlled gravity; does not explain residual amplitude. |
| Ref. | EFT of DE literature (e.g. Gubitosi et al. arXiv:1210.0201) |

### T2.3 Multiscale backreaction / morphon (structure-emerging DE)

| | |
|:--|:--|
| Idea | Hierarchy of averaging domains; effective scalar (“morphon”) from backreaction (Wiegand & Buchert). |
| Why intermediate | Explicitly links structure scales to effective DE; closer to T1.1 with more machinery. |
| Risk | Heavy formalism; easy to lose contact with a single $\ell_{\ast}$ and DESI residual kernel. |
| Ref. | arXiv:[1002.3912](https://arxiv.org/abs/1002.3912) |

---

## Tier 3 — Low weight for this open question

| Candidate | Why deprioritize here |
|:----------|:---------------------|
| Classic holographic DE with $L=H^{-1}$ | Predicts horizon scale ($\mathrm{Gpc}$), not 8–12 Mpc |
| Pure Planck-cell vacuum counting | Sorkin seed — wall already measured |
| Soft amplifiers / complex $\omega$ on residual to move $H_0$ by 9% | Amplitude short by $\times 10^{2}$–$10^{3}$ |
| Fitting $\ell_{\ast}$ to $R_8$ or $r_0$ after looking | Excluded (BOUNDARY) |
| “Voxel vacuum” / ad hoc IR cutoffs without structure derivation | Undeclared free length |

---

## Recommended order of attack

```
1) T1.1 Averaging domain L_av := R_nl (from sigma(R)=1 only)
 → residual variance on that domain vs sigma_X ceiling
2) T1.2 Residual operator supported where |δ_m| ~ O(1)
 → correlation length of that mask from P(k)
3) T1.3 Only if (1)–(2) need an IR-cutoff language
4) T2.* Methods borrow, not primary claims
```

Each step: blind length from matter, then a posteriori DESI / $r_0$ / $R_8$.

### Status of computations (July 2026)

| Step | Status | Where |
|:-----|:-------|:------|
| T1.1 numbers | Done — $L_{\mathrm{av}}=R_{\mathrm{nl}}\Rightarrow\sigma_{d=3}\approx 8.5\times 10^{-5}$ under ceiling | [`r1-t1-mechanisms-compute.md`](r1-t1-mechanisms-compute.md) |
| T1.2 numbers | Done — $f(\delta>1)\approx 0.16$, $\ell_{\mathrm{sep}}\approx 16\,\mathrm{Mpc}$ packing OOM | same |
| T1.2 mask $r_e$ | Done — $r_{e,\mathrm{mask}}\approx 1.11\,R_{\mathrm{nl}}$ | [`r1-derivation-sandwich.md`](r1-derivation-sandwich.md) |
| Sandwich uniqueness | Done under A0–A4 — free residual cell forced to $\sim R_{\mathrm{nl}}$ | same |
| T1.3 | Optional language only | — |
| Existence of $\chi$ + coupling from SM | Still open (postulates A0–A1) | cannot be replaced by sandwich |

The serious candidates are those that already treat the nonlinear structure scale as an IR domain (averaging / backreaction / edge of collapse). Decoherence-to-mean-$\Lambda$ and EFT $k_{\mathrm{max}}$ are real physics but weaker maps to a residual grain of few Mpc. Horizon holography and soft amplifiers are the wrong scale or outside this residual sector.
