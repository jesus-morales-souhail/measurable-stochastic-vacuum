# Toy a priori map: path depth \(\to\) distance bias (H0-bridge test)

**Author:** Jesús Morales Souhail  
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Date:** July 2026  
**Status:** Toy map + amplitude honesty check — **not** a solution of the Hubble tension  
**Code:** [`scripts/closed/h0_bridge_toy.py`](../../scripts/closed/h0_bridge_toy.py)  
**Parent:** [`h0-running-brachistochrone-bridge.md`](h0-running-brachistochrone-bridge.md) · [`r1-open-kernel.md`](../r1_kernel/r1-open-kernel.md) · [`OBSERVABLE_WALL.md`](../core/OBSERVABLE_WALL.md)

---

## Abstract

We implement the promised **a priori** toy:
\[
\left\lvert\frac{\delta D}{D}\right\rvert
=
\begin{cases}
s_{\mathrm{loc}}\sqrt{\chi/\ell_*} & \text{(S) stochastic / path RMS}\\
s_{\mathrm{loc}}\,(\chi/\ell_*) & \text{(C) coherent (flagged)}\\
\end{cases}
\]
with \(\ell_*\) **fixed** from the R1 landscape (NP-A or \(R_8\)-class) and \(s_{\mathrm{loc}}=\lvert\gamma-1\rvert\) from the Einstein+Morales wall at the DESI residual ceiling. We also track the amplitude-free shape \(f(z)=\sqrt{\chi(z)/\chi(1.5)}\).

**Result:** under DESI-safe stochastic accumulation, the induced \(H_0(0.15)/H_0(1.5)\) ratio shift is **\(\mathcal{O}(0.1\%)\)**, not the observed \(\sim 8\%\). The bridge **does not** explain the Hubble tension at safe amplitude. Coherent accumulation can reach \(\mathcal{O}(10\%)\) but is the **excluded** free-amplifier class. The **shape** \(f(z)\) does vary through the literature running window \(z\sim 0.5\)–\(0.7\) — scale class only.

---

## 1. A priori inputs (no H0 dial)

| Symbol | Value | Source |
|:-------|:------|:-------|
| \(\ell_*^{\mathrm{NP\text{-}A}}\) | \(\approx 2.07\,\mathrm{Mpc}\) | \(d=3\), \(\sigma=10^{-5}\) counting inverse |
| \(\ell_*^{R_8}\) | \(\approx 11.87\,\mathrm{Mpc}\) | \(R_8=8/h\) (R1d **class**, not derived) |
| \(s_{\mathrm{loc}}\) | \(\lvert\gamma-1\rvert(\sigma_X=1.5\times 10^{-4},\varepsilon=1,z=0.5)\) | wall formula |
| \(H_0^{\mathrm{true}}\) | \(67.4\) | Planck-class fiducial for toy |
| Observed ratio | \(73/67.4\approx 1.083\) | literature anchor only |

**Forbidden:** adjust \(\ell_*\) or \(s_{\mathrm{loc}}\) so that the ratio becomes \(1.083\).

---

## 2. Inference toy

If a path effect **overestimates** distance by \(\delta=\lvert\delta D/D\rvert\), a Hubble-law inference underestimates \(H_0\):
\[
H_0^{\mathrm{inf}}(z)\approx\frac{H_0^{\mathrm{true}}}{1+\delta(z)}.
\]
Then deep probes (large \(\delta\)) give **lower** \(H_0\), local probes (small \(\delta\)) **higher** — the **sense** of H0-running / tension (local high, CMB low), if the amplitude were large enough.

```bash
python scripts/closed/h0_bridge_toy.py
```

---

## 3. Machine results (verified)

### 3.1 Stochastic (S) — DESI-safe, programme-consistent

| \(\ell_*\) | \(\delta(0.15)\) | \(\delta(1.5)\) | \(H_0(0.15)/H_0(1.5)\) | vs obs \(1.083\) |
|:-----------|:-----------------|:----------------|:-----------------------|:-----------------|
| NP-A \(\approx 2.06\) Mpc | \(3.41\times 10^{-3}\) | \(9.01\times 10^{-3}\) | \(\mathbf{1.0056}\) | short |
| \(R_8\approx 11.87\) Mpc | \(1.42\times 10^{-3}\) | \(3.76\times 10^{-3}\) | \(\mathbf{1.0023}\) | short |

