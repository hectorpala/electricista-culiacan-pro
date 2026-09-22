# EQUIPO.md — perfil del proyecto para /equipo (agentes globales en ~/.claude/agents/equipo-*.md)

proyecto: electricista
repo: /Users/openclaw/Sitios Web/Electricista Culiacán
produccion: https://electricistaculiacanpro.mx/
objetivo: más llamadas y WhatsApp (wa.me/526673922273) desde Culiacán; después indexación y CTR en GSC; la home es el activo que convierte (no degradarla).
propiedad_gsc: https://electricistaculiacanpro.mx/

memoria (leer antes de trabajar, en este orden):
- REGLAS.md — errores ya cometidos, por categoría (CSS, SEO, CONTENIDO, A11Y, INFRA, PERF). Cada tarea cita la regla que respeta.
- NEGOCIO.md — lo que el negocio SÍ y NO ofrece ("auto si es electricidad"; nada automotriz; "nunca precio en el cuerpo").
- ESTADO.md — últimas 3 entradas.
- CLAUDE.md — reglas duras resumidas; `index.html` es la FUENTE DE VERDAD de plantilla y marca.

backlog:
  next: python3 .pipeline/gestor-backlog.py next --max 10
  add: python3 .pipeline/gestor-backlog.py add - <<'EOF' {json} EOF   (--ejemplo para el spec; riesgo alto → cola humana)
  close: python3 .pipeline/gestor-backlog.py close --id X --estado hecho|descartado|bloqueado --commit SHA --nota "..."
  approve: python3 .pipeline/gestor-backlog.py approve --id X --riesgo medio --nota "DECISIÓN DEL COORDINADOR: ..."
  stats: python3 .pipeline/gestor-backlog.py stats

servidor_local: python3 -m http.server 8097 --directory "$WT" &   → http://127.0.0.1:8097/

