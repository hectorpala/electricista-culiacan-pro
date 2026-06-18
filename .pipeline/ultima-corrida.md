# Última corrida — mantenimiento autónomo

## 2026-06-17 18:22 — rama `auto/mantenimiento-20260617-1822` — **NO PUBLICADO** (detenido por concurrencia)

### Resultado: trabajo verificado, NO publicado. Preservado como patch para revisión humana.

### ⚠️ MOTIVO DE LA DETENCIÓN (root cause operacional — ACCIÓN HUMANA)
Durante esta corrida, **otro pipeline autónomo `/expandir-sitio` estaba corriendo EN PARALELO sobre el MISMO repo**, commiteando a `main` cada ~30 s, pusheando, y haciendo `git checkout` en el mismo worktree. Evidencia:
- HEAD saltó **3+ veces** sin acción mía durante la sesión: `646ddb17` → `83ba72a5` (piloto 8 colonias) → `88c32d8d` (enriquecimiento colonias) → `edb28cdc` ("colonias lote 2 (8 mas)") → … y seguía.
- Mi rama checked-out fue cambiada de `auto/mantenimiento-20260617-1822` a `main` por un `git checkout` externo a mitad de corrida.
- El archivo compartido `HISTORIAL.jsonl` fue co-escrito: mis 8 entradas terminaron commiteadas a `main` por el `git add HISTORIAL.jsonl` del proceso expandir (no por mí).

Publicar (merge/push) en un worktree que otro proceso checkoutea y commitea activamente es inseguro: la secuencia merge `--ff-only` + `--no-ff` + push puede operar sobre la rama equivocada o corromperse si un `git checkout` externo aterriza a media secuencia. Por mandato ("ante cualquier ambigüedad o riesgo, prefiere NO publicar"), **aborté la publicación**.

**FIX RECOMENDADO (humano):** el wrapper `.pipeline/mantener-diario.sh` debe garantizar **exclusión mutua** entre `/expandir-sitio` y `/mantener-sitio` (lockfile / no lanzarlos concurrentes sobre el mismo repo, o usar git worktrees separados por job). Hoy ambos comparten `.git/HEAD`, índice y worktree → colisión.

**FIX RECOMENDADO #2 (humano):** el agente `/expandir-sitio` escribe "PUBLICADO ✅" en ESTADO.md **antes** de commitear (al inicio de la corrida su trabajo de 8 colonias estaba *staged sin commit* mientras ESTADO ya decía publicado). Debe escribir "PUBLICADO" sólo DESPUÉS de un push exitoso confirmado.

### Lo que SÍ se hizo (verificado, escéptico, sitio corriendo)
HEALTH CHECK previo OK (home, /contacto/, /servicios/, /blog/, /servicios/electricista/, /servicios/instalacion-electrica/ → 200). 9 revisores en paralelo; verificación ciega OK (indexabilidad 60 págs/exit 0, plantilla 682 archivos/exit 0, producción headless OK, GSC datos reales como siteOwner — ninguno pasó callando).

4 hallazgos mecánicos alta/media arreglados y verificados (5 archivos):
1. **a11y (media)** `servicios/electricista-colonias-culiacan/index.html`: botones de paginación prev/next (solo SVG chevron) sin nombre accesible → `aria-label="Página anterior/siguiente"` + `aria-hidden="true"` al svg. Verificado: 2 aria-label, HTTP 200.
2. **perf (media)** `blog/como-prevenir-cortocircuitos-casa/` y `blog/senales-instalacion-electrica-obsoleta/`: cargaban `/main.js` crudo (27 KB) → `/main.min.js` (5.7 KB, el que usa index/servicios). Verificado: 0 refs a /main.js, HTTP 200 ambos.
3. **perf/plantilla (media, resuelve plt-001)** `blog/index.html`: imagen del post destacado (LCP) era `eager` sin `fetchpriority` → añadido `fetchpriority="high"` (NO lazy: es el LCP). check-plantilla 2→1.
4. **gsc/seo (media)** `sitemap_index.xml`: `lastmod` de `sitemap.xml` desactualizado (2026-06-05) aunque cambió hoy → bump a 2026-06-17. XML válido.

Diff = 5 archivos, 8/8 líneas, 100% mecánico, 0 borrados. Todos los candados de CONTENIDO pasaban; solo se detuvo por la concurrencia git, no por un problema del diff.

### CÓMO APLICAR (humano, una vez que el batch de expandir TERMINE y main esté quieto)
El trabajo está preservado en: **`.pipeline/mantenimiento-20260617-1822.patch`**

```bash
cd "/Users/openclaw/Sitios Web/Electricista Culiacán"
# asegúrate de que NINGÚN otro pipeline esté corriendo (ps ax | grep mantener-diario)
git fetch origin && git checkout main && git merge --ff-only origin/main
git apply --3way .pipeline/mantenimiento-20260617-1822.patch
# verificar: grep main.min.js en los 2 blogs, fetchpriority en blog/index, aria-label en colonias index, lastmod 2026-06-17 en sitemap_index
git add -A && git commit -m "fix: mantenimiento auto 2026-06-17 — 4 hallazgos (a11y paginacion, perf main.min.js x2, LCP fetchpriority, sitemap lastmod)"
PATH="/usr/local/bin:$PATH" git push
```
NOTA: las 8 entradas de HISTORIAL.jsonl de esta corrida YA están en `main` (las barrió el commit concurrente del expandir) y dicen estado "hecho", pero el código de los 4 fixes NO está commiteado hasta que se aplique el patch de arriba. Al aplicar el patch, main queda consistente.

### PENDIENTE HUMANO (hallazgos no-mecánicos de esta corrida)
- **sub-sitemap colonias desincronizado** (`sitemaps/servicios_colonias_sitemap.xml`, media): lista 16 colonias viejas (comentario dice "642"), diverge del `sitemap.xml`. Las nuevas YA están en `sitemap.xml` (registrado en GSC) → indexación cubierta; el sub-sitemap es ruido. Decisión de arquitectura SEO: consolidar / noindex / regenerar.
- **Colonias promovidas aún sin indexar** (alta, monitoreo): GSC inspección real = "rastreada sin indexar" o "no reconoce URL". Código correcto; auto-indexación del pre-push ya disparada. Re-evaluar en 2-3 semanas; si siguen, reenviar via Indexing API.
- **GSC CTR bajo / striking-distance** (media): home top-3 con 0 clics en "cerca de mí"/"24 horas"; queries pos 4-10 captables por instalacion-electrica. Decisión copy/title/meta + enlazado interno.
- **Falso positivo** `google0164859d93c23fd0.html` sin theme-color: es el stub de verificación de Google, no es página de contenido. No se toca.

### REGLA NUEVA SUGERIDA para REGLAS.md (no la añadí porque REGLAS.md se estaba co-escribiendo en main)
`[2026-06-17] OPERACIÓN-PIPELINE (concurrencia): NUNCA correr /expandir-sitio y /mantener-sitio (ni dos instancias del mismo) en paralelo sobre el mismo repo/worktree — comparten .git/HEAD, índice y working tree. Síntoma observado: HEAD saltó 3+ veces y la rama checked-out fue cambiada bajo los pies del agente de mantenimiento, dejando código verificado sin poder publicar de forma segura. El wrapper mantener-diario.sh debe serializar los jobs (lockfile) o aislarlos con git worktrees. Además, /expandir-sitio escribió "PUBLICADO ✅" en ESTADO antes de commitear (debe hacerlo sólo tras push exitoso). Severidad: alta (operacional).`
