# WP2 — R3: open-horizon map (soft gain and no-gain theorems)

**Author:** Jesús Morales Souhail · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Programme:** measurable-stochastic-vacuum  
**Status:** Soft-regime theorems closed; hard bath open  
**Date:** July 2026  
**Code:** [`scripts/r3_open_horizon_map.py`](../scripts/r3_open_horizon_map.py) · [`scripts/lib_verified.py`](../scripts/lib_verified.py)  
**Input:** WP1 seed landscape  

> **Hard claims:** cite only [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) (gated by `pytest -q`).

---

## 1. Question

Given $\sigma_{0,\mathrm{eff}}$ from R1, can open-horizon dynamics produce a telescope residual without free lunch?

---

## 2. Residual definition

$$
\sigma_{\mathrm{res}} = G_U\, G_F\, G_O\, \sigma_{0,\mathrm{eff}},
\qquad
G_O = e^{2r}.
$$

Defaults in the soft regime: $G_F=1$ (freeze preserves), $G_U=1$ (late $\Delta x=\mathcal{O}(1)$ is not inflation’s $e^{60}$).

---

## 3. Verified no-gain statements

| Layer | Result | Status |
|:------|:-------|:-------|
| Late stretch | $G_U=\mathcal{O}(1)$ for $\Delta x=\mathcal{O}(1)$ | OOM theorem |
| Freeze-out | $G_F=1$ | Consistent with sister Route 2 scans |
| Soft squeeze | $r=\mathcal{O}(1)\Rightarrow G_O=\mathcal{O}(10)$ | Exact identity of $e^{2r}$ |
| Sorkin rescue | Need $r\sim 64$ to reach $10^{-5}$ | Exact log arithmetic |

**Soft open dynamics do not replace R1.**

---

## 4. Table (soft map)

| Seed | $G_O=1$ | $G_O\approx 20$ | In band $10^{-5}$–$10^{-4}$? |
|:-----|:--------|:----------------|:-----------------------------|
| Sorkin $\sim 10^{-61}$ | $\sim 10^{-61}$ | $\sim 10^{-60}$ | No |
| $10^{-5}$ (mesoscopic count) | $10^{-5}$ | $\sim 2\times 10^{-4}$ | Yes / near DESI ceiling a posteriori |

---

## 5. Open (not claimed)

Microscopic horizon Lindblad model fixing $r\gg 1$.  
Until derived, $r\sim 64$ is forbidden as a dial (A3, A5).

---

## 6. R3 status (A4)

| Piece | Status |
|:------|:-------|
| Soft $G_O$ bound | **Closed** |
| Hard bath | **Absent (declared)** |

---

*End of WP2 discussion note.*
