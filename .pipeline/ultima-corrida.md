# Última corrida — Electricista Culiacán

**Fecha:** 2026-06-16 (corrida 9:00 AM)
**Resultado:** PUBLICADO ✅ — commit `f221d4ee` en `main`, push OK, auto-indexación disparada (3 URLs a Google).

## Health check
- Home, `/contacto/`, `/servicios/instalacion-electrica/`, `/blog/` → 200. Nada roto de entrada.

## Qué se arregló (mecánico, alta severidad, verificado)
**1 mejora (regla "una mejora por sesión"): a11y — labels de formulario en 3 páginas.**
- `servicios/electricista-cerca-de-mi/index.html`, `blog/como-prevenir-cortocircuitos-casa/index.html`, `blog/senales-instalacion-electrica-obsoleta/index.html` tenían el form con inputs solo-placeholder, SIN `<label>` (la homepage —fuente de verdad— sí los tiene). Regresión de plantilla.
- Fix additivo: `id` único por campo + `<label for="…" class="sr-only">` (nombre/teléfono/email/mensaje).
- **Hallazgo clave durante la verificación:** `.sr-only` NO está definida en ningún CSS externo; solo vive en el `<style>` inline de `index.html`. Sin añadir la regla, los labels se renderizarían VISIBLES. Se añadió la definición `.sr-only` al `<style>` crítico inline de cada una de las 3 páginas. (Regla nueva en REGLAS.md.)

## Verificación (escéptica)
- 4 labels + 4 ids coincidentes por página; 0 ids duplicados; `.sr-only` def = 1 por página; HTTP 200.
- `validate-landing.sh` PASA en la página de servicio (las 2 de blog fallan por diferencias pre-existentes blog-vs-landing: sin exit-popup / sin main.min.js — NO introducidas por este cambio, y el pre-commit solo valida `servicios/`).
- Checkers deterministas sin regresión: check-plantilla 2 (pre-existentes: img eager en blog/index + theme-color en archivo de verificación Google), check-indexabilidad 0.

## Candados de publicación (todos OK)
- Auto-revisión sin problemas de correctitud (diff = solo labels + def .sr-only).
- Diff toca **3 archivos** (≤ 15). 0 borrados estructurales. Sin tocar tests/copy/precios.

## Verificación ciega — GSC (resuelta, NO era ceguera)
- El subagente `revisor-gsc` está cableado a `mcp__local-seo` (propiedad de Plomero) y emitió "verificación ciega" para electricista. Correcto que lo emita dado SU tooling.
- PERO el servidor MCP `gsc` del entorno SÍ expone `https://electricistaculiacanpro.mx/` (verificado con `gsc_list_sites`). La indexación NO está ciega; el revisor está mal configurado. → Pendiente humano: reapuntar `revisor-gsc` a `mcp__gsc__*`.
- Los otros 3 deterministas (plantilla, indexabilidad, producción) corrieron sanos sobre datos reales (673 archivos / 44 URLs / 9 páginas en vivo), no ciegos.

## Pendiente para humano (NO auto — estratégico/masivo/diseño)
- Reconfigurar `revisor-gsc` → `mcp__gsc__*`.
- Contraste WCAG AA del CTA naranja (#F97316 2.8:1, #E36414 3.44:1) — decisión de diseño + 3 CSS + sw bump.
- focus-visible global (3 CSS + sw bump).
- CSS render-blocking en 642 colonias + contacto/gracias/blog-index (>15 archivos, corrida dedicada).
- aggregateRating/Review self-serving en homepage + 16 servicios (+ ~642 colonias ya anotadas).
- 8 meta descriptions de blog/servicio demasiado largas (edición de copy).
- Heredados: fuga copy "10 de Abril" en wa.me de colonias, 16 colonias indexables fuera del sitemap, 3 tablas de blog sin table-wrapper, ETA inconsistente, theme-color placeholder.

## Aprendizajes (REGLAS.md)
- Nueva regla A11Y/CSS: `.sr-only` solo existe inline en index.html → al propagar markup sr-only a otra página, copiar también la definición a su `<style>` inline.
- Nueva regla PIPELINE/GSC: revisor-gsc mal apuntado; el MCP `gsc` real sí tiene la propiedad — no confundir "revisor mal configurado" con "indexación ciega".
