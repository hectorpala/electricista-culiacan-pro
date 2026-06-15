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
- **Estado:** ⬜ PENDIENTE
- **Qué:** Esas páginas cargan el CSS bloqueando el render (más lento), a diferencia de la home que usa carga async. El blog usa `styles.min.css` sin hash.
- **Por qué importa:** Peor LCP/performance y Core Web Vitals.
- **Alcance:** ~25 archivos → corrida dedicada.
- **Plan:** Replicar EXACTO el patrón async de la homepage (preload + onload, o el que use index.html). Verificar con check-produccion/Lighthouse. Rama dedicada.
- **Autorización:** ⬜
- **Resultado:** —

### B2 — `focus-visible` global ausente (accesibilidad de teclado)
- **Estado:** ⬜ PENDIENTE
- **Qué:** No hay outline de foco visible para navegación con teclado (salvo `.seo-card`/`.floating-btn`).
- **Por qué importa:** Accesibilidad (WCAG) — usuarios de teclado no ven dónde están.
- **Alcance:** los 3 CSS + crítico inline → **ceremonia de versionado** (`?v=` + sw.js).
- **Plan:** Añadir regla `:focus-visible { outline }` a los 3 CSS + inline crítico, bump `?v=` y sw.js. Rama dedicada.
- **Autorización:** ⬜
- **Resultado:** —

## 🟡 MEDIA / BAJA — chico o editorial

### C1 — 3 tablas de blog sin `<div class="table-wrapper">`
- **Estado:** ⬜ PENDIENTE
- **Qué:** 3 tablas en blogs se desbordan en móvil (sin scroll wrapper).
- **Alcance:** 3 archivos (chico).
- **Plan:** Envolver cada `<table>` en `table-wrapper`. Rama.
- **Autorización:** ⬜
- **Resultado:** —

### C2 — ETA inconsistente (20-30 vs 30-60 min)
- **Estado:** ⬜ PENDIENTE
- **Qué:** Las colonias dicen "20-30 min"; home/servicios dicen "30-60 min".
- **Plan (requiere TU decisión):** ¿cuál es el correcto? Lo unifico en todo el sitio.
- **Autorización:** ⬜ (dime el ETA correcto)
- **Resultado:** —

### C3 — theme-color #0066cc / faltante
- **Estado:** ⬜ PENDIENTE
- **Qué:** Algunas páginas usan el placeholder `#0066cc` o no tienen `theme-color`.
- **Plan (requiere TU decisión):** ¿cuál es tu color de marca exacto? Lo aplico a todas.
- **Autorización:** ⬜ (dime el hex de marca)
- **Resultado:** —

### C4 — Títulos/descripciones duplicados (directorio vs colonias index)
- **Estado:** ⬜ PENDIENTE
- **Qué:** Title/description repetidos entre la página directorio y el index de colonias.
- **Plan:** Editorial — propongo variantes y tú apruebas.
- **Autorización:** ⬜
- **Resultado:** —

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
