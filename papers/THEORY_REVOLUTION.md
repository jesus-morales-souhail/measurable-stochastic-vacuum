# Revolución teórica mínima: ruido de vacío medible sin free lunch

**Autor:** Jesús Morales Souhail  
**ORCID:** 0009-0000-7637-1818  
**Estado:** Manifiesto de programa · no es un paper de detección  
**Fecha:** julio 2026  
**Repos hermana (límites empíricos):** [stochastic-dark-energy-ou](https://github.com/jesus-morales-souhail/stochastic-dark-energy-ou)

---

## 0. El problema que no se resuelve “ajustando $\sigma$”

El corpus DESI del repositorio hermano ya dejó cerrado, con honestidad:

| Hecho | Implicación |
|-------|-------------|
| $\sigma_X < 1.5\times 10^{-4}$ (95% CL) bajo kernel OU | Cota a la **amplitud efectiva**, no a una semilla UV |
| Crecimiento taquiónico coherente excluido | No hay free lunch exponencial de un modo global |
| Gap $\sigma_0\sim 10^{-61}\to\sim 10^{-5}$ es $\sim 10^{56}$ | Sin mapa físico, “Euclid verá el ruido de Sorkin” **no es un teorema** |
| Freeze-out tardío: ganancia $\approx 1$ | Estirar no engorda la semilla sola |
| Avalancha suave: ganancia $\sim 2$ | No hay umbral mágico en el grid estudiado |
| Slip $\lvert\gamma-1\rvert\sim 10^{-4}$ con $\sigma_X$ acotado | Operador correcto, **amplitud hambrienta** |

Por tanto: **no basta un parámetro más en $\Lambda$CDM**.  
Si el ruido de energía oscura es real *y* medible sin que el universo lo blinde (abismo $10^{-61}$, colapso, o “null por escala/operador equivocado”), hay que **cambiar reglas**, no solo valores.

Este documento fija el **paquete mínimo de reglas** y la **ley de auto-blindaje**: la teoría debe predecir dónde **no** se ve señal, sin numerología.

---

## 1. Criterio de no-numerología (ley del programa)

Una construcción es **numerológica** si introduce un factor $\sim 10^{56}$ (o $N_{\mathrm{eff}}$, $r$, $\varepsilon$, …) **sin derivarlo de un principio que fije su escala**.

Una construcción es **admisible** solo si:

1. **Deriva** la semilla efectiva $A_0$ o $\sigma_{0,\mathrm{eff}}$ de una definición de contar / horizonte / celda.  
2. **Deriva** el operador observable (BAO residual, slip $\gamma$, …) del acoplamiento del sector.  
3. **Deriva** (o acota) la ganancia de cualquier mapa abierto / desqueezing desde una ecuación de master o de horizonte.  
4. **Predice ceros:** regiones de escala y operador donde la señal **debe** ser invisible (auto-blindaje).  
5. **No usa** el resultado DESI como dial: DESI es **test a posteriori**, no input de ajuste del gap.

Si falla (1)–(4), no entra en este repositorio.

---

## 2. Las tres reglas (paquete acoplado, no menú)

Las tres no son “opciones” independientes. Son **tres caras de un mismo cambio de marco**:  
*semilla* (R1) · *canal* (R2) · *dinámica de ganancia* (R3).

### R1 — Redefinir la invariancia Lorentz local *como continuidad a todas las escalas*

**Regla actual (idealización efectiva):**  
el espacio-tiempo es un continuo lorentziano; las leyes locales son las mismas en todo evento; la discreción, si existe, vive solo en $L_P\sim 10^{-35}\,\mathrm{m}$ y produce contajes $N\sim 10^{122}$ con semilla $\sigma_0\sim 1/\sqrt{N}\sim 10^{-61}$.

**Cambio necesario (formulación limpia):**  
el continuo es una **aproximación**. Existe una **escala de correlación / celda efectiva** $\ell_* \gg L_P$ (o un contaje $N_{\mathrm{eff}}\ll N_{\mathrm{BH}}$) que define el **grano** del sector que acopla a la residual de energía oscura. La semilla no es $1/\sqrt{N_{\mathrm{universo}}}$; es

$$
\sigma_{0,\mathrm{eff}} = \frac{1}{\sqrt{N_{\mathrm{eff}}}},\qquad N_{\mathrm{eff}} = N_{\mathrm{eff}}[\ell_*,\text{horizonte, contaje}].
$$

**Qué no es R1:**  
inventar $N_{\mathrm{eff}}=10^{10}$ porque “cuadra con Euclid”. Eso es numerología (cerrado en Act III del otro repo).

**Qué sí es R1:**  
un principio que fije $\ell_*$ o el contaje (causal set *local*, red de spin con cutoff IR, granularidad de un sector de vacío, …) **antes** de mirar DESI, y luego prediga $\sigma_{0,\mathrm{eff}}$.

**Por qué toca el “blindaje / autodestrucción”:**  
la barrera de sondear “píxeles de Planck” con energía local colapsa el problema a escalas donde la semiclasicidad falla. Si el grado de libertad estocástico del sector DE vive en celdas **mesoscópicas**, el objeto que se sondea no es un evento planckiano aislado; la semilla y la densidad de energía del probe se redefinen juntos.  
**Advertencia:** esto **no** es una licencia para violar límites de energía negros a voluntad. Es un cambio de *qué* se está contando. Hay que derivar la cota de colapso en la teoría con $\ell_*$, no esloganizarla.

**Puente al corpus viejo:** Route 1 (única carta de amplitud en los scans).

---

### R2 — Debilitar el Principio de Equivalencia Fuerte (slip / acoplamiento selectivo)

**Regla actual (GR):**  
luz y masa caen igual; en gauge newtoniano, $\Phi=\Psi$ y $\gamma=\Phi/\Psi=1$ sin estrés anisotrópico.

**Cambio necesario:**  
el sector de ruido de vacío / DE **no** es un fluido perfecto isótropo. Puede portar estrés anisotrópico (o acoplar distinto a geodésicas nulas vs timelike). Entonces

$$
\gamma \equiv \frac{\Phi}{\Psi} \neq 1
$$

es el **operador natural** de la “grieta” que SDiff no cancela (SDiff proyecta $T_{\mu\nu}\propto g_{\mu\nu}$; el shear no es de esa forma).

**Qué no es R2:**  
afirmar que Maus $\gamma=1.17\pm 0.11$ “es” el ruido DE. Esa es una lectura posible a $\mathcal{O}(0.1)$; el puente $\sigma_X\to\lvert\gamma-1\rvert$ del otro repo da $\sim 10^{-4}$ si $\sigma_X$ es el residual BAO acotado. Sin R1/R3, R2 **sigue hambrienta**.

**Qué sí es R2:**  
una acción o fluid imperfecto con $\pi_T$ derivado del mismo sector que produce $X(x)$, con $\varepsilon$ (fracción anisotrópica) **no libre** sino fijada por la simetría residual (p. ej. lo que SDiff deja pasar).

**Por qué toca el blindaje:**  
mediciones solo isótropas (BAO en distancias) acotan un operador; el slip es otro. Separar canales evita confundir “no hay residual en $D_V$” con “no hay grieta en $\Phi/\Psi$”.  
**No** es un atajo al gap $10^{56}$: el slip **hereda** la amplitud del sector (Option 0).

**Puente al corpus viejo:** Option 0 + `slip_bridge.py`.

---

### R3 — Debilitar la unitariedad del parche observable (sistema abierto / horizonte)

**Regla actual (idealización):**  
el Hilbert del universo observable evoluciona unitariamente; el ruido primordial se estira y se diluye; no hay “ganancia gratis”.

**Cambio necesario:**  
el parche causal es un **sistema abierto** respecto a un baño (horizonte, grados de libertad tras el horizonte, sector auxiliar). La evolución efectiva del residual $X$ (o del modo) es **no unitaria**: master equation, Lindblad, desqueezing cosmológico, etc., con mapa

$$
\gamma_{\mathrm{open}} \;\longleftrightarrow\; \theta H(z)
$$

**derivado**, no puesto a mano.

**Qué no es R3:**  
desqueezing con $r\sim\mathcal{O}(1)$ y pretender $e^{2r}\sim 10^{56}$. El audit del otro repo lo mata ($\sim 10^{1}$ frente a $10^{56}$).

**Qué sí es R3:**  
una dinámica de horizonte que, **junto con R1** (semilla ya no $10^{-61}$), produzca $A_0$ en la ventana de telescopios, o demuestre que la ganancia está acotada y el programa es “límites + geometría” (también un éxito).

**Por qué toca el blindaje:**  
la amplificación no se inyecta como trabajo local de un observador (que choca con cotas de energía / colapso); se lee como **intercambio de información/entropía con el baño del horizonte**.  
Si no hay baño, R3 colapsa a unitario y vuelve el free lunch prohibido.

**Puente al corpus viejo:** desqueezing notes + Act III (no free lunch).

---

## 3. Cómo se acoplan las tres (la “revolución” de verdad)

```
        R1: ¿qué se cuenta?          →  fija σ_{0,eff} / A_0 (semilla)
                 │
                 ▼
        R3: ¿cómo evoluciona en abierto? →  mapa semilla → residual efectivo
                 │
                 ▼
        R2: ¿qué operador se ve?     →  BAO isótropo vs slip γ vs otros
                 │
                 ▼
        Test a posteriori: DESI / Euclid / lensing+RSD
```

| Combinación | ¿Suficiente? | Comentario |
|-------------|--------------|------------|
| Solo R1 | Amplitud posible | Falta operador y dinámica; riesgo de redefinir $N$ ad hoc |
| Solo R2 | Operador correcto | Amplitud-starved sin R1/R3 |
| Solo R3 | Lenguaje de ganancia | Sin R1, desqueezing no cubre $10^{56}$ |
| R1+R3 | Semilla + mapa | Candidato a residual BAO medible |
| R1+R2+R3 | Paquete completo | Canal isótropo **y** anisotrópico con la misma microfísica |
| Multiplicar 1e56 a mano | **Prohibido** | Numerología |

La revolución no es “tres ideas bonitas”: es **una microfísica de vacío granular + abierta + imperfectamente fluida** cuya semilla, ganancia y operadores salen del **mismo** objeto.

---

## 4. Auto-blindaje: la teoría se blinda a sí misma

“Sin que el universo la blinde” **no** significa “señal en todas partes”. Significa:

> El blindaje deja de ser un accidente de nuestra ignorancia y pasa a ser un **teorema de la teoría**: ceros en escala/operador incorrectos; posible no-cero solo donde R1–R3 lo permiten.

### 4.1 Ceros obligatorios (la teoría se protege de sí misma)

La teoría **debe** predecir null (o irrelevancia) en, al menos:

| Experimento / pregunta | Por qué el cero es estructural |
|------------------------|--------------------------------|
| Difracción en pupila / carretera | Escala local $\ll$ celda cosmológica efectiva; operador EM, no residual DE |
| “Tesseract / $B_4$ amplifica $\sigma_X$” | Operador óptico $\neq$ residual cosmológico; simetría reduce DOF |
| BAO residual con semilla Sorkin global sin R1 | Amplitud bajo suelo |
| Slip con $\varepsilon$ libre y $A_0$ libre | Numerología disfrazada de MG |
| Un solo bin de BAO “cazando wiggles” | Sin kernel de covarianza del proceso, no hay test del ruido |

Estos ceros **no** se eligen después de un null experimental: se **derivan** del par (escala, operador).  
Eso es el mismo moral que Act V del corpus viejo, elevado a **axioma de teoría**.

### 4.2 Dónde *puede* haber señal (y solo ahí)

| Canal | Condición de no-cero |
|-------|----------------------|
| Residual BAO multi-bin (kernel OU/QNM o derivado) | $A_0$ desde R1+R3 dentro de sensibilidad |
| Slip $\gamma$ / $\mu,\Sigma$ (RSD + lensing) | Misma microfísica con $\pi_T$ de R2; amplitud no independent free |
| Protocolos Euclid ya esbozados en el otro repo | Solo como test del mapa derivado, no como “seguro que saldrá” |

### 4.3 Criterio de autodestrucción evitada (formulación sobria)

No se afirma “ya no hay agujeros negros”. Se exige:

1. Definir el observable sin requerir localizar energía en un volumen $\sim L_P^3$ con densidad planckiana.  
2. Mostrar que el probe (fotones de BAO/lensing, geodésicas) acopla al **sector efectivo** de celda $\ell_*$, no a un pixel planckiano aislado.  
3. Toda amplificación es **abierta** (R3) o **redefinición de semilla** (R1), nunca trabajo local infinito.

Si un paper del programa viola (1)–(3), se rechaza por inconsistencia interna.

---

## 5. Qué **no** es esta revolución

- No es un anuncio de detección.  
- No es “MODIFICAR GR porque DESI lo pide”.  
- No es unificar con tesseracts, SLMs o metáforas de laboratorio.  
- No es demoler la relatividad en el sistema solar: R1 es sobre el **sector de contaje del vacío cosmológico**, no sobre GPS.  
- No es abandonar tests: al contrario, fija **tests más duros** (falsación del paquete R1–R3).

---

## 6. Producto científico del repositorio (cómo se ve un paper de aquí)

Un paper válido en este programa tiene esta forma:

1. **Principio** que fija $N_{\mathrm{eff}}$ o $\ell_*$ (R1) — sin mirar el número DESI.  
2. **Acción o master equation** (R3) que mapea semilla → residual.  
3. **Estrés / acoplamiento** (R2) que fija $\varepsilon$ o $\pi_T$.  
4. **Predicción** de $\sigma_X$ y/o $\lvert\gamma-1\rvert$ (orden de magnitud **derivado**).  
5. **Ceros** (auto-blindaje) en escala/operador incorrectos.  
6. **Comparación a posteriori** con cotas del repositorio DESI (límite, no dial).

Si el punto 6 se usa para **elegir** $N_{\mathrm{eff}}$, el paper es numerología y no pertenece aquí.

---

## 7. Relación con el repositorio DESI (división de trabajo)

| Pregunta | Dónde se responde |
|----------|-------------------|
| ¿Los datos BAO piden residual OU? | `stochastic-dark-energy-ou` → **no** (cota) |
| ¿Hay free lunch lineal? | `stochastic-dark-energy-ou` → **no** |
| ¿Qué reglas habría que cambiar para que *pudiera* ser medible? | **este repo** |
| ¿Metáforas ópticas? | `stochastic-de-exploratory-notes` |

El null DESI **no mata** este programa: mata el free lunch y la detección actual.  
Este programa nace **después** del null, no para eludirlo.

---

## 8. Frase de cierre

> Para que el ruido de energía oscura sea real y medible, el continuo lorentziano a todas las escalas, la equivalencia fuerte universal y la unitariedad del parche observable no pueden permanecer las tres intactas a la vez; pero tampoco se puede romper una sola a manivela numérica. El paquete R1+R2+R3 debe **derivar** semilla, ganancia y operador, y **predecir** sus propios ciegos. Eso es la revolución: no un parámetro, sino un marco que se blinda a sí mismo.

---

*Fin del manifiesto. Siguiente: `SELF_SHIELDING_AXIOMS.md` y `notes/WORK_PACKAGES.md`.*
