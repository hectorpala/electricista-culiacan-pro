# ESTADO — Electricista Culiacán

## 2026-07-01 (Auto Agente diario — 1 ALTA: regresión de contraste WCAG rating-stars en 18/30 páginas · 7 tareas nuevas a backlog) — PUBLICADO ✅
Rama `auto/diario-20260701-2001`, merge `15dbeb75` a main (push OK; pre-push auto-indexó 18 URLs).
Aprendizaje (2 reglas nuevas + 1 check nuevo) en commit separado `20113bcf`. HEALTH CHECK:
home/contacto/servicios/blog → 200 (servidor 8123). ci-gate 0 ALTA · 34+2 media/baja (33
precio-en-body + 1 theme-color conocidos + 2 twitter:url nuevos, ambos ya en backlog). 9
revisores corrieron en paralelo como subagentes.

- **REGRESIÓN DE CONTRASTE WCAG (alta, a11y, 18/30 páginas hoy):** el fix de contraste del
  2026-06-30 (`#FBBC04`/`#FFA000` → `#B45309`) solo tocó las 3 hojas CSS compartidas. Quedaron
  30 páginas con el color viejo (~1.71:1, falla WCAG AA) en el `<style>` crítico INLINE de cada
  página y en atributos `style=""` inline de los testimonios (mayor especificidad, el CSS
  externo nunca los sobreescribe). Corregidas 18 de 30 hoy (home + 11 blogs + 6 servicios,
  dentro del cap de 18 páginas/corrida) + el CSS huérfano `assets/css/critical.css`. Las 12
  páginas de servicio restantes quedaron en `BACKLOG.jsonl` (`bk-3d5ba91f`) para mañana.

- **DESCUBRIMIENTO — auto-fixer roto (media, tooling):** el fixer `tap-target-44` de
  `auto-fixers.py` busca `.breadcrumb-link` en las 3 hojas CSS compartidas, pero ese selector en
  realidad vive en el `<style>` crítico inline de CADA página — el fixer es un no-op silencioso
  que siempre reporta "nada que arreglar" sin haber arreglado nada. Documentado en REGLAS.md,
  encolado `bk-afcc93f1` (requiere reescribir el fixer, fuera de alcance hoy).

- **GSC (FASE 6):** 100 clics/28d, 4558 impr, CTR 2.19%, pos 7.1 (estable vs. ayer). Sin
  indexación bloqueada. Canibalización "electricista"/sitemap fantasma siguen pendiente-humano
  (heredados). Sin páginas nuevas: el diff de FASE 5 ya llegó al cap de 18 páginas. Detalle en
  `.pipeline/oportunidades-20260701.md`.

- **BACKLOG — 7 tareas nuevas encoladas (ninguna ejecutada hoy, solo triaje):**
  `bk-3d5ba91f` (12 páginas de servicio con la regresión de contraste, riesgo bajo),
  `bk-e5b86d92` (geo faltante en 40 colonias indexables, requiere_humano — sin fuente de GPS
  real en el repo, inventar coords violaría anti-doorway), `bk-038f8c19` (fuentes @font-face
  duplicadas byte-idénticas, ~47KB extra), `bk-f865534d` (2 blog cards sin variante -420w),
  `bk-f93458cd` (main.min.js/analytics-events.min.js sin versionar, cambio estructural de 676
  páginas), `bk-afcc93f1` (tap-target de nav/breadcrumb/footer, ver arriba), `bk-e042beca`
  (`servicios/index.html` no existe → 404 real, 32 breadcrumbs rotos — candidato de crecimiento),
  `bk-f07ed321` (2 blogs sin meta twitter:url, hallazgo del verificador).

- **APRENDIZAJE:** 2 reglas nuevas en REGLAS.md (regresion-contraste-inline-20260701,
  auto-fixer-selector-inexistente-20260701) + 1 check nuevo activo (`check-indexabilidad.py`
  twitter:url==canonical, excluyendo colonias que nunca tuvieron esa etiqueta por diseño). Un
  segundo check (check 33 de `check-plantilla.py`, contraste dentro del HTML) quedó ESCRITO pero
  INACTIVO a propósito: activarlo hoy con 12 páginas aún pendientes habría bloqueado el
  pre-commit hook (corre sobre todo el disco) para todas las corridas futuras — se activa cuando
  `bk-3d5ba91f` cierre. Más de 51 reglas aprendidas en total.

- **VERIFICACIÓN:** Verificador ok=true. Confirmó las 18 páginas con HTTP 200, JSON-LD válido,
  `#FBBC04` ya no aparece en ninguna, `#FFA000` (no tocado) intacto, 0 enlaces rotos, sin
  precios/tests/borrados/contaminación de email, BACKLOG.jsonl jsonlines íntegro. 4 hallazgos no
  bloqueantes reportados (documentación de más, 2 preexistentes ya en backlog, 1 CSS huérfano).

