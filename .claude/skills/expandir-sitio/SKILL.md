---
name: expandir-sitio
description: Agente de CRECIMIENTO autónomo — determina qué le falta al sitio (oportunidades GSC, geo, blog, mejoras), CREA las páginas con contenido único y, si pasan TODOS los candados, publica e indexa solo. Invocar con /expandir-sitio.
---

# Agente de crecimiento autónomo — `/expandir-sitio`

Hermano de `/mantener-sitio`: aquél **arregla** lo existente; éste **expande** el sitio
creando lo que le falta. Trabaja en rama, verifica con candados deterministas y
**auto-publica solo si TODO pasa** (si algo falla, deja en rama y avisa).

Muestra EVIDENCIA (salida de comando) en cada fase. NO afirmes éxito sin probarlo.

## Configuración de la corrida (defaults)
- `MAX_PAGINAS = 3` — tope duro de páginas nuevas por corrida (evita generación masiva = doorway).
- `DIMENSIONES = [gsc, geo, blog, mejoras]` — las 4 activas.
- `AUTO_PUBLICA = sí` — si los candados pasan, mergea a main + indexa. Si fallan, NO publica.
- Propiedad GSC: `https://electricistaculiacanpro.mx/`. Email del sitio: `contacto@electricistaculiacanpro.mx`.

## MODO AUTÓNOMO (NO PARAR)
Una vez invocado, ejecuta las 8 fases de corrido **sin detenerte a pedir confirmación**.
Decide con las REGLAS DURAS y los datos; no preguntes al humano. Al inicio, anuncia en UNA
lista breve QUÉ vas a hacer (las acciones priorizadas) y luego hazlo todo hasta publicar.
Las ÚNICAS razones legítimas para no publicar algo son:
  (a) un CANDADO falla → deja esa página en la rama, NO la publiques, y sigue con las demás;
  (b) una acción marcada como **decisión de negocio** (p.ej. nicho "eléctrico automotriz"):
      NO la ejecutes; solo anótala como PENDIENTE HUMANO y continúa.
Nunca te detengas "por si acaso". Si una acción es de bajo riesgo y pasa candados, publícala.

## REGLAS DURAS (innegociables — leer antes de crear nada)
1. **Anti-doorway:** jamás crear páginas casi-idénticas. Cada página debe tener contenido
   sustancialmente único (H1, hero, secciones, FAQ, testimonios, schema). El candado
   `gate-pagina.py` BLOQUEA si la similitud Jaccard ≥ 0.80 con una hermana. Respétalo.
2. **Paridad de plantilla:** toda página nueva replica EXACTO `index.html` (la fuente de
   verdad). Por eso se generan con `gen-landing.py` desde un esqueleto que YA pasa
   validate-landing.sh — NO se escriben a mano desde cero.
3. **Email:** nunca un email con "plomero". El generador aborta si detecta esa fuga.
4. **Sin enlaces rotos:** todo `href` interno debe resolver a un archivo real. Verifícalo.
5. **`index.html` es intocable salvo necesidad real:** si hay que cambiarlo, se arregla
   PRIMERO ahí y se propaga; no es el objetivo de este agente (su objetivo es crear páginas).
6. **noindex fuera del sitemap;** índex dentro del sitemap. Cada página nueva indexable
   se agrega a `sitemap.xml` y se le dan enlaces ENTRANTES (no huérfanas).

---

## FASE 0 — Memoria
Lee `REGLAS.md`, `ESTADO.md` y las últimas líneas de `HISTORIAL.jsonl`. Anota qué ya se
hizo para no repetir (p.ej. las 5 zona-pages ya existen).

## FASE 1 — Health check
Levanta `python3 -m http.server 8080` en background. `curl -sI` a la home y 2-3 páginas
clave (/contacto/, /servicios/instalacion-electrica/, /blog/). Si algo ya está roto (≠200),
PARA y repórtalo: no se expande sobre un sitio roto.

## FASE 2 — AUDITORÍA DE HUECOS (determinar bien qué falta)
Recolecta señales de las 4 dimensiones y construye una lista RANKeada. Sé concreto.

### 2a. Oportunidades de GSC (datos reales — máxima prioridad)
Con el MCP `gsc` sobre la propiedad real:
- `mcp__gsc__gsc_opportunities` y `mcp__gsc__gsc_keywords` → queries con IMPRESIONES pero
  posición 8-30 y/o sin página dedicada (el sitio sale "de rebote"). Cada una = candidata
  a página propia que captaría ese tráfico.
- `mcp__gsc__gsc_performance` → páginas con CTR bajo / impresiones altas (mejora) y queries
  emergentes.
- `mcp__gsc__gsc_inspect` sobre páginas nuevas recientes → "descubierta sin indexar" =
  reforzar enlaces internos, no crear duplicado.
Para cada query/oportunidad anota: query, impresiones, posición, ¿existe página propia?,
tipo de página que la captaría (servicio / zona / colonia / blog).

### 2b. Expansión geográfica
Lista servicios/zona y colonias existentes (`ls servicios/`, colonias indexables con
`grep -L noindex`). Cruza con demanda real (2a). Detecta zonas/colonias con búsquedas pero
sin página única. NO inventes colonias sin señal de demanda (riesgo doorway).

