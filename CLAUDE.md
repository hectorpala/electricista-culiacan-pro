# Electricista Culiacán — Instrucciones del proyecto

## Memoria (LEER SIEMPRE antes de trabajar)
- ANTES de hacer cualquier cambio, lee REGLAS.md (errores ya cometidos que NO debes repetir).
- Registra hallazgos nuevos en HISTORIAL.jsonl (una línea JSON por hallazgo).
- El estado de la última corrida está en ESTADO.md.

## Reglas de trabajo (estilo Anthropic)
- VERIFICA tu trabajo antes de darlo por hecho: corre el sitio y compruébalo, no asumas que "se ve bien".
- HEALTH CHECK primero: antes de tocar nada, revisa que lo existente no esté roto.
- UNA mejora por sesión. No abarques de más.
- JAMÁS borres ni edites tests para "hacer pasar" algo. Eso oculta funcionalidad rota.
- Cambios mínimos. No refactorices fuera del alcance pedido.
- Muestra EVIDENCIA (salida de comando, captura) en vez de afirmar éxito.

## Reglas duras del sitio (resumen — el detalle está en REGLAS.md)
- CSS: al cambiar estilos, versionar URL (?v=AAAAMMDD) Y subir versión del service worker (sw.js). Aplicar el fix en los TRES archivos CSS (styles.css, styles.min.css y el .hash.css servido).
- MÓVIL: tablas con scroll horizontal (`<div class="table-wrapper">`); imágenes con max-width:100%; grids con auto-fit minmax, no columnas fijas; tap targets ~44px.
- SEO: nada de doorways (páginas casi idénticas); coordenadas GPS reales y únicas; sin aggregateRating self-serving en blog; og:image/twitter:image deben existir; al borrar páginas, cero enlaces rotos + actualizar sitemap.
- JS: tras minificar, verificar que las URLs wa.me no queden truncadas (rompe todo el sitio).
- CONTACTO: el email correcto es `contacto@electricistaculiacanpro.mx`. NUNCA un email con "plomero" (sería una fuga de copy-paste de la plantilla origen).
- CONSISTENCIA / PLANTILLA (regla dura del dueño): TODA página nueva o que se modifique debe replicar EXACTAMENTE la estructura de la homepage (`index.html`) — misma tipografía (Montserrat 800 + @font-face inline), mismo CSS crítico, misma estructura HTML, botones flotantes, breadcrumb, popup, footer, y la MISMA estructura/markup de imágenes (mismo patrón `<picture>`/`srcset`, tamaños 420/800/1200w WebP, fetchpriority del hero, loading lazy del resto). `index.html` es la FUENTE DE VERDAD. Validar SIEMPRE con `bash validate-landing.sh <pagina>` (corre en pre-commit) y las skills `page-validator` / `page-consistency-enforcer`. Si la homepage tiene un defecto, se corrige PRIMERO en la homepage (es la referencia) y luego se propaga.

## Pipeline de mantenimiento autónomo
- Invocar con `/mantener-sitio` (skill en `.claude/skills/mantener-sitio/SKILL.md`) o con `.pipeline/mantener-prompt.txt`.
- 9 revisores: 5 LLM (seo, movil, a11y, perf, links) para lo SUBJETIVO + 4 DETERMINISTAS (gsc, indexabilidad, produccion, plantilla) que corren scripts en `.pipeline/` y garantizan las reglas mecánicas.
- Checkers deterministas (solo reportan, no arreglan):
  - `python3 .pipeline/check-plantilla.py` — reglas mecánicas de plantilla (enlaces/og:image rotos, popup sin ARIA, fetchpriority/CLS, paridad CSS, table-wrapper, theme-color, email contaminado).
  - `python3 .pipeline/check-indexabilidad.py` — sitemap vs realidad, canonical/og:url/breadcrumbs.
  - `node .pipeline/check-produccion.mjs` — producción en vivo (requiere `npm i puppeteer`).

## Comandos útiles
- git log --oneline -30  (ver historia reciente)
- Servidor local para probar: `python3 -m http.server 8080`
