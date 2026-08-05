# WP1 — R1: counting principle for the stochastic seed

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail) · July 2026

ORCID: [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)
Programme: measurable-stochastic-vacuum

*Partial derivation — landscape and zeros. Discussion/expansion of verified results.*

Code: [`scripts/r1/r1_counting_landscape.py`](../../scripts/r1/r1_counting_landscape.py) · [`scripts/core/lib_verified.py`](../../scripts/core/lib_verified.py)
Documented results: [`VERIFIED_RESULTS.md`](../core/VERIFIED_RESULTS.md) (gated by `pytest -q`).

---

## 1. What is derived

Under the counting hypothesis for the DE residual sector,

$$
N_{\mathrm{eff}}=\left(\frac{L}{\ell_{\ast}}\right)^{d}, \qquad \sigma_{0,\mathrm{eff}}=\frac{1}{\sqrt{N_{\mathrm{eff}}}}=\left(\frac{\ell_{\ast}}{L}\right)^{d/2}.
$$

The excluded Sorkin seed is the special case $\ell_{\ast}=L_P$, $d=2$ (holographic count on the Hubble sphere): $\sigma_0\sim 10^{-61}$.

Not done here: choosing $\ell_{\ast}$ to “enter Euclid” (excluded by A3, A5).

---

## 2. Landscape (verified)

With $L=L_H=c/H_0$ and target $\sigma=10^{-5}$:

| Cell $\ell_{\ast}$ | $d$ | $\sigma_{0,\mathrm{eff}}$ | Status |
|:--------------|:----|:--------------------------|:-------|
| $L_P$ | 2/3/4 | $\sim 10^{-61}$ / $10^{-92}$ / $10^{-122}$ | Structural zero |
| $\sim 0.04$ Mpc | 2 | $10^{-5}$ | Measurable band *if* principle fixes this cell |
| $\sim 2.1$ Mpc | 3 | $10^{-5}$ | Same |
| $\sim 14$ Mpc | 4 | $10^{-5}$ | Same |

Telescope-band residuals from counting alone require a mesoscopic DE counting cell, not a Planck cell. The factor $\ell_{\ast}/L_P\sim 10^{56}$ is not a free multiplier; it is the statement that the two cells are different counting objects.

---

## 3. Structural zeros

1. Planck cell $\Rightarrow$ null for any soft gain (verified).
2. $\ell_{\ast}=L_H\Rightarrow\sigma\sim 1$ (upper structural absurdity for BAO smoothness).
3. Wrong operator (lab optics) $\Rightarrow$ null (exploratory related repository).

---

## 4. Open kernel (load-bearing question)

> What principle fixes a galactic/mesoscopic counting cell for the DE sector, distinct from the Planck/holographic cell?

| Candidate | Open problem |
|:----------|:-------------|
| R1a — local causal set | What sets the DE correlation scale? |
| R1b — IR cutoff of a vacuum sector | Derive $\ell_{\ast}$ from an action |
| R1c — unimodular/SDiff grain | Why cosmological rather than Planck? |
| R1d — nonlinear structure scale | Why would DE count cells at $R_{\mathrm{nl}}$ / $R_8$? |

**R1 status:** landscape derived; form of the principle under A0–A4 closed by sandwich uniqueness (see [`r1-derivation-sandwich.md`](r1-derivation-sandwich.md)); existence of residual sector and local coupling still postulates. As a nature claim, the principle fixing $\ell_{\ast}$ remains open until A0–A1 are grounded.

Publication-oriented expansion (walls vs kernel, R1d scale table, falsifiers):
[`r1-open-kernel.md`](r1-open-kernel.md) · `python scripts/r1/r1_open_kernel_scales.py`

---

## 5. A posteriori DESI use (A5)

Sister bound $\sigma_X<1.5\times 10^{-4}$ (95% CL) is a test only:

- derived $\sigma_{0,\mathrm{eff}}$ in $[10^{-5},1.5\times 10^{-4}]$ → compatible, Euclid can decide;
- $\ll 10^{-5}$ → predict null;
- $\gg 1.5\times 10^{-4}$ without damping → tension.

Never tune $\ell_{\ast}$ to that number.
Never tune $\ell_{\ast}$ to $R_8$ after inspecting S$_8$ either (same dial class; see open-kernel note §7).

---

## 6. Next

WP2 takes $\sigma_{0,\mathrm{eff}}$ as input ([`r3-open-horizon-map.md`](../work_packages/r3-open-horizon-map.md)).
Closing WP1 as a nature claim requires A0–A1 (or equivalent) from microphysics under criteria P1–P6 in [`r1-open-kernel.md`](r1-open-kernel.md); the scale form under those axioms is already the sandwich.
