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
- MARCA/COLOR (contrato — la home `index.html` es la FUENTE DE VERDAD): la paleta es NARANJA **+ AZUL** (este sitio SÍ usa azul a propósito, no es contaminación): naranja `#E36414`/`#F97316`/`#C2410C` y AZUL DE MARCA `#1e40af`/`#0f4fa8`/`#1a73e8`/`#0d3f8a`. Verdes/otros LEGÍTIMOS: `#22c55e` (punto "disponible"), WhatsApp `#25d366`/`#128c7e`, logo de Google `#4285f4`/`#ea4335`/`#34a853`/`#fbbc05` (solo en `<path fill>` de SVG), neutros slate y ámbar de avisos. PROHIBIDO: azules que NO sean los de marca (`#0066cc`/`#0284c7`/`#0369a1`…), morado, rojo y verde decorativo (entran por clonar el sitio hermano). Mapear: azul-no-marca → `#1e40af`, rojo → `#C2410C`, verde decorativo → `#22c55e`, fondos claros → `#FFF7ED`. Tipografía Montserrat 800 + Inter; las 3 hojas `styles*.css` en PARIDAD. Las páginas NUEVAS heredan todo copiando el esqueleto (`gen-landing.py`/`crear-servicio.py`/`generar-colonias.py`) — NUNCA escribir colores a mano. Enforcement: `check-plantilla.py` check 11b MARCA el off-brand (sin marcar el azul de marca) y `auto-fixers.py` (fixer `color-off-brand`, calibrado: azul-no-marca→#1e40af, rojo→#C2410C, verde→#22c55e) lo AUTO-SANA — corre en FASE 5 del prompt diario con `python3 .pipeline/auto-fixers.py run --apply`. Detalle: REGLAS.md (color-elec-20260620).

## Pipeline de mantenimiento autónomo
- Invocar con `/mantener-sitio` (skill en `.claude/skills/mantener-sitio/SKILL.md`) o con `.pipeline/mantener-prompt.txt`.
- 9 revisores: 5 LLM (seo, movil, a11y, perf, links) para lo SUBJETIVO + 4 DETERMINISTAS (gsc, indexabilidad, produccion, plantilla) que corren scripts en `.pipeline/` y garantizan las reglas mecánicas.
- Checkers deterministas (solo reportan, no arreglan):
  - `python3 .pipeline/check-plantilla.py` — reglas mecánicas de plantilla (enlaces/og:image rotos, popup sin ARIA, fetchpriority/CLS, paridad CSS, table-wrapper, theme-color, email contaminado).
  - `python3 .pipeline/check-indexabilidad.py` — sitemap vs realidad, canonical/og:url/breadcrumbs.
  - `node .pipeline/check-produccion.mjs` — producción en vivo (requiere `npm i puppeteer`).

## Pipeline de crecimiento autónomo
- **Mapa completo del sistema: `AUTOMATIZACION.md`** (cómo encajan skill + orquestador + motor + hooks + memoria).
- **Orquestador (punto de entrada determinista): `scripts/crecer.py`** — `estado` | `servicio spec.json` | `colonia spec.json` | `gate <ruta>` | `publicar "msg"`. Automatiza crear + sitemap + enlace en la home + bump sw + candado + publicar.
- Invocar con `/expandir-sitio` (skill en `.claude/skills/expandir-sitio/SKILL.md`). Hermano de `/mantener-sitio`: aquél ARREGLA, éste CREA lo que falta. La auditoría GSC y la indexación por MCP viven en el skill.
- Determina huecos en 4 dimensiones (oportunidades GSC con datos reales, geo, blog, mejoras), crea páginas con contenido único y **auto-publica solo si pasan TODOS los candados** (si fallan, deja en rama y avisa). Tope duro `MAX_PAGINAS=3` por corrida.
- Backbone determinista (garantiza paridad de plantilla y bloquea doorways):
  - `python3 .pipeline/gen-landing.py spec.json` — genera una landing copiando un esqueleto byte a byte + sustituciones afirmadas (aborta si no calzan o si hay fuga "plomero").
  - `python3 .pipeline/gate-pagina.py <ruta/index.html> ...` — candado todo-en-uno: validate-landing + ci-gate (0 ALTA) + anti-doorway (Jaccard < 0.80 vs hermanas).
- Generadores reusables (se apoyan en gen-landing.py; corren `--ejemplo` para ver el spec):
  - `python3 scripts/crear-servicio.py spec.json` — crea una página de SERVICIO nueva.
  - `python3 scripts/diferenciar-colonia.py spec.json` — promueve una colonia noindex→indexable con contenido único.

## Comandos útiles
- git log --oneline -30  (ver historia reciente)
- Servidor local para probar: `python3 -m http.server 8080`
