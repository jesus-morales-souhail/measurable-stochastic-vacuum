# Independent clustering lengths vs NP-A \(\ell_*\)

**Author:** Jesús Morales Souhail  
**ORCID / web:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)  
**Date:** July 2026  
**Status:** External-scale test — **not** a derivation of \(\ell_*\)  
**Code:** [`scripts/closed/ell_star_r0_peculiar.py`](../../scripts/closed/ell_star_r0_peculiar.py)  
**Note:** This is not a re-display of the MW–Andromeda / Virgo tables ([`ell-star-external-scales.md`](ell-star-external-scales.md)).

---

## Abstract

The open R1 question is whether a **mesoscopic** counting cell \(\ell_*\) is fixed by physics. NP-A gives the **arithmetic** value
\[
\ell_*^{\mathrm{NP\text{-}A}}=2.0646\,\mathrm{Mpc}
\quad(d=3,\ \sigma=10^{-5},\ H_0=67.4).
\]
Here I compare that number to **independent, pre-existing** scales of **galaxy clustering** and **peculiar velocities**, computed without targeting \(2.06\,\mathrm{Mpc}\).

**Result:** standard \(L_*\) galaxy correlation lengths are
\[
r_0(L_*)\sim 5\text{–}6\,h^{-1}\mathrm{Mpc}
\approx 7.4\text{–}8.9\,\mathrm{Mpc}
\quad(h=0.674),
\]
a factor \(\sim 3.5\)–\(4.3\) **above** NP-A. Mean inter-galaxy separation \(n_*^{-1/3}\) is \(\sim 6.9\,\mathrm{Mpc}\). Peculiar-velocity coherence / bulk-flow scales are **tens to hundreds** of \(h^{-1}\mathrm{Mpc}\). **None** independently hits \(2.06\,\mathrm{Mpc}\).

So the open kernel remains: arithmetic without an external prior at the NP-A row. The DESI-ceiling \(d=3\) cell (\(\approx 12.6\,\mathrm{Mpc}\)) sits nearer \(R_8\) and the \(r_0\) decade, but that is a **different \(\sigma\) row** and still not a principle.

---

## 1. What is new here

| Already done (previous notes) | This note |
|:------------------------------|:----------|
| MW–Andromeda, Virgo radii vs NP-A | **No** (not repeated as “new”) |
| \(R_8\) vs DESI-ceiling cell | Context only |
| **Galaxy \(r_0\) from 2PCF** | **Yes** |
| **\(n^{-1/3}\)** | **Yes** |
| **Peculiar-velocity scale class** | **Yes** |

---

## 2. Programme anchors (for comparison only)

| Anchor | Value [Mpc] | Origin |
|:-------|:------------|:-------|
| NP-A \(\ell_*\) | \(2.0646\) | Counting inverse \(\sigma=10^{-5}\), \(d=3\) |
| DESI-ceiling \(\ell_*\) (\(d=3\)) | \(12.557\) | Counting inverse \(\sigma=1.5\times 10^{-4}\) |
| \(R_8=8/h\) | \(11.869\) | Definition |

---

## 3. Galaxy correlation length \(r_0\)

Power-law model \(\xi_{gg}(r)=(r/r_0)^{-\gamma}\) (\(\gamma\sim 1.7\)–\(1.9\)): \(r_0\) is the scale where \(\xi\sim 1\).

| Sample class | \(r_0\) [\(h^{-1}\) Mpc] | \(r_0\) [Mpc] at \(h=0.674\) | vs NP-A | vs \(R_8\) |
|:-------------|:------------------------|:-----------------------------|:--------|:-----------|
| \(L_*\) / main (low) | \(5.0\) | \(7.42\) | \(+259\%\) | \(-37\%\) |
| \(L_*\) / main (high) | \(6.0\) | \(8.90\) | \(+331\%\) | \(-25\%\) |
| Luminous (upper OOM) | \(8.0\) | \(11.87\) | \(+475\%\) | \(\sim 0\%\) |

**Sources (SDSS clustering, luminosity/color dependence):**  
Zehavi et al., arXiv:[1005.2413](https://arxiv.org/abs/1005.2413); arXiv:[astro-ph/0408569](https://arxiv.org/abs/astro-ph/0408569).  
Those works measure \(w_p(r_p)\) and report correlation amplitudes that, in the classical power-law language used across the literature, place **typical \(L_*\) samples near \(r_0\sim 5\)–\(6\,h^{-1}\mathrm{Mpc}\)**; brighter/redder samples sit higher. I use that **established range**, not a fit to NP-A.

**Verdict:** \(r_0(L_*)\) is **not** \(\approx 2.06\,\mathrm{Mpc}\). It is several times larger, in the same **broad decade** as \(R_8\) / DESI-ceiling cell, not the Euclid-target NP-A cell.

---

## 4. Mean inter-galaxy separation

For a characteristic abundance \(n_*\sim 0.01\,h^{3}\mathrm{Mpc}^{-3}\) (order of \(L_*\) space density),
\[
n_*^{-1/3}\approx 4.64\,h^{-1}\mathrm{Mpc}\approx 6.89\,\mathrm{Mpc}.
\]
| vs NP-A | vs \(R_8\) |
|:--------|:-----------|
| \(+234\%\) | \(-42\%\) |

Again: **not** an independent hit on \(2.06\,\mathrm{Mpc}\).

---

## 5. Peculiar-velocity coherence

Bulk-flow / Cosmicflows-type analyses discuss velocity field coherence and convergence on scales of order **\(50\)–\(150\,h^{-1}\mathrm{Mpc}\)** (\(\sim 75\)–\(220\,\mathrm{Mpc}\) at \(h=0.674\)) — far above NP-A. There is **no** single \(r_0\)-like number that lands on \(2\,\mathrm{Mpc}\).

---

## 6. Machine output

```bash
python scripts/closed/ell_star_r0_peculiar.py
```

---

## 7. Implications for the open kernel

| Statement | Status |
|:----------|:-------|
| NP-A \(2.06\,\mathrm{Mpc}\) is clean counting arithmetic | True |
| \(r_0\), \(n^{-1/3}\), \(v_{\mathrm{pec}}\) independently equal NP-A | **False** (this note) |
| \(r_0\) / \(R_8\) / DESI-ceiling cell share a \(\sim 10\,\mathrm{Mpc}\) class | Roughly true; **not** a derivation |
| Principle fixing \(\ell_*\) | **Still absent (declared)** |
| Scope if \(\ell_*\) ever derived | Residual / slip band — **not** \(9\%\) \(H_0\) |

**Illegal:** after seeing \(2.06\), hunt a rare faint subsample with \(r_0\sim 1.4\,h^{-1}\mathrm{Mpc}\) and call it confirmation.  
**Legal next step:** pre-register a sample definition (e.g. DESI BGS/LRG volume-limited cut) and measure \(r_0\) **blind**, then compare once.

---

## 8. Claim checklist

| ID | Claim | Evidence |
|:---|:------|:---------|
| R0-1 | \(r_0(L_*)\sim 5\)–\(6\,h^{-1}\mathrm{Mpc}\to 7.4\)–\(8.9\,\mathrm{Mpc}\) at \(h=0.674\) | literature range + conversion |
| R0-2 | That range is \(\times 3.5\)–\(4.3\) above NP-A | arithmetic |
| R0-3 | \(n_*^{-1/3}\sim 6.9\,\mathrm{Mpc}\) ≠ NP-A | arithmetic |
| R0-4 | \(v_{\mathrm{pec}}\) coherence ≫ NP-A | scale class |
| R0-5 | Open kernel still open | programme status |
