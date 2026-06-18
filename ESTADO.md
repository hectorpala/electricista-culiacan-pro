# ESTADO — Electricista Culiacán

## 2026-06-17 (colonias LOTE 2 — 8 mas, ya enriquecidas) — PUBLICADO ✅
Segundo lote de 8 colonias diferenciadas+promovidas, ya con el template enriquecido completo desde el inicio (meta unica + 3 parrafos + 'Problemas comunes' + servicios).
- **8 colonias:** barrancos, lazaro-cardenas, gabriel-leyva, la-campina, valle-alto, recursos-hidraulicos, hacienda-del-valle, antonio-toledo-corro. ~390 palabras c/u.
- **Candado:** anti-doorway 0.49-0.64 (<0.80), ci-gate 0 ALTA, HTTP 200. Indexables de colonia: 24 -> **32** (de 642). Sitemap 60->68.
- **Indexacion:** cuota diaria de la Indexing API agotada hoy; el pre-push hook las encolo y las reintenta manana automaticamente (ese mecanismo ya es el "siempre indexa al crear").
- **PENDIENTE:** medir en GSC (gsc_inspect) en 2-3 semanas si los 2 lotes (16 colonias) se indexan, antes de escalar.


## 2026-06-17 (colonias piloto — enriquecimiento para indexabilidad) — PUBLICADO ✅
Sobre el piloto de 8 colonias: para que Google SI las indexe (no las deje en "descubierta sin indexar" por delgadas), se subio el contenido unico.
- **ENRIQUECIDAS las 8** (6-de-enero, bachigualato, bugambilias, nuevo-culiacan, colinas-de-san-miguel, lomas-de-tamazula, rafael-buelna, las-americas): meta description UNICA por colonia (antes era plantilla con solo el nombre), 3er parrafo unico + lista "Problemas electricos comunes en X" (4 propios). Palabras ~320 -> ~390-450; contenido unico ~120 -> ~240.
- **Candado:** anti-doorway MEJORO 0.61 -> **0.50-0.59**; ci-gate 0 ALTA; HTTP 200; revisado visual.
- **PENDIENTE:** medir indexacion real en GSC en 2-3 semanas (gsc_inspect) antes de escalar a mas colonias.


## 2026-06-17 (agente /expandir-sitio — PILOTO diferenciacion de colonias) — PUBLICADO ✅
Diagnostico: 642 colonias, 16 indexables (unicas, Jaccard 0.35-0.48), 626 noindex doorways (Jaccard 0.95-0.98, ~80 palabras). GSC SIN demanda por nombre de colonia (apuesta long-tail, ROI a medir).
- **DIFERENCIADAS Y PROMOVIDAS 8 colonias reconocidas** (6-de-enero, bachigualato, bugambilias, nuevo-culiacan, colinas-de-san-miguel, lomas-de-tamazula, rafael-buelna, las-americas): a cada una se le inyecto seccion UNICA "Electricidad en <Colonia>: lo que debes saber" (2 parrafos propios reales + servicios), flip noindex->index, fix breadcrumb (item 3 sin URL propia), sitemap 52->60. **Candado:** anti-doorway Jaccard **0.61-0.62** (<0.80), ci-gate 0 ALTA, HTTP 200, revisado visualmente.
- **Tooling:** gate-pagina.py ahora omite validate-landing en colonias (plantilla distinta a servicios v2.0.0). Leccion del breadcrumb guardada en REGLAS para futuras promociones.
- **PENDIENTE:** medir en GSC en 2-3 semanas si estas 8 traen trafico antes de escalar a mas colonias.


## 2026-06-17 (agente /expandir-sitio — blog 'como elegir electricista') — PUBLICADO ✅
Hueco de paridad con Plomero (tiene `como-identificar-buen-plomero`, Electricista no). Intencion confianza/seleccion, sin canibalizar (distinto a precios).
- **CREADO Y PUBLICADO:** `/blog/como-elegir-buen-electricista-culiacan/` — gen-landing.py (33 sustituciones) desde esqueleto recibo-luz. Contenido original: tabla "buen electricista vs señal de alerta", 6 pasos para verificar antes de contratar, FAQ de confianza (garantia, factura, norma CFE). **Candado VERDE:** ci-gate 0 ALTA, anti-doorway Jaccard **0.36**. Sitemap 51→52; enlace entrante desde blog/index (tarjeta + JSON-LD); HTTP 200.


