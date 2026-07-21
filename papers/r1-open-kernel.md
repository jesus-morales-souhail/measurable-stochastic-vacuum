# The open kernel of R1: measured walls versus an undeclared counting cell

**Author:** Jesús Morales Souhail  
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Email:** jmskjym@gmail.com  
**Programme:** [measurable-stochastic-vacuum](https://github.com/jesus-morales-souhail/measurable-stochastic-vacuum)  
**Date:** July 2026  
**Status:** Publication-oriented programme note — **not** a derivation of \(\ell_*\); **not** peer reviewed  
**Verified kinematics:** [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) · `pytest -q`  
**Parent WP1 note:** [`r1-counting-principle.md`](r1-counting-principle.md)  
**Sister empirical bound:** \(\sigma_X < 1.5\times 10^{-4}\) (95% CL, OU kernel) in [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)

---

## Abstract

This note separates two kinds of incompleteness in the stochastic vacuum programme, which are often conflated.

1. **Measured walls.** Candidate mechanisms that start from a Planck / Sorkin seed \(\sigma_0\sim 10^{-61}\) and try to reach telescope-band residuals \(\sim 10^{-5}\)–\(10^{-4}\) have been audited with numbers: soft squeeze requires \(r\sim 64\); geometric path accumulation supplies only \(\sqrt{N}=\mathcal{O}(10\)–\(10^{2})\); soft avalanche gains are \(\mathcal{O}(1)\). These channels are not “still open.” They are **insufficient by measured factors**.

2. **Open kernel (load-bearing).** Under the counting hypothesis
   \(N_{\mathrm{eff}}=(L/\ell_*)^d\), \(\sigma_{0,\mathrm{eff}}=(\ell_*/L)^{d/2}\),
   a residual already in the \(10^{-5}\) band requires a **mesoscopic** cell \(\ell_*\sim 0.04\)–\(14\,\mathrm{Mpc}\) (\(d\in\{2,3,4\}\)), not \(L_P\). The programme states, and does not fill:

   > What principle fixes a galactic/mesoscopic counting cell for the DE sector, distinct from the Planck/holographic cell?

   That question is **declared absent**, not “tried and failed.”

We record criteria for what would count as a principle, list hypothesis classes R1a–R1d (including a **nonlinear structure scale** class R1d that sits numerically near the existing landscape), state illegal moves (no DESI-tuned \(\ell_*\); no S\(_8\)-tuned \(\ell_*\)), and give a posteriori falsifiers. **We do not claim** that \(\ell_*\) is \(R_8\), that S\(_8\) is explained, or that any R1 class is derived.

---

## 1. Why this distinction is publication-relevant

The sister DESI corpus closes **empirical** statements: null residual under the stated OU/QNM kernel, \(\sigma_X < 1.5\times 10^{-4}\) (95% CL), coherent tachyonic growth excluded, linear amplification of a pure Sorkin seed closed as an amplification gap.

The theory repository closes **kinematics**: counting inversion, soft open gain bounds, local slip under stated GR assumptions, path \(\mathrm{RMS}=s\sqrt{N}\). Automated gate: `pytest -q`.

What remains for a positive detection claim is not another soft amplifier. It is a **principle that fixes the counting cell**, or a derived hard open map (not constructed). Mixing “we failed to amplify Planck” with “we never derived the grain” misreports the map: the first is a wall; the second is the only soft-regime door still marked *unknown*.

---

## 2. Two kinds of incompleteness

| Type | Definition | Status language | Role in the map |
|:-----|:-----------|:----------------|:----------------|
| **Measured wall** | A candidate mechanism was specified and checked; the required gain or parameter lies outside the soft / derived regime | *Proven insufficient* (height measured) | Do not dig deeper for free gain |
| **Open kernel** | The ingredient was never derived; kinematics wait on it | *Absent (declared)* | Only load-bearing soft-regime gap |

**Amplification gap (wall class):** there is no free gain factor that multiplies \(\sigma_0\sim 10^{-61}\) into \(10^{-5}\) under audited soft channels.  
**R1 kernel (open class):** the *starting grain* may not be Planckian. If a principle sets \(\ell_*\) mesoscopic, \(\sigma_{0,\mathrm{eff}}\) already sits in the telescope band **without** \(r\sim 64\).

These are not two incomplete answers to the same question. They are different questions.

---

## 3. Walls already measured (not open)

All entries below are verified algebraically or numerically in-repo or in the sister amplification-route scans. Full identities: [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md); sister Act III: `papers/amplification-gap.md`.

| Candidate rescue of a pure Sorkin seed | What was checked | Result |
|:---------------------------------------|:-----------------|:-------|
| Soft squeeze \(G_O=e^{2r}\) alone | \(r\) such that \(e^{2r}\sigma_0=10^{-5}\) | \(r\sim 64\) — new scale, not soft open |
| Path accumulation \(\sqrt{N_{\mathrm{pat}}}\) alone | \(N_{\mathrm{pat}}=\chi/\ell_*\) for Mpc cells, Gpc paths | \(\sqrt{N}=\mathcal{O}(10\)–\(10^{2})\); need \(\sim 10^{59}\) |
| Soft open **and** path stacked | Combined map on Sorkin | Still \(\mathrm{RMS}\ll 10^{-50}\) |
| Late freeze \(\Delta x=\mathcal{O}(1)\) as “\(e^{60}\)” | Sister Route 2 MC | Freeze/restore gain \(=1\) |
| Soft double-well avalanche | Sister Route 3 | Gain \(\mathrm{p95}/\sigma\sim 2\) |
| Local slip with BAO-bounded \(\sigma\) | \(\lvert\gamma-1\rvert=2\varepsilon\sigma(\rho_X/\rho_m)/\lvert\delta_m\rvert\) | \(\mathcal{O}(10^{-4})\) under DESI ceiling — amplitude starved |
| Wrong-scale optics / tesseract \(B_4\) | Exploratory sister notes | Closed as wrong operator / wrong scale |

**Reading:** each row is a **wall with measured height**. Publishing “maybe soft amplification still works” without a new derived map would contradict the verified core.

---

## 4. Open kernel (load-bearing)

### 4.1 Counting hypothesis (verified kinematics)

\[
N_{\mathrm{eff}}=\Bigl(\frac{L}{\ell_*}\Bigr)^{d},\qquad
\sigma_{0,\mathrm{eff}}=\frac{1}{\sqrt{N_{\mathrm{eff}}}}=\Bigl(\frac{\ell_*}{L}\Bigr)^{d/2},\qquad
\ell_*=L\,\sigma_{0,\mathrm{eff}}^{2/d}.
\]

Sorkin is the special case \(d=2\), \(\ell_*=L_P\), \(L=L_H\): \(\sigma_0\sim 10^{-61}\).

### 4.2 Landscape (verified inverse)

With \(L=L_H=c/H_0\) (\(H_0=67.4\,\mathrm{km\,s^{-1}Mpc^{-1}}\)) and target \(\sigma_{0,\mathrm{eff}}=10^{-5}\):

| \(d\) | \(\ell_*\) | Character |
|:------|:-----------|:----------|
| 2 | \(\approx 0.044\,\mathrm{Mpc}\) | mesoscopic |
| 3 | \(\approx 2.07\,\mathrm{Mpc}\) | group / small-cluster scale |
| 4 | \(\approx 14.1\,\mathrm{Mpc}\) | large-scale structure scale |

For the a-posteriori DESI residual ceiling \(\sigma=1.5\times 10^{-4}\) at \(d=3\): \(\ell_*\approx 12.6\,\mathrm{Mpc}\).

**Verified reading:** telescope-band residuals from counting alone require a **mesoscopic DE counting cell**, not a Planck cell. The ratio \(\ell_*/L_P\sim 10^{56}\) is not a free multiplier; it is the statement that the two cells are different counting objects.

### 4.3 Declared absence

> What principle fixes a galactic/mesoscopic counting cell for the DE sector, distinct from the Planck/holographic cell?

**R1 status:** landscape derived; principle fixing \(\ell_*\) **absent (declared)** ([`r1-counting-principle.md`](r1-counting-principle.md) §4).  
Closing WP1 requires one of the hypothesis classes below **fully derived**, not dialed.

---

## 5. What would count as a principle

A candidate \(P\) closes the open kernel only if it satisfies **all** of:

| # | Requirement |
|:--|:------------|
| P1 | \(P\) predicts \(\ell_*\) or \(N_{\mathrm{eff}}\) (or a sharp prior band) from stated microphysics / symmetry / IR dynamics |
| P2 | The prediction is **independent** of DESI residual likelihoods and of S\(_8\) tension papers used as targets |
| P3 | \(\sigma_{0,\mathrm{eff}}=(\ell_*/L)^{d/2}\) is then a **downstream** number, not an input |
| P4 | Structural zeros are stated: Planck cell \(\Rightarrow\) null under soft dynamics; \(\ell_*\sim L_H\Rightarrow\sigma\sim 1\) (absurd for BAO smoothness) |
| P5 | DESI \(\sigma_X\) and growth/S\(_8\) enter only **a posteriori** (compatible / null / tension) |
| P6 | Falsifiers are explicit ([`wp5-falsification.md`](wp5-falsification.md)) |

Anything that chooses \(\ell_*\) so that \(\sigma\) “enters Euclid” or “matches \(R_8\) after looking at S\(_8\)” fails P2 and is out of scope ([`BOUNDARY.md`](../BOUNDARY.md)).

---

## 6. Hypothesis classes (not yet derived)

| ID | Sketch | Open problem that remains |
|:---|:-------|:--------------------------|
| **R1a** | Local causal set / meso \(N_{\mathrm{eff}}\) | What sets the DE correlation scale? |
| **R1b** | IR cutoff of a vacuum sector | Derive \(\ell_*\) from an action |
| **R1c** | Unimodular / SDiff grain | Why cosmological rather than Planck? |
| **R1d** | Nonlinear structure scale | Why would the DE residual sector count cells at \(R_{\mathrm{nl}}\) / \(R_8\) / \(k_{\mathrm{nl}}^{-1}\)? |

R1d is singled out **only** because its natural scale sits in the same mesoscopic band already forced by the counting inverse (§4.2). That is a **scale coincidence under the counting hypothesis**, not a derivation.

### 6.1 R1d — nonlinear structure scale (hypothesis class)

**Statement (conditional):**  
*If* the effective counting cell of the DE residual sector is set by the scale at which cosmic structure becomes nonlinear — denoted \(R_{\mathrm{nl}}\) and often summarised by \(R_8\equiv 8\,h^{-1}\mathrm{Mpc}\) — *then* \(\sigma_{0,\mathrm{eff}}\) is fixed once \(d\) and \(L\) are chosen, without soft amplification of a Planck seed.

**Not claimed:** that DE “knows” about galaxies; that S\(_8\) is solved; that \(d=3\) is mandatory.

### 6.2 Scale table (verified arithmetic, fiducial \(H_0=67.4\))

Define the conventional length \(R_8=8/h\,\mathrm{Mpc}\) with \(h=H_0/100\), so \(R_8\approx 11.87\,\mathrm{Mpc}\) at this \(H_0\).

| Input | Output under counting | Comment |
|:------|:----------------------|:--------|
| Fix \(\sigma=10^{-5}\), \(d=3\) | \(\ell_*\approx 2.07\,\mathrm{Mpc}\) | Below \(R_8\) |
| Fix \(\sigma=10^{-5}\), \(d=4\) | \(\ell_*\approx 14.1\,\mathrm{Mpc}\) | Near \(R_8\) |
| Fix \(\sigma=1.5\times 10^{-4}\), \(d=3\) | \(\ell_*\approx 12.56\,\mathrm{Mpc}\) | Within \(\sim 6\%\) of \(R_8\) |
| Fix \(\ell_*=R_8\), \(d=3\) | \(\sigma\approx 1.38\times 10^{-4}\) | Sits at DESI ceiling order |
| Fix \(\ell_*=R_8\), \(d=4\) | \(\sigma\approx 7.12\times 10^{-6}\) | Near \(10^{-5}\) band |

Reproducible: `python scripts/r1_open_kernel_scales.py` · identities in `scripts/lib_verified.py`.

**Legitimate use of the table:** motivate *which* principle classes are worth deriving (those that land \(\ell_*\) near Mpc–tens of Mpc).  
**Illegitimate use:** pick the row that matches DESI or S\(_8\) and call it a principle.

### 6.3 S\(_8\) / growth (non-claim with a shared target)

The S\(_8\) tension lives at the same **class of scales** as the mesoscopic counting landscape. That is a reason to *investigate* a joint physical map; it is **not** a map.

A publishable link would require at least:

1. a principle \(P\) fixing \(\ell_*\) (or a transfer function) without tension data as input;  
2. an operator from residual grain \(\sigma\) to \(P(k)\) or to the growth function;  
3. a posteriori comparison to S\(_8\) and to \(\sigma_X\).

Until (1)–(2) exist, **S\(_8\) is not a claim of this repository**. The honest status is: two open questions may share a scale; they do not yet share a theory.

---

## 7. Illegal moves (BOUNDARY)

| Move | Why forbidden |
|:-----|:--------------|
| Fit \(\ell_*\) or \(r\) to DESI BAO residuals | Turns a null bound into a detection dial |
| Fit \(\ell_*\) to \(R_8\) after inspecting S\(_8\) | Same dial, different dataset |
| Treat \(\ell_*/L_P\sim 10^{56}\) as a free gain | Undeclared free parameter (amplification gap) |
| Stack soft \(r\sim\mathcal{O}(1)\) and path \(\sqrt{N}\) as if they rescued Sorkin | Contradicts verified combined null |
| Cite this note as “\(\ell_*=R_8\) is derived” | It is not |

**Legal a-posteriori use:** given a derived \(\sigma_{0,\mathrm{eff}}\),

- in \([10^{-5},\,1.5\times 10^{-4}]\) → compatible band; Euclid can decide;  
- \(\ll 10^{-5}\) → predict structural null under soft dynamics;  
- \(\gg 1.5\times 10^{-4}\) without damping → tension with sister bound.

---

## 8. Falsifiers (once a principle exists)

From [`wp5-falsification.md`](wp5-falsification.md), specialised to R1:

| If principle \(P\) implies… | Then… |
|:----------------------------|:------|
| \(\ell_*\sim L_P\) | Soft-regime telescope null is a **theorem**; no detection claim |
| \(\ell_*\sim L_H\) | \(\sigma\sim 1\): excluded by BAO smoothness |
| Fixed \(\ell_*\) with \(\sigma_{0,\mathrm{eff}}\gg 1.5\times 10^{-4}\) and no damping | Tension with sister DESI bound |
| Fixed \(\ell_*\) in the mesoscopic band | Residual amplitude is a **prediction**; Euclid/DESI test a posteriori |
| Any of R1a–R1d only after seeing data | Reject under self-shielding axioms (overclaim death) |

---

## 9. Orthogonal channel (recorded, out of programme scope)

A genuinely different probe of spacetime granularity is **energy-dependent time-of-flight** of high-energy photons from distant GRBs (propagation, not vacuum gravitation). Public Fermi-LAT GRB catalogues allow such tests without a new cosmological MCMC.

That channel does **not** close R1: it does not fix \(\ell_*\) for the DE residual sector. It is listed here only to prevent category errors — a change of terrain, not a substitute for the open kernel. If pursued, it should live under a separate claim boundary.

---

## 10. Publication stance

| May be published as result | Must not be published as result |
|:---------------------------|:--------------------------------|
| Walls of §3 with measured heights | “Soft amplification can still reach Euclid from Sorkin” without a new derived map |
| Counting landscape and structural zeros (§4) | “\(\ell_*\) is galactic” as a derived fact |
| Criteria P1–P6 and illegal moves | DESI- or S\(_8\)-tuned \(\ell_*\) |
| R1d as a **hypothesis class** with scale table (§6) | “S\(_8\) explained by stochastic DE” |
| Declared open kernel sentence | Closure of WP1 without a principle |

**One-sentence summary for referees:**

> Soft amplifiers of a Planck counting seed are closed by measurement; the remaining soft-regime question is whether a mesoscopic DE counting cell is fixed by a principle — a question the programme states and has not answered.

---

## 11. Reproducibility

```bash
pip install -r requirements.txt
pytest -q
python scripts/r1_counting_landscape.py
python scripts/r1_open_kernel_scales.py
python scripts/lib_verified.py
```

**Related documents:**  
[`r1-counting-principle.md`](r1-counting-principle.md) · [`NARROW_PATH.md`](NARROW_PATH.md) · [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) · [`wp5-falsification.md`](wp5-falsification.md) · [`FOR_REFEREES.md`](FOR_REFEREES.md) · sister `papers/amplification-gap.md`

---

*End of R1 open-kernel note.*
