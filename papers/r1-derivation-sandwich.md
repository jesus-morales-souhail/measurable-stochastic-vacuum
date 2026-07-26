# Sandwich derivation: uniqueness of residual grain \(\ell_*\sim R_{\mathrm{nl}}\)

**Author:** Jesús Morales Souhail  
**Date:** July 2026  
**Status:** **Derivation under stated axioms** + executed numbers — not a Standard-Model proof that nature realises the axioms  
**Code:** [`scripts/r1_sandwich_derivation.py`](../scripts/r1_sandwich_derivation.py)  
**Results:** [`results/r1_sandwich/`](../results/r1_sandwich/)  
**Depends on:** [`r1-principle-nonlinear-matter.md`](r1-principle-nonlinear-matter.md) · [`r1-t12-bbks-and-derivation.md`](r1-t12-bbks-and-derivation.md) · [`r1-open-kernel.md`](r1-open-kernel.md)

---

## Abstract

The open R1 kernel asks: *what principle fixes a mesoscopic counting cell for the DE residual sector?*  
Previous notes stated the **hypothesis** P\(_\mathrm{nl}\) (\(\ell_*=R_{\mathrm{nl}}\)) and a **sketch** (coarse-graining under coupling to classical matter).  

This note elevates that sketch to a **sandwich uniqueness argument**:

> **Under axioms A0–A4** (residual sector; local coupling \(g\chi\delta_m\); matter classicality on nonlinear patches; counting of free residual DOF after decoherence; no free \(10^{56}\)),  
> the free residual counting cell is forced into the band
> \[
> \ell_*\sim R_{\mathrm{nl}}
> \]
> up to \(\mathcal{O}(1)\) geometric factors fixed by the same matter field (\(R_*\), \(\ell_{\mathrm{sep}}\), \(r_{e}\)).  
> Cells \(\ell\ll R_{\mathrm{nl}}\) are **UV-forbidden** (decoherence / not free).  
> Cells \(\ell\gg R_{\mathrm{nl}}\) **IR-renormalize** to \(R_{\mathrm{nl}}\) patches under local coupling.

**Executed:** real-space \(\xi_\delta(r)\) and Gaussian-threshold mask correlation at \(R=R_{\mathrm{nl}}\); decoherence OOM rates; sandwich table.  
**Still not claimed:** that the Standard Model + GR *must* contain \(\chi\); value of \(g\) from microphysics (bounded a posteriori by DESI).

This is the programme’s first **conditional theorem** for the open kernel — not another coincidence table.

---

## 1. Why this is the advance

| Before this note | After this note |
|:-----------------|:----------------|
| \(\ell_*=R_{\mathrm{nl}}\) is a **hypothesis** that “looks interesting” because numbers sit in the 8–12 Mpc decade | \(\ell_*\sim R_{\mathrm{nl}}\) is the **unique free residual cell** *if* A0–A4 hold |
| Sketch B.4 in [`r1-t12-bbks-and-derivation.md`](r1-t12-bbks-and-derivation.md) | Lemmas UV + IR + uniqueness + numbers |
| “The principle that fixes the galactic grain remains open” (open-kernel) | Principle **form** is fixed under axioms; open problem shrinks to *whether nature realises A0–A1* |

**Honest scope:** a derivation *under axioms* is still a derivation. It is not a proof from the Standard Model alone. That is the correct publication bar for this stage.

---

## 2. Axioms (explicit)

| ID | Axiom | Status |
|:---|:------|:-------|
| **A0** | Residual sector \(\chi\) exists; isotropic mean is projected out (SDiff / unimodular structural zero of the programme). Free residual is the fluctuation about that mean. | Programme postulate |
| **A1** | Local coupling \(\mathcal{L}_{\mathrm{int}}=g\,\chi\,\delta_m\) (or density form). Interaction is **local in space**. | Postulate; \(\lvert g\rvert\) bounded a posteriori |
| **A2** | On filters with \(\sigma(R)\ge 1\), matter is effectively classical (pointer basis of structure formation). Classical coherence scale of the nonlinear patch is \(\sim R_{\mathrm{nl}}\). | Standard structure-formation lore (input, not re-proven) |
| **A3** | After environment-induced decoherence, **free residual DOF** are those not monitored by the classical matter record; they are counted as volume cells of size \(\ell_*\) in a Hubble volume: \(\sigma=(\ell_*/L_H)^{d/2}\). | Programme counting hypothesis |
| **A4** | No free soft gain \(10^{56}\) from a pure Planck seed. Amplitude is the counting result, not a dial. | Measured wall |

