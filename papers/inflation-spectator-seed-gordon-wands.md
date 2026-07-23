# Inflationary spectator seed for DE: Gordon & Wands (2005), revalidated for this programme

**Author:** Jesús Morales Souhail  
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Date:** July 2026  
**Status:** Literature revalidation note — **respectful external theory**, not a detection claim  
**Primary reference:** C. Gordon & D. Wands, *The amplitude of dark energy perturbations*, Phys. Rev. D **71**, 123505 (2005); arXiv:[astro-ph/0504132](https://arxiv.org/abs/astro-ph/0504132)  
**Related programme notes:** [`amplification-gap` sister](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou/blob/main/papers/amplification-gap.md) · [`r1-open-kernel.md`](r1-open-kernel.md) · [`NARROW_PATH.md`](NARROW_PATH.md)  
**Code (arithmetic of their eqs only):** [`scripts/gordon_wands_factor45.py`](../scripts/gordon_wands_factor45.py)

---

## Abstract

Gordon & Wands (2005) is a serious PRD calculation of **dark-energy isocurvature** seeded by a **light spectator field during inflation**, using standard cosmological perturbation theory (separate-universe / large-scale limit). It must **not** be dismissed by equating their “tachyonic amplification” with the excluded coherent GPE/tachyonic **BAO residual** of the sister DESI corpus.

**Verified from the paper (not from memory of the word “tachyonic”):**

1. **Seed is not Sorkin.** For a light canonical field during inflation they use  
   \(\mathcal{P}_Q^{1/2}=H_{\mathrm{inf}}/(2\pi)\) [their Eq. (12)], not \(\sigma_0=L_P/L_H\sim 10^{-61}\).  
2. **Frozen case is insufficient *for their target*** (large DE density contrast for the low CMB quadrupole), not “insufficient by \(10^{56}\).”  
3. **Growth factor needed after inflation:** \(\delta Q_f/\delta Q_i>45\) [Eq. (27)], equivalently \(\phi_f/\phi_i>45\) [Eq. (32)] in their Mexican-hat construction — **order forty-five**, not \(10^{56}\).  
4. The factor \(\sim 45\) follows from the tension between the inflation energy needed for a frozen light field to meet their amplitude [Eq. (25)] and the **then-current** tensor bound [Eq. (26)].

**For this programme:** this is the first literature pathway we have revalidated whose “how much is missing” is **not** \(G_{\mathrm{Euclid}}\sim 10^{56}\), but **depends on \(H_{\mathrm{inf}}\) (unmeasured) and on a derived post-inflation map**. It is a **different starting physics**, not a soft rescue of holographic Sorkin counting. It does **not** automatically become a DESI BAO residual prediction without a full re-derivation of seed → residual → covariance.

**Next step (done as OOM atlas):** modern \(r\) → \(\delta Q\) → \(\sigma_\rho(\varepsilon_Q,A)\) vs residual band —  
[`inflation-spectator-residual-atlas.md`](inflation-spectator-residual-atlas.md).
---

## 1. Respect and scope

| | Gordon & Wands (2005) | This programme (three repos) |
|:--|:---------------------|:----------------------------|
| **Goal in the paper** | Large **isocurvature** DE perturbations anti-correlated with curvature, aimed at the **low CMB TT quadrupole** | Bound / structure of **late-time residual** noise on BAO distances; amplification gap for **Sorkin seed** |
| **Seed** | Light field: \(\delta Q\sim H_{\mathrm{inf}}/(2\pi)\) | Motivational UV: \(\sigma_0\sim 10^{-61}\) (holographic) |
| **“Not enough if frozen”** | Not enough for **their** \(\delta\rho_Q/\rho_Q\sim 6\times 10^{-4}\) target without growth or high \(H_{\mathrm{inf}}\) | Soft maps cannot lift Sorkin to \(10^{-5}\)–\(10^{-4}\) |
| **Amplification** | Derived radial roll, \(\phi_f/\phi_i>45\) | Soft \(r\sim 64\), path \(\sqrt{N}\sim 10\)–\(100\), excluded GPE, … |

Equating the two “tachyonic” words was a **category error** (same name, different seed and different observable). This note corrects that.

---

## 2. What the paper actually does (verified equations)

### 2.1 Light spectator during inflation

If the quintessence is light,
\[
\frac{\partial^2 V_Q}{\partial Q^2}\ll H_{\mathrm{inf}}^2,
\]
it acquires the standard spectrum [Eq. (12)]
\[
\mathcal{P}_Q^{1/2}(k)=\frac{H_{\mathrm{inf}}}{2\pi}.
\]
This is the **same structural mechanism** that seeds adiabatic curvature for the CMB when the inflaton fluctuates — textbook, not an ad hoc late-time dial.

### 2.2 Their amplitude target (not DESI \(\sigma_X\))

From the low-quadrupole motivation and adiabatic violation they work with a large fractional DE density contrast of order [Eq. (15)]
\[
\frac{1}{\rho_Q}\mathcal{P}_{\rho_Q}^{1/2}=6\times 10^{-4}.
\]
Under slow-roll / potential domination this becomes a lower bound on field perturbations during DE domination [Eq. (24)]
\[
\mathcal{P}_Q^{1/2}>4\times 10^{-4}\,M_p
\]
(for \(\epsilon_Q<1\)).

### 2.3 Frozen case vs tensors (why “not of sufficient size”)

If \(\delta Q\) is constant from inflation to DE domination, Eqs. (24)+(12) force a **high** inflation scale [Eq. (25)]
\[
V_{\mathrm{inf}}^{1/4}>7\times 10^{-2}\,M_p,
\]
while then-current tensor limits gave [Eq. (26)]
\[
V_{\mathrm{inf}}^{1/4}<10^{-2}\,M_p\quad(95\%~\mathrm{CL}).
\]
Hence frozen inflationary DE perturbations are **not of sufficient size for their quadrupole target without either high \(H_{\mathrm{inf}}\) (excluded then) or post-inflation growth**.

### 2.4 Factor \(>45\) (verified arithmetic)

Because \(\delta Q\sim H_{\mathrm{inf}}/(2\pi)\) and \(H\sim V^{1/2}/(\sqrt{3}M_p)\), the ratio of energy-scale bounds \(\sim 7\) becomes a field-perturbation ratio of order \(7^2\sim 50\). The paper states explicitly [Eq. (27)]
\[
\frac{\delta Q_f}{\delta Q_i}>45,
\]
and with \(Q=\phi\theta\), \(\delta\theta\) frozen [Eq. (32)]
\[
\frac{\phi_f}{\phi_i}>45.
\]
**Reproduce:** `python scripts/gordon_wands_factor45.py`.

### 2.5 Tachyonic / Mexican-hat implementation (their proposal)

Complex field; radial \(\phi\) in a Mexican-hat potential [Eq. (37)]; trapped near the top during inflation; rolls to the minimum after inflation, amplifying angular / quintessence perturbations. DE today is a PNGB-like angular direction.

This is a **derived** post-inflation map of \(\mathcal{O}(10^{1}\)–\(10^{2})\) growth — not a free \(10^{56}\) dial, and **not** the sister-repo excluded coherent GPE residual on BAO.

They also discuss difficulties (radial field as inflaton produces uncorrelated curvature; variable-decay reheating for anti-correlation). Those caveats are **in the paper**; we do not paper over them.

---

## 3. Relation to this programme’s amplification gap

| Question | Sorkin soft gap (this programme) | Gordon & Wands spectator |
|:---------|:---------------------------------|:-------------------------|
| What is fixed? | \(\sigma_0\sim 10^{-61}\) if holographic count is assumed | \(H_{\mathrm{inf}}\) **not** fixed by horizon-area counting |
| Missing factor if frozen at “wrong” scale | \(G_{\mathrm{Euclid}}\sim 10^{56}\), \(G_{\mathrm{DESI}}\sim 10^{57}\) | \(\sim 45\) for **their** CMB-isocurvature target under 2005 tensor bound |
| Soft open \(r\sim\mathcal{O}(1)\) | Useless vs \(10^{56}\) | Not their mechanism |
| Path \(\sqrt{N}\) | \(\mathcal{O}(10\)–\(100)\) | Not their mechanism |
| Structural category | Amplify or redefine **counting cell** (R1) | **Change UV seed physics** (inflation spectator) |

**One-sentence distinction:**

> Closing the Sorkin gap asks for a free factor \(\sim 10^{56}\) on a fixed holographic seed; Gordon & Wands never accept that seed — they start from inflationary vacuum fluctuations of a light DE field, so the open number is \(H_{\mathrm{inf}}\) (and a \(\mathcal{O}(10^{1}\)–\(10^{2})\) derived roll), not \(L_P/L_H\).

---

## 4. What would be required to *use* this for DESI residuals (honest checklist)

This note does **not** claim the checklist is done.

| # | Requirement | Status |
|:--|:------------|:-------|
| I1 | Assume (or derive) that the DE sector was a **light field during inflation** | Assumption — serious, not automatic |
| I2 | Fix or bound \(H_{\mathrm{inf}}\) from tensors / \(r\) (modern limits, not only 2005) | **Open** (science has not measured \(H_{\mathrm{inf}}\)) |
| I3 | Map \(\delta Q\to\delta\rho_Q/\rho_Q\to\) **BAO residual kernel** \(\sigma_X\) (not only CMB isocurvature) | **Not done here** |
| I4 | Covariance on DESI BAO distances under that map; re-run sister likelihood | **Not done** |
| I5 | Check DESI ceiling \(\sigma_X<1.5\times 10^{-4}\) a posteriori | Only after I3–I4 |
| I6 | Do **not** smuggle Sorkin \(\sigma_0\) back in as the seed | Label rule |

Until I3–I4 exist, Gordon & Wands is a **validated literature door**, not a DESI claim of this repo.

---

## 5. Modern context (pointers, not re-derived)

- Tensor bounds have evolved since 2005; any **numerical** update of Eqs. (25)–(27) must use current \(r\) / \(V_{\mathrm{inf}}\) limits, not only the paper’s \(V^{1/4}<10^{-2}M_p\).  
- Spectator / quintessence-during-inflation literature is larger than one paper; Gordon & Wands is the **worked PRD example** we revalidated equation-by-equation.  
- Sister DESI exclusion of **coherent tachyonic residual growth on BAO** remains; it does **not** automatically exclude a **post-inflation radial roll** of a complex PNGB sector aimed at isocurvature.

---

## 6. Claim checklist

| ID | Claim | Evidence |
|:---|:------|:---------|
| GW1 | Paper uses \(\mathcal{P}_Q^{1/2}=H_{\mathrm{inf}}/(2\pi)\) for light field | Eq. (12) |
| GW2 | Frozen case insufficient for **their** target under **their** tensor bound | Eqs. (24)–(26); abstract / §8 |
| GW3 | Required growth \(\delta Q_f/\delta Q_i>45\) | Eq. (27); script |
| GW4 | Mexican-hat roll implements \(\phi_f/\phi_i>45\) | Eqs. (31)–(32), (37) |
| GW5 | Seed is **not** Sorkin \(\sigma_0\sim 10^{-61}\) | Entire construction |

| Non-claim | |
|:----------|:--|
| N-GW1 | Gordon & Wands **solves** DESI residual detectability |
| N-GW2 | Their tachyonic roll = sister GPE BAO residual (excluded) |
| N-GW3 | \(H_{\mathrm{inf}}\) is measured and large enough |
| N-GW4 | Factor 45 applies unchanged to \(\sigma_X\) BAO kernel without re-derivation |
| N-GW5 | This replaces R1 open kernel without new work |

---

## 7. Programme stance (after revalidation)

1. **Respect:** Gordon & Wands is competent standard theory; “same wall as Sorkin \(10^{56}\)” was **false**.  
2. **Category:** open question of type **“\(H_{\mathrm{inf}}\) + derived \(\mathcal{O}(10^{1}\)–\(10^{2})\) map”**, not type **“free \(10^{56}\) on holographic seed.”**  
3. **Next science (if pursued):** modern tensor prior → \(\delta Q\) band → explicit map to residual / slip operators → a posteriori DESI.  
4. **Until then:** cite this note as **literature door + arithmetic check**, not as a new DESI result.

---

## 8. Reproduce

```bash
cd measurable-stochastic-vacuum
python scripts/gordon_wands_factor45.py
pytest -q  # includes factor-45 arithmetic test
```

**Paper PDF:** https://arxiv.org/pdf/astro-ph/0504132

---

*End of Gordon & Wands revalidation note.*
