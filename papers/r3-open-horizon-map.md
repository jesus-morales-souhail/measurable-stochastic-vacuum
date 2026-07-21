# WP2 — R3: mapa abierto del horizonte (ganancia o teorema de no-ganancia)

**Autor:** Jesús Morales Souhail · ORCID [0009-0000-7637-1818](https://orcid.org/0009-0000-7637-1818)  
**Programa:** measurable-stochastic-vacuum  
**Estado:** Primera derivación de WP2 · no es detección  
**Fecha:** julio 2026  
**Código:** [`scripts/r3_open_horizon_map.py`](../scripts/r3_open_horizon_map.py)  
**Input (WP1):** [`r1-counting-principle.md`](r1-counting-principle.md) — $\sigma_{0,\mathrm{eff}}$ como **dato de principio**, no dial  
**Cumple:** A1, A3, A4 (R3 acotado), A5, A6  

---

## 1. Pregunta

WP1 fija (como paisaje) que una semilla telescópica exige celda de contaje **mesoscópica**.  
WP2 pregunta:

> Dada una semilla $\sigma_{0,\mathrm{eff}}$ (de R1), ¿puede la dinámica de un **sistema abierto** al horizonte convertirla en residual BAO medible $A_0$ o $\sigma_{\mathrm{res}}$ **sin** free lunch, o queda demostrada una **cota de ganancia**?

El audit del repo hermano ya mató: desqueezing $e^{2r}\sim\mathcal{O}(10)$, freeze-out tardío ganancia $=1$, $\sqrt{N}$ doble-contado. Aquí se **formaliza** el mapa residual y se separan dos salidas honestas:

| Salida | Significado |
|:-------|:------------|
| **Ganancia acotada** | $G \le G_{\max}$ derivado; si $\sigma_{0,\mathrm{eff}}$ es Sorkin, residual sigue muerto |
| **Ganancia útil** | Solo si R1 ya puso $\sigma_{0,\mathrm{eff}}$ en la banda; R3 no multiplica $10^{56}$ |

---

## 2. Residual de camino (definición operativa)

En el corpus DESI, el residual path-integrated tiene la forma (pequeño $\theta$):

$$
\sigma_{\mathrm{res}} = A_0\, e^{-\theta\,\Delta x},
$$

con $x=\ln a$ y $\Delta x$ del orden de la trayectoria en $z\sim 0$–$2$ ($\Delta x =\mathcal{O}(1)$ en aceleración tardía, **no** $\sim 60$ e-folds inflacionarios).

Identificamos la **semilla de entrada** del proceso residual con el output de WP1:

$$
A_0 \;\equiv\; G\,\sigma_{0,\mathrm{eff}},
$$

donde $G$ es la **ganancia neta del mapa abierto** (R3). El caso unitario / cerrado es $G=1$.

**Prohibido (A3):** poner $G=10^{56}$ a mano.

---

## 3. Tres capas de ganancia (todas derivadas o acotadas)

### 3.1 Capa U — unitaria / estiramiento de fondo

En un parche cerrado, el estiramiento cosmológico redistribuye modos pero **no** convierte $\sigma_0\sim 10^{-61}$ en $10^{-5}$ con $\Delta x\sim\mathcal{O}(1)$:

$$
G_U \sim e^{c\,\Delta x} \quad\text{con}\quad \Delta x\sim\mathcal{O}(1) \;\Rightarrow\; G_U =\mathcal{O}(1)\text{–}\mathcal{O}(e).
$$

(El factor $e^{60}$ es de **inflación**, otro régimen y otra semilla natural $\sim H/M_{\mathrm{Pl}}$, no Sorkin tardío.)

**Teorema de no-ganancia (capa U, tardío):**  
con $\Delta x=\mathcal{O}(1)$, $G_U$ no cierra el gap Sorkin $\to$ Euclid.

### 3.2 Capa F — freeze-out de $\theta$ (Route 2 del corpus hermano)

Si $\theta\to 0$ tras “salida de horizonte” tardía, el residual se **congela**, no se engorda. El scan del repo hermano dio:

$$
\frac{\mathrm{rms}(X_f)}{\sigma} =\mathcal{O}(1),\qquad
\frac{\mathrm{rms}_{\mathrm{freeze}}}{\mathrm{rms}_{\mathrm{restore}}} = 1.000.
$$

**Teorema de no-ganancia (capa F):** freeze-out tardío $\Rightarrow G_F=1$ (preserva semilla).

### 3.3 Capa O — abierto / desqueezing (Lindblad)

Un baño de horizonte puede des-squeezear o relajar un modo con tasa $\gamma_{\mathrm{open}}$. El mapa de trabajo del corpus hermano es:

$$
\gamma_{\mathrm{open}} \;\longleftrightarrow\; \theta H_0
\quad\text{(correspondencia de escalas, no identidad de unidades).}
$$

La ganancia de intensidad de un squeeze parameter $r$ es $G_O \sim e^{2r}$.  
Para $r\sim\mathcal{O}(1)$ (régimen “suave”, sin nueva escala):

$$
G_O \sim 10^{0}\text{–}10^{1} \ll 10^{56}.
$$

**Teorema de no-ganancia (capa O, $r=\mathcal{O}(1)$):**  
desqueezing cosmológico suave **no** salva la semilla de Sorkin.

Para que $G_O\sim 10^{56}$ haría falta $r\sim \tfrac12\ln(10^{56})\sim 64$, es decir **otra física de escala** (equivalente a redefinir la semilla o el número de e-folds) — y eso **debe** derivarse, no fijarse al número DESI (A5).

---

## 4. Mapa compuesto (fórmula de programa)

$$
\sigma_{\mathrm{res}} = G_U\, G_F\, G_O\, \sigma_{0,\mathrm{eff}}
\;\approx\;
G_O\,\sigma_{0,\mathrm{eff}}
\quad (G_U\sim\mathcal{O}(1),\; G_F=1).
$$

Con la cota suave $G_O \le G_O^{\max}\sim 20$ ($r\le 1.5$):

| Semilla (WP1) | $G_O=1$ | $G_O=20$ | ¿Entra en banda $\sim 10^{-5}$–$10^{-4}$? |
|:--------------|:--------|:---------|:------------------------------------------|
| Sorkin $1.2\times 10^{-61}$ | $1.2\times 10^{-61}$ | $2.4\times 10^{-60}$ | **No** (cero estructural) |
| $\sigma_{0,\mathrm{eff}}=10^{-5}$ (celda Mpc de WP1) | $10^{-5}$ | $2\times 10^{-4}$ | **Sí** (borde DESI: test a posteriori) |
| $\sigma_{0,\mathrm{eff}}=10^{-6}$ | $10^{-6}$ | $2\times 10^{-5}$ | Marginal / Euclid |

**Lectura estructural:**

> R3 **no sustituye** a R1. R3 como mucho multiplica por $\mathcal{O}(10)$ en el régimen suave. La medibilidad exige que WP1 ya haya sacado la semilla del abismo planckiano.

Eso **no** es un fracaso de R3: es el **teorema de no free lunch en sistemas abiertos suaves**, alineado con Act III del corpus empírico.

---

## 5. Qué faltaría para una “ganancia útil grande” (sin numerología)

Solo tres salidas legítimas (A3):

1. **R1 resuelto:** un principio fija $\ell_*\sim$ kpc–Mpc $\Rightarrow \sigma_{0,\mathrm{eff}}$ ya en banda; entonces $G_O\sim\mathcal{O}(1)$ basta.  
2. **R3 fuerte derivado:** una master equation de horizonte predice $r\gg 1$ o un número de ciclos de desqueezing $N_{\mathrm{cyc}}$ con $e^{2r N}$ anclado en física del baño (temperatura de horizonte, tasa de escape), **antes** de mirar DESI.  
3. **Cierre honesto:** demostrar $G_O^{\max}=\mathcal{O}(10)$ en toda la clase de baños admisibles $\Rightarrow$ el programa se queda en “límites + geometría + semilla mesoscópica como hipótesis abierta”.

La opción “pongo $r=64$” está **prohibida**.

---

## 6. Ceros estructurales (A6) añadidos por R3

1. **Sorkin + abierto suave** $\Rightarrow$ residual $\ll 10^{-5}$ (null telescópico es teorema).  
2. **Freeze-out solo** $\Rightarrow$ no hay amplificación (confirma Route 2 hermana).  
3. **Operador equivocado** (lab) $\Rightarrow$ R3 no aplica: no hay baño de horizonte en una pupila.

---

## 7. Comparación a posteriori con DESI (A5)

Sea $\sigma_{\mathrm{res}}^{\mathrm{th}} = G_O\,\sigma_{0,\mathrm{eff}}$.

| Predicción | Test |
|:-----------|:-----|
| $\sigma_{\mathrm{res}}^{\mathrm{th}} \ll 10^{-5}$ | Compatible con null DESI; predice null Euclid en residual |
| $10^{-5} \lesssim \sigma_{\mathrm{res}}^{\mathrm{th}} < 1.5\times 10^{-4}$ | Compatible con cota; Euclid puede decidir |
| $\sigma_{\mathrm{res}}^{\mathrm{th}} > 1.5\times 10^{-4}$ | Tensión con DESI (descartar o añadir damping $\theta$ fuerte) |

Nunca se ajusta $G_O$ ni $\ell_*$ para sentarse justo bajo $1.5\times 10^{-4}$.

---

## 8. Estado de R3 en la tabla A4

| Pieza | Estado |
|:------|:-------|
| $G_F=1$ (freeze tardío) | **Derivado / machine-checked** (repo hermano + aquí) |
| $G_U=\mathcal{O}(1)$ para $\Delta x=\mathcal{O}(1)$ | **Derivado** (orden de magnitud) |
| $G_O\sim e^{2r}$ con $r=\mathcal{O}(1)$ $\Rightarrow$ $G_O=\mathcal{O}(10)$ | **Acotado** (audit + este mapa) |
| Master equation microscópica del baño de horizonte | **Ausente** (abierto; no inventada) |
| $r\gg 1$ cosmológico | **Ausente** salvo nueva derivación |

**Estado R3:** teorema de no-ganancia en el régimen suave **cerrado**; dinámica de baño “fuerte” **no construida** (y no se finge).

---

## 9. Implicación para el programa completo

```
WP1:  σ_{0,eff} = (ℓ_*/L)^{d/2}     →  paisaje (Planck = cero; Mpc = banda)
WP2:  σ_res ≈ G_O σ_{0,eff}         →  G_O = O(10) en régimen suave
        ⇒  medibilidad ⇔ R1 mesoscópico (o R3 fuerte aún no derivado)
WP3:  slip hereda la misma A_0      →  sin R1, sigue starved
```

El null DESI **confirma** el cero Sorkin+suave.  
No obliga a abandonar el programa: obliga a **no mentir sobre la ganancia** y a resolver $\ell_*$ (R1a–c) o a cerrar en geometría.

---

## 10. Siguiente

- **Paralelo:** elegir un candidato R1a/b/c y derivar $\ell_*$.  
- **WP3:** `r2-slip-from-same-sector.md` con $A_0 = G_O\sigma_{0,\mathrm{eff}}$ del mapa de aquí.  

---

*Fin de WP2 (mapa abierto + teoremas de no-ganancia en régimen suave).*