**Notation:** \(R_{\mathrm{nl}}\) is defined *only* by the matter variance integral \(\sigma(R_{\mathrm{nl}})=1\) ([`r1_sigma_R_full.py`](../scripts/r1_sigma_R_full.py)). DESI residual likelihoods do **not** enter the definition of \(R_{\mathrm{nl}}\).

---

## 3. Lemmas

### Lemma UV (no free residual at \(\ell\ll R_{\mathrm{nl}}\))

**Statement.** Under A1–A2, residual field configurations of \(\chi\) that differ *within* a single nonlinear patch of size \(R_{\mathrm{nl}}\) are monitored by the same classical record \(m_p=\delta_m\big|_p\). Influence-functional / open-system logic then suppresses coherences between such configurations on timescales short compared with cosmic evolution when \(g\,\sigma_\delta\) is not parametrically tiny (see §5).  

**Consequence.** The *effective free residual* after decoherence is the **patch-averaged** field
\[
\chi_{\mathrm{eff}}(p)=\frac{1}{V_p}\int_p\chi\,.
\]
A counting cell \(\ell_*\ll R_{\mathrm{nl}}\) does **not** describe free residual DOF — those modes are decohered or absorbed into the classical matter record.  

**UV bound:** \(\ell_*\not\ll R_{\mathrm{nl}}\).

### Lemma IR (super-cells renormalize)

**Statement.** Suppose one claims a free residual cell \(\ell\gg R_{\mathrm{nl}}\). Under A1, the interaction on that super-cell is a sum of nearly independent contributions from \(N_p=(\ell/R_{\mathrm{nl}})^d\) nonlinear patches. The residual DOF that couple independently are therefore the **patch** modes, not a single coherent super-cell mode. Averaging independent patch residuals gives
\[
\sigma_{\mathrm{eff}}(\ell)
=\frac{\sigma(R_{\mathrm{nl}})}{\sqrt{N_p}}
=\sigma_{\mathrm{count}}(R_{\mathrm{nl}})\cdot\Bigl(\frac{R_{\mathrm{nl}}}{\ell}\Bigr)^{d/2},
\]
which is exactly the counting result **as if** the cell were \(R_{\mathrm{nl}}\) (the naive \(\sigma_{\mathrm{count}}(\ell)\) overcounts free residual variance).

**IR bound:** any claimed \(\ell_*\gg R_{\mathrm{nl}}\) **renormalizes** to effective grain \(R_{\mathrm{nl}}\).

### Theorem (sandwich uniqueness)

**Under A0–A4:**
\[
\boxed{\ell_*\sim R_{\mathrm{nl}}\qquad\text{(unique free residual counting scale up to \(\mathcal{O}(1)\) geometry).}}
\]

**\(\mathcal{O}(1)\) geometric factors** from the *same* filtered matter field (not free dials):

| Factor | Role | Typical value (this repo) |
|:-------|:-----|:--------------------------|
| \(R_{\mathrm{nl}}\) | Domain / filter / averaging cell | \(8.61\,\mathrm{Mpc}\) |
| \(r_{e,\delta}\) | \(\xi_\delta(r)/\xi_\delta(0)=1/e\) | \(\approx 14.6\,\mathrm{Mpc}\approx 1.7\,R_{\mathrm{nl}}\) |
| \(r_{e,\mathrm{mask}}\) | threshold mask \(m=\mathbf{1}\{\delta>1\}\) | \(\approx 9.5\,\mathrm{Mpc}\approx 1.1\,R_{\mathrm{nl}}\) |
| \(\ell_{\mathrm{sep}}\) | packing of \(\delta>1\) patches | \(\approx 15.9\,\mathrm{Mpc}\) |
| \(R_*\) | BBKS peak curvature (substructure) | \(\approx 1.58\,\mathrm{Mpc}\) — **inside** the domain; not a free residual cell under Lemma UV |

