# PLAN DE ARREGLOS PENDIENTES — Electricista Culiacán

> Generado tras la corrida del pipeline (hallazgos de los revisores LLM que NO se
> auto-arreglan por ser masivos o estratégicos). Se arregla **UNO A LA VEZ**, con
> **autorización explícita del dueño** antes de tocar nada. Se documenta antes/después.

## Cómo se trabaja — MODO SEMI-AUTOMÁTICO
El agente **avanza solo por la lista**; tú solo **apruebas**. Por cada ítem:
1. El agente presenta **en corto** el siguiente ítem y el fix exacto que va a hacer.
2. Tú respondes **"OK"** (o "OK todo" para autorizar varios de corrido). El agente NO hace nada sin tu OK.
3. Con tu OK: trabaja **en una rama**, aplica, **verifica** (checkers/captura), publica y **pasa SOLO al siguiente** ítem, presentándolo. No te pregunta de más.
4. Documenta cada ítem como ✅ con su resultado en la **Bitácora** de abajo.
5. **Se detiene y pregunta SOLO** cuando: un ítem necesita una decisión tuya (sitemap indexar/noindex, ETA correcto, color de marca, copy), o algo sale mal/riesgoso.

> Atajos de aprobación: **"OK"** (este ítem) · **"OK todo"** (todos los que no requieran decisión) · **"OK sin publicar"** (hace pero no publica hasta tu visto bueno final) · **"alto"** (pausa).

## Estados
⬜ PENDIENTE · 🟡 AUTORIZADO · 🔧 EN PROGRESO · ✅ HECHO · ⏸️ EN PAUSA

---

## 🔴 ALTA — riesgo SEO / penalización

### A1 — Quitar `aggregateRating` self-serving de 642 colonias
- **Estado:** ✅ HECHO
- **Qué:** Cada página de colonia tiene un schema `aggregateRating` idéntico ("4.8★, 150 reseñas") replicado en masa.
- **Por qué importa:** Google prohíbe reseñas self-serving/falsas; 642 idénticas = riesgo de **acción manual** (penalización).
- **Alcance:** 642 archivos (`servicios/electricista-colonias-culiacan/*/index.html`). > candado de 15 → batch dedicado.
- **Plan:** Script Python que, por archivo, quita SOLO la propiedad `aggregateRating` del JSON-LD (como en los 9 blogs), valida que el JSON-LD siga parseando, y verifica con check-plantilla. Rama dedicada. Diff enorme pero mecánico y validado.
- **Autorización:** ✅ (dueño, 2026-06-14)
- **Resultado:** 642 archivos limpiados, 0 saltados, 0 residuales. JSON-LD validado por archivo (json.loads). check-plantilla sin hallazgos de aggregateRating. Pre-commit (validate-landing) pasó las 642. Commit `ec410e2`, publicado a `main` (Netlify auto-deploy).

### A2 — Personalizar fuga de copy "10 de Abril" en wa.me de 96 colonias
- **Estado:** ✅ HECHO
- **Qué:** 96 colonias tienen el enlace `wa.me` con el texto fijo *"necesito electricista en 10 de Abril"* (copiado de la colonia plantilla, sin personalizar).
- **Por qué importa:** Un cliente en otra colonia manda un WhatsApp citando "10 de Abril" → se ve descuidado y confunde el lead. 6 de esas páginas son indexables.
- **Alcance:** 96 archivos. Cambio de contenido en lote.
- **Plan:** Script que reemplace el nombre de colonia en el texto del `wa.me` por el de CADA página (derivado del path/título). Validar muestra. Rama dedicada.
- **Autorización:** ✅ (dueño, 2026-06-14)
- **Resultado:** 95 colonias personalizadas (la nº96, `10-de-abril`, ya era correcta: es su nombre real). Nombre derivado de `areaServed.name`; URL-encoding UTF-8 idéntico al de las correctas (acentos/paréntesis). 0 fugas residuales. Indexable de muestra (Guadalupe) validó. Commit `ad73fb9`, publicado a `main`.