### 2c. Blog SEO
Inventario `ls blog/`. Detecta keywords eléctricas de Culiacán con volumen (de 2a o del
sentido común del nicho: "¿cuánto cuesta…?", problemas, guías, normas CFE) que el blog aún
NO cubre. Una idea = un post con intención de búsqueda clara.

### 2d. Mejoras a páginas existentes
Corre `python3 .pipeline/check-plantilla.py` y `python3 .pipeline/check-indexabilidad.py`.
Identifica páginas FLOJAS: contenido delgado, sin FAQ, og:image incoherente, interlinking
pobre, meta description larga. Estas se MEJORAN (editar), no se recrean.

### Entregable de la fase
Escribe `.pipeline/oportunidades-<YYYYMMDD>.md` con una tabla rankeada:
`| # | oportunidad | dimensión | impacto (alto/med/bajo) | esfuerzo | riesgo doorway | acción |`
Ordena por impacto/riesgo. Esto es "determinar bien qué falta".

## FASE 3 — Priorizar (tope duro)
Elige las **top `MAX_PAGINAS`** acciones de menor riesgo y mayor impacto. Prefiere
oportunidades respaldadas por datos de GSC sobre las especulativas. Si NO hay ninguna
oportunidad de bajo riesgo y alto impacto, está PERMITIDO crear 0 páginas esta corrida y
solo dejar el reporte (no fuerces crecimiento sin señal — eso genera doorways).

## FASE 4 — CONSTRUIR (autónomo)
Para cada acción elegida:

**Página de servicio / zona / colonia (geo):**
1. Elige un esqueleto: una página HERMANA que YA pasa validate-landing.sh (p.ej.
   `servicios/electricista-cerca-de-mi/index.html` o la más parecida a la intención).
2. Escribe un **spec JSON** para `gen-landing.py` con sustituciones de contenido ÚNICAS:
   título/desc/keywords, geo.position/ICBM (coords reales y distintas), canonical/og/twitter,
   breadcrumb, Service+FAQ JSON-LD, H1, hero, benefits, grid de colonias con enlaces REALES,
   3 testimonios y FAQ propios. El slug global se sustituye con `n` = nº de ocurrencias.
3. `python3 .pipeline/gen-landing.py /tmp/spec.json` (aborta si algo no calza → corrige el spec).
4. Agrega la URL a `sitemap.xml` (priority 0.8 servicio/zona, 0.7 colonia) y crea enlaces
   ENTRANTES desde una página ya rastreada (p.ej. el índice de colonias o un servicio afín).

**Post de blog:** mismo método con un esqueleto de `blog/<post>/index.html` que pase los
checkers; contenido original por keyword; agregar a sitemap (priority 0.7) y enlazar desde
`blog/` y desde un servicio relacionado.

**Mejora a página existente:** edición mínima y quirúrgica (añadir FAQ, ampliar contenido
delgado, corregir interlinking/og:image). NO reescribir la página entera.

> Recuerda el bug de zsh (REGLAS): en bucles usa arrays `("${X[@]}")` o
> `grep -rl … | while IFS= read -r f`; confirma con `git diff --stat` que los archivos cambiaron.

## FASE 5 — CANDADOS (puerta de publicación)
Corre el candado todo-en-uno sobre CADA página nueva/modificada:
```
python3 .pipeline/gate-pagina.py <ruta1/index.html> <ruta2/index.html> ...
```
Hace: validate-landing.sh + ci-gate (0 ALTA) + anti-doorway (Jaccard < 0.80).
Además verifica a mano: JSON-LD parsea, canonical==og:url==twitter:url, 0 enlaces de colonia
rotos, HTTP 200 en local (`curl`).
**Si el candado FALLA (exit≠0): NO publiques.** Deja todo en la rama, escribe el motivo en
ESTADO.md y termina avisando al humano. No "fuerces" el arreglo si implica romper otra regla.

## FASE 6 — PUBLICAR (auto, solo si FASE 5 fue 100% verde)
```
git checkout -b auto/expansion-<YYYYMMDD-HHMM>
git add <páginas nuevas> sitemap.xml <archivos de enlaces entrantes> ESTADO.md HISTORIAL.jsonl
git commit -m "feat: expansión autónoma — <resumen>" -m "Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
git checkout main
git merge --no-ff auto/expansion-<...> -m "Merge: expansión autónoma <fecha>"
PATH="/usr/local/bin:$PATH" git push origin main      # el pre-push auto-indexa en GSC
```
Luego refuerza la indexación vía MCP (excluye las noindex):
`mcp__gsc__gsc_index(site, [urls indexables nuevas])`.
Borra la rama temporal (`git branch -d`).

## FASE 7 — Bitácora
- `ESTADO.md`: nueva entrada ARRIBA con fecha, qué se creó, evidencia de candados, URLs indexadas.
- `HISTORIAL.jsonl`: una línea JSON por página creada/mejorada (campos: fecha, archivo,
  categoria, severidad, descripcion, estado, regla, nota).
- `REGLAS.md`: si aprendiste algo nuevo (un patrón, un casi-error), añádelo como una línea.

## FASE 8 — Reporte final
Resume: qué huecos se detectaron, qué se creó, resultado de los candados, qué se publicó e
indexó, y qué quedó como PENDIENTE HUMANO (oportunidades de alto impacto pero alto riesgo o
que exceden el tope). Sé honesto: si no se creó nada por falta de señal, dilo.