- **PENDIENTE-HUMANO (heredados + nuevos):**
  - Geo faltante en 40 colonias indexables (`bk-e5b86d92`) — requiere coordenadas GPS reales,
    no hay fuente en el repo y no se pueden inventar (anti-doorway).
  - Canibalización interna "electricista" entre home/servicios/colonias — apuesta de estrategia
    SEO, no auto-arreglable.
  - Sitemap fantasma en Search Console (`/sitemaps/servicios_colonias_sitemap.xml`) — acción
    manual en la consola, no hay tool por código.
  - `/servicios/index.html` no existe → 404, 32 breadcrumbs rotos (`bk-e042beca`).
  - Precios en body HTML: 33 páginas (decisión estratégica del dueño).
  - Heredados: aria-expanded JS toggle, popup emoji aria-hidden en contacto/, skip-link/tap-
    target, title/description largos en colonias, meta X-Frame-Options inválido (~50 páginas
    reales, corregido el conteo de ~692 estimado).

## 2026-06-30 (Auto Agente diario — 2 ALTA: contraste WCAG estrellas + CSS no-bloqueante 16 colonias · 1 MEDIA: logo JSON-LD 2 blogs) — PUBLICADO ✅
Rama `auto/diario-20260630-2000`, merge `51f44ac1` a main (push OK; pre-push auto-indexó 86 URLs). Aprendizaje (2 checks nuevos + 3 reglas) en commit separado `4b28ebbe`. HEALTH CHECK: home/contacto/servicios/blog → 200 (servidor 8110). ci-gate 0 ALTA · 34 media/baja (precio-en-body 33 conocidas + google-stub baja). check-indexabilidad 0. 18 páginas HTML con contenido real tocado (16 colonias + 2 blogs, exactamente al cap) + 689 con bump de versión de CSS (cambio lógico de asset, excluido del cap). 9 revisores corrieron en paralelo como subagentes.

- **CONTRASTE WCAG (alta, a11y, site-wide):** `.rating-stars` (`#FBBC04` ~1.71:1) y `.stars` (`#FFA000` ~2.04:1) en 686/692 páginas (hero + testimonios) fallaban el mínimo WCAG AA de 4.5:1. Corregido a `#B45309` (~5:1) en las 3 hojas CSS en paridad, con bump `?v=20260621→20260630` en 689 páginas y `CACHE_VERSION v16→v17` en sw.js.

- **CSS NO-BLOQUEANTE en 16 colonias indexables (alta, perf):** las únicas 16 colonias que Google realmente indexa cargaban el CSS compartido de forma render-blocking (`<link rel="stylesheet">` directo) mientras el resto del sitio ya usa el patrón no-bloqueante de la home (`media="print" onload` + `<noscript>`). Corregido en las 16.

- **LOGO JSON-LD roto en 2 blogs (media, links):** `como-prevenir-cortocircuitos-casa` y `senales-instalacion-electrica-obsoleta` tenían el campo `logo` del schema apuntando a una ruta con carpeta duplicada (`assets/images/assets/images/...`), archivo inexistente (404 silencioso en el schema). Corregido.

- **GSC (FASE 6):** 98 clics, 4490 impr, CTR 2.18% (↑ desde 2.05%), pos 7.1. Tendencia positiva. Sin páginas nuevas ni optimizaciones ejecutadas hoy: el diff de FASE 5 ya llegó al cap de 18 páginas con las correcciones ALTA. 4 oportunidades de bajo riesgo encoladas al backlog para la próxima corrida (`bk-fbde293f` tap-target skip-link, `bk-22c6bf24` title/description largos, `bk-df162f50` meta X-Frame-Options inválido, `bk-f38bd140` CTR-fix instalacion-contactos). Detalle completo en `.pipeline/oportunidades-20260630.md`.

- **APRENDIZAJE:** +2 checks deterministas (31: ruta duplicada en URL propia; 32: regresión de contraste rating-stars) en check-plantilla.py, ambos probados (cazan el defecto real, 0 falsos positivos). +3 reglas nuevas en REGLAS.md. Más de 49 reglas aprendidas en total.

- **VERIFICACIÓN:** Verificador ok=true, 0 problemas. Confirmó paridad byte a byte de los 3 CSS, los 18 archivos de contenido real, ci-gate 0 ALTA, gate-pagina.py OK en los 18, HTTP 200 en todas las páginas muestreadas, sin precios/borrados/contaminación de email.

