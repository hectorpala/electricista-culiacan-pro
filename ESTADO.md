# ESTADO — Electricista Culiacán

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
