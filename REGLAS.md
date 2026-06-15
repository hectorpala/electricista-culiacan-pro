# REGLAS APRENDIDAS — Electricista Culiacán

Reglas duras extraídas de errores reales ya cometidos, para que un agente NO los repita.
Cada línea documenta UN error concreto. Formato: `- [FECHA] CATEGORÍA: regla — por qué (referencia). Severidad: X`.

Este archivo arranca **limpio** (el sitio se incorporó al pipeline el 2026-06-14). Las
reglas MECÁNICAS de plantilla ya NO dependen de la memoria del LLM: las verifican de forma
determinista los checkers de `.pipeline/` (revisor-plantilla, revisor-indexabilidad,
revisor-produccion). Aquí se acumula lo que esos checkers NO cubren y haya que recordar:
patrones nuevos, decisiones de contenido/estrategia, y regresiones.

> Heredado de la plantilla (mismo template que Plomero Culiacán), válido salvo prueba en contra:
> - CSS/PARIDAD: cada fix de estilos va en los 3 archivos (styles.css, styles.min.css, styles.<hash>.css); versionar `?v=` + subir CACHE_NAME de sw.js si el asset se sirve.
> - SEO/SCHEMA: NO aggregateRating/Review self-serving en blog; og:url/canonical/breadcrumb deben coincidir con la URL propia de cada página (último item del BreadcrumbList == canonical, 3 niveles en /servicios/).
> - JS: tras minificar main.js, verificar que las URLs `wa.me` no queden truncadas.
> - CONTENIDO: email correcto = `contacto@electricistaculiacanpro.mx` (nunca con "plomero").

<!-- Las reglas específicas de Electricista se añaden debajo, una por línea, conforme se aprendan. -->

- [2026-06-14] LINKS/SLUG: el slug real del servicio es `reparacion-cortocircuitos` (una sola palabra, sin "s" intermedia). NUNCA enlazar a `/servicios/reparacion-cortos-circuitos/` (404). Por qué: 18 enlaces en 14 páginas de servicio apuntaban al slug erróneo (fuga de plantilla); si una página nueva se genera copiando otra, hereda el typo. Verificación: `grep -rl "reparacion-cortos-circuitos" --include="*.html" .` debe dar vacío. Severidad: alta.
- [2026-06-14] OPERACIÓN-PIPELINE (publicación): (1) el hook `.git/hooks/pre-push` ejecuta `node` (auto-indexación GSC) y node vive en `/usr/local/bin` pero NO está en el PATH del shell del pipeline → el primer `git push` aborta con "node: command not found". Solución: `PATH="/usr/local/bin:$PATH" git push origin main` (NO usar `--no-verify`: saltarse el hook omite la indexación en Google, que es parte del flujo). (2) zsh NO hace word-splitting de variables sin comillas en `for f in $files` → un `sed -i` en lote falla silenciosamente (git diff vacío). Usar `grep -rl ... | while IFS= read -r f; do ...; done` y SIEMPRE confirmar con `git diff --stat` que los archivos cambiaron. Severidad: media.
- [2026-06-14] CONSISTENCIA/PLANTILLA (regla dura del dueño): toda página nueva o modificada debe replicar EXACTAMENTE la homepage (`index.html`) — tipografía (Montserrat 800 + @font-face inline), CSS crítico, estructura HTML, botones flotantes, breadcrumb, popup, footer y la MISMA estructura/markup de imágenes (`<picture>`/`srcset`, 420/800/1200w WebP, fetchpriority del hero, lazy del resto). `index.html` = FUENTE DE VERDAD. Por qué: evita la deriva (ej. el form de la home quedó con `.error-message`/`.success-message` visibles que las páginas de servicio NO tienen → inconsistencia). Si la homepage tiene un defecto, se arregla PRIMERO en la homepage y luego se propaga. Verificación: `validate-landing.sh` (pre-commit) + skills `page-validator`/`page-consistency-enforcer`. Severidad: alta.
