# T1.1 / T1.2 computations: averaging domain and nonlinear mask

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail) · July 2026 · not peer reviewed

*Quantitative Tier-1 machinery. Still not an action-level derivation of decoherence.*

Code: [`scripts/r1/r1_t1_mechanisms_compute.py`](../../scripts/r1/r1_t1_mechanisms_compute.py)  
Depends on: [`scripts/r1/r1_sigma_R_full.py`](../../scripts/r1/r1_sigma_R_full.py) · [`r1-mechanism-candidates.md`](r1-mechanism-candidates.md)

---

## Abstract

I execute the first two Tier-1 work items with numbers:

1. **T1.1** — Set the averaging domain \(L_{\mathrm{av}}:=R_{\mathrm{nl}}\) from the full \(\sigma(R)=1\) integral only. Count effective residual DOF as \(N=(L_H/L_{\mathrm{av}})^d\).
2. **T1.2** — Model nonlinear “edge” regions as the Gaussian excursion set \(\delta>\delta_c\) on a field with \(\sigma(R_{\mathrm{nl}})=1\); report volume fraction and packing separation.

Results (fiducial run): \(R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\); \(d=3\) counting gives \(\sigma\approx 8.5\times 10^{-5}\) (under DESI ceiling \(1.5\times 10^{-4}\)); nonlinear volume fraction at \(\delta_c=1\) is \(f\approx 0.16\); inter-patch separation \(\sim R_{\mathrm{nl}}f^{-1/3}\approx 16\,\mathrm{Mpc}\) (same decade as \(R_8\) / DESI-ceiling cell).

Still open: why the vacuum residual must live on that domain (master equation / action). These steps only show that *if* it does, lengths and amplitudes are DESI-compatible without \(10^{56}\).

---

## 1. Shared a priori length

From [`scripts/r1/r1_sigma_R_full.py`](../../scripts/r1/r1_sigma_R_full.py):

\[
R_{\mathrm{nl}}\approx 5.803\,h^{-1}\mathrm{Mpc}\approx 8.610\,\mathrm{Mpc}
\quad(\sigma_8=0.81,\ h=0.674).
\]

No DESI residual number enters this solve.

```bash
python scripts/r1/r1_t1_mechanisms_compute.py
```

---

## 2. T1.1 — Averaging domain = \(R_{\mathrm{nl}}\)

### 2.1 Statement

In Buchert-type language, cosmological equations are averaged on a domain of size \(L_{\mathrm{av}}\). I identify
\[
L_{\mathrm{av}}:=R_{\mathrm{nl}}
\]
as the natural domain once structure is nonlinear (Tier-1 candidate T1.1). Residual stochastic freedom is then counted as one effective mode per domain:
\[
N_{\mathrm{eff}}=\Bigl(\frac{L_H}{L_{\mathrm{av}}}\Bigr)^{d},\qquad
\sigma_{0,\mathrm{eff}}=\Bigl(\frac{L_{\mathrm{av}}}{L_H}\Bigr)^{d/2}.
\]
This is the same algebra as R1 counting with \(\ell_*=R_{\mathrm{nl}}\) — now motivated as averaging-domain size, still not derived from vacuum QFT.

### 2.2 Numbers

| \(d\) | \(N_{\mathrm{eff}}\) | \(\sigma_{0,\mathrm{eff}}\) | vs DESI \(1.5\times 10^{-4}\) |
|:------|:---------------------|:----------------------------|:-----------------------------|
| 2 | \(\sim 2.7\times 10^{5}\) | \(\sim 1.9\times 10^{-3}\) | above (not the default \(d\)) |
| 3 | \(\sim 1.4\times 10^{8}\) | \(\sim 8.5\times 10^{-5}\) | under |
| 4 | \(\sim 7\times 10^{10}\) | \(\sim 3.8\times 10^{-6}\) | under |

Programme default \(d=3\): residual amplitude from domain counting is DESI-safe and \(\mathcal{O}(10^{-4})\), without soft \(10^{56}\) gain.

### 2.3 What this does not prove

- That Buchert \(Q\) explains mean cosmic acceleration.
- That the residual is Gaussian OU with that \(\sigma\).
- That averaging is the correct microphysics of the vacuum.

---

## 3. T1.2 — Nonlinear mask / edge scale

### 3.1 Statement