- **PENDIENTE-HUMANO (heredados + nuevos):**
  - CTR emergencia-24-7: `electricistas 24 horas` pos 13.7 — bk-9d8c6176 (necesita mejora de contenido, no solo CTR)
  - Canibalización interna de "electricista" entre home/electricista/electricista-precios — apuesta de estrategia SEO, no auto-arreglable
  - Sitemap fantasma en Search Console (`/sitemaps/servicios_colonias_sitemap.xml`, ya no existe en disco) — requiere quitarlo manualmente en la consola de GSC, no hay tool para hacerlo por código
  - `/servicios/index.html` NO existe → 404 (breadcrumbs rotos site-wide)
  - Precios en body HTML: 33 páginas (decisión estratégica del dueño)
  - Heredados: aria-expanded JS toggle (bk-b7465a9a); popup emoji aria-hidden contacto/ (bloqueado); contraste WCAG AA nav-link/btn-primary; skip-link/main (~31-47 págs) + tap-target 44px (bk-fbde293f, nuevo hoy); title/description largos en colonias (bk-22c6bf24, nuevo hoy); meta X-Frame-Options inválido site-wide (bk-df162f50, nuevo hoy, ~692 páginas)

## 2026-06-29-nocturna (Auto Agente diario — 16 popup ortografía colonias + CTR home meta) — PUBLICADO ✅
Rama `auto/diario-20260629-2000`, merge `c026f01b` a main (push OK; pre-push **auto-indexó 17 URLs**: home + 16 colonias). HEALTH CHECK: home/contacto/servicios/blog → 200 (servidor 8102). ci-gate 0 ALTA · 34 media/baja (precio-en-body 33 conocidas + google-stub baja). check-indexabilidad 0. 17 HTML (dentro del cap de 18). Verificador y Aprendiz corrieron en paralelo como subagentes.

- **16 COLONIAS — Popup ortografía (media, contenido):** Completó el backlog bk-549b7b15. Las 16 colonias indexables restantes (centro, chapultepec, guadalupe, infonavit-humaya, la-conquista, la-primavera, las-coloradas, las-quintas, montebello, prados-de-la-conquista, santa-aynes, stanza-toscana, tierra-blanca, tres-rios, villa-universidad, zona-dorada) tenían los 3 errores heredados de plantilla: `>Espera!</h3>` → `>¡Espera!</h3>`, `Tienes una emergencia` → `¿Tienes una emergencia`, `Contactanos` → `Contáctanos`. Script con re.sub + lookbehind `(?<!¿)` para evitar cascada doble-¿. **Popup corregido en todo el sitio** (49 páginas total). 0 mojibake, 0 bug cascada.

- **HOME — CTR meta description (media, SEO):** Completó bk-a4194608. `electrica cerca de mi ubicación` pos 2.2, 31 impr, CTR 3.2% (esperado ~15% en pos 2). Meta description: "cerca de ti" → "cerca de tu ubicación"; "Vamos a domicilio 24/7 con llegada" → "A domicilio 24/7, llegada"; "Técnico certificado 4.8★" → "Técnico experto ★4.8". Las 3 ocurrencias (meta, og:description, twitter:description) actualizadas. Medir CTR en ~3-4 semanas.

- **GSC (FASE 6):** 92 clics, 4483 impr, CTR 2.05%, pos 7.1. Clics -13% vs anterior, impr +2%. Sin páginas nuevas: el sitio cubre la demanda. `electricista culiacan` pos 4.3, CTR 9.4% (OK para pos 4). `electricista` pos 3.3, 103 impr, CTR 3.9% (pendiente). `electricistas 24 horas` pos 13.7 (bk-9d8c6176 — pos 13 no mejora con CTR fix, necesita contenido).

- **APRENDIZAJE:** +1 check nuevo (check 30: popup ortografía en páginas con exit-intent-popup, MEDIA). 2 entradas en HISTORIAL.jsonl. Total reglas > 46.

- **VERIFICACIÓN:** Verificador ok=true, 16/16 popup OK, home CTR OK, ci-gate 0 ALTA, HTTP 200 en 5/5, 0 problemas.

- **PENDIENTE-HUMANO (heredados + actualizados):**
  - CTR emergencia-24-7: `electricistas 24 horas` pos 13.7 — bk-9d8c6176 (en pos 13 el CTR fix no ayuda; necesita mejora de contenido para subir a pág 1)
  - `/servicios/index.html` NO existe → 404 (breadcrumbs rotos site-wide)
  - Precios en body HTML: 33 páginas (decisión estratégica del dueño)
  - Heredados: aria-expanded JS toggle (bk-b7465a9a); popup emoji aria-hidden contacto/ (bloqueado); contraste WCAG AA nav-link/btn-primary; skip-link/main (~31-47 págs)
  - Experimento title home: medir pos/CTR de "electricista culiacan" ~2026-07-15

## 2026-06-29 (Auto Agente diario — 18 popup ortografía servicios+hub / verificador atrapó bug de replace cascada) — PUBLICADO ✅
Rama `auto/diario-20260629-0017`, merge `3709f447` a main (push OK; pre-push **auto-indexó 18 URLs**). HEALTH CHECK: home/contacto/servicios/blog → 200 (servidor 8099). ci-gate 0 ALTA · 34 media/baja (precio-en-body 33 conocidas + google-stub baja). check-indexabilidad 0. 18 HTML (exactamente al cap). Revisores LLM stalled (mismo problema de streaming); se usaron checkers deterministas directamente.

