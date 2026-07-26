# T1.2 BBKS refinement + derivation sketch for vacuum grain $\sim R_{\mathrm{nl}}$

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail) · July 2026 · not peer reviewed

*(A) BBKS numbers executed. (B) Derivation sketch with explicit postulates — not a finished QFT proof.*

Code: [`scripts/r1/r1_t12_bbks_peaks.py`](../../scripts/r1/r1_t12_bbks_peaks.py) · [`scripts/r1/r1_t1_mechanisms_compute.py`](../../scripts/r1/r1_t1_mechanisms_compute.py)

---

## Part A — BBKS peak geometry (executed)

### A.1 Definitions (Bardeen, Bond, Kaiser, Szalay 1986)

For a Gaussian field smoothed with window $W(kR)$:

$$
\sigma_j^2(R)=\int_0^\infty\frac{\mathrm{d}k}{k}\,\Delta^2(k)\,k^{2j}\,W^2(kR),
\gamma_{\mathrm{BBKS}}=\frac{\sigma_1^2}{\sigma_0\sigma_2},\qquad R_{\ast}=\sqrt{3}\,\frac{\sigma_1}{\sigma_2}.
$$

$R_{\ast}$ is the curvature radius of peaks (scale of the peak tip), not the filter radius $R$.

### A.2 Results at $R=R_{\mathrm{nl}}$ (full $P(k)$, top-hat)

| Quantity | Value |
|:---------|:------|
| Filter $R_{\mathrm{nl}}$ | $5.803\,h^{-1}\mathrm{Mpc}=8.610\,\mathrm{Mpc}$ |
| $\sigma_0(R_{\mathrm{nl}})$ | $1.000$ (by construction) |
| $\gamma_{\mathrm{BBKS}}$ | $\approx 0.18$ |
| Peak curvature $R_{\ast}$ | $1.062\,h^{-1}\mathrm{Mpc}=1.576\,\mathrm{Mpc}$ |
| $R_{\ast}/R_{\mathrm{nl}}$ | $\approx 0.18$ |
| Packing sep on $R_{\mathrm{nl}}$ ($\delta_c=1$) | $\approx 15.9\,\mathrm{Mpc}$ |

```bash
python scripts/r1/r1_t12_bbks_peaks.py
```

### A.3 Reading

| Scale | Role | Programme link |
|:------|:-----|:---------------|
| $R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}$ | Filter / averaging domain / nonlinear patch size | T1.1; matches $r_0$ decade |
| $R_{\ast}\approx 1.58\,\mathrm{Mpc}$ | Curvature of density peaks (sharper) | Closer to group/NP-A arithmetic row — different object |
| $\ell_{\mathrm{sep}}\approx 16\,\mathrm{Mpc}$ | Typical separation of $\delta>1$ patches | Near $R_8$ / DESI-ceiling cell decade |

BBKS does not collapse everything to one number. It splits geometry into:
- a domain/filter scale $\sim 8$–$9\,\mathrm{Mpc}$ (T1.1 lead), and
- a peak-tip scale $\sim 1.6\,\mathrm{Mpc}$ (finer structure inside the patch).

For residual counting of independent domains, $R_{\mathrm{nl}}$ (or $\ell_{\mathrm{sep}}$) remains the natural cell; $R_{\ast}$ is the substructure scale, not a replacement without a new principle.

---

## Part B — Derivation sketch (postulates marked)

Goal: derive, as far as honesty allows,

$$
\ell_{\ast}\sim R_{\mathrm{nl}}
$$

for a residual vacuum sector, without fitting DESI.

### B.1 Field content (postulate P0)

Introduce a residual scalar sector $\chi$ (the programme’s stochastic residual / grain field) with:
- no classical homogeneous VEV that sources FLRW (SDiff / unimodular projection of isotropic vacuum — programme structural zero);
- residual fluctuations $\delta\chi$ that may source anisotropic stress / path slip after projection.

### B.2 Coupling to matter (postulate P1)

$$
\mathcal{L}_{\mathrm{int}}=g\,\chi\,\delta_m \quad\text{(or }g\,\chi\,\rho_m\text{ density coupling).}
$$

Not derived here: value of $g$. Only the scale structure of the interaction is used.

### B.3 Matter becomes classical at $R_{\mathrm{nl}}$ (standard input S1)

On scales where $\sigma(R)\gtrsim 1$, matter density perturbations are in the nonlinear, effectively classical regime (standard structure-formation lore; environment-induced decoherence of gravitational/density degrees of freedom is a large literature).  
Input, not re-derived: the classical pointer basis for late-time matter is organized by nonlinear patches of size $\sim R_{\mathrm{nl}}$.

