# Cross-repository consistency audit (July 2026)

**Author:** Jesús Morales Souhail  
**Scope:** `stochastic-dark-energy-ou` · `measurable-stochastic-vacuum` · `stochastic-de-exploratory-notes`  
**Gate:** `pytest -q` in theory repo → **42 passed**

---

## 1. Repository roles (must not mix)

| Repo | Role | Peer-review claims? |
|:-----|:-----|:--------------------|
| **stochastic-dark-energy-ou** | DESI BAO residuals, $\sigma_X$ bound, model kills, amplifier audit | **Yes** (empirical) |
| **measurable-stochastic-vacuum** | Minimal Model, wall, light-cone path, test-gated theory | **Yes** (theory kinematics) |
| **stochastic-de-exploratory-notes** | Optics / wrong-scale pedagogy | **No** |

---

## 2. Canonical numbers (must match everywhere)

| Quantity | Value | Source of truth |
|:---------|:------|:----------------|
| DESI residual ceiling | $\sigma_X < 1.5\times 10^{-4}$ (95% CL) | DESI repo `resume.txt` / PREPRINT |
| Sorkin holographic seed | $\sigma_0 = L_P/L_H \approx 1.18\times 10^{-61}$ | `lib_verified.sorkin_holographic` |
| Soft open $r=1.5$ | $G_O=e^{3}\approx 20.086$ | `lib_verified.soft_squeeze_gain` |
| $r$ to lift Sorkin to $10^{-5}$ | $\approx 64.4$ | algebra |
| $\ell_*$ for $\sigma=10^{-5}$, $d=3$ | $\approx 2.065 \mathrm{Mpc}$ | `ell_for_target_sigma` |
| Slip wall $z=0$, $\varepsilon=1$, $\sigma_X=1.5\times 10^{-4}$ | $\lvert\gamma-1\rvert\approx 6.52\times 10^{-4}$ | `slip_deviation` |
| Path RMS NP-A $z_s=1.5$ | $\approx 3.5\times 10^{-4}$ | light-cone atlas |
| Path RMS NP-B $z_s=1.5$ | $\approx 4.4\times 10^{-3}$ | light-cone atlas |
| Path boost NP-A $z_s=1.5$ | $\sqrt{N}\approx 46.6$ | $\chi/\ell_*$ |

---

## 3. Canonical equations (single chain)

$$
\begin{aligned}
&(E1)\quad k^{2}\Psi=-4\pi G a^{2}\rho_m\delta_m\\
&(E2)\quad k^{2}(\Phi-\Psi)=8\pi G a^{2}\pi_T\\
&(M1)\quad \pi_T=\varepsilon\sigma_X\rho_X\\
&(W)\quad \lvert\gamma-1\rvert=2\varepsilon\sigma_X\frac{\rho_X}{\rho_m\lvert\delta_m\rvert}\\
&(P)\quad \mathrm{RMS}_{\mathrm{path}}=\lvert\gamma-1\rvert_{\mathrm{loc}}\sqrt{\chi/\ell_*}\\
&(B)\quad \sigma=(\ell_*/L_H)^{3/2}\quad(d=3)\\
&(G)\quad \sigma_{\mathrm{res}}=e^{2r}\sigma,\quad r=\mathcal{O}(1)
\end{aligned}
$$

**Forbidden identities**

- $\mathrm{RMS}=\sigma\times G_O\times\sqrt{N}$ as an equality  
- $\xi_{\mathrm{LIV}}=\sigma_X$ without derivation  
- Soft $r\sim 64$ or $N\sim 10^{119}$ as “natural”

---

## 4. Math hygiene applied (this audit)

| Fix | Action |
|:----|:-------|
| GitHub KaTeX thin spaces ` ` | Removed across all three repos |
| Multi-line `$$` with lone `=` | Collapsed to single-line displays |
| Broken `\boxed{...}` after cleanup | Removed; equations left plain |
| Broken `\tag{W}}` | Fixed to `\tag{W}` |
| Brace mismatches in display math | Balanced in theory papers |
| Corrupted `manuscript/README.md` | Rewritten |

---

## 5. Peer-review entry points

| Repo | Start |
|:-----|:------|
| DESI empirical | `manuscript/PREPRINT.md` + `manuscript/CLAIMS.md` |
| Theory | `papers/FOR_REFEREES.md` → `OBSERVABLE_WALL.md` → `PAST_LIGHT_CONE_INTEGRATION.md` → `SIMPLE_AS_LAMBDA.md` → `VERIFIED_RESULTS.md` |
| Exploratory | `README.md` only (no cosmology claims) |

---

## 6. Sense check (does the story cohere?)

1. **Data:** DESI residual prefers smooth $\Lambda$-like bulk; $\sigma_X$ ceiling is tiny.  
2. **Wall:** Einstein+Morales map that ceiling to $\lvert\gamma-1\rvert\sim 10^{-4}$ → self-shielded vs Euclid floors $\sim 0.03$.  
3. **Only natural boost:** past light cone $\sqrt{N}\sim 40$–$70$ → $\mathrm{RMS}\sim 10^{-4}$–$10^{-3}$ (frontier, not easy detection).  
4. **Minimal model:** keep $\Lambda$CDM + one grain $\sigma$ + $\mathrm{RMS}\sim\sigma^{2/3}$.  
5. **Sorkin:** structural null under soft dynamics.  
6. **Analogy (Hall edge):** bulk=$\Lambda$, edge=$\sigma$; does not claim cosmos is a Hall bar.

**Verdict:** the three repos form one coherent programme: empirical nulls / bounds; theory kinematics and wall; exploratory fence. Hard claims are test-gated in the theory repo and empirically bounded in the DESI repo.

---

*Regenerate numbers:* `pytest -q && python scripts/light_cone_atlas.py && python scripts/simple_as_lambda.py`