- **18 SERVICIOS+HUB — Popup ortografía (media, contenido):** Completó el backlog bk-72cc7764 para páginas de servicios. 17 servicios menores (cambio-cableado, contrato-luz-medidor-cfe, dictamen-electrico, iluminacion-led, instalacion-bomba-agua, instalacion-calentador-electrico, instalacion-camaras-seguridad, instalacion-centro-carga, instalacion-cercas-electricas, instalacion-minisplit, instalacion-paneles-solares, instalacion-planta-luz-generador, instalacion-porton-electrico, instalacion-tierra-fisica, instalacion-ventiladores-techo, mantenimiento-tableros, reparacion-minisplit) + hub electricista-colonias-culiacan. Los 3 errores heredados de plantilla: `>Espera!</h3>` → `>¡Espera!</h3>`, `Tienes una emergencia...` → `¿Tienes una emergencia...`, `Contactanos` → `Contáctanos`. **INCIDENTE de aprendizaje:** el script original tenía 3 `str.replace()` en cascada → Variant B encontró "Tienes...Contáctanos" como substring del resultado ya corregido de Variant A → producía `¿¿Tienes` (doble signo). El verificador ronda 1 lo atrapó (ok=false). Se corrigió con un segundo replace `¿¿Tienes`→`¿Tienes`. Verificador ronda 2 ok=true. Nueva regla en REGLAS.md: `OPERACION-PIPELINE/REPLACE-CASCADA`.

- **GSC (FASE 6):** 94 clics, 4679 impr, CTR 2.01%, pos 7.0. Clics -10% vs anterior, impr +7% → CTR sigue siendo el reto. `electricista culiacan` mejoró de pos 7.7 → 4.3 (experimento title 2026-06-22 funcionando — medir hasta 2026-07-15). Sin páginas nuevas: todas las queries tienen página. Backlogs encolados: bk-549b7b15 (popup 16 colonias), bk-a4194608 (CTR home meta), bk-9d8c6176 (CTR emergencia-24-7).

- **VERIFICACIÓN (2 rondas):** Ronda 1: ok=false (bug ¿¿Tienes doble). Ronda 2: **ok=true, 0 problemas** (ci-gate 0 ALTA; validate-landing 18/18 PASO; ¿Tienes simple en todos; 0 mojibake; 0 plomero; 0 borrados; HTTP 200).

- **APRENDIZAJE:** +1 regla nueva (replace-cascada-20260629): `OPERACION-PIPELINE/REPLACE-CASCADA`. Total reglas > 45.

- **PENDIENTE-HUMANO (heredados + actualizados):**
  - Popup ortografía: 16 colonias indexables pendientes — bk-549b7b15
  - CTR home meta description: "electrica cerca de mi ubicación" pos 2.1, 36 impr, CTR 2.8% (pos 2 debería dar ~15%) — bk-a4194608
  - CTR emergencia-24-7: queries "electricistas 24 horas" pos 13.7 — bk-9d8c6176
  - Experimento title home: medir pos/CTR de "electricista culiacan" ~2026-07-15
  - `/servicios/index.html` NO existe → 404 (breadcrumbs rotos site-wide)
  - Precios en body HTML: 33 páginas (decisión estratégica del dueño)
  - Heredados: aria-expanded JS toggle (bk-b7465a9a); popup emoji aria-hidden contacto/ (bloqueado); contraste WCAG AA nav-link/btn-primary; skip-link/main (~31-47 págs)

## 2026-06-28 (Auto Agente diario — 2 fixes: popup ortografía 15 páginas + enlace interno blog) — PUBLICADO ✅
Rama `auto/diario-20260628-1250`, merge `d03e27b7` a main (push OK; pre-push **auto-indexó 15 URLs**). HEALTH CHECK: home/contacto/servicios/blog → 200. ci-gate 0 ALTA · 34 media/baja (precio-en-body 33 conocidas + google-stub baja). check-indexabilidad 0. 15 HTML (dentro del cap de 18). Revisores especializados tuvieron timeout (problema de streaming); se usaron checkers deterministas directamente.

- **15 SERVICIOS — Popup ortografía rota (media, contenido):** 49 páginas tenían el popup exit-intent con 3 errores de apertura heredados de la plantilla: `Espera!` (sin `¡`), `Tienes una emergencia de electricidad?` (sin `¿`), `Contactanos` (sin tilde). Corregidas las 15 de mayor tráfico: electricista, emergencia-24-7, electricista-a-domicilio, reparacion-cortocircuitos, no-hay-luz, instalacion-electrica, electricista-cerca-de-mi, electricista-comercial, electricista-precios, 4 zonas (norte/sur/oriente/poniente), electricista-centro y instalacion-contactos. **34 páginas restantes (colonias + servicios menores) en backlog bk-72cc7764.**

