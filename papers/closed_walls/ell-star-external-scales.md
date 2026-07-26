# External scale candidates for \(\ell_*\): checked, not confirmed

**Author:** Jesús Morales Souhail  
**ORCID / web:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818) · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail)  
**Date:** July 2026  
**Status:** Desk note — this is **not** a derivation of \(\ell_*\)  
**Code:** [`scripts/closed/ell_star_external_scales.py`](../../scripts/closed/ell_star_external_scales.py)  
**Parent:** [`r1-open-kernel.md`](../r1_kernel/r1-open-kernel.md) · [`r1-counting-principle.md`](../r1_kernel/r1-counting-principle.md)

---

## 1. What \(\ell_*\approx 2.07\,\mathrm{Mpc}\) is (and is not)

I keep coming back to this number, so I want the status plain.

| | |
|:--|:--|
| **What it is** | Algebraic inverse of counting: \(\ell_*=L_H\sigma^{2/d}\) at \(d=3\), \(\sigma=10^{-5}\) (NP-A) |
| **Exact (code)** | \(\ell_*^{\mathrm{NP\text{-}A}}=2.0646\,\mathrm{Mpc}\) (\(H_0=67.4\)) |
| **What it is not** | A measured galaxy separation; a DESI fit; a derived decoherence scale |
| **Open** | A principle that actually *fixes* a mesoscopic cell (R1 kernel) |

The circular trap is easy: round \(2.0646\to 2.01\) or \(2.07\), call it “typical galaxy separation,” and feel as if something has been checked. That is the same number re-labelled, not an independent test.

---

## 2. Amplifiers vs open kernel (status)

| Class | Examples | Status |
|:------|:---------|:-------|
| **Measured walls** (multiply a fixed small seed) | Soft \(r\sim 64\); path \(\sqrt{N}\sim 10\)–\(100\); G&W \(\sim 45\); residual \(\sigma_X\) vs \(9\%\) \(H_0\) (\(\times 500+\)) | **Insufficient** by structure: soft processes give decades, not \(10^{56}\) |
| **Open kernel** (wrong starting cell?) | Mesoscopic \(\ell_*\) so \(\sigma\) is already \(10^{-5}\)–\(10^{-4}\) | **Absent (declared)** — not “failed,” **never derived** |

Even if \(\ell_*\) is physical, the programme toys I have run open **residual / slip** at \(10^{-4}\)–\(10^{-3}\), **not** the \(\sim 9\%\) Hubble tension.

---

## 3. External candidates (literature anchors, not fits)

| Candidate | Value (order) | \(\lvert\ell/\ell_*^{\mathrm{NP\text{-}A}}-1\rvert\) | Verdict as *independent* confirmation of NP-A |
|:----------|:--------------|:-----------------------------------------------------|:-----------------------------------------------|
| MW–Andromeda distance | \(\sim 0.78\,\mathrm{Mpc}\) | \(\sim 62\%\) | **No** |
| Virgo \(r_{200}\) (X-ray, Urban et al. 2011 class) | \(\sim 1.08\,\mathrm{Mpc}\) | \(\sim 48\%\) | **No** |
| Virgo (Ferrarese et al. 2012 class) | \(\sim 1.55\,\mathrm{Mpc}\) | \(\sim 25\%\) | **Closer, not confirmation** |
| Virgo (older Hoffman-class) | \(\sim 1.8\,\mathrm{Mpc}\) | \(\sim 13\%\) | **Closer, still not a principle** |
| \(R_8=8/h\) | \(\approx 11.87\,\mathrm{Mpc}\) | \(\sim 475\%\) vs NP-A; **near** DESI-ceiling \(d=3\) \(\ell_*\approx 12.56\,\mathrm{Mpc}\) | Scale class for **another** row (ceiling), not NP-A |
| “2.01 Mpc galaxy separation” | — | — | **Circular** if it is NP-A rounded |

Reproduce distances to NP-A / \(R_8\):

```bash
python scripts/closed/ell_star_external_scales.py
```

---

## 4. What would count as a real crack (same bar as R1d)

A candidate \(P\) is legal only if:

1. It predicts a length (or \(N_{\mathrm{eff}}\)) from **matter / gravity / decoherence** stated **before** targeting \(2.06\,\mathrm{Mpc}\);  
2. DESI residual and \(R_8\) enter only **a posteriori**;  
3. It does not use “\(\ell_*\) was 2.06, so look for a 2 Mpc object.”

Calculable quantities I have not yet used as an R1 principle in this repo:

- Galaxy two-point correlation length \(r_0\) / \(\xi_{gg}(r)=1\) scale (DESI / SDSS public);  
- Scale where peculiar-velocity correlations decay;  
- Horizon / non-linear scale at structure re-entry (distinct from pure \(R_8\) tag);  
- Thermal / interaction decoherence length of a vacuum sector coupled to collapsed matter (theory, not a fit).

If any of these, computed **blind** to \(2.0646\), lands near NP-A or near the DESI-ceiling cell \(\sim 12\,\mathrm{Mpc}\), that upgrades R1 from arithmetic to a hypothesis with an external prior. Until then: honest number, open principle.

---

## 5. Claim checklist

| ID | Claim |
|:---|:------|
| E1 | NP-A \(\ell_*=2.0646\,\mathrm{Mpc}\) is counting inverse only |
| E2 | MW–Andromeda \(\sim 0.78\,\mathrm{Mpc}\) is **not** a match to NP-A |
| E3 | Virgo radii \(\sim 1\)–\(1.8\,\mathrm{Mpc}\) are **not** independent confirmation |
| E4 | “2.01” as galaxy separation is **circular** if it is NP-A |
| E5 | Principle for mesoscopic grain remains **open** |

| Non-claim | |
|:----------|:--|
| N-E1 | \(\ell_*\) is the MW–Andromeda distance |
| N-E2 | Virgo proves the counting cell |
| N-E3 | Mesoscopic grain solves \(H_0\) tension |
