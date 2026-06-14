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