## 2026-06-17 (consistencia de botones del hero) — PUBLICADO ✅
Revisión exacta (con CSS real + medición puppeteer) del acomodo de botones escritorio vs movil. Unico desajuste: el HERO. Lo demas (flotantes, CTA final, form) ya era consistente.
- **ARREGLADO:** hero CTA unificado a 2 botones (WhatsApp naranja + Llamar azul) IGUALES en ambas vistas — misma fila en escritorio, apilados full-width en movil. Antes: escritorio mostraba 1 boton (ancho auto) y ocultaba el telefono (`hero-phone-link display:none`); movil mostraba boton full-width + link "O llama". Solucion: clase propia `.hero-cta-buttons` con CSS inline en index.html (NO toca los 3 CSS externos → sin problema de paridad), reusando `btn-primary`/`btn-secondary`. Bump service worker v8→v9.
- **Verificado:** puppeteer mide escritorio=misma fila (lado a lado), movil=apilados anchos iguales; checkers 0 ALTA; HTTP 200. Revisado visualmente por el dueño (eligio el diseno de 2 botones).


## 2026-06-17 (agente /expandir-sitio — blog de precios) — PUBLICADO ✅
2ª acción del agente autónomo. Hueco: blog "¿cuánto cuesta?" (Plomero tiene `cuanto-cobra-plomero`, Electricista no; intención comercial sin canibalizar la pagina de servicio precios).
- **CREADO Y PUBLICADO:** `/blog/cuanto-cuesta-electricista-culiacan/` — generado con `gen-landing.py` (33 sustituciones) desde el esqueleto `recibo-luz-alto`. Contenido original: **tabla de precios por servicio 2026** (visita, contactos, pastilla, cortocircuito, tablero, minisplit, tierra física, LED, cableado), factores que mueven el costo, pasos para cotizar sin pagar de más, FAQ de precios. **Candado VERDE:** ci-gate 0 ALTA, anti-doorway Jaccard **0.25** (muy distinta). Sitemap 50→51; enlace entrante desde `blog/index.html` (tarjeta + JSON-LD); HTTP 200; **revisado visualmente** (desktop+móvil) por el dueño.
- **Mejora de tooling:** `gate-pagina.py` ahora detecta blogs y omite validate-landing (plantilla distinta), evaluando paridad contra hermanas de blog.


## 2026-06-17 (agente /expandir-sitio — 1ª corrida autónoma) — PUBLICADO ✅
Agente de crecimiento autónomo. Auditoría GSC (28 días: 94 clics / 4,164 impr / pos 6.8) → reporte en `.pipeline/oportunidades-20260617.md`.
- **DETERMINÓ y DESCARTÓ (juicio anti-doorway, lo correcto):** `electricista-urgente` NO se crea (la home y sobre todo `emergencia-24-7` —titulada "Electricista 24 Horas… Emergencia Urgente"— ya cubren "urgente/24 horas" → sería canibalización); mejora de "evitar cortocircuito" NO se hace (el post ya tiene "10 Medidas para Evitar Cortocircuitos").
- **CREADO Y PUBLICADO:** `/servicios/electricista-comercial/` — hueco estructural de paridad (Plomero tiene `plomeria-comercial`), intención B2B distinta (negocios/locales/oficinas, trifásica, mantenimiento programado, factura). Generada con `gen-landing.py` (27 sustituciones, paridad por construcción). **Candado VERDE:** validate-landing PASA, ci-gate 0 ALTA, anti-doorway Jaccard **0.55**. Sitemap 49→50; enlace entrante desde la pillar `/servicios/electricista/` (tarjeta con imagen real); HTTP 200.
- **PENDIENTE HUMANO (decisión de negocio):** "eléctrico automotriz a domicilio" rankea pos 2.6 (21 impr) sin página → definir si el negocio entra a ese nicho antes de crearla.

