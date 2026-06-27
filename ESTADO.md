# ESTADO — Electricista Culiacán

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