- **1 SERVICIO — Enlace interno cortocircuitos → blog prevención (baja, SEO):** `servicios/reparacion-cortocircuitos/index.html` no enlazaba al blog `como-prevenir-cortocircuitos-casa/`. El blog ranquea en pos 8.3 para "como evitar un corto circuito en casa" (15 impr, 0 clics) sin enlace desde la página de servicio más relevante. Añadido enlace al final del FAQ.

- **GSC (FASE 6):** 91 clics, 4689 impr, CTR 1.94%, pos 7.0. Clics -13% vs anterior, impr +7% → problema de CTR. Query "electricista" a pos 3.2 con 108 impr y CTR 2.8% (debería ser ~10%). Sin creación de páginas nuevas: el sitio cubre la demanda; "electrician near me" y "automotriz" no proceden per NEGOCIO.md.

- **VERIFICACIÓN:** ok=true, 0 problemas (ci-gate 0 ALTA; validate-landing 15/15 PASO; popup correcto en 5 páginas muestreadas; blog link presente; 0 plomero; 0 borrados; HTTP 200 en todas).

- **PENDIENTE-HUMANO (heredados + actualizados):**
  - Popup ortografía: 34 páginas restantes (colonias indexables + servicios menores) — bk-72cc7764
  - Problema CTR: "electricista" pos 3.2, 108 impr, CTR 2.8% — investigar qué URL y por qué tan bajo
  - `/servicios/index.html` NO existe → 404 (breadcrumbs rotos site-wide)
  - Precios en body HTML: 33 páginas (decisión estratégica del dueño)
  - Heredados: aria-expanded JS toggle (bk-b7465a9a); popup emoji aria-hidden contacto/ (bloqueado); contraste WCAG AA nav-link/btn-primary; skip-link/main (~31-47 págs)

## 2026-06-27 (Auto Agente diario — 9 fixes 6-blogs/1-servicio: JSON-LD image, JS-IIFE, precio-FAQ, CTR) — PUBLICADO ✅
Rama `auto/diario-20260626-2000`, merge `1f5f5836` a main (push OK; pre-push **auto-indexó 7 URLs**: 6 blogs + instalacion-contactos). HEALTH CHECK: home/contacto/servicios/blog → 200. ci-gate 0 ALTA · 34 media/baja (precio-en-body 33 conocidas + google-stub baja). check-indexabilidad 0. 7 HTML (dentro del cap de 18).

- **4 BLOGS — JSON-LD "image" URL incorrecta (media, schema):** ahorro-energia-led, cuando-llamar-emergencia, mantenimiento-tablero, seguridad-lluvias tenían `"image": "...electricista-culiacan-hero-800w.webp"` (nombre del esqueleto) en el JSON-LD Electrician en vez del nombre real del asset `hero-electricista-culiacan-800w.webp`. Corregido en los 4 blogs.

- **2 BLOGS — main.min.js duplicado en blogs con IIFE inline (baja→media, JS):** como-prevenir-cortocircuitos-casa y senales-instalacion-electrica-obsoleta tenían `<script src="/main.min.js" defer>` ADEMÁS de su IIFE inline completo (~4512 chars). Per REGLAS.md 2026-06-23 (PERF/JS-INLINE-IIFE), añadir main.min.js a un blog con IIFE propio duplicaría el listener del menú toggle y lo rompería. Eliminado main.min.js de los 2 blogs.

- **2 BLOGS — precio de servicio en FAQ body (media, negocio):** como-prevenir-cortocircuitos-casa tenía en el FAQ visible `"cuesta desde $500 MXN"` y mantenimiento-tablero tenía `"desde $600 hasta $1,500 MXN"`. NEGOCIO.md: "NUNCA precio visible en el cuerpo". Reemplazados por "Solicita tu cotización sin costo" en ambos lugares (HTML visible + JSON-LD FAQPage text).

- **1 SERVICIO — CTR optimization contactos (media, seo):** instalacion-contactos/index.html: title/og/twitter actualizados de "Instalación de Contactos Eléctricos en Culiacán | 24 Horas" → "Contactos Eléctricos Culiacán | Instalación y Cambio · 24/7" para capturar keyword `contactos culiacan` (pos 4.9, 15 impr, 0 clics en GSC).

- **GSC (FASE 6):** 87 clics, 4381 impr, CTR 1.99%, pos 7.2. Clics -15% vs anterior. `electricista culiacán` pos 4.7 (↑ desde 8.2 — título cambiado 2026-06-22 funcionó). No se crearon páginas nuevas: el sitio cubre la demanda; la única acción de crecimiento fue la optimización CTR de contactos ya en working tree.

- **VERIFICACIÓN (1 ronda):** ok=true, 0 problemas (7 archivos verificados: ci-gate 0 ALTA, HTTP 200 en todos, JSON-LD image correcto, main.min.js ausente en IIFE blogs, precios quitados del HTML, nuevo title contactos, 0 plomero, 0 borrados).

