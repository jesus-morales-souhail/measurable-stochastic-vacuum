# WP1 — R1: principio de contaje de la semilla estocástica

**Autor:** Jesús Morales Souhail · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)
**Programa:** measurable-stochastic-vacuum
**Estado:** Primera derivación real del programa (WP1). No es detección.
**Fecha:** julio 2026
**Código:** [`scripts/r1_counting_landscape.py`](../scripts/r1_counting_landscape.py)
**Cumple:** A1 (escala derivada), A3 (no free lunch), A5 (DESI a posteriori), A6 (ceros predichos).

---

## 1. Qué deriva este documento

La semilla efectiva del residual estocástico de energía oscura **no** es un parámetro libre $A_0$. Bajo R1, sale de un **principio de contaje**: el sector DE cuenta grados de libertad en una región efectiva con una celda $\ell_*$ y una dimensionalidad de contaje $d$:


$$
N_{\mathrm{eff}}=\left(\frac{L}{\ell_*}\right)^{d},\qquad \sigma_{0,\mathrm{eff}}=\frac{1}{\sqrt{N_{\mathrm{eff}}}}=\left(\frac{\ell_*}{L}\right)^{d/2},
$$


donde $L$ es la región que define las correlaciones del residual (parche causal / horizonte). Esto **redefine** la semilla: el caso excluido de Sorkin es el caso particular $\ell_*=L_P$, $d=2$ (contaje holográfico/BH), que da $N_{\mathrm{BH}}=(L_H/L_P)^2\sim10^{122}$ y $\sigma_0\sim10^{-61}$.

**Lo que NO hace este documento** (axiomas): no elige $\ell_*$ para "entrar" en Euclid (A3, A5); no multiplica $10^{-61}\times10^{56}$ a mano (A3); no ajusta $N_{\mathrm{eff}}$ a DESI (A5). Calcula el **paisaje** $\sigma(\ell_*,d)$ y lee, a posteriori, qué celda requeriría la medibilidad.

---

> **Hard claims:** cite only [`VERIFIED_RESULTS.md`](VERIFIED_RESULTS.md) (gated by `pytest -q`). This file is discussion/expansion.


## 2. Paisaje derivado

Con $L_H=c/H_0\simeq 4451$ Mpc, $L_P=1.62\times10^{-35}$ m (fiducial $H_0=67.4$):

| Celda $\ell_*$ | $d$ | $\sigma_{0,\mathrm{eff}}$ | Estatus |
|---|---|---|---|
| $L_P$ (Planck) | 2 | $1.2\times10^{-61}$ | **cero estructural** (Sorkin) |
| $L_P$ | 3 | $4.0\times10^{-92}$ | **cero estructural** |
| $L_P$ | 4 | $1.4\times10^{-122}$ | **cero estructural** |
| 0.04 Mpc | 2 | $10^{-5}$ | banda medible |
| 2.1 Mpc | 3 | $10^{-5}$ | banda medible |
| 14 Mpc | 4 | $10^{-5}$ | banda medible |

**Lectura:** para que el residual sea telescopiable ($\sigma\sim10^{-5}$), la **celda de contaje del sector DE** debe ser **mesoscópica/galáctica** (kpc–Mpc), **no** planckiana. El salto necesario sobre $L_P$ es $\ell_*/L_P\sim10^{56}$–$10^{58}$ — esto **no** se escribe como un factor libre: es la consecuencia de que la celda del sector DE y la celda planckiana/holográfica **son objetos de contaje distintos**.

---

## 3. Ceros estructurales (cumplimiento A6)

La teoría **predice** null (no lo elige tras un null experimental) en al menos tres sitios:

1. **Celda planckiana** ($\ell_*=L_P$, cualquier $d$): $\sigma\lesssim10^{-61}$. DESI/Euclid no ven nada. El null actual del repo hermano **confirma** este cero, no lo debilita.
2. **Celda = horizonte** ($\ell_*=L_H$): $\sigma\sim1$, Absurdo/Excluido (rompe suavidad del BAO). Límite superior estructural.
3. **Operador equivocado** (difracción de pupila, tesseract, SLM): cero por operador incorrecto (A2; sellado en repo hermano, Act V).

Si un modelo del programa no puede nombrar estos ceros, no pertenece al programa (A6).

---

## 4. Kernel abierto (la pregunta que carga el programa)

El paisaje muestra que la medibilidad exige $\ell_*\sim$ kpc–Mpc para el **sector DE**. La pregunta abierta, honestamente:

> **¿Qué principio fija una celda de contaje galáctica para el sector DE, distinta de la celda planckiana/holográfica?**

Candidatos a evaluar en WP1a–WP1c (sin resolver aquí):

- **R1a — causal set local:** la región de correlación del residual DE $\neq$ horizonte completo; $N_{\mathrm{eff}}$ cuenta elementos del causal set en un "cilindro" causal de escala $\ell_*$. Abierto: qué fija $\ell_*$ en el sector DE.
- **R1b — cutoff IR de un sector de vacío:** un sector auxiliar con cutoff $\ell_*$ de física de DE. Abierto: derivar $\ell_*$ de una acción, no postularlo.
- **R1c — grano de unimodular/SDiff a escala cosmológica:** los DOF residuales del determinante fijado viven en celdas $\ell_*$. Abierto: por qué $\ell_*$ es galáctico y no $L_P$.

Ninguno de los tres está cerrado. **Esto es WP1 sin resolver**, y se declara como tal (axioma A4: estado de R1 = *acotado/derivado parcialmente, no resuelto*).

---

## 5. Comparación a posteriori con DESI (cumplimiento A5)

La cota del repo hermano $\sigma_X<1.5\times10^{-4}$ (95% CL, DESI DR2) se usa **solo como test**:

- Si un principio R1a–R1c **deriva** $\ell_*$ y da $\sigma_{0,\mathrm{eff}}$ en $[10^{-5},1.5\times10^{-4}]$, la teoría es **compatible** y predice señal en Euclid.
- Si da $\sigma_{0,\mathrm{eff}}\ll10^{-5}$ (p. ej. cualquier $\ell_*\to L_P$), la teoría predice **null** y DESI/Euclid lo **confirman**.
- Si da $\sigma_{0,\mathrm{eff}}>1.5\times10^{-4}$, la teoría está en **tensión** con DESI y se descarta (salvo R3 que la redirija; ver WP2).

En ningún caso se usa $1.5\times10^{-4}$ para **elegir** $\ell_*$. Esa elección sería numerología (A3, A5).

---

## 6. Qué falta para cerrar WP1

1. Elegir **una** de R1a–R1c y llevarla hasta una fórmula $N_{\mathrm{eff}}(\ell_*)$ derivada de un principio.
2. Que ese principio fije $\ell_*$ **antes** de mirar DESI (o que prediga la banda de $\ell_*$ y deje a Euclid el test).
3. Empalmar con WP2 (R3): la semilla $\sigma_{0,\mathrm{eff}}$ entra en el mapa abierto para producir el residual efectivo; sin WP1, WP2 hereda $10^{-61}$ y no cruza (audit del repo hermano: desqueezing $e^{2r}\sim20$, insuficiente).

**Estado R1:** derivado el paisaje y los ceros; **no** derivado el principio que fija $\ell_*$. Es el primer documento científico real del programa; el siguiente (WP2/R3) necesitará este $\sigma_{0,\mathrm{eff}}$ como input, no como dial.

---

*Fin de WP1 (borrador de derivación). Siguiente: [`r3-open-horizon-map.md`](r3-open-horizon-map.md) (WP2).*