### A3 — Sitemap: 16 colonias con contenido único + `terminos/` fuera del sitemap
- **Estado:** ✅ HECHO
- **Qué:** ~16 colonias indexables (contenido único) y `terminos/` no están en el sitemap.
- **Por qué importa:** Google podría no descubrirlas. (Las colonias "thin"/doorway sí están en `noindex` — correcto.)
- **Alcance:** decisión SEO + edición del sitemap.
- **Plan (requiere TU decisión):** ¿agregar esas 16+terminos al sitemap (indexar) o ponerles `noindex`? Según tu respuesta, edito el sitemap o el `<meta robots>`.
- **Autorización:** ✅ Decisión dueño 2026-06-14: **16 colonias → indexar** · **terminos/ → noindex**.
- **Resultado:** sitemap.xml 29→45 URLs (+16 colonias). `terminos/` → `noindex, follow` y fuera del sitemap. Extra mecánico: 14 de las 16 tenían el último breadcrumb sin `item`; se les agregó `item`=canonical (igual que centro/chapultepec) → check-indexabilidad pasó de 14 "alta" a 0 en estas colonias (quedan solo 2 "media" = ítem C4 preexistente). XML bien formado, JSON-LD validado, validate-landing PASÓ. Commit `99fb2d5`, publicado a `main`.

## 🟠 ALTA — performance / accesibilidad

### B1 — CSS render-blocking en ~15 servicios + 10 blogs
- **Estado:** ✅ HECHO
- **Qué:** Esas páginas cargan el CSS bloqueando el render (más lento), a diferencia de la home que usa carga async. El blog usa `styles.min.css` sin hash.
- **Por qué importa:** Peor LCP/performance y Core Web Vitals.
- **Alcance:** ~25 archivos → corrida dedicada.
- **Plan:** Replicar EXACTO el patrón async de la homepage (preload + onload, o el que use index.html). Verificar con check-produccion/Lighthouse. Rama dedicada.
- **Autorización:** ✅ (dueño, 2026-06-14)
- **Resultado:** 24 archivos (15 servicios + 9 blogs) convertidos a CSS no-bloqueante: `media="print" onload="this.media='all'"` + `<noscript>`, conservando el archivo CSS de cada página. **OJO:** NO se usó `preload` porque el validador de landings lo prohíbe (`Sin preload de styles externo`) — se descubrió en verificación y se ajustó. CSS crítico inline (7.6-8 KB) evita FOUC. Sin bump de sw.js (no cambia CSS). Verificación: 15 servicios PASAN validate-landing (pre-commit), 0 bloqueantes residuales, CSS sirve HTTP 200 local. Commit `e3ad624`, publicado a `main`. **Pendiente separado:** los blogs siguen usando `styles.min.css` (49KB, distinto y sin hash) vs `styles.7f293647.css` (36KB) del resto — unificarlo es otra decisión (cambia CSS real del blog + cache-busting).

### B2 — `focus-visible` global ausente (accesibilidad de teclado)
- **Estado:** ✅ HECHO
- **Qué:** No hay outline de foco visible para navegación con teclado (salvo `.seo-card`/`.floating-btn`).
- **Por qué importa:** Accesibilidad (WCAG) — usuarios de teclado no ven dónde están.
- **Alcance:** los 3 CSS + crítico inline → **ceremonia de versionado** (`?v=` + sw.js).
- **Plan:** Añadir regla `:focus-visible { outline }` a los 3 CSS + inline crítico, bump `?v=` y sw.js. Rama dedicada.
- **Autorización:** ✅ (dueño, 2026-06-14 — "ceremonia completa")
- **Resultado:** Regla global `:focus-visible{outline:3px solid #e67e22;outline-offset:2px}` en los 3 CSS. Cache-busting: `?v=20260614` en 1322 referencias de 670 HTML (el CSS se sirve `immutable` en netlify.toml/_headers, por eso era obligatorio). sw.js v6→v7 + precache con `?v=`. NO se duplicó en inline crítico (redundante: con `?v=` el CSS externo ya llega garantizado y el foco se activa post-carga). Verificación: paridad CSS OK, validate-landing PASÓ con `?v=`, CSS sirve HTTP 200 con la regla, pre-commit validó servicios. Commit `a60843b`, publicado a `main`.

## 🟡 MEDIA / BAJA — chico o editorial

