# H0 tension, “brachistochrone” intuition, and a bridge to the open kernel

**Author:** Jesús Morales Souhail  
**ORCID:** [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Date:** July 2026  
**Status:** Literature + geometry note — **not** a solution of the Hubble tension; **not** a derivation of \(\ell_*\)  
**Code:** [`scripts/h0_running_geometry.py`](../scripts/h0_running_geometry.py)  
**Related:** [`r1-open-kernel.md`](r1-open-kernel.md) · [`lensing-rms-forecast-real-data.md`](lensing-rms-forecast-real-data.md) · sister DESI bound  

---

## Abstract

A working intuition — measure the Hubble tension as if comparing “paths” under fixed gravity at long vs short distance — is fixed into four testable statements. The classical Bernoulli brachistochrone is **not** the photon path; the real multi-path, multi-time observable is **strong-lensing time delay**. The literature already studies **H0 running / redshift evolution of inferred \(H_0\)** (Krishnan et al.; Dainotti et al.; Wong/H0LiCOW trend). The observed local/early ratio is \(\sim 73/67.4\approx 1.083\).

We then ask, without fitting, whether the programme’s **mesoscopic grain** (\(\ell_*\sim\mathrm{Mpc}\), \(R_8\sim 12\,\mathrm{Mpc}\)) points at a **similar redshift class** as the reported transition (\(z\sim 0.3\)–\(0.7\)). Geometry: matter–DE equality sits at \(z_{\mathrm{eq}}\approx 0.30\); lookback and \(\chi(z)\) grow through the same window where path patch counts \(N=\chi/\ell_*\) become large. That is a **shared scale class**, not a derived mechanism for \(H_0(z)\).

---

## 1. Four fixed statements (so nothing is guessed)

| # | Question | Fixed answer for this note |
|:--|:---------|:---------------------------|
| **1. What travels?** | Photons follow **null geodesics** (Fermat-type stationarity of arrival time in a static lens, not Bernoulli sliding under \(g\)). Classical brachistochrone = massive particle, uniform \(g\), cycloid. **Not** a direct translation to light. Closest real physics: **multiple lensed images** of one quasar, **different paths, different arrival times** (time-delay cosmography). |
| **2. “Fixed gravity”** | **Local regime** \(z\ll 1\): \(H(z)\approx H_0\) constant, \(v=H_0 d\). That *is* the definition of the local \(H_0\) ladder. Not a Newtonian \(g=\mathrm{const}\) along a wire. |
| **3. Short vs long path** | **Short / fast (local):** SN Ia + Cepheids / TRGB, \(z\lesssim 0.15\) (SH0ES-class). **Long / early:** CMB last-scattering \(z\sim 1100\) (Planck-class under \(\Lambda\)CDM). Intermediate: BAO, lens redshifts \(z_d\sim 0.3\)–\(0.8\), SN bins. |
| **4. What number?** | Tension ratio **observed**: \(H_0^{\mathrm{local}}/H_0^{\mathrm{CMB}}\approx 73.0/67.4\approx\mathbf{1.083}\) (order \(9\%\)). Any mechanism *claim* must eventually predict this ratio (or a trend \(H_0^{\mathrm{inf}}(z)\)) **before** fitting it. This note does **not** claim that prediction yet. |

---

## 2. Real data and literature (external anchors)

### 2.1 Absolute anchors (standard tension)

| Probe | \(H_0\) [km s\(^{-1}\) Mpc\(^{-1}\)] | Ref. class |
|:------|:-------------------------------------|:-----------|
| Planck CMB (\(\Lambda\)CDM) | \(67.4\pm 0.5\) | Planck 2018 |
| SH0ES local ladder | \(\sim 73\)–\(74\) | Riess et al. series |
| **Ratio** | \(\sim 1.08\)–\(1.10\) | \(\sim 5\sigma\) class tension (method-dependent) |

### 2.2 Time-delay cosmography (multi-path photons) — point 1 made real

| Result | Value | Reference |
|:-------|:------|:----------|
| H0LiCOW XIII (6 lenses) | \(H_0=73.3^{+1.7}_{-1.8}\) (2.4%) | Wong et al., MNRAS 498, 1420 (2020); arXiv:[1907.04869](https://arxiv.org/abs/1907.04869) |
| Trend of inferred \(H_0\) with **lens redshift** / \(D_{\Delta t}\) | Mild decline, \(\sim 1.8\)–\(1.9\sigma\) | Same paper (Appendix / §5 discussion) |
| TDCOSMO + external kinematics (example) | Can pull toward lower \(H_0\) when mass-sheet degeneracy broken | Birrer et al. TDCOSMO series; e.g. hierarchical analyses \(\sim 67\)–\(74\) depending on prior |

**Physics:** same source, several null paths, measured **time delays** → absolute distance scale \(\propto 1/H_0\). This is the honest “several paths, different times” laboratory — not a cycloid wire.

### 2.3 H0 running / binned late-time probes — point 3 made real

Active (and debated) line:

| Work | What they do | Reported sense of trend |
|:-----|:-------------|:------------------------|
| **Dainotti et al.** | Binned Pantheon SN Ia; effective \(H_0\) vs redshift | Decreasing trend; arXiv:[2103.02117](https://arxiv.org/abs/2103.02117), ApJ 912, 150 (2021) |
| **Krishnan et al.** | Evolution / FLRW consistency tests of the tension | arXiv:[2105.09790](https://arxiv.org/abs/2105.09790); earlier related [2002.06044](https://arxiv.org/abs/2002.06044) |
| **Wong / H0LiCOW** | \(H_0\) vs \(z_d\), \(D_{\Delta t}\) | Mild negative trend \(\sim 1.9\sigma\) (arXiv:1907.04869) |
| Follow-ups | Various SN + BAO + lens binning | Transition often discussed around **\(z\sim 0.5\)–\(0.7\)**; significance **method-dependent** (\(\sim 2\sigma\) to higher claims) |

**Honest status of the field:** descriptive binning + mild lens trends are **published**; a single derived mechanism that *predicts* the slope a priori is **not** established. Selection, calibration, and “look-elsewhere” effects are openly discussed (e.g. TDCOSMO systematics papers).

### 2.4 Number (point 4)

\[
\frac{H_0^{\mathrm{SH0ES}}}{H_0^{\mathrm{Planck}}}\approx\frac{73}{67.4}\approx 1.083.
\]
Literature “running” claims aim to connect high-\(H_0\) at low \(z\) to low-\(H_0\) at high \(z\) in a continuous way. **We do not re-fit SN bins here.**

---

## 3. Geometry in this programme (no free dial)

Fiducial flat \(\Lambda\)CDM: \(H_0=67.4\), \(\Omega_m=0.315\), \(\Omega_\Lambda=0.685\).  
Reproduce: `python scripts/h0_running_geometry.py`.

### 3.1 Cosmic path length and patch counts

| \(z\) | \(\chi(z)\) [Mpc] | \(\chi/L_H\) | \(N=\chi/R_8\) (\(R_8\approx 11.87\) Mpc) | \(\sqrt{N}\) |
|:------|:------------------|:-------------|:------------------------------------------|:-------------|
| 0.15 (local ladder depth) | \(\sim 640\) | 0.14 | \(\sim 54\) | \(\sim 7\) |
| 0.30 (\(\approx z_{\mathrm{eq}}\)) | \(\sim 1240\) | 0.28 | \(\sim 104\) | \(\sim 10\) |
| 0.50 | \(\sim 1950\) | 0.44 | \(\sim 164\) | \(\sim 13\) |
| 0.70 | \(\sim 2590\) | 0.58 | \(\sim 218\) | \(\sim 15\) |
| 1.50 (path RMS atlas) | \(\sim 4480\) | 1.01 | \(\sim 378\) | \(\sim 19\) |

Matter–DE equality: \(z_{\mathrm{eq}}=(\Omega_\Lambda/\Omega_m)^{1/3}-1\approx\mathbf{0.30}\).

### 3.2 What matches the literature window — and what does not

| Programme scale | Redshift class | Relation to H0-running window \(z\sim 0.5\)–\(0.7\) |
|:----------------|:---------------|:-----------------------------------------------------|
| \(z_{\mathrm{eq}}\approx 0.30\) | DE starts to dominate | **Adjacent** to reported transition (same late-time era, not identical) |
| Path \(N=\chi/R_8\gtrsim 100\) | \(z\gtrsim 0.3\) | Path accumulation of mesoscopic patches becomes large |
| NP path RMS (sister atlas) | \(z_s\sim 1.5\) | Deeper; uses same \(\sqrt{\chi/\ell_*}\) logic |
| R1 open kernel \(\ell_*\sim\mathrm{Mpc}\) | IR grain | **Same scale class** as \(R_8\); **no** derived \(H_0(z)\) |

**Legitimate reading:** two open stories (mesoscopic DE grain; \(H_0\) evolving with probe depth) both care about the **late, post-equality, few-Gpc path** regime.  
**Illegitimate reading:** “therefore \(\ell_*=R_8\) explains the Hubble tension.”

---

## 4. Bridge hypothesis (declared open — same discipline as R1d)

**H-bridge (hypothesis class, not a theorem):**

> If the DE residual sector has a mesoscopic counting / correlation cell \(\ell_*\) of structure scale, then **path-integrated** observables (lensing time delays, distance residuals, slip RMS) acquire a depth-dependent bias once \(N=\chi(z)/\ell_*\) is large — i.e. once probes leave the strictly local \(H(z)\approx H_0\) regime. That can *look like* a running of inferred \(H_0\) with redshift **without** changing early-universe sound horizon physics.

| Requirement to promote H-bridge to a claim | Status |
|:-------------------------------------------|:-------|
| Derive map \(\ell_*\to\delta H_0(z)\) or \(\delta D(z)\) | **Absent** |
| Predict ratio \(\approx 1.083\) a priori | **Absent** |
| Predict transition near \(z\sim 0.5\)–\(0.7\) | **Only scale-class coincidence** with \(z_{\mathrm{eq}}\) and path \(N(R_8)\) |
| Survive BAO residual ceiling \(\sigma_X<1.5\times 10^{-4}\) | Must be checked a posteriori |
| Fit \(\ell_*\) to SH0ES–Planck gap | **Forbidden** (BOUNDARY) |

This is the same pattern as R1d \(\leftrightarrow R_8\): **shared scale language**, not a fitted solution.

---

## 5. Brachistochrone language — what to keep, what to drop

| Keep | Drop |
|:-----|:-----|
| Multi-path, multi-time (lensing delays) | Massive particle cycloid as cosmology |
| Local = short path, \(H\approx\mathrm{const}\) | “Gravity fixed” = Newtonian \(g\) wire |
| Longer baseline → different inferred \(H_0\) in literature | Claim that Bernoulli calculus derives \(73/67\) |
| Geometry of \(\chi(z)/\ell_*\) | Free \(10^{56}\) or DESI-tuned \(\ell_*\) |

---

## 6. Claim checklist

| ID | Claim | Evidence |
|:---|:------|:---------|
| H1 | H0LiCOW \(H_0=73.3^{+1.7}_{-1.8}\) | arXiv:1907.04869 |
| H2 | Mild \(H_0\)–\(z_d\) trend \(\sim 1.9\sigma\) in that sample | same |
| H3 | Dainotti et al. report decreasing effective \(H_0\) in SN bins | arXiv:2103.02117 |
| H4 | \(73/67.4\approx 1.083\) | arithmetic |
| H5 | \(z_{\mathrm{eq}}\approx 0.30\); \(\chi(z)\), \(N=\chi/R_8\) as in §3 | script |
| H6 | H-bridge is **hypothesis class** only | this note |

| Non-claim | |
|:----------|:--|
| N-H1 | Brachistochrone solves Hubble tension |
| N-H2 | Mesoscopic grain **derived** from H0 running |
| N-H3 | Programme predicts \(1.083\) |
| N-H4 | H0 running is settled physics (it is contested) |

---

## 7. Next honest steps (if pursued)

1. **External:** freeze a public H0-running table (Dainotti bins / Krishnan compilations) as CSV with arXiv tags — no re-fit.  
2. **Internal:** toy operator \(\delta D(z)/D(z)=f(\sqrt{\chi/\ell_*})\) with \(\ell_*\) from R1 landscape **fixed a priori**, then compare shape to published trend (a posteriori).  
3. **Joint:** same \(\ell_*\) must also obey sister \(\sigma_X\) and path-RMS wall.  
4. **Experiment:** more TDCOSMO systems + SN binning with pre-registered bins (kill look-elsewhere).

---

## 8. One-sentence verdict

> The brachistochrone metaphor becomes real as **time-delay multi-path light** and as **H0-running literature**; the number to match is \(\sim 1.08\); the open-kernel grain sits in the **same late-time depth class** as the reported transition — a bridge worth building carefully, not a solution already in hand.

---

## 9. Reproduce

```bash
cd measurable-stochastic-vacuum
python scripts/h0_running_geometry.py
pytest -q
```

---

*End of H0 / brachistochrone / open-kernel bridge note.*