SDiff / edge language: residual support lives where matter is nonlinear. Model the linear field as Gaussian with \(\sigma(R_{\mathrm{nl}})=1\). Nonlinear mask:
\[
m=\mathbf{1}\{\delta>\delta_c\}.
\]
Volume fraction (exact for Gaussian):
\[
f=\tfrac12\,\mathrm{erfc}\Bigl(\frac{\delta_c}{\sqrt{2}\,\sigma}\Bigr),\qquad\sigma=1.
\]
Packing OOM for separation of nonlinear blobs of size \(\sim R_{\mathrm{nl}}\):
\[
\ell_{\mathrm{sep}}\sim R_{\mathrm{nl}}\,f^{-1/3}.
\]
Blob size / mask correlation scale \(\sim R_{\mathrm{nl}}\) (filter scale; full BBKS peak theory is a refinement).

### 3.2 Numbers (\(\sigma=1\))

| \(\delta_c\) | \(f_{\mathrm{vol}}\) | blob \(\sim R_{\mathrm{nl}}\) [Mpc] | \(\ell_{\mathrm{sep}}\) [Mpc] |
|:-------------|:---------------------|:-----------------------------------|:------------------------------|
| \(1.0\) | \(0.159\) | \(8.61\) | \(\approx 15.9\) |
| \(1.5\) | \(0.067\) | \(8.61\) | \(\approx 21.2\) |
| \(2.0\) | \(0.023\) | \(8.61\) | \(\approx 30.3\) |

Reading:
- Edge / blob scale \(\sim 8.6\,\mathrm{Mpc}\) sits on \(r_0\) and in the 8–12 decade.
- Separation of nonlinear patches \(\sim 16\,\mathrm{Mpc}\) (at \(\delta_c=1\)) sits near \(R_8\) / DESI-ceiling cell (\(\sim 12\,\mathrm{Mpc}\)) — same decade, not a fit.

### 3.3 What this does not prove

- Full excursion-set mass functions / halo exclusion.
- That the residual operator equals the indicator \(m\).
- Decoherence rate from gravitational collapse.

---

## 4. Joint reading

| Mechanism step | Length scale | Amplitude if counting \(d=3\) |
|:---------------|:-------------|:------------------------------|
| T1.1 domain | \(R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\) | \(\sigma\approx 8.5\times 10^{-5}\) |
| T1.2 edge size | \(\sim R_{\mathrm{nl}}\) | — |
| T1.2 inter-edge sep | \(\sim 16\,\mathrm{Mpc}\) (\(\delta_c=1\)) | if used as \(\ell_*\): \(\sigma\sim 2\times 10^{-4}\) (order of ceiling) |

T1.1 and T1.2 are consistent with each other at the decade level: both point to mesoscopic structure scales fixed by matter, with residual amplitudes that do not require free \(10^{56}\).

---

## 5. BBKS refinement + derivation sketch

Peak curvature \(R_*\approx 1.58\,\mathrm{Mpc}\) vs domain \(R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\): see [`r1-t12-bbks-and-derivation.md`](r1-t12-bbks-and-derivation.md).  
Derivation sketch (postulates P0–P1 + standard S1 \(\Rightarrow\) coarse-graining \(\ell_*\sim R_{\mathrm{nl}}\)) in the same note.

---

## 6. Remaining physics gap

Geometry is viable. The sketch derives coarse-graining under stated postulates; it does not derive the coupling \(g\) or prove nature realizes P0–P1.

---

## 7. Claim checklist

| ID | Claim | Evidence |
|:---|:------|:---------|
| M1 | \(R_{\mathrm{nl}}\approx 8.61\,\mathrm{Mpc}\) from full \(\sigma(R)\) | `r1_sigma_R_full` |
| M2 | \(d=3\) counting on \(L_{\mathrm{av}}=R_{\mathrm{nl}}\) \(\Rightarrow\sigma\approx 8.5\times 10^{-5}<1.5\times 10^{-4}\) | script |
| M3 | \(f(\delta>1)\approx 0.159\) for unit Gaussian | erfc identity |
| M4 | \(\ell_{\mathrm{sep}}(\delta_c=1)\approx 16\,\mathrm{Mpc}\) packing OOM | script |
| M5 | Microphysics still open | this note |

| Non-claim | |
|:----------|:--|
| N-M1 | Buchert explains \(\Lambda\) |
| N-M2 | Action-level decoherence derived |
| N-M3 | \(H_0\) tension solved |