## 2026-06-17 (paridad con Plomero — privacidad + 5 zona-pages) — PUBLICADO ✅
Rama `feat/paridad-plomero-privacidad-zonas` mergeada (`--no-ff`) a main y pusheada (commit f8cff0a1). Auto-indexación GSC: 6 URLs enviadas (5 zona-pages + índice de colonias); privacidad NO enviada (noindex, correcto).
Petición del dueño: replicar la estructura de **Plomero Culiacán** y crear lo que le falta a Electricista.
Diagnóstico de huecos reales (Plomero tiene, Electricista no): `/privacidad/`, 5 zona-pages, partials (descartados: andamiaje no usado). NO-huecos: `/precios/` top-level (Electricista usa `/servicios/electricista-precios/`) y dirs de tooling.

- **CREADO — `/privacidad/` (Aviso de Privacidad, LFPDPPP):** Plomero la tenía y Electricista no (ni se enlazaba). Molde = `terminos/` (plantilla legal `noindex,follow`), branding electricista, `GTM-5Z2QRZ5Q`, Clarity, email `contacto@electricistaculiacanpro.mx`. 0 fugas de "plomero". Enlazada desde `terminos/` (descubrible site-wide). Fuera del sitemap (correcto, noindex). validate-landing → OMITIDO (noindex). HTTP 200.
- **CREADO — 5 zona-pages** (`servicios/electricista-zona-{norte,sur,oriente,poniente}-culiacan/` + `electricista-centro-culiacan/`), paridad con las de Plomero:
  - **Método:** generador determinista (`/tmp/gen-zonas.py`) que copia el esqueleto `electricista-cerca-de-mi/index.html` byte a byte (paridad estructural por construcción → no hay drift de plantilla) y sustituye SOLO regiones de contenido, afirmando cada replace (aborta si una no ocurre). Corrigió de paso el bug zsh de no-word-splitting (REGLAS OPERACIÓN-PIPELINE) en el loop de verificación.
  - **Anti-doorway:** contenido ÚNICO por zona (title/desc/kw, H1, hero, benefits, grid de colonias con enlaces, 3 testimonios, 5 FAQ JSON-LD+HTML, schema Service, coords meta). Jaccard de contenido visible 0.61–0.69 (<0.75). Mapeo geográfico REAL de Culiacán cruzado con las 16 colonias indexables (cada zona ≥2 colonias propias; coords meta únicas por zona; el schema `#business` mantiene el HQ 24.7903 como el resto del sitio).
  - **Verificación:** validate-landing.sh PASA en las 5; JSON-LD válido; canonical==og:url==twitter:url; 0 enlaces de colonia rotos (16 slugs confirmados en disco); agregadas a `sitemap.xml` (44→49 URLs, priority 0.8); enlaces entrantes desde el índice de colonias (bloque "Electricista por Zona"); checkers deterministas sin regresión (plantilla 2 pre-existentes, indexabilidad 0 sobre las nuevas); HTTP 200 en las 5 + hero/main.min.js/colonia.
- **PENDIENTE:** revisión humana + publicar (rama/commit). Diff > candado de 15 archivos (7 nuevos + sitemap + colonias-index + terminos) → corrida fuera de la automatización de "una mejora", por petición explícita del dueño.