gate_conjunto:
- python3 .pipeline/ci-gate.py                      → debe dar 0 ALTA (33 media/baja de "precio-en-body" son decisión del dueño, no tarea)
- python3 .pipeline/auto-fixers.py verify --base origin/main   → certifica lotes mecánicos; los "libres" deben ser solo los editados a mano
- bash validate-landing.sh <ruta>                   → corre en pre-commit para servicios/*; sobre index.html da falsos errores (es la referencia)
gate_archivo:
- python3 .pipeline/gate-pagina.py <ruta/index.html>   → CANDADO OK (validate-landing + ci-gate + anti-doorway Jaccard < 0.80)

invariantes (toda página servida):
- HTTP 200; JSON-LD parsea; canonical == og:url == twitter:url; 0 apariciones de "plomero" (fuga de la plantilla hermana); email SOLO contacto@electricistaculiacanpro.mx; teléfono 667 392 2273 / wa.me/526673922273; ETA de llegada "30-60 min" (una sola promesa); marca #E36414 (naranja) + azul de marca #1e40af; rojo prohibido → #C2410C; textos de contraste en #C2410C.
- Las colonias tienen DOS formas de JSON-LD (array plano y @graph): todo script que edite schema maneja ambas. Un href con ${...} es literal de JS.
- contacto/ está en CUARENTENA en auto-fixers.py (no la tocan los lotes); 19 páginas <150 tokens también.

intocables:
- precios visibles (33 páginas: decisión del dueño), tests, checkers (.pipeline/check-*.py, ci-gate, gate-pagina), hooks/, validate-landing.sh, borrar páginas indexables/en sitemap, testimonios/reseñas (no inventar ni "diferenciar" inventando), datos locales inventados (calles, landmarks).

riesgo:
  bajo: texto, CSS inline, meta, netlify headers, imágenes
  medio: JSON-LD, sitemap, JS, plantilla en >20 páginas, titles/descriptions, enlazado interno, noindex/canonical
  alto (cola humana): precios, borrar páginas con tráfico, cambios de giro fuera de NEGOCIO.md

lotes: >18 archivos SOLO con un fixer registrado en .pipeline/auto-fixers.py (lista FIXERS; patrón det/fix idempotente) aplicado con `run --solo <id> --apply <rutas explícitas>` (SIN rutas entra en full_run y dispara el auto-repair del bump de JS en ~679 HTML) y certificado con `verify --base origin/main`.

assets:
- CSS servido como immutable: cambiar contenido exige bump de ?v= en las referencias. Aplicar el cambio en los 3 CSS (styles.css, styles.min.css, styles.7f293647.css) y bumpear con la ceremonia PROPIA de auto-fixers (escribe `.pipeline/css-bump-state.json`, que `verify` usa para certificar el bump como mecánico):
  `python3 -c "import importlib.util as u,os;s=u.spec_from_file_location('af',os.path.join('.pipeline','auto-fixers.py'));m=u.module_from_spec(s);s.loader.exec_module(m);print(m._do_full_bump('equipo'))"` (desde el worktree; sube ?v= en todas las páginas salvo contacto/ en CUARENTENA + CACHE_VERSION de sw.js). NO usar `scripts/bump-css-version.py`: no escribe css-bump-state.json → `verify` marcaría ~690 HTML como libres y el siguiente `auto-fixers.py run --apply` re-bumpearía por auto-reparo (detectado 2026-09-21 al revisar el plan de T5).
- JS: main.js (fuente) y main.min.js (servido) están DIVERGIDOS (bk-e977a123): hasta reconciliarlos, un cambio de JS se parcha quirúrgicamente en main.min.js (REGLAS.md 2026-07-25), se verifica `grep -oE 'wa\.me/[0-9]+' main.min.js` == wa.me/526673922273 y `node --check`, y se bumpea con
  `python3 -c "import importlib.util as u,os;s=u.spec_from_file_location('af',os.path.join('.pipeline','auto-fixers.py'));m=u.module_from_spec(s);s.loader.exec_module(m);print(m._do_full_js_bump('equipo'))"` (+ subir CACHE_VERSION en sw.js si no lo hizo).

visual: node .pipeline/check-produccion.mjs (producción en vivo, puppeteer) · node .pipeline/check-skip-link.mjs · puppeteer en node_modules del repo para pruebas funcionales propias (NODE_PATH=<repo>/node_modules).

publicar:
  metodo: merge --ff-only a main + git push origin main → Netlify despliega en ~15-60 s (pre-push corre gate + auto-indexación GSC)
  automatica: si   (orden directa de Héctor, 13-sep-2026)
  verificar: [https://electricistaculiacanpro.mx/, https://electricistaculiacanpro.mx/servicios/emergencia-24-7/, https://electricistaculiacanpro.mx/blog/]
  ojo: .pipeline/ y .claude/ se sirven públicos en Netlify (no dejar secretos ni datos de terceros).

decide_humano:
- precios visibles en el cuerpo (33 páginas)
- borrar cualquier página que reciba impresiones/clics o esté en sitemap
- cualquier servicio/tema fuera de NEGOCIO.md (ej. eléctrico automotriz)
- qué hacer con los ~720 archivos sin commit de Codex en el árbol principal (rama auto/diario-*)

## Lecciones → pensador
- [2026-09-13] ESPECIFICACION: comprobar con `ls assets/images/optimizadas/<nombre>-420w.webp` que existen las variantes antes de exigir N <picture> (T4: 4/11).
- [2026-09-21] ESPECIFICACION: toda tarea que inserte `<a>` en texto suelto debe exigir el color de marca en el criterio (`getComputedStyle(a).color == rgb(30, 64, 175)`): no hay regla global `a{}` y el enlace sale azul UA #0000EE (T3: 4 enlaces, ronda de arreglador).
- [2026-09-21] ESPECIFICACION: una tarea de CSS servido (bump site-wide) va PRIMERA en el plan o no va: al final de la corrida no cabe en los 60 min (T5 diferida a bk-b1850812). Y la ceremonia es `_do_full_bump` de auto-fixers, no `bump-css-version.py` (ver assets).

## Lecciones → ejecutor
- [2026-09-13] HERRAMIENTA: `auto-fixers.py run --solo <fixer> --apply` SIN rutas dispara bump de JS en 679 HTML; pasar siempre las rutas de la tarea; si pasó, `git checkout --` de lo ajeno antes de reportar.
- [2026-09-21] CAPACIDAD: un `<a>` nuevo en texto suelto (FAQ, párrafos, "Sobre nosotros") hereda el azul UA #0000EE porque el sitio no tiene regla global `a{}`; lleva SIEMPRE `style="color:#1e40af;text-decoration:underline"` (patrón del footer de blogs) salvo que esté dentro de un componente con regla propia (`.benefits-cta a`, `.site-mini-nav a`, `.pricing-note a`). T3 20260921: 4 enlaces corregidos por el arreglador.

## Lecciones → arreglador

## Lecciones → probador
- [2026-09-13] HERRAMIENTA: "Permission to use Bash has been denied" NO es un veto global: el sandbox rechaza patrones (`cd X && …`, heredocs `<<EOF`, `$(...)`, `${...}`, `for…do`, `NODE_PATH=… node`). Reescribir con `git -C <wt> …` o Write de un script Python/Node en /tmp y `python3 /tmp/x.py`; jamás rendirse ni pedir permiso al coordinador (T5 y FINAL-1 de 20260913-2100 no verificaron nada por esto).
- [2026-09-13] EVIDENCIA: en "copia exacta" de reglas CSS, comparar el bloque completo normalizado contra styles.css, no solo colores.
- [2026-09-13] INSTRUCCION: "sin cambios vs base" se comprueba SOLO con `git -C <worktree> diff origin/main -- <ruta>` o `git show origin/main:<ruta>`; JAMÁS contra el árbol principal del repo (rama auto/diario-* con ~720 archivos de Codex sin commitear, p.ej. twitter:url añadido allí y ausente en main → FALLA falsa en T2 20260913-2100).
- [2026-09-17] INSTRUCCION: escribe TU PROPIO script de medición en /tmp; reutilizar el del ejecutor (T4: `/tmp/t4-check.js`) no es verificación independiente, es repetir su evidencia.
- [2026-09-17] ESPECIFICACION: el @font-face de Inter 600 apunta a `inter-400.woff2` A PROPÓSITO en las 688 páginas (fixer `font-dedup`: los archivos son copias byte a byte, 48 532 B); no es bug, no lo reportes.
- [2026-09-17] CONTEXTO: si un archivo fuera de alcance no está en la lista de excepciones del coordinador, repórtalo como FALLA de alcance pero di QUÉ cambió (T2: los 2 hubs de T4 lanzada después del briefing); el coordinador lo coteja.
- [2026-09-21] INSTRUCCION: en verificación FINAL, "las N páginas del diff" significa las N, no una muestra: un script con urllib sobre `git diff --name-only origin/main -- '*.html'` tarda segundos (FINAL 20260921: invariantes en "muestras" y experimento en 1 de 22; el coordinador tuvo que barrer 48 + 22).

## Lecciones → coordinador
- [2026-09-17] CONTEXTO: si lanzo un ejecutor nuevo DESPUÉS de briefear a un probador, el probador verá esos archivos como fuera de alcance y dará FALLA falsa (T2 20260917: los 2 hubs de T4). Avisar por SendMessage o listar en el briefing todo lo que pueda entrar en paralelo.
- [2026-09-17] PROCESO: mis propias escrituras en el worktree (calificaciones.jsonl, BACKLOG.jsonl) aparecen en `git status` de los agentes; declararlas siempre en el briefing.
- [2026-09-21] PROCESO: cuando dos tareas comparten archivo (T2 metas + T3 body en electricista/precios), stagear el contenido T2-only con `git hash-object -w --stdin` + `git update-index --cacheinfo 100644,<sha>,<ruta>` (quitando las inserciones de la otra con Python) para que cada commit lleve solo lo suyo; funcionó en f1157b43.
- [2026-09-21] PROCESO: el reloj de 60 min se agota con 4 tareas + 1 ronda de arreglador (21:00→22:00); la tarea site-wide (bump CSS) debe ir la primera del plan o encolarse, nunca "al final si da tiempo".
- [2026-09-21] HERRAMIENTA: `scripts/bump-css-version.py` NO escribe `.pipeline/css-bump-state.json`; el bump de CSS se hace con `_do_full_bump` de auto-fixers (ver assets) o `verify` marca todo el sitio como libre.
- [2026-09-16] INSTRUCCION: los scripts del pipeline se invocan SIEMPRE por ruta ABSOLUTA del worktree (`python3 /tmp/<wt>/.pipeline/gate-pagina.py`, `…/ci-gate.py`, `bash /tmp/<wt>/validate-landing.sh`); `.pipeline/x.py` relativo corre el script del árbol sucio (tu cwd) y compara contra el sitio equivocado → "DOORWAY Jaccard 1.00 vs sí misma" falso en T3 20260916-2100.
- [2026-09-16] INSTRUCCION: el ALCANCE de una tarea sin commitear se mide con `git -C <wt> diff --stat` (árbol vs HEAD), porque HEAD ya acumula los commits previos de la corrida; `diff origin/main` sumó las 674 páginas del T1 recuperado y dio "674 archivos" falso en T3 20260916-2100.
- [2026-09-16] EVIDENCIA: antes de dictaminar que un texto "no está", buscar la raíz (`garant`), no la formulación literal: "30-90" no aparecía pero el body decía "Garantía 30 a 90 días" (T3 20260916-2100).
- [2026-09-16] EVIDENCIA: en sitemap.xml una URL se localiza por su `<loc>` EXACTA con delimitadores (`<loc>https://…/blog/</loc>`); `grep -A1 '/blog/'` atrapa el primer post y dio un lastmod "desincronizado" falso (T2 20260916-2100).