### C1 — 3 tablas de blog sin `<div class="table-wrapper">`
- **Estado:** ✅ HECHO
- **Qué:** 3 tablas en blogs se desbordan en móvil (sin scroll wrapper).
- **Alcance:** 3 archivos (chico). → **En realidad 5**: 3 blogs + homepage + `electricista-precios` (el checker las detectó todas; la home es la referencia, se incluyó por la regla dura).
- **Plan:** Envolver cada `<table>` en `table-wrapper`. Rama.
- **Autorización:** ✅ ("OK todo", 2026-06-14)
- **Resultado:** 5 tablas envueltas en `<div class="table-wrapper">`. Regla canónica `.table-wrapper{overflow-x:auto;...}` añadida a los 3 CSS (no existía; tampoco había fallback global — solo `overflow-x:hidden` que recortaba la tabla). Para entrega inmediata sin re-bump de `?v=`, la regla se inyectó también en el CSS crítico inline de las 5 páginas. Verificación: check-plantilla 0 tablas sin wrapper, electricista-precios PASÓ validate-landing, home sin errores nuevos (los 4 que marca son preexistentes del validador sobre la propia referencia). Commit `11d2b37`, publicado a `main`.

### C2 — ETA inconsistente (20-30 vs 30-60 min)
- **Estado:** ✅ HECHO
- **Qué:** Las colonias dicen "20-30 min"; home/servicios dicen "30-60 min".
- **Plan (requiere TU decisión):** ¿cuál es el correcto? Lo unifico en todo el sitio.
- **Autorización:** ✅ Decisión dueño 2026-06-14: **30-60 min**.
- **Resultado:** 3196 reemplazos de `20-30 min`→`30-60 min` en 643 archivos (colonias). Cubre también "20-30 minutos". Preservado el "20-30%" del blog de ahorro (porcentaje, no ETA). 0 "20-30 min" residuales, sitio uniforme en 30-60 min. Commit `e23b7d9`, publicado a `main`.

### C3 — theme-color #0066cc / faltante
- **Estado:** ✅ HECHO
- **Qué:** Algunas páginas usan el placeholder `#0066cc` o no tienen `theme-color`.
- **Plan (requiere TU decisión):** ¿cuál es tu color de marca exacto? Lo aplico a todas.
- **Autorización:** ✅ Decisión dueño 2026-06-14: **#E36414**.
- **Resultado:** home `#F97316`→`#E36414`, `servicios/electricista` `#0066cc`→`#E36414`, `contacto` +theme-color. Stub `google…html` omitido (no es página). 671 páginas uniformes en #E36414, 0 con #F97316/#0066cc. Commit `9f8105f`, publicado a `main`.

### C4 — Títulos/descripciones duplicados (directorio vs colonias index)
- **Estado:** ✅ HECHO
- **Qué:** Title/description repetidos entre la página directorio y el index de colonias.
- **Plan:** Editorial — propongo variantes y tú apruebas.
- **Autorización:** ✅ (dueño aprobó copy 2026-06-14)
- **Resultado:** Index → "Electricista por Colonia en Culiacán | Cobertura 24/7 en tu Zona" (ángulo zona); Directorio → "Directorio A-Z de Colonias con Electricista | Culiacán Pro" (ángulo lista). Description y og: actualizados en ambas. check-indexabilidad: 0 duplicados (de 2 a 0). Commit `d706f7a`, publicado. **Nota:** ambas son casi el directorio completo (~627 enlaces) → consolidar/301 una es decisión estratégica aparte (relacionada con D1).

## 🟢 ESTRATEGIA DE CONTENIDO (decisión grande)

### D1 — Diferenciar las 17 colonias INDEXABLES con contenido local único
- **Estado:** ⬜ PENDIENTE
- **Qué:** De las 643 colonias, **626 están en `noindex`** (Google las ignora — se dejan como están, no estorban) y **17 son indexables**. Esas 17 hoy son **casi calcadas** entre sí (mismo template) → riesgo de doorway/contenido duplicado.
- **Por qué importa:** Páginas indexables casi idénticas = señal de thin/doorway. Diferenciarlas las vuelve **valiosas e indexables de verdad** → tráfico local real por colonia.
- **Alcance:** **17 archivos** (solo las indexables). Es **contenido, no mecánico** → requiere criterio/generación.
- **Decisión previa (TUYA):** **(1) diferenciar** las 17 con contenido único, **(2) consolidar** (quedarte con pocas páginas de zona fuertes y 301 el resto, como Plomero), o **(3) dejar** (solo limpiar, sin tocar contenido).
- **Plan si eliges (1) diferenciar:** por cada una de las 17, generar contenido LOCAL ÚNICO (puntos conocidos, calles, datos y problemas eléctricos típicos de esa zona), variando intro, FAQ y meta — **manteniendo EXACTO la estructura de la homepage** (regla de consistencia). Verificar con check-indexabilidad (sin title/desc duplicados) y validate-landing. Rama dedicada.
- **Nota:** las 626 `noindex` NO se tocan en este ítem (no compiten); opcional borrarlas algún día por orden.
- **Autorización:** ⬜ (dime: **diferenciar**, **consolidar** o **dejar**)
- **Resultado:** —

