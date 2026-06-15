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
- **Estado:** ⬜ PENDIENTE
- **Qué:** Cada página de colonia tiene un schema `aggregateRating` idéntico ("4.8★, 150 reseñas") replicado en masa.
- **Por qué importa:** Google prohíbe reseñas self-serving/falsas; 642 idénticas = riesgo de **acción manual** (penalización).
- **Alcance:** 642 archivos (`servicios/electricista-colonias-culiacan/*/index.html`). > candado de 15 → batch dedicado.
- **Plan:** Script Python que, por archivo, quita SOLO la propiedad `aggregateRating` del JSON-LD (como en los 9 blogs), valida que el JSON-LD siga parseando, y verifica con check-plantilla. Rama dedicada. Diff enorme pero mecánico y validado.
- **Autorización:** ⬜
- **Resultado:** —

### A2 — Personalizar fuga de copy "10 de Abril" en wa.me de 96 colonias
- **Estado:** ⬜ PENDIENTE
- **Qué:** 96 colonias tienen el enlace `wa.me` con el texto fijo *"necesito electricista en 10 de Abril"* (copiado de la colonia plantilla, sin personalizar).
- **Por qué importa:** Un cliente en otra colonia manda un WhatsApp citando "10 de Abril" → se ve descuidado y confunde el lead. 6 de esas páginas son indexables.
- **Alcance:** 96 archivos. Cambio de contenido en lote.
- **Plan:** Script que reemplace el nombre de colonia en el texto del `wa.me` por el de CADA página (derivado del path/título). Validar muestra. Rama dedicada.
- **Autorización:** ⬜
- **Resultado:** —

### A3 — Sitemap: 16 colonias con contenido único + `terminos/` fuera del sitemap
- **Estado:** ⬜ PENDIENTE
- **Qué:** ~16 colonias indexables (contenido único) y `terminos/` no están en el sitemap.
- **Por qué importa:** Google podría no descubrirlas. (Las colonias "thin"/doorway sí están en `noindex` — correcto.)
- **Alcance:** decisión SEO + edición del sitemap.
- **Plan (requiere TU decisión):** ¿agregar esas 16+terminos al sitemap (indexar) o ponerles `noindex`? Según tu respuesta, edito el sitemap o el `<meta robots>`.
- **Autorización:** ⬜ (dime: **indexar** o **noindex**)
- **Resultado:** —

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

---

## Bitácora (se llena conforme se ejecuta)
<!-- fecha · ID · acción · commit · publicado sí/no · verificación -->
