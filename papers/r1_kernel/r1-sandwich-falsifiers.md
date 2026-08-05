# Operational falsifiers of the sandwich uniqueness theorem

Jesús Morales Souhail · [github.com/jesus-morales-souhail](https://github.com/jesus-morales-souhail) · July 2026

*Pre-registered falsifiers and executed numbers. Not a claim of Stage-IV detection.*

Code: [`scripts/r1/r1_sandwich_falsifiers.py`](../../scripts/r1/r1_sandwich_falsifiers.py)
Results: [`results/r1_falsifiers/`](../results/r1_falsifiers/)
Depends on: [`r1-derivation-sandwich.md`](r1-derivation-sandwich.md) · [`wp5-falsification.md`](../work_packages/wp5-falsification.md) · [`lensing-rms-forecast-real-data.md`](../side_threads/lensing-rms-forecast-real-data.md)

---

## Abstract

The sandwich theorem states: if A0–A4 hold, free residual grain $\ell_{\ast}\sim R_{\mathrm{nl}}$. A theorem is scientific only if it can lose. This note pre-registers operational falsifiers and reports predictions at the programme working point versus published / forecast floors.

Primary gates: (F1) BAO residual amplitude at fixed $\ell_{\ast}=R_{\mathrm{nl}}$; (F2) residual correlation length in the $\mathcal{O}(1)\times R_{\mathrm{nl}}$ band if a residual is detected; (F3) slip / path-RMS consistency with Maus/Sakr; (F4) excluded moves (post-hoc $\ell_{\ast}$, free $10^{56}$, $m$-bias rebrand).

---

## 1. Working-point predictions (a priori under sandwich + counting)

| Quantity | Value | Origin |
|:---------|:------|:-------|
| $R_{\mathrm{nl}}$ | $\approx 8.61\,\mathrm{Mpc}$ | $\sigma(R)=1$ matter integral |
| $\sigma_{\mathrm{free}}$ | $\approx 8.5\times 10^{-5}$ | $d=3$ counting |
| $\lvert\lambda\rvert_{\mathrm{work}}$ | $\lesssim 1.24\times 10^{-4}$ | DESI $\sigma_X<1.5\times 10^{-4}$ (95% CL) map |
| $\lvert g\rvert_{\mathrm{work}}$ | $\lesssim 1.45$ | $\lambda=g\sigma_{\mathrm{free}}$ |
| $\lvert\gamma-1\rvert_{\mathrm{loc}}$ (free / work) | $\sim 4\times 10^{-4}$ / $\sim 6\times 10^{-4}$ | slip wall, $\varepsilon=1$, $z=0.8$ |
| $\mathrm{RMS}_{\mathrm{path}}$ (free / work) | $\sim$ few $\times 10^{-3}$ | path accumulation $z_s=1.5$ |
| Allowed $\ell_{\ast}$ band | $[0.5,\,3]\times R_{\mathrm{nl}}\approx [4.3,\,25.8]\,\mathrm{Mpc}$ | sandwich $\mathcal{O}(1)$ |

```bash
python scripts/r1/r1_sandwich_falsifiers.py
```

Exact numbers are written to `results/r1_falsifiers/`.

---

## 2. Falsifier table

| ID | Observable | Prediction | External floor | Kills sandwich-band if… | Supports if… |
|:---|:-----------|:-----------|:---------------|:------------------------|:-------------|
| F1 | BAO residual $\sigma_{\mathrm{res}}$ | $\sigma_{\mathrm{free}}\sim 8.5\times 10^{-5}$ | DESI $\sigma_X<1.5\times 10^{-4}$ (95% CL) (sister) | Measured residual $\gg 1.5\times 10^{-4}$ at fixed $\ell_{\ast}=R_{\mathrm{nl}}$ with no derived damping | Residual stays under ceiling with $\ell_{\ast}$ locked |
| F2 | Residual correlation length $\ell_{\ast}$ | $\sim R_{\mathrm{nl}}$ (band $\mathcal{O}(1)$) | — (requires residual detection) | Free residual $\xi$ at $\sigma\sim 10^{-4}$ measured $\ll 1\,\mathrm{Mpc}$ or $\gg 100\,\mathrm{Mpc}$ | Measured $\ell_{\ast}\in[0.5,3]R_{\mathrm{nl}}$ |
| F3a | Local $\lvert\gamma-1\rvert$ | $\sim 10^{-4}$ | Maus $\sigma(\gamma)=0.11$ | Required mean slip $\gg 0.1$ for $\varepsilon\sim 1$ at DESI-safe $\sigma$ (would need huge $\varepsilon$) | Predicted $\ll$ Maus (today: automatic consistency) |
| F3b | Path $\mathrm{RMS}$ | $\sim 10^{-3}$ | Sakr constant $\eta\sim 0.05$; free $ (z,k)\sim 0.3$ | Stochastic path-RMS proxy measured far above prediction without systematics budget | Remains below mean-$\eta$ floors |
| F4 | Method integrity | — | — | Post-hoc $\ell_{\ast}$ fit to DESI; free $10^{56}$; equate Stage-IV $m\sim 10^{-3}$ with path-RMS detection | Self-shielding axioms held |

Today: F1 is compatible (working bound). F3 is automatically consistent (floors $\gg$ prediction). F2 is the decisive geometric test but requires a residual detection or a well-defined residual two-point analysis. F4 is continuous discipline.

---

## 3. What Stage-IV can and cannot do

| Claim | Status |
|:------|:-------|
| Stage-IV tightens BAO / residual $\sigma_X$(F1 deeper) | Yes — primary path |
| Stage-IV mean $\eta$ / $\gamma$ reaches sandwich path-RMS | Not established — Sakr constant $\eta\sim 5\%$ still $\gg 10^{-3}$ path-RMS if naively equated |
| Stage-IV $m$-bias $\sim 10^{-3}$ = detection of residual texture | False (wrong operator) |
| Euclid residual band $\sim 10^{-5}$ | Can confirm free-grain OOM or deepen null under fixed $\ell_{\ast}=R_{\mathrm{nl}}$ |

See [`lensing-rms-forecast-real-data.md`](../side_threads/lensing-rms-forecast-real-data.md) for operator honesty.

---

## 4. Decision tree

```
A0–A1 true (residual χ couples locally to δ_m)?
 NO → sandwich N/A; scale undetermined
 YES → ell_* ~ R_nl (theorem)
 │
 ├─ residual ξ ≪ 1 Mpc or ≫ 100 Mpc at σ~1e-4? → F2 KILL
 ├─ σ_res ≫ 1.5e-4 at fixed ell_*=R_nl, no damping? → F1 KILL
 ├─ slip/path far above Maus/Sakr without systematics? → F3 tension
 └─ all gates green → package lives; Euclid residual is next precision
```

Levels aligned with [`wp5-falsification.md`](../work_packages/wp5-falsification.md): F1/F2 failures are L2 (candidate death for this principle form), not L0 identity failure.

---

## 5. What does not kill the sandwich

- Null BAO residual under Sorkin counting (expected; different cell).
- Maus $\gamma-1\sim 0.1$ (wrong sensitivity for $10^{-4}$ residual).
- Stage-IV shear calibration meeting $m\sim 10^{-3}$.
- Mild preference for percent-level free $\sigma_{\mathrm{res}}$ in absolute $D/r_d$ fits (background offset thrashing — see full-cov note).

---

## 6. Summary

| ID | Claim | Evidence |
|:---|:------|:---------|
| Fals1 | Working-point predictions tabulated | script |
| Fals2 | F1–F4 pre-registered | this note |
| Fals3 | Stage-IV $m$-bias not a path-RMS test | definitional + lensing note |

| Not claimed | |
|:----------|:--|
| N-F1 | Stage-IV will detect sandwich residual |
| N-F2 | Maus already tests path-RMS |
| N-F3 | Sandwich proven in nature (only under A0–A4) |

---

## Reproduce

```bash
python scripts/r1/r1_sandwich_falsifiers.py
pytest -q
```