---

## Bitácora (se llena conforme se ejecuta)
<!-- fecha · ID · acción · commit · publicado sí/no · verificación -->
- 2026-06-14 · A1 · Quitado `aggregateRating` de 642 colonias vía `.pipeline/fix-a1-aggregaterating.py` (regex puntual + json.loads por archivo) · commit `ec410e2` · publicado SÍ (push a main → Netlify) · verificación: 642 cambiados/0 saltados/0 residuales, diff quirúrgico, check-plantilla limpio, pre-commit validó 642 landings.
- 2026-06-14 · A2 · Personalizado texto wa.me en 95 colonias vía `.pipeline/fix-a2-wame-colonias.py` (nombre desde `areaServed.name` + URL-encode UTF-8) · commit `ad73fb9` · publicado SÍ (push a main → Netlify) · verificación: 0 fugas residuales, 10-de-abril intacta, indexable de muestra validó, check-plantilla sin hallazgos nuevos.
- 2026-06-14 · A3 · sitemap +16 colonias indexables; `terminos/`→noindex,follow; +`item`=canonical al último breadcrumb de 14 colonias (igualar a centro/chapultepec) · commit `99fb2d5` · publicado SÍ (push a main → Netlify) · verificación: sitemap 45 URLs y XML bien formado, check-indexabilidad de 14 "alta"→0 en estas colonias, JSON-LD válido, validate-landing PASÓ.
- 2026-06-14 · B1 · CSS no-bloqueante en 24 archivos (15 servicios + 9 blogs): `media=print onload` + `<noscript>`, SIN preload (prohibido por validate-landing) · commit `e3ad624` · publicado SÍ (push a main → Netlify) · verificación: pre-commit validó 15 servicios, 0 bloqueantes residuales, CSS HTTP 200 local. Nota: blog `styles.min.css` sin hash queda como ítem aparte.
- 2026-06-14 · B2 · `:focus-visible` global en los 3 CSS + `?v=20260614` en 1322 refs de 670 HTML + sw.js v6→v7 · commit `a60843b` · publicado SÍ (push a main → Netlify) · verificación: paridad CSS OK, validate-landing PASÓ, CSS HTTP 200 con la regla, pre-commit OK.
- 2026-06-14 · C1 · 5 tablas envueltas en `.table-wrapper` (3 blogs + home + electricista-precios); regla `.table-wrapper{overflow-x:auto}` en los 3 CSS + inline en las 5 páginas (sin re-bump ?v=) · commit `11d2b37` · publicado SÍ (push a main → Netlify) · verificación: check-plantilla 0 tablas sin wrapper, validate-landing del servicio PASÓ, home sin errores nuevos.
- 2026-06-14 · C2 · ETA unificado a "30-60 min" (3196 reemplazos en 643 colonias; "20-30%" preservado) · commit `e23b7d9` · publicado SÍ (push a main → Netlify) · verificación: 0 "20-30 min" residuales, pre-commit OK.
- 2026-06-14 · C3 · theme-color unificado a #E36414 (home, electricista, contacto; stub google omitido) · commit `9f8105f` · publicado SÍ (push a main → Netlify) · verificación: 671 páginas uniformes, 0 #F97316/#0066cc, pre-commit OK.
- 2026-06-14 · C4 · title/description/og diferenciados entre index de colonias ("por colonia/tu zona") y directorio ("A-Z") · commit `d706f7a` · publicado SÍ (push a main → Netlify) · verificación: check-indexabilidad 0 duplicados.