**\(\beta\) needed** if \(\delta=\beta\sqrt{\chi/\ell_*}\) to force ratio \(1.083\):  
\(\beta\approx 3.0\times 10^{-3}\) (NP-A) or \(7.2\times 10^{-3}\) (\(R_8\)) vs wall \(s_{\mathrm{loc}}\approx 1.93\times 10^{-4}\) → short by **\(\times 16\)–\(38\)**. That residual / slip amplitude sits **above** the sister DESI ceiling → **excluded** under current programme bounds.

### 3.2 Coherent (C) — amplitude large, class excluded

| \(\ell_*\) | ratio \(H_0(0.15)/H_0(1.5)\) | vs \(1.083\) |
|:-----------|:----------------------------|:-------------|
| NP-A | \(1.34\) | **overshoots** |
| \(R_8\) | \(1.062\) | near but still short; \(\beta\) needed \(\sim 1.3\times s_{\mathrm{loc}}\) |

Coherent line-of-sight stacking is the same **logical family** as free path amplifiers already closed for residual honesty (no free \(N\) boost). **Not** a legal save of the bridge.

### 3.3 Shape-only \(f(z)=\sqrt{\chi(z)/\chi(1.5)}\)

| \(z\) | \(f(z)\) |
|:------|:---------|
| 0.30 | \(0.525\) |
| 0.50 | \(0.660\) |
| 0.70 | \(0.759\) |
| 1.00 | \(0.871\) |

The shape **does** change through the window where Dainotti / Krishnan-style running and H0LiCOW \(z_d\) trends are discussed. That supports **shared depth language**, not a 9% amplitude.

---

## 4. Verdict for the H-bridge

| Question | Answer |
|:---------|:-------|
| Does DESI-safe path RMS explain \(H_0\) tension? | **No** — short by \(\sim 10^{2}\) in \(\beta\) |
| Does the **sense** (local high / deep low) match? | **Yes** under the distance-overestimate toy |
| Does the **shape** vary at \(z\sim 0.5\)–\(0.7\)? | **Yes** (scale class) |
| Can coherent stacking save it? | Amplitude yes, **class no** (excluded) |
| Fit \(\ell_*\) to 1.083? | **Illegal** |

**Programme consequence:** the open kernel / mesoscopic grain remains interesting for **residual, slip, and path RMS** at \(10^{-4}\)–\(10^{-3}\); it is **not** a free lunch for the Hubble tension under self-shielding. Any H0 solution still needs different physics (or a derived coherent channel that survives DESI — not currently available).

---

## 5. Claim checklist

| ID | Claim | Evidence |
|:---|:------|:---------|
| T1 | \(\ell_*\) NP-A and \(R_8\) fixed a priori | counting / \(R_8\) def |
| T2 | Stochastic ratio shift \(\mathcal{O}(0.1\%)\) | script + tests |
| T3 | \(\beta\) for 1.083 \(\gg s_{\mathrm{loc}}\) | script |
| T4 | Shape \(f(z)\) monotonic through 0.5–0.7 | script |

| Non-claim | |
|:----------|:--|
| N-T1 | Toy solves Hubble tension |
| N-T2 | Coherent mode allowed |
| N-T3 | \(\delta D/D\equiv\) path RMS is proven GR |

---

## 6. Related filter (desqueezing packaging)

Invented \(H_0(z)=H_{0,\mathrm{fid}}[1+\varepsilon e^{-\theta x}]\) with \(\theta\) tuned to \(z\sim 0.5\)–\(0.7\) is **rejected** in [`h0-desqueezing-filter.md`](h0-desqueezing-filter.md).  
Complex \(\omega\) does not raise the \(\sigma_X\) energy budget. Same shortfall vs \(8\%\).

## 7. Reproduce

```bash
cd measurable-stochastic-vacuum
python scripts/closed/h0_bridge_toy.py
python scripts/closed/h0_desqueezing_filter.py
python scripts/closed/h0_running_geometry.py
pytest -q
```

