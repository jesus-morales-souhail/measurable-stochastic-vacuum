# WP5 — Falsification criteria

**Author:** Jesús Morales Souhail · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Programme:** measurable-stochastic-vacuum  
**Status:** Method note — how the programme dies or narrows  
**Date:** July 2026  
**Hard claims:** [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md)  

---

## 1. Purpose

A theory programme is scientific only if it can **lose**.  
This note lists falsification and narrowing criteria for the R1–R2–R3 package **without** using DESI as a dial to save the model.

---

## 2. Levels of failure

| Level | Meaning | Action |
|:------|:--------|:-------|
| **L0 — Identity failure** | Algebra in `lib_verified` / tests break | Stop; fix maths (not physics) |
| **L1 — Soft-regime theorem stands** | Sorkin + soft open + path still null | **Not** a failure — confirmed structural zero |
| **L2 — Candidate death** | A specific R1a/b/c or hard-R3 model is excluded | Discard that candidate; package may continue |
| **L3 — Package death** | Every viable path to mesoscopic $\sigma$ or derived hard gain is excluded | Close programme as “limits + geometry only” (honest success of sister repo) |
| **L4 — Overclaim death** | Publication uses free $10^{56}$, free $r\sim 64$, or DESI-tuned $\ell_*$ | Reject paper under self-shielding axioms |

---

## 3. Falsifiers for counting (R1)

Once a principle $P$ predicts $\ell_*$ or $N_{\mathrm{eff}}$:

| Outcome | Verdict |
|:--------|:--------|
| $P\Rightarrow \ell_*\sim L_P$ | Predicts structural null; **confirmed** if residual stays null; **does not** yield detection claims |
| $P\Rightarrow \sigma_{0,\mathrm{eff}}\in[10^{-5},1.5\times 10^{-4}]$ | A posteriori compatible with sister DESI ceiling; Euclid residual can falsify |
| $P\Rightarrow \sigma_{0,\mathrm{eff}}\gg 1.5\times 10^{-4}$ with no damping mechanism | **Tension** with DESI residual bound (sister repo) → candidate dies unless $\theta$-damping derived |
| $P$ contradicts local Lorentz tests **that actually constrain that sector** | Candidate dies |

**Illegal move:** change $\ell_*$ after seeing DESI to sit under $1.5\times 10^{-4}$.

---

## 4. Falsifiers for soft / hard open maps (R3)

| Outcome | Verdict |
|:--------|:--------|
| Soft $r=\mathcal{O}(1)$ claimed to fix Sorkin | **Already false** (verified: need $r\sim 64$) |
| Hard map derives $r\sim 64$ from horizon bath, then data exclude $\sigma_{\mathrm{res}}$ | Candidate dies |
| Hard map predicts $G_O^{\max}=\mathcal{O}(10)$ for all allowed baths | Strengthens no-free-lunch; package narrows to R1-only door |
| Claim $e^{60}$ late stretch equals inflationary gain for Sorkin seed | **Already false** (regime mismatch) |

---

## 5. Falsifiers for slip / light path (R2)

| Outcome | Verdict |
|:--------|:--------|
| Model predicts $\mathrm{RMS}_{\mathrm{path}}\gtrsim 0.05$–$0.1$ with $\sigma$ allowed by DESI residual | Conflict with slip floors / GR-like measurements at that OOM → die or reduce $\varepsilon$ **if $\varepsilon$ derived** |
| Setting $\varepsilon=0$ by symmetry | Slip channel closes; only isotropic residual remains |
| Free $\varepsilon$ fitted to Maus $\gamma=1.17$ | **Illegal** (DESI/Maus as dial) |

---

## 6. Combined decision tree

```
Is the seed Sorkin (ell_* = L_P)?
  YES → soft R3 + path → structural NULL (L1 confirm)
         hard R3 with derived r~60?
            NO  → no detection path (L3 if no other R1)
            YES → predict sigma_res; confront DESI/Euclid (L2/L3)
  NO  → R1 principle gave mesoscopic ell_*?
            NO  → still open research (not yet falsifiable as package)
            YES → predict sigma_res and RMS_path
                   within DESI ceiling?  → Euclid / slip tests (L2)
                   above ceiling with no damping? → dead (L2)
```

---

## 7. What does *not* falsify the programme

- Null BAO residual under Sorkin counting (expected).  
- Null lab diffraction / tesseract tests (wrong scale/operator).  
- Mild $\gamma-1=\mathcal{O}(0.1)$ hints without a derived $\varepsilon$ and $\sigma$ (insufficient).  
- Soft open gain $\mathcal{O}(10)$ being small (theorem, not failure).

---

## 8. Minimal checklist before any “positive” paper

- [ ] `pytest -q` green  
- [ ] Claims subset of [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) **or** new tests added  
- [ ] $\ell_*$ or $r$ or $\varepsilon$ derived, not fitted to DESI  
- [ ] Zeros Z1–Z4 stated  
- [ ] A posteriori DESI comparison only  
- [ ] No $10^{56}$ free factor  

---

## 9. Closing posture

> The empirical sister repository already succeeded as **limits and exclusions**.  
> This theory programme succeeds either by a **derived** mesoscopic seed / hard open map that passes WP5, or by proving that no such path exists without numerology — in which case the scientific answer is: *stochastic vacuum noise of Sorkin type is not telescope-measurable under soft dynamics.*

---

*End of WP5.*