- **PENDIENTE-HUMANO (heredados + nuevos de esta corrida):**
  - `/servicios/index.html` NO existe → 404 en Netlify (breadcrumbs de TODAS las páginas de servicio enlazan ahí). Opciones: (1) crear hub servicios/index.html o (2) hacer la miga no-enlazable. Candidata a corrida de crecimiento.
  - Precios en body HTML: 33 páginas (blogs + servicios) con precios de mercado, testimonios y nuestra tarifa. Check 28 los detecta pero son decisión de estrategia (cuanto-cuesta y electricista-precios son páginas DE precios — quitarles el precio destruiría el contenido). Pendiente: ¿tolerar precios educativos/de mercado en blog o reescribir?
  - Heredados: popup ortografía (~49 págs, bk-72cc7764); aria-expanded JS toggle (bk-b7465a9a); canibalización home/contacto; contraste WCAG AA nav-link/btn-primary; skip-link/main (~31-47 págs); preload as=style hint en 33 servicios + 11 blogs

## 2026-06-26 (Auto Agente diario 2ª corrida — 13 fixes home/zonas/blogs/tierra-fisica) — PUBLICADO ✅
Rama `auto/diario-20260626-1227`, merge `296c0208` a main (push OK; pre-push **auto-indexó 13 URLs**: home, 5 zonas, 6 blogs, tierra-fisica). HEALTH CHECK: ci-gate 0 ALTA · 1 baja (falso positivo google-stub pre-existente). check-indexabilidad 0. 13 HTML + sitemap (16 archivos diff).

- **HOME — og:image/CLS/logo (media, index.html) — lo principal:** (a) `og:image`/`twitter:image` apuntaban a `reparacion-cortocircuitos-culiacan-800w.webp` en vez del hero → corregido a `hero-electricista-culiacan-800w.webp`; `og:image:height` 800→437 (reales del WebP). (b) Hero `<img height="800">` cuando `hero-electricista-culiacan-1200w.webp` mide 1200×655 → CLS fijo con `height="655"`. (c) JSON-LD logo usaba `logo-512.webp` (y antes .png) → corregido a `electricista-culiacan-pro-logo.webp` (que es el logo de marca, 512×512) en las 2 ocurrencias de JSON-LD; `height` 366→512. Anchor `<a href="/servicios/emergencia-24-7/">Electricista 24 horas Culiacán</a>` añadido a lista semántica.

- **HOME — validate-landing pre-existente (fix estructural):** index.html fallaba gate-pagina.py con 4 errores pre-existentes que bloquearon el candidato en primera pasada del verificador. Corregidos: (a) security headers meta (X-Content-Type-Options, X-Frame-Options, X-XSS-Protection); (b) `<meta name="template-version" content="v2.0.0">`; (c) JSON-LD logo → logo correcto (también arreglaba punto c de arriba); (d) eliminado `<link rel="preload" href="styles.*.css" as="style">` pre-existente (CSS sigue cargando async vía media=print trick, el preload era redundante y validate-landing lo prohibía). Ahora `bash validate-landing.sh index.html` → PASO (1 warning no-crítico: meta author).

- **5 ZONAS — GPS inconsistentes en JSON-LD (media):** Las 5 páginas de zona tenían `meta geo.position` con coords reales de la zona, pero el JSON-LD `GeoCoordinates` usaba el centro de la ciudad (24.7903/-107.3878) para todas. Corregido con las coords únicas de cada zona: norte 24.8230/-107.4090, sur 24.7560/-107.3960, oriente 24.8050/-107.3760, poniente 24.8090/-107.4180, centro 24.7993/-107.3938.

- **6 BLOGS — margin-top:20rem (baja, layout móvil):** Los 6 blogs tenían `.hero-rating { margin-top:20rem }` en el bloque `@media(max-width:768px)`, empujando el badge de calificación 320px debajo del H1 en móvil. Corregido a `margin-top:1rem`. Además: blog cortocircuitos H2 renombrado a la keyword exacta del query; blog emergencia y blog lluvias — 6 y 5 `.benefit-icon` decorativos añadidos `aria-hidden="true"`.

- **TIERRA FÍSICA — precio visible en body (media):** `servicios/instalacion-tierra-fisica/index.html` tenía "Desde $1,500 MXN" en meta description (ya corregido corrida anterior), PERO también en el hero-subtitle y en el FAQ HTML body. NEGOCIO.md: "NUNCA precio visible en el cuerpo". Eliminado de ambos lugares; FAQ ahora dice "cotización sin costo para tu caso específico". El JSON-LD `priceRange`/`offers` con precios se conserva (es el lugar correcto per NEGOCIO.md).

