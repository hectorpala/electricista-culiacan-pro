# Oportunidades GSC — 2026-07-06

Rendimiento 28d: 102 clics, 4747 impresiones, CTR 2.15%, posición 7.0 (vs 2026-07-03: 104 clics,
4764 impr, CTR 2.18%, pos 7.1 — fluctuación normal de ventana rodante, sin caída real).

## Tabla rankeada por impacto/riesgo-doorway

| Oportunidad | Impacto | Riesgo doorway | Acción sugerida |
|---|---|---|---|
| Sitemap huérfano en consola GSC (`servicios_colonias_sitemap.xml`, 404, 1 error, no se refresca desde 2026-06-08) | bajo | ninguno (no es contenido) | acción manual en consola GSC (eliminar el registro); revisar en FASE 6 si el MCP permite hacerlo por API |
| Canibalización "electricista culiacan": home (pos 6.5, CTR 10.2%) vs colonias infonavit-humaya (pos 8.6, 0 clics) y tulipanes (pos 11.1, 0 clics) | medio | bajo (no crea páginas, solo retoca title/H1 existentes) | encolado bk-f052cf43, riesgo bajo |
| "electrician near me" pos 3.4, 0 clics | — | — | **IGNORAR**: decisión de negocio permanente (NEGOCIO.md, no perseguir inglés) |
| "eléctrico automotriz a domicilio" pos 9.1, 0 clics | — | — | **IGNORAR**: decisión de negocio permanente (fuera de giro) |
| CTR-fix electricista-precios vs blog cuanto-cuesta (title casi idéntico) | bajo | ninguno | encolado bk-3276eda1, riesgo bajo |

## Sin huecos de página NUEVA detectados hoy
No hay query con demanda real (≥umbral) en posición 8-30 que carezca de página propia y caiga
claramente en el giro eléctrico. Las 2 oportunidades de "0 clics con buena posición" ya identificadas
(home CTR-fix vetado 2026-07-03 por experimento en curso hasta 2026-07-15, contactos-culiacan
bk-f38bd140 ya en backlog) siguen siendo las mismas de corridas anteriores.

## Nota operativa del día
El diff de FASE 5 ya llegó al cap de 18 páginas HTML con los fixes ALTA/media de hoy (nav
transparente en desktop + contraste/tap-target de breadcrumb + CSS faltante en hub de colonias +
aria-controls roto + fechas de blog desincronizadas). Por eso HOY no se ejecuta ninguna tarea nueva
de crecimiento/optimización que toque páginas — se documentan y encolan para drenar en la próxima
corrida (mismo patrón que 2026-07-01 y 2026-07-03).
