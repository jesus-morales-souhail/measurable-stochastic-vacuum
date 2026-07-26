# Clustering lengths and peculiar-velocity scales vs NP-A $\ell_{\ast}$

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail) · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
July 2026

External-scale comparison — not a derivation of $\ell_{\ast}$.  
Code: [`scripts/closed/ell_star_r0_peculiar.py`](../../scripts/closed/ell_star_r0_peculiar.py)  
MW–Andromeda / Virgo tables: [`ell-star-external-scales.md`](ell-star-external-scales.md).

---

## Abstract

NP-A gives the arithmetic value

$$
\ell_{\ast}^{\mathrm{NP\text{-}A}}=2.0646\,\mathrm{Mpc} \quad(d=3,\ \sigma=10^{-5},\ H_0=67.4).
$$

I compare it to independent galaxy clustering and peculiar-velocity scales, without fitting them to $2.06\,\mathrm{Mpc}$.

Standard $L_*$ correlation lengths are

$$
r_0(L_*)\sim 5\text{–}6\,h^{-1}\mathrm{Mpc} \approx 7.4\text{–}8.9\,\mathrm{Mpc} \quad(h=0.674),
$$

a factor $\sim 3.5$–$4.3$ above NP-A. Mean inter-galaxy separation $n_*^{-1/3}$ is $\sim 6.9\,\mathrm{Mpc}$. Peculiar-velocity coherence scales are tens to hundreds of $h^{-1}\mathrm{Mpc}$. None of these equals $2.06\,\mathrm{Mpc}$.

The NP-A row therefore has no external prior from these scales. The DESI-ceiling $d=3$ cell ($\approx 12.6\,\mathrm{Mpc}$) sits nearer $R_8$ and the $r_0$ decade, but that is a different $\sigma$ row and still not a derivation of $\ell_{\ast}$.

---

## Scope of this note

| Already in other notes | This note |
|:-----------------------|:----------|
| MW–Andromeda, Virgo vs NP-A | not repeated |
| $R_8$ vs DESI-ceiling cell | context only |
| Galaxy $r_0$ from 2PCF | yes |
| $n^{-1/3}$ | yes |
| Peculiar-velocity scale class | yes |

---

## Programme anchors (comparison only)

| Anchor | Value [Mpc] | Origin |
|:-------|:------------|:-------|
| NP-A $\ell_{\ast}$ | $2.0646$ | counting inverse, $\sigma=10^{-5}$, $d=3$ |
| DESI-ceiling $\ell_{\ast}$ ($d=3$) | $12.557$ | counting inverse, $\sigma=1.5\times 10^{-4}$ |
| $R_8=8/h$ | $11.869$ | definition |

---

## Galaxy correlation length $r_0$

Power-law model $\xi_{gg}(r)=(r/r_0)^{-\gamma}$ ($\gamma\sim 1.7$–$1.9$): $r_0$ is where $\xi\sim 1$.

| Sample class | $r_0$ [$h^{-1}$ Mpc] | $r_0$ [Mpc] at $h=0.674$ | vs NP-A | vs $R_8$ |
|:-------------|:------------------------|:-----------------------------|:--------|:-----------|
| $L_*$ / main (low) | $5.0$ | $7.42$ | $+259\%$ | $-37\%$ |
| $L_*$ / main (high) | $6.0$ | $8.90$ | $+331\%$ | $-25\%$ |
| Luminous (upper OOM) | $8.0$ | $11.87$ | $+475\%$ | $\sim 0\%$ |

Sources: Zehavi et al., arXiv:[1005.2413](https://arxiv.org/abs/1005.2413); arXiv:[astro-ph/0408569](https://arxiv.org/abs/astro-ph/0408569).  
Typical $L_*$ samples sit near $r_0\sim 5$–$6\,h^{-1}\mathrm{Mpc}$; brighter/redder samples sit higher. I use that literature range, not a fit to NP-A.

$r_0(L_*)$ is not $\approx 2.06\,\mathrm{Mpc}$. It is several times larger, in the same broad decade as $R_8$ and the DESI-ceiling cell, not the NP-A cell.

---

## Mean inter-galaxy separation

For $n_*\sim 0.01\,h^{3}\mathrm{Mpc}^{-3}$ (order of $L_*$ space density),

$$
n_*^{-1/3}\approx 4.64\,h^{-1}\mathrm{Mpc}\approx 6.89\,\mathrm{Mpc}.
$$

| vs NP-A | vs $R_8$ |
|:--------|:-----------|
| $+234\%$ | $-42\%$ |

Not a match to $2.06\,\mathrm{Mpc}$.

---

## Peculiar-velocity coherence

Bulk-flow / Cosmicflows analyses discuss velocity coherence on scales of order $50$–$150\,h^{-1}\mathrm{Mpc}$ ($\sim 75$–$220\,\mathrm{Mpc}$ at $h=0.674$) — far above NP-A. There is no single $r_0$-like number that lands on $2\,\mathrm{Mpc}$.

---

## Reproduce

```bash
python scripts/closed/ell_star_r0_peculiar.py
```

---

## Implications

| Statement | Status |
|:----------|:-------|
| NP-A $2.06\,\mathrm{Mpc}$ is clean counting arithmetic | true |
| $r_0$, $n^{-1/3}$, $v_{\mathrm{pec}}$ equal NP-A | false |
| $r_0$ / $R_8$ / DESI-ceiling share a $\sim 10\,\mathrm{Mpc}$ class | roughly true; not a derivation |
| Principle fixing $\ell_{\ast}$ | still open |
| Scope if $\ell_{\ast}$ is derived | residual / slip band, not $9\%\,H_0$ |

After the fact, selecting a rare faint subsample with $r_0\sim 1.4\,h^{-1}\mathrm{Mpc}$ to match NP-A would not be an independent test. A cleaner path is a pre-registered sample (e.g. DESI BGS/LRG volume-limited cut), measure $r_0$ once, then compare.

---

## Summary table

| ID | Result |
|:---|:-------|
| R0-1 | $r_0(L_*)\sim 5$–$6\,h^{-1}\mathrm{Mpc}\to 7.4$–$8.9\,\mathrm{Mpc}$ at $h=0.674$ |
| R0-2 | factor $\times 3.5$–$4.3$ above NP-A |
| R0-3 | $n_*^{-1/3}\sim 6.9\,\mathrm{Mpc}$ ≠ NP-A |
| R0-4 | $v_{\mathrm{pec}}$ coherence ≫ NP-A |
