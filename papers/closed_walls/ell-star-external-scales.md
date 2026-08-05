# External scale candidates for $\ell_{\ast}$

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail) · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)
July 2026

Not a derivation of $\ell_{\ast}$.
Code: [`scripts/closed/ell_star_external_scales.py`](../../scripts/closed/ell_star_external_scales.py)
Related: [`r1-open-kernel.md`](../r1_kernel/r1-open-kernel.md) · [`r1-counting-principle.md`](../r1_kernel/r1-counting-principle.md)

---

## Status of $\ell_{\ast}\approx 2.07\,\mathrm{Mpc}$

| | |
|:--|:--|
| Definition | $\ell_{\ast}=L_H\sigma^{2/d}$ at $d=3$, $\sigma=10^{-5}$ (NP-A row) |
| Value ($H_0=67.4$) | $2.0646\,\mathrm{Mpc}$ |
| Not | a measured galaxy separation, a DESI fit, or a derived decoherence scale |
| Still open | a physical principle that fixes a mesoscopic cell |

Rounding $2.0646$ to $2.01$ or $2.07$ and calling it “typical galaxy separation” is not an independent check; it is the same number under another name.

---

## Amplifiers vs cell size

| Class | Examples | Status |
|:------|:---------|:-------|
| Soft amplifiers of a fixed small seed | Soft $r\sim 64$; path $\sqrt{N}\sim 10$–$100$; G&W $\sim 45$; residual vs $9\%\,H_0$ | Decades of gain, not $10^{56}$ |
| Mesoscopic $\ell_{\ast}$ so $\sigma$ is already $10^{-5}$–$10^{-4}$ | Open kernel (R1) | Not derived |

Even if $\ell_{\ast}$ is physical, the residual / slip channels I have computed sit near $10^{-4}$–$10^{-3}$, not the $\sim 9\%$ Hubble tension.

---

## External candidates (literature anchors)

| Candidate | Order of magnitude | vs NP-A | Independent confirmation of NP-A? |
|:----------|:-------------------|:--------|:----------------------------------|
| MW–Andromeda distance | $\sim 0.78\,\mathrm{Mpc}$ | $\sim 62\%$ off | No |
| Virgo $r_{200}$ (Urban et al. 2011 class) | $\sim 1.08\,\mathrm{Mpc}$ | $\sim 48\%$ | No |
| Virgo (Ferrarese et al. 2012 class) | $\sim 1.55\,\mathrm{Mpc}$ | $\sim 25\%$ | Closer, not confirmation |
| Virgo (older Hoffman-class) | $\sim 1.8\,\mathrm{Mpc}$ | $\sim 13\%$ | Closer, not a principle |
| $R_8=8/h$ | $\approx 11.87\,\mathrm{Mpc}$ | far from NP-A; near DESI-ceiling cell $\approx 12.56\,\mathrm{Mpc}$ | Different $\sigma$ row |
| “2.01 Mpc galaxy separation” | — | — | Circular if it is NP-A rounded |

```bash
python scripts/closed/ell_star_external_scales.py
```

---

## What would count as an independent prior

A useful principle should:

1. Predict a length (or $N_{\mathrm{eff}}$) from matter, gravity, or decoherence **without** targeting $2.06\,\mathrm{Mpc}$ first.
2. Use DESI residual and $R_8$ only afterwards.
3. Avoid choosing an object because its size matches the counting inverse.

Candidates I have not yet used as the R1 principle in this repo:

- galaxy two-point correlation length $r_0$ (DESI / SDSS)
- scale where peculiar-velocity correlations decay
- horizon / nonlinear scale at structure re-entry (if distinct from pure $R_8$)
- thermal / interaction decoherence length of a vacuum sector coupled to collapsed matter

If any of these, computed without targeting $2.0646$, lands near NP-A or near the DESI-ceiling cell $\sim 12\,\mathrm{Mpc}$, that is an external prior for R1. Until then the NP-A length is only counting arithmetic.

---

## Summary

| | |
|:--|:--|
| NP-A $\ell_{\ast}=2.0646\,\mathrm{Mpc}$ | counting inverse only |
| MW–Andromeda $\sim 0.78\,\mathrm{Mpc}$ | not a match |
| Virgo $\sim 1$–$1.8\,\mathrm{Mpc}$ | not independent confirmation |
| “2.01” as galaxy separation | circular if it is NP-A |
| Mesoscopic grain principle | still open |

Not claimed: $\ell_{\ast}$ is the MW–Andromeda distance; Virgo proves the counting cell; mesoscopic grain solves $H_0$.
