# Última corrida — Electricista Culiacán

**Fecha:** 2026-06-14 (corrida 6:20 PM)
**Resultado:** PUBLICADO ✅ — commit `40beb89` en `main`, push OK, auto-indexación disparada (14 URLs a Google).

## Qué se arregló (mecánico, alta severidad, verificado)
1. **18 enlaces internos rotos** en 14 páginas de servicio: apuntaban a `/servicios/reparacion-cortos-circuitos/` (404, slug con guion extra). Corregidos a `/servicios/reparacion-cortocircuitos/` (directorio real, responde 200). Checker plantilla: 28 → 14 hallazgos (los 14 restantes son falsos positivos confirmados por el revisor-links: enlaces dentro de `<script>` con template literal `${c.s}` y rutas de fonts `../../../` que el navegador recorta a la raíz y resuelven OK).
2. **`/gracias/` removida de `sitemap.xml`**: la página tiene `robots noindex,follow` pero estaba listada en el sitemap (contradicción → warning en GSC). XML validado. Checker indexabilidad: 20 → 19, gracias = 0.

## Candados de publicación (todos OK)
- Auto-revisión sin problemas de correctitud (diff = solo el href del slug en 14 archivos + bloque gracias en sitemap).
- Diff toca **15 archivos** (= límite máximo permitido).
- 0 borrados estructurales inesparados; sin tocar tests ni contenido/copy.

## Incidencia operativa (resuelta)
- El primer `git push` abortó: el hook `.git/hooks/pre-push` llama `node` (auto-indexación GSC) y node está en `/usr/local/bin`, fuera del PATH del shell del pipeline. Resuelto reintentando con `PATH="/usr/local/bin:$PATH" git push` (sin `--no-verify`, para no omitir la indexación). Regla añadida a REGLAS.md.
- Nota zsh: `for f in $files` no hace word-splitting → un `sed -i` en lote falló silencioso; se rehízo con `while IFS= read`. Regla añadida.

## Pendiente para humano (NO auto — masivo o estratégico)
Detectado por los revisores LLM (seo, perf, a11y, movil). Detalle en ESTADO.md:
- **aggregateRating self-serving en ~642 colonias** (alta) — riesgo de acción manual de Google; quitar schema en lote (batch dedicado, > candado 15 archivos).
- **Fuga de copy "10 de Abril" en wa.me de ~96 colonias** (alta) — personalizar por colonia.
- **16 colonias indexables + terminos/ fuera del sitemap** (alta) — decisión SEO (agregar o noindex).
- **CSS render-blocking en ~15 servicios + 10 blog** (perf alta) — replicar patrón async de la home; corrida dedicada.
- **3 tablas de blog sin table-wrapper** (movil alta) — siguiente mejora.
- **focus-visible global ausente** (a11y alta) — fix en los 3 CSS + crítico.
- **ETA inconsistente** 20-30 vs 30-60 min (contenido); theme-color #0066cc/faltante (baja); títulos/descr duplicados directorio vs colonias (editorial).