## 2026-06-17 (corrida 11:26 AM) — PUBLICADO ✅
- Rama `auto/mantenimiento-20260617-1126`, mergeada (`--no-ff`) a main y pusheada.
- HEALTH CHECK previo OK (home, /contacto/, /servicios/instalacion-electrica/, /blog/, /servicios/electricista/ → 200).
- **ARREGLADO (media, mecánico — leak de plantilla):** `twitter:url` apuntaba a `/servicios/reparacion-cortocircuitos/` en vez del canonical propio en 4 páginas de servicio (cambio-cableado-electrico, electricista-a-domicilio, instalacion-centro-carga, instalacion-ventiladores-techo). El 2026-06-14 se arreglaron canonical+og:url de estas mismas pero `twitter:url` (3er campo de URL) sobrevivió. Fix: `twitter:url` = canonical propio. Verificado site-wide: 0 mismatch canonical-vs-twitter en 674 HTML; la página legítima reparacion-cortocircuitos intacta; validate-landing.sh PASA en las 4; HTTP 200; checkers sin regresión (plantilla 2 pre-existentes, indexabilidad 0).
- Candados: diff = 4 archivos (≤15), 0 borrados estructurales, auto-revisión OK → publicado.
- **GSC verificado con datos REALES (no ciego):** consulté `mcp__gsc__*` con la propiedad real `https://electricistaculiacanpro.mx/`. Sitemaps 0 errores (sitemap.xml 30 envíadas/3 warn, colonias 16/0, images 14/1 warn). Home y /servicios/instalacion-electrica/ indexadas; `/blog/` "Descubierta: sin indexar aún" (informativo, nunca crawleada — no mecánico). Producción en vivo: 0 hallazgos.

### PENDIENTE HUMANO (nuevos esta corrida — NO auto: copy/diseño/estrategia o fuera de la "una mejora")
- **Copy leak "reparación de cortocircuitos"** (media, seo): H2 principal y CTA de `cambio-cableado-electrico` e `instalacion-ventiladores-techo` (13 menciones) hablan de cortocircuitos en páginas de otro servicio. Cambio de copy.
- **`<h1>` duplicado** en `servicios/electricista-colonias-culiacan/` (media, a11y): único con 2 h1 idénticos; mecánico 1 línea (degradar 2º a h2), próxima corrida.
- **`.letter-btn` tap target <44px** en colonias (media, móvil): 23 botones A-Z ~38x34px; fix inline min-height/min-width 44px.
- **Tarjetas sociales incompletas** en `servicios/electricista-colonias-culiacan/` (media, seo): sin og:url/og:image ni twitter cards; replicar bloque de index.html.
- **`gracias/` carga main.js sin minificar** (baja, perf) + **footer logo de index.html sin loading=lazy** (baja, perf, se hereda).
- **blog/index.html img featured eager sin fetchpriority** (plt-001, media): fix template-correcto = añadir `fetchpriority="high"` (es el LCP, NO lazy), próxima corrida.
- 8 meta descriptions de blog con cola comercial de plantilla + og:image temáticamente incoherentes en varios blogs/servicios (baja, copy).

## 2026-06-16 (corrida 9:00 AM) — PUBLICADO ✅ (commit f221d4ee)
- Rama `auto/mantenimiento-20260616-0900`, mergeada (`--no-ff`) a main y pusheada. Auto-indexación: 3 URLs enviadas a Google.
- HEALTH CHECK previo OK (home, /contacto/, /servicios/instalacion-electrica/, /blog/ → 200).
- **ARREGLADO (alta, mecánico — regresión de plantilla):** 3 páginas (servicios/electricista-cerca-de-mi, blog/como-prevenir-cortocircuitos-casa, blog/senales-instalacion-electrica-obsoleta) tenían el formulario SIN `<label>` (solo placeholder → invisible para lectores de pantalla). Se añadió `id` único + `<label for class="sr-only">` por campo. OJO: hubo que añadir también la definición `.sr-only` al `<style>` crítico inline de cada página (no existe en CSS externo, solo inline en index.html) — sin ella el texto quedaría visible. Verificado: 4 labels/4 ids por página, 0 ids duplicados, sr-only def=1, HTTP 200, validate-landing.sh PASA en la de servicio, checkers deterministas sin regresión (plantilla 2 pre-existentes, indexabilidad 0).
- Candados: diff = 3 archivos (≤15), 0 borrados estructurales, auto-revisión OK → publicado.
- **Verificación ciega GSC RESUELTA (no era ceguera real):** el subagente revisor-gsc está cableado a `mcp__local-seo` (apunta a plomero) y emitió "verificación ciega"; pero el MCP `gsc` del entorno SÍ tiene la propiedad `https://electricistaculiacanpro.mx/` (confirmado con gsc_list_sites). La indexación NO está ciega; el revisor está MAL CONFIGURADO → pendiente humano (reapuntar revisor-gsc a `mcp__gsc__*`).

