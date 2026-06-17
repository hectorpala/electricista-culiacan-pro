# Última corrida — Electricista Culiacán

**Fecha:** 2026-06-17 (corrida 11:26 AM)
**Resultado:** PUBLICADO ✅ — rama `auto/mantenimiento-20260617-1126` mergeada (`--no-ff`) a main y pusheada.

## Health check
- Home, `/contacto/`, `/servicios/instalacion-electrica/`, `/blog/`, `/servicios/electricista/` → 200. Nada roto de entrada.

## Qué se arregló (mecánico, media, verificado) — "una mejora por sesión"
**SEO/social — `twitter:url` filtrado en 4 páginas de servicio.**
- `servicios/{cambio-cableado-electrico, electricista-a-domicilio, instalacion-centro-carga, instalacion-ventiladores-techo}/index.html` tenían `twitter:url` apuntando a `/servicios/reparacion-cortocircuitos/` en lugar de su canonical propio.
- Origen: leak de la plantilla de cortocircuitos. El 2026-06-14 se corrigieron canonical + og:url de estas mismas páginas, pero `twitter:url` (un 3er campo de URL) quedó sin tocar y sobrevivió 3 días.
- Fix additivo/mínimo: `twitter:url` = canonical propio (1 línea por archivo).

## Verificación (escéptica)
- Barrido site-wide (674 HTML): **0** mismatch canonical-vs-twitter:url (normalizando trailing slash). Antes: 4.
- Cada `twitter:url` == su `canonical`/`og:url`. La página legítima `reparacion-cortocircuitos` quedó intacta (su twitter:url sigue siendo self).
- `validate-landing.sh` PASA en las 4. HTTP 200 en las 4 (servidor local).
- Checkers deterministas sin regresión: check-plantilla **2** (pre-existentes: plt-001 img eager en blog/index, plt-002 theme-color en archivo de verificación Google = falso positivo), check-indexabilidad **0**, check-produccion **0**.

## Candados de publicación (todos OK)
- Auto-revisión: diff = solo líneas `twitter:url`, sin efectos colaterales.
- Diff toca **4 archivos** (≤ 15). 0 borrados estructurales. Sin tocar tests/copy/precios.

## GSC — verificado con datos REALES (NO ciego)
- El subagente `revisor-gsc` sigue mal cableado a `mcp__local-seo` (plomero) → emitiría "verificación ciega" falsa. Lo cubrí consultando directamente `mcp__gsc__*` con la propiedad real `https://electricistaculiacanpro.mx/`.
- Sitemaps: 0 errores (sitemap.xml 30 enviadas/3 warn; colonias 16/0; images 14/1 warn).
- Inspección: home y `/servicios/instalacion-electrica/` "Enviada e indexada"; `/blog/` "Descubierta: actualmente sin indexar" (informativo, nunca crawleada — no es defecto mecánico).

## Pendiente para humano (NO auto — copy/diseño/estrategia o fuera de "una mejora")
- Copy leak "reparación de cortocircuitos" en H2/CTA de `cambio-cableado-electrico` e `instalacion-ventiladores-techo` (cambio de copy).
- `<h1>` duplicado en `electricista-colonias-culiacan` (mecánico 1 línea, próxima corrida).
- `.letter-btn` tap target <44px en colonias (inline min-height/width 44px).
- Tarjetas sociales incompletas (sin og:url/og:image/twitter) en `electricista-colonias-culiacan`.
- `gracias/` carga main.js sin minificar (baja); footer logo de index.html sin loading=lazy (baja, se hereda).
- blog/index.html img featured eager sin fetchpriority (plt-001): añadir `fetchpriority="high"` (es el LCP, NO lazy), próxima corrida.
- Heredados sin resolver: contraste WCAG AA del CTA naranja, focus-visible global, CSS render-blocking en 642 colonias, aggregateRating self-serving (home+16 servicios+642 colonias), meta descriptions largas/con cola comercial, fuga "10 de Abril" en wa.me, 16 colonias fuera de sitemap, 3 tablas de blog sin table-wrapper, reapuntar `revisor-gsc` a `mcp__gsc__*`.

## Aprendizajes (REGLAS.md)
- Nueva regla SEO/SOCIAL: al corregir un canonical/og:url filtrado, revisar SIEMPRE `twitter:url` también (es un 3er campo de URL que se filtra por separado). Verificación: canonical == twitter:url en todo HTML.
