# ESTADO — Electricista Culiacán

## 2026-06-14 (corrida 6:20 PM) — PUBLICADO ✅ (commit 40beb89)
- Rama `auto/mantenimiento-20260614-1820`, mergeada a main y pusheada (auto-indexación: 14 URLs a Google).
- **ARREGLADO (alta, mecánico):** 18 enlaces rotos en 14 páginas de servicio → slug correcto `reparacion-cortocircuitos` (eran `reparacion-cortos-circuitos`, 404). Checker plantilla 28→14 (los 14 restantes son falsos positivos: `${c.s}` template-literal JS y fonts `../../../` que el navegador recorta).
- **ARREGLADO (alta, mecánico):** `/gracias/` (noindex) removida de `sitemap.xml`. Checker indexabilidad 20→19, gracias=0, XML válido.
- Candados: diff = 15 archivos (límite), 0 borrados estructurales inesperados, auto-revisión OK → publicado.
- Incidencia operativa resuelta: pre-push hook necesitaba node en PATH (ver REGLAS.md OPERACIÓN-PIPELINE).

### PENDIENTE HUMANO (detectado por revisores LLM esta corrida — NO auto: masivo/estratégico)
- **aggregateRating self-serving en ~642 páginas de colonia** (alta, seo-004): mismo ratingValue 4.8/reviewCount 150 replicado en masa → riesgo de acción manual de Google. Requiere quitar el bloque de schema en lote (642 archivos, > candado de 15). Decidir batch dedicado.
- **Fuga de copy "necesito electricista en 10 de Abril" en wa.me de ~96 colonias** (alta, seo-001): texto de plantilla origen no personalizado por colonia (6 son indexables). Cambio de contenido en lote.
- **16 colonias indexables fuera del sitemap + terminos/** (alta, idx/seo-003): decisión SEO (agregar al sitemap o noindex). Las thin pages doorway están en noindex (correcto); las ~16 con contenido único deberían entrar al sitemap.
- **CSS render-blocking en /servicios/ (~15) y /blog/ (10)** (perf alta, perf-001/002): no replican el patrón async de la homepage; blog usa `styles.min.css` sin hash. Toca >15 archivos → corrida dedicada.
- **3 tablas de blog sin `table-wrapper`** (movil alta) + tabla en homepage (baja): mecánico pero fuera del alcance de esta corrida (otra mejora).
- **focus-visible global ausente** (a11y alta, a11y-001): falta outline de foco para teclado salvo .seo-card/.floating-btn; fix en los 3 CSS + crítico inline.
- **ETA inconsistente** 20-30 min (colonias) vs 30-60 min (home/servicios) (seo-005): unificar — decisión de contenido.
- **theme-color placeholder #0066cc** en servicios/electricista/ (baja) y faltante en contacto/terminos (baja). Marca = `#F97316`.
- Duplicado title/description directorio vs colonias index (media): editorial.

## 2026-06-14 — Instalación del pipeline de mantenimiento
- Se portó el pipeline de mantenimiento autónomo desde Plomero Culiacán (rama `feat/checkers-deterministas`).
- **Checkers deterministas instalados** (`.pipeline/`): check-plantilla.py, check-indexabilidad.py, check-produccion.mjs.
- **9 revisores** disponibles en `.claude/agents/`: 5 LLM (seo, movil, a11y, perf, links) + 4 deterministas (gsc, indexabilidad, produccion, plantilla).
- Skill `/mantener-sitio` y `.pipeline/mantener-prompt.txt` adaptados a este sitio.

### Estado de los checkers
- ✅ check-plantilla.py — operativo.
- ✅ check-indexabilidad.py — operativo (lee `sitemap.xml`).
- ⚠️ check-produccion.mjs — portado pero **requiere `npm i puppeteer`** para correr.

### Hallazgos iniciales detectados (aún NO arreglados — pendientes para la primera corrida del pipeline)
- check-plantilla: **65** (46 links/recursos rotos [alta], 9 schema con aggregateRating/Review en blog [alta], y varios baja/media de perf/movil).
- check-indexabilidad: **46** (17 BreadcrumbList con último item apuntando a `/#servicios` en vez del canonical, 21 páginas indexables fuera del sitemap, duplicados de title/description).

### Pendiente
- Instalar puppeteer para activar check-produccion.
- Primera corrida del pipeline para empezar a arreglar los hallazgos mecánicos de alta/media.
- (Opcional) dar a Electricista su propio contenedor GTM (hoy comparte el de Plomero: GTM-W75CRTX5).

## 2026-06-14 — Primera corrida del pipeline (modo seguro, en rama)
- Rama: auto/mantenimiento-20260614-1414 (sin publicar; pendiente de revisión humana).
- ARREGLADO: `aggregateRating` self-serving removido del JSON-LD de **9 posts de blog** (regla 08a95902). JSON-LD validado, checker confirma 0 hallazgos de aggregateRating.
- PENDIENTE HUMANO: 46 imágenes rotas (varias no existen en disco en ninguna versión → hay que generarlas/conseguirlas, no auto-arreglable) y 17 breadcrumbs de servicio cuyo último item apunta a `/#servicios` en vez del canonical (revisar plantilla de breadcrumb).

## 2026-06-14 (cont.) — BUG SERIO encontrado y arreglado: canonicals incorrectos
- 5 páginas tenían canonical apuntando a OTRA URL (4 a `/servicios/reparacion-cortos-circuitos/` que NO existe —typo de "reparacion-cortocircuitos"— y 1 a `.../directorio/`). Google las trataría como duplicados de una 404 → riesgo de desindexación.
- ARREGLADO: canonical + og:url → self-referencial (derivado del path) en las 5. Checker: 0 canonical-a-otra-URL. Lo detectó el revisor-indexabilidad.
- PENDIENTE (siguiente pasada, con cuidado): breadcrumbs — el último item del BreadcrumbList no apunta al canonical en ~17 páginas (baja severidad; requiere edición de JSON-LD por página). NO auto-arreglado en esta pasada tras un casi-error (usar URL derivada del path, no el canonical).

## 2026-06-14 (cont.) — Breadcrumbs arreglados (método correcto)
- 16 páginas: el último item del BreadcrumbList no tenía `item` (apuntaba implícitamente a /#servicios o /blog/). Se añadió `item` = URL propia derivada del PATH (no del canonical, tras el casi-error anterior). Fixer agnóstico al formato (multilínea y single-line), con validación JSON y verificación post-fix por archivo.
- Checker: 0 breadcrumbs (eran 16). Indexabilidad 36 -> 20.
- Quedan ~20 en indexabilidad (mayormente "página indexable fuera del sitemap" — revisar si deben ir al sitemap o llevar noindex; decisión SEO, no auto).

## 2026-06-14 (cont.) — Imágenes rotas: arregladas las seguras
- ARREGLADO (6, en 11 archivos): refs a imágenes que existían con otro nombre/ruta → apuntadas al archivo real (match ESTRICTO: todos los tokens + mismo tamaño + archivo no-.backup). Incluye el logo roto (`../electricista-culiacan-pro-logo.webp` → `/assets/images/...`) en contacto/gracias/colonias.
- NO auto-arregladas (~14 refs / pendiente humano): imágenes genuinamente ausentes o sin el tamaño pedido — REQUIEREN generar/subir la imagen:
  * instalacion-iluminacion-led (420w, 800w) — no existe
  * mantenimiento-tablero-electrico-420w, reparacion-cortocircuito (420w/800w), prevenir-cortocircuitos-420w — falta ese tamaño (existe 800w/1200w del nombre correcto; decidir si regenerar 420w o ajustar el srcset)
  * logo-512.webp — no existe (¿usar /assets/icons/icon-512x512.webp? decisión humana)
- NOTA: el matcher difuso inicial propuso destinos ERRÓNEOS (.backup, imagen distinta); se descartó y solo se aplicaron matches estrictos verificados.