### PENDIENTE HUMANO (esta corrida — NO auto: estratégico/masivo/diseño)
- **revisor-gsc mal configurado** (media): reapuntar a `mcp__gsc__*` con la propiedad `https://electricistaculiacanpro.mx/` para que deje de emitir falsa "verificación ciega".
- **Contraste WCAG AA del CTA de marca** (alta, a11y-004/005): `#F97316` 2.8:1 y `#E36414` 3.44:1 sobre blanco fallan AA. Decisión de diseño (qué tono oscuro, p.ej. `#C2410C`). Toca 3 CSS + bump sw.js.
- **focus-visible global ausente** (media, a11y-006): falta foco de teclado salvo .seo-card. 3 CSS + sw bump (ya venía de antes).
- **CSS render-blocking en 642 colonias + contacto/gracias/blog-index** (perf alta): no replican patrón async de la home. >15 archivos → corrida dedicada.
- **aggregateRating/Review self-serving en homepage + 16 servicios** (alta, seo): además de las ~642 colonias ya anotadas. Riesgo de acción manual. Batch dedicado (>15 archivos).
- **8 meta descriptions de blog/servicio > 155-160 car.** (baja): edición de copy, no auto.
- **`.service-cta` y formularios de blog/servicio sin replicar EXACTO la plantilla** (consistencia): los 2 blogs fallan validate-landing.sh (sin exit-popup ni main.min.js) — pre-existente, decisión de plantilla del dueño.
- Heredados sin resolver de corridas previas: fuga copy "10 de Abril" en wa.me de ~96 colonias; 16 colonias indexables fuera del sitemap; 3 tablas de blog sin table-wrapper; ETA inconsistente; theme-color placeholder.

## 2026-06-14 (corrida 6:20 PM) — PUBLICADO ✅ (commit 40beb89)
- Rama `auto/mantenimiento-20260614-1820`, mergeada a main y pusheada (auto-indexación: 14 URLs a Google).
- **ARREGLADO (alta, mecánico):** 18 enlaces rotos en 14 páginas de servicio → slug correcto `reparacion-cortocircuitos` (eran `reparacion-cortos-circuitos`, 404). Checker plantilla 28→14 (los 14 restantes son falsos positivos: `${c.s}` template-literal JS y fonts `../../../` que el navegador recorta).
- **ARREGLADO (alta, mecánico):** `/gracias/` (noindex) removida de `sitemap.xml`. Checker indexabilidad 20→19, gracias=0, XML válido.
- Candados: diff = 15 archivos (límite), 0 borrados estructurales inesperados, auto-revisión OK → publicado.
- Incidencia operativa resuelta: pre-push hook necesitaba node en PATH (ver REGLAS.md OPERACIÓN-PIPELINE).