### B.4 Influence on $\chi$: coarse-graining (derived under P0–P1 + S1)

If $\delta_m$ is classical and only coherent inside patches of size $R_{\mathrm{nl}}$, the interaction Hamiltonian for $\chi$ is a sum of nearly independent contributions from each patch:

$$
H_{\mathrm{int}}\sim g\sum_{p}\chi_p\,m_p,
$$

where $\chi_p$ is the mean of $\chi$ on patch $p$ and $m_p$ is the matter content of that patch.

Consequence (standard open-system / influence-functional logic):  
coherences of $\chi$ between configurations that differ within a single patch faster than $R_{\mathrm{nl}}$ are suppressed by the classical record in $m_p$ (many environmental degrees of freedom per patch).

Thus the effective residual free field after decoherence is the patch-averaged field

$$
\chi_{\mathrm{eff}}(p)=\frac{1}{V_p}\int_{p}\chi,
$$

i.e. an IR description with cell size

$$
\ell_{\ast}\sim R_{\mathrm{nl}}.
$$

This step is the closest thing to a derivation available without a full QFT-on-inhomogeneous-background calculation:  
*if* $\chi$ couples to classical $\delta_m$ structured on $R_{\mathrm{nl}}$, *then* the residual that remains quantum/stochastic at late times is coarse-grained at $R_{\mathrm{nl}}$.

### B.5 Amplitude after coarse-graining (derived under counting)

With one residual degree of freedom per patch in a Hubble volume,

$$
N=\Bigl(\frac{L_H}{R_{\mathrm{nl}}}\Bigr)^{3},\qquad \sigma=\frac{1}{\sqrt{N}}=\Bigl(\frac{R_{\mathrm{nl}}}{L_H}\Bigr)^{3/2}\approx 8.5\times 10^{-5},
$$

under the DESI ceiling (T1.1 numbers).

SDiff projection removes the isotropic mean; $\sigma$ is the residual fluctuation scale about that mean — consistent with programme nulls on mean DE time drift (BAO $w_0,w_a\approx\Lambda$) while allowing small residual amplitude.

### B.6 Where the sketch is still incomplete

| Step | Status |
|:-----|:-------|
| P0: residual sector $\chi$ exists | Programme postulate |
| P1: coupling $g\chi\delta_m$ | Postulate (strength $g$ free) |
| S1: matter classical on $R_{\mathrm{nl}}$ | Standard, not re-proven |
| Coarse-graining $\Rightarrow\ell_{\ast}\sim R_{\mathrm{nl}}$ | Derived under P0–P1+S1 (influence-functional logic) |
| Sandwich uniqueness (UV+IR) | Elevated: [`r1-derivation-sandwich.md`](r1-derivation-sandwich.md) |
| Full relativistic averaging = Buchert $Q$ | Not identified; optional |
| Peak-tip $R_{\ast}$ vs domain $R_{\mathrm{nl}}$ | BBKS shows both; domain is the residual cell under B.4 |
| Compute $g$ from microphysics | Open (working bound $\lvert g\rvert\lesssim 1.45$) |
| Path-integral proof on exact FLRW+structure metric | Open |

---

## Part C — What “derive” means here

| Claim I may publish under this sketch | Claim I may not |
|:--------------------------------------|:----------------|
| Under coupling to classical nonlinear matter, residual $\chi$ is coarse-grained at $R_{\mathrm{nl}}$ | Microscopic derivation of $g$ from the Standard Model + GR |
| Geometry + counting give $\sigma\sim 8.5\times 10^{-5}$ | Proof that nature realizes P0–P1 |
| BBKS splits peak tip vs domain scales | $\ell_{\ast}=R_{\ast}$ without a new principle |
| Compatible with DESI residual ceiling | Solution of $H_0$ tension |

---

## Claim checklist

| ID | Claim | Evidence |
|:---|:------|:---------|
| B1 | At $R_{\mathrm{nl}}$, $\sigma_0=1$, $R_{\ast}\approx 1.58\,\mathrm{Mpc}$, $\gamma_{\mathrm{BBKS}}\approx 0.18$ | script |
| B2 | Domain cell $R_{\mathrm{nl}}$ remains the counting scale under B.4 | derivation sketch |
| B3 | $\sigma(d=3,R_{\mathrm{nl}})\approx 8.5\times 10^{-5}<1.5\times 10^{-4}$ | T1.1 |
| B4 | Coarse-graining step assumes P0–P1+S1 | this note |

---

## Reproduce

```bash
python scripts/r1/r1_sigma_R_full.py
python scripts/r1/r1_t1_mechanisms_compute.py
python scripts/r1/r1_t12_bbks_peaks.py
pytest -q
```