**Reading:** every independent geometric estimator of “how large is a nonlinear structure unit” lands in the **same decade** and within \(\mathcal{O}(1)\) of \(R_{\mathrm{nl}}\). The sandwich forbids both Planck and Hubble as free residual cells.

---

## 4. Executed numbers

```bash
python scripts/r1_sandwich_derivation.py
```

### 4.1 Matter correlation at \(R=R_{\mathrm{nl}}\)

| Quantity | Value |
|:---------|:------|
| \(R_{\mathrm{nl}}\) | \(8.610\,\mathrm{Mpc}\) |
| \(\sigma_0=\sqrt{\xi_\delta(0)}\) | \(1.000\) (by construction) |
| \(r_{e,\delta}\) (\(\xi/\xi_0=1/e\)) | \(\mathbf{14.56\,\mathrm{Mpc}}=1.69\,R_{\mathrm{nl}}\) |
| \(r_{e,\mathrm{mask}}\) (\(\delta_c=1\)) | \(\mathbf{9.53\,\mathrm{Mpc}}=1.11\,R_{\mathrm{nl}}\) |
| \(f(\delta>1)\) | \(0.159\) |
| \(\ell_{\mathrm{sep}}\) packing | \(15.9\,\mathrm{Mpc}\) |

**Key:** the mask correlation length — the natural support scale if residual lives on nonlinear edges — is **\(1.11\times R_{\mathrm{nl}}\)**, not a new free parameter.

### 4.2 Sandwich table (\(d=3\))

| Trial \(\ell\) | Regime | \(\sigma_{\mathrm{naive}}\) | \(\sigma_{\mathrm{eff}}\) after renorm |
|:---------------|:-------|:---------------------------|:--------------------------------------|
| \(\ll R_{\mathrm{nl}}\) (e.g. \(0.1\,\mathrm{Mpc}\)) | UV forbidden | tiny | free residual \(\to 0\) (decohered) |
| \(R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\) | **ALLOWED** | \(8.5\times 10^{-5}\) | \(8.5\times 10^{-5}\) |
| \(\ell_{\mathrm{sep}}\approx 16\,\mathrm{Mpc}\) | ALLOWED (\(\mathcal{O}(1)\)) | \(\sim 2\times 10^{-4}\) | same order as DESI ceiling |
| \(50\)–\(100\,\mathrm{Mpc}\) | IR renorm | larger naive | collapses toward \(\sigma(R_{\mathrm{nl}})/\sqrt{N_p}\) |
| \(L_H\) | IR renorm | \(1\) (absurd for BAO) | \(\sim 10^{-8}\) effective free residual |

### 4.3 Decoherence OOM

Model: \(\Gamma\sim g^2\sigma_\delta^2/\tau_c\), report \(\Gamma/H_0\).

| \(g\) | Fast bath \(\tau_c=R_{\mathrm{nl}}/c\) | Slow bath \(\tau_c=1/H_0\) |
|:------|:-------------------------------------|:--------------------------|
| \(1\) | \(\Gamma/H_0\sim 5\times 10^{2}\) | \(\sim 1\) |
| \(g_{\mathrm{work}}\approx 1.45\) | \(\sim 10^{3}\) | \(\sim 2\) |
| \(10^{-3}\) | \(\sim 5\times 10^{-4}\) | \(\sim 10^{-6}\) |

**Reading:** for couplings of order the working DESI bound (\(\lvert g\rvert\sim\mathcal{O}(1)\) under \(\lambda=g\sigma_{\mathrm{free}}\)), residual modes are decohered on \(\lesssim\) Hubble timescales in the fast-bath estimate — consistent with Lemma UV. Parametrically tiny \(g\) weakens decoherence (and also weakens the induced residual \(\lambda\)); that corner is constrained by requiring a measurable residual *or* is simply a null.

---

## 5. What is derived vs postulated

