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