- **VERIFICACIÓN (3 rondas):** 1ª: ok=false (contacto/ falla gate pre-existente; precio tierra-fisica body; servidor :8080 era del sitio hermano) → contacto/ revertido (backlog), precio corregido, servidor :8091. 2ª: ok=false (index.html falla gate por 4 errores pre-existentes) → 5 fixes en index.html para que pase validate-landing. 3ª: **ok=true, 0 problemas** (ci-gate 0 ALTA; validate-landing index.html PASO; gate-pagina todos los archivos OK; GPS únicos; precios solo en JSON-LD; og:image correcto; 0 mojibake; 0 plomero; 13/13 URLs 200).

- **APRENDIZAJE (FASE 9):** +5 reglas nuevas: `gps-jsonld-meta-inconsistency`, `hero-rating-margin-top-20rem`, `og-image-hero-match`, `jsonld-logo-brand-asset`, `precio-visible-body`. +3 checks en check-plantilla.py: GPS inconsistency (MEDIA), precio en body visible (MEDIA), logo JSON-LD asset (MEDIA).

- **ENCOLADO/DIFERIDO:** bk-72cc7764 popup ortografía ~49 págs; bk-b7465a9a aria-expanded JS toggle; bk-dbdf31bc ctr-fix electricista-precios; bk nuevo contacto/ emoji aria-hidden (bloqueado hasta migración plantilla v2.0.0).

- **PENDIENTE-HUMANO (heredados + nuevos de esta corrida):**
  - Precios visibles en body: home `section#precios` FAQ (estrategia conversión); emergencia-24-7, mantenimiento-tableros, páginas de zona con precios de $200 (estrategia)
  - Página `electricista-precios` y blog `cuanto-cuesta` (precio table — decisión dueño)
  - Sitemap fantasma `/sitemaps/servicios_colonias_sitemap.xml` (consola GSC, borrar manual)
  - Canibalización "electricista culiacán" home/contacto/precios
  - skip-link/`<main>` template-wide (~31-47 págs)
  - Contraste WCAG AA `.nav-link` y `.btn-primary`
  - preload as=style hint en 33 servicios + 11 blogs (lote > cap)
  - CLS height fix en blog articles (heights variadas por imagen)
  - contacto/index.html migración a plantilla v2.0.0 (pre-requisito para el fix emoji a11y)

## 2026-06-26 (Auto Agente maratón — twitter:card en 40 colonias indexables) — PUBLICADO ✅
Rama `auto/twitter-card-colonias-20260626`. HEALTH CHECK: ci-gate 0 ALTA · 0 media (solo falso positivo baja google-stub pre-existente). check-indexabilidad 0. Cambio puro mecánico, solo HTML inline (no CSS servido → sin bump ?v=/sw.js). 42 archivos: 40 colonias + HISTORIAL + REGLAS.
- **TWITTER:CARD FALTANTE EN 40 COLONIAS INDEXABLES (media, seo/social) — lo principal:** cierra el backlog `bk-228a32dd` encolado 2026-06-23. Las 40 colonias indexables tenían `<meta name="twitter:image">` pero NO `<meta name="twitter:card" content="summary_large_image">` → Twitter/X ignoraba toda la metadata (sin card, no se genera tarjeta social). El lote previo `twitter-image-parity` añadió la imagen pero olvidó el card. Fix: `<meta name="twitter:card" content="summary_large_image" />` insertado antes de `twitter:image` en las 40 colonias con Python UTF-8. Verificado: 0 mojibake (`Ã` / replacement char), orden card-antes-image correcto en muestra, ci-gate VERDE, check-plantilla 0 ALTA · 0 MEDIA.
- **Stash incluido (del 2026-06-25):** HISTORIAL.jsonl + REGLAS.md con la entrada del fix de reintentos del crecer-diario.sh (corrida 2026-06-25 no había committeado la memoria).
- **ENCOLADO/DIFERIDO (sin cambio):** bk-72cc7764 popup ortografía ~49 págs; bk-b7465a9a aria-expanded JS toggle; bk-4654c8eb enriquecer emergencia-24-7; bk-dbdf31bc ctr-fix electricista-precios.
- **PENDIENTE-HUMANO (heredados):** canibalización "electricista culiacán" entre home/contacto/electricista-precios; contraste WCAG AA `.nav-link`/`.btn-primary`; foco/focus-trap exit-popup main.js; skip-link/`<main>` en ~31-47 págs; reapuntar revisor-gsc; sitemap fantasma `/sitemaps/servicios_colonias_sitemap.xml`.