### PENDIENTE HUMANO (detectado por revisores LLM esta corrida — NO auto: masivo/estratégico)
- **aggregateRating self-serving en ~642 páginas de colonia** (alta, seo-004): mismo ratingValue 4.8/reviewCount 150 replicado en masa → riesgo de acción manual de Google. Requiere quitar el bloque de schema en lote (642 archivos, > candado de 15). Decidir batch dedicado.
- **Fuga de copy "necesito electricista en 10 de Abril" en wa.me de ~96 colonias** (alta, seo-001): texto de plantilla origen no personalizado por colonia (6 son indexables). Cambio de contenido en lote.
- **16 colonias indexables fuera del sitemap + terminos/** (alta, idx/seo-003): decisión SEO (agregar al sitemap o noindex). Las thin pages doorway están en noindex (correcto); las ~16 con contenido único deberían entrar al sitemap.
- **CSS render-blocking en /servicios/ (~15) y /blog/ (10)** (perf alta, perf-001/002): no replican el patrón async de la homepage; blog usa `styles.min.css` sin hash. Toca >15 archivos → corrida dedicada.
- **3 tablas de blog sin `table-wrapper`** (movil alta) + tabla en homepage (baja): mecánico pero fuera del alcance de esta corrida (otra mejora).
- **focus-visible global ausente** (a11y alta, a11y-001): falta outline de foco para teclado salvo .seo-card/.floating-btn; fix en los 3 CSS + crítico inline.
- **ETA inconsistente** 20-30 min (colonias) vs 30-60 min (home/servicios) (seo-005): unificar — decisión de contenido.
- **theme-color placeholder #0066cc** en servicios/electricista/ (baja) y faltante en contacto/terminos (baja). Marca = `#F97316`.
- Duplicado title/description directorio vs colonias index (media): editorial.

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

## 2026-06-14 — Primera corrida del pipeline (modo seguro, en rama)
- Rama: auto/mantenimiento-20260614-1414 (sin publicar; pendiente de revisión humana).
- ARREGLADO: `aggregateRating` self-serving removido del JSON-LD de **9 posts de blog** (regla 08a95902). JSON-LD validado, checker confirma 0 hallazgos de aggregateRating.
- PENDIENTE HUMANO: 46 imágenes rotas (varias no existen en disco en ninguna versión → hay que generarlas/conseguirlas, no auto-arreglable) y 17 breadcrumbs de servicio cuyo último item apunta a `/#servicios` en vez del canonical (revisar plantilla de breadcrumb).

## 2026-06-14 (cont.) — BUG SERIO encontrado y arreglado: canonicals incorrectos
- 5 páginas tenían canonical apuntando a OTRA URL (4 a `/servicios/reparacion-cortos-circuitos/` que NO existe —typo de "reparacion-cortocircuitos"— y 1 a `.../directorio/`). Google las trataría como duplicados de una 404 → riesgo de desindexación.
- ARREGLADO: canonical + og:url → self-referencial (derivado del path) en las 5. Checker: 0 canonical-a-otra-URL. Lo detectó el revisor-indexabilidad.
- PENDIENTE (siguiente pasada, con cuidado): breadcrumbs — el último item del BreadcrumbList no apunta al canonical en ~17 páginas (baja severidad; requiere edición de JSON-LD por página). NO auto-arreglado en esta pasada tras un casi-error (usar URL derivada del path, no el canonical).

## 2026-06-14 (cont.) — Breadcrumbs arreglados (método correcto)
- 16 páginas: el último item del BreadcrumbList no tenía `item` (apuntaba implícitamente a /#servicios o /blog/). Se añadió `item` = URL propia derivada del PATH (no del canonical, tras el casi-error anterior). Fixer agnóstico al formato (multilínea y single-line), con validación JSON y verificación post-fix por archivo.
- Checker: 0 breadcrumbs (eran 16). Indexabilidad 36 -> 20.
- Quedan ~20 en indexabilidad (mayormente "página indexable fuera del sitemap" — revisar si deben ir al sitemap o llevar noindex; decisión SEO, no auto).

## 2026-06-14 (cont.) — Imágenes rotas: arregladas las seguras
- ARREGLADO (6, en 11 archivos): refs a imágenes que existían con otro nombre/ruta → apuntadas al archivo real (match ESTRICTO: todos los tokens + mismo tamaño + archivo no-.backup). Incluye el logo roto (`../electricista-culiacan-pro-logo.webp` → `/assets/images/...`) en contacto/gracias/colonias.
- NO auto-arregladas (~14 refs / pendiente humano): imágenes genuinamente ausentes o sin el tamaño pedido — REQUIEREN generar/subir la imagen:
  * instalacion-iluminacion-led (420w, 800w) — no existe
  * mantenimiento-tablero-electrico-420w, reparacion-cortocircuito (420w/800w), prevenir-cortocircuitos-420w — falta ese tamaño (existe 800w/1200w del nombre correcto; decidir si regenerar 420w o ajustar el srcset)
  * logo-512.webp — no existe (¿usar /assets/icons/icon-512x512.webp? decisión humana)
- NOTA: el matcher difuso inicial propuso destinos ERRÓNEOS (.backup, imagen distinta); se descartó y solo se aplicaron matches estrictos verificados.