| Claim | Status |
|:------|:-------|
| \(\ell_*\sim R_{\mathrm{nl}}\) **if** A0–A4 | **Derived** (sandwich) |
| \(R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\) from \(\sigma(R)=1\) | **Computed** (matter geometry) |
| \(r_{e,\mathrm{mask}}\approx 1.1\,R_{\mathrm{nl}}\) | **Computed** |
| \(\sigma_{d=3}\approx 8.5\times 10^{-5}\) under DESI ceiling | **Computed** (counting) |
| Existence of \(\chi\) (A0) | **Postulate** |
| Coupling \(g\chi\delta_m\) (A1) | **Postulate** (strength bounded) |
| Matter classicality at \(\sigma\ge 1\) (A2) | **Standard input** |
| Full QFT on exact inhomogeneous metric | **Open** (rigorous upgrade path) |
| \(H_0\) tension from residual | **Excluded** at safe amplitude |

---

## 6. Relation to the open-kernel declaration

[`r1-open-kernel.md`](r1-open-kernel.md) stated:

> “What principle fixes a galactic/mesoscopic counting cell … remains open.”

**Update:**

| Layer | Status now |
|:------|:-----------|
| **Form of the principle** | Closed under A0–A4: sandwich uniqueness \(\ell_*\sim R_{\mathrm{nl}}\) |
| **Existence of the residual sector + coupling** | Still the load-bearing **postulates** (A0–A1) |
| **Geometry of \(R_{\mathrm{nl}}\)** | Closed (full \(\sigma(R)\)) |
| **Amplitude under counting** | Closed downstream |
| **Empirical ceiling on \(\lambda,g\)** | Working bound from sister DESI |

The open problem is **narrowed**: it is no longer “any mesoscopic scale could do”; it is “does nature implement a residual sector that couples locally to classical nonlinear matter?” — a sharper, falsifiable question.

---

## 7. Falsifiers of the sandwich itself

| If… | Then… |
|:----|:------|
| Residual is purely gravitational with **no** local coupling to \(\delta_m\) (A1 false) | UV/IR lemmas do not apply; grain scale undetermined by this argument |
| Matter never becomes classical on \(R_{\mathrm{nl}}\) (A2 false) | Pointer basis missing; decoherence argument fails |
| Free residual measured with correlation length \(\ll 1\,\mathrm{Mpc}\) or \(\gg 100\,\mathrm{Mpc}\) at \(\sigma\sim 10^{-4}\) | Tension with uniqueness band |
| Only way to fit data is to float \(\ell_*\) away from matter \(R_{\mathrm{nl}}\) after looking at DESI | Illegal under BOUNDARY; reject as free dial |

---

## 8. Claim checklist

| ID | Claim | Evidence |
|:---|:------|:---------|
| S1 | Axioms A0–A4 stated | this note |
| S2 | Lemma UV + Lemma IR | §3 |
| S3 | Theorem: \(\ell_*\sim R_{\mathrm{nl}}\) under A0–A4 | §3 |
| S4 | \(r_{e,\delta}\approx 1.7\,R_{\mathrm{nl}}\), \(r_{e,\mathrm{mask}}\approx 1.1\,R_{\mathrm{nl}}\) | script |
| S5 | Sandwich table UV/ALLOWED/IR | script |
| S6 | Decoherence OOM for \(g\sim\mathcal{O}(1)\) | script |

| Non-claim | |
|:----------|:--|
| N-S1 | Proof that SM+GR implies A0–A1 |
| N-S2 | Microscopic derivation of \(g\) |
| N-S3 | \(H_0\) from residual |
| N-S4 | Peer-reviewed status |

---

## 9. One-sentence status

> Under residual sector + local coupling to classical nonlinear matter + counting after decoherence, the free residual grain is **uniquely** \(\ell_*\sim R_{\mathrm{nl}}\) (sandwich); the geometry of that scale and the DESI-safe amplitude are computed — the remaining open is whether nature realises the residual sector, not which mesoscopic number to pick.

---

## Reproduce

```bash
python scripts/r1_sigma_R_full.py
python scripts/r1_t12_bbks_peaks.py
python scripts/r1_sandwich_derivation.py
pytest -q
```

---

*End of sandwich derivation note.*