## 2026-06-23 (Auto Agente diario — destapa checker de indexabilidad CIEGO + perf contacto/gracias/hub + check 25) — PUBLICADO ✅
Rama `auto/diario-20260623-2000`, merge `9406d9f7` a main (push OK; pre-push **auto-indexó 2 URLs**: /contacto/ y el hub de colonias — 0 en cola). HEALTH CHECK previo OK (home, /contacto/, /servicios/, /blog/, instalacion-electrica, electricista → 200 en :8080). Sincronizado main con origin (--ff-only "Already up to date") antes de ramificar. 9 revisores en paralelo. **GSC FUNCIONAL** (`mcp__gsc__*` cargadas con ToolSearch select:; `gsc_list_sites` confirmó la propiedad): 85 clics, 4199 impr, CTR 2.02%, pos 7.1 (clics −9%, impr −2% vs periodo anterior).
- **CHECKER DE INDEXABILIDAD CIEGO (alta, infra) — lo principal:** `.pipeline/check-indexabilidad.py` apuntaba a `sitemaps/main_sitemap.xml` (estructura del sitio HERMANO Plomero, de donde se portó en commit 20d41380) pero ESTE sitio tiene el sitemap en `sitemap.xml` en la RAÍZ. Devolvía `{"hallazgos":[], "error":"no se encontro main_sitemap.xml"}` → un consumidor que solo lee 'hallazgos' lo tomaba por "sitio limpio" = verificación CIEGA silenciosa (justo la trampa que el mandato advierte). El revisor-indexabilidad lo cazó esta corrida (emitió ALTA "verificación ciega"). FIX: (a) `SITEMAP=sitemap.xml` en raíz; (b) si el sitemap NO existe, ahora EMITE un hallazgo ALTA "verificación ciega" en vez de vaciar en silencio. Ahora recorre las 87 URLs (0 hallazgos = realmente limpio).
- **PERF render-blocking + LCP (media, 3 págs):** contacto/ y gracias/ cargaban el CSS BLOQUEANTE → patrón `media="print" onload` + `<noscript>`. Hub colonias sin preload LCP del hero → `<link rel="preload" as="image">`. Cierra bk-5f77e166.
- **twitter:card FALTANTE en 40 colonias (media, seo) — encolado:** 40 archivos > candado 18 → bk-228a32dd.
- **CRECER (FASE 6): 0 páginas nuevas.**
- **APRENDIZAJE:** +3 reglas (41→44): INFRA/PORT-CHECKER-CIEGO, SEO/TWITTER-CARD, PERF/JS-INLINE-IIFE. check 25 nuevo.

## 2026-06-22 (Auto Agente diario 2ª corrida — honestidad "30-60 min" en 5 BLOGS + priceRange + perf upscale + checks 23/24) — PUBLICADO ✅
Rama `auto/diario-20260622-2213`, merge `c971a3d4` a main (push OK; pre-push **auto-indexó las 11 URLs**, 0 en cola). HEALTH CHECK previo OK (home, /contacto/, /servicios/, /blog/, instalacion-electrica, electricista → 200 en :8080). Sincronizado main con origin (--ff-only "Already up to date") antes de ramificar. 9 revisores; **deterministas SANOS y NO ciegos** (ci-gate 0 ALTA; indexabilidad 87 URLs/0; producción en vivo 0; plantilla solo el falso positivo google-stub). **GSC FUNCIONAL** (`mcp__gsc__*` cargadas con ToolSearch select:; `gsc_list_sites` confirmó la propiedad): 89 clics, 4376 impr, CTR 2.03%, pos 7.1 (impr +3%, clics −5% vs periodo anterior).
- **REGRESIÓN 30-60 MIN EN BLOGS (media, 5 blogs) — lo principal:** el badge de plantilla hero `<span>Llegamos en 30-60 min</span>` (promesa incondicional de llegada) sobrevivía en 5 blogs INFORMATIVOS (ahorro-energia-iluminacion-led, senales-instalacion-electrica-obsoleta, seguridad-electrica-temporada-lluvias, como-prevenir-cortocircuitos-casa, mantenimiento-tablero-electrico-preventivo). La corrida de ayer (check 22) solo escaneaba `servicios/`, así que los blogs escaparon. Decisión del dueño (NEGOCIO.md, 2026-06-22): 30-60 solo en emergencia. Reescrito el hero → "Cotización sin costo"; quitado bullet "· Llegada 30-60 min" de meta/og en ahorro/senales/como-prevenir; 2 frases de body de servicio AGENDABLE (instalación LED, mantenimiento tableros). **CONSERVADO lo legítimo:** cards "Emergencias 24/7", FAQ schema de cortocircuito, cross-sell emergencia-24-7, y el blog `cuando-llamar-electricista-emergencia` (NO tocado, sí es de emergencia). Editado con Python UTF-8 (0 mojibake).
- **BUG priceRange (alta mecánica, instalacion-electrica):** `"priceRange": "18270"` (pesos crudos) en el JSON-LD → `"$$"` (formato schema.org).
- **PERF imágenes upscale (media, 5 blogs):** hero `instalacion-minisplit-culiacan-1200w.webp` era realmente 800×447 → honestado.
- **SEO twitter (media, blog/index + 3 blogs):** blog/index solo tenía twitter:image → +4 tags.
- **A11Y (baja, home):** `<section class="stats-bar">` sin nombre accesible → +`aria-label`.
- **APRENDIZAJE:** +2 reglas (39→41): SEO/BLOG-30-60-MIN, PERF/UPSCALE-CLS. checks 23/24 nuevos.
