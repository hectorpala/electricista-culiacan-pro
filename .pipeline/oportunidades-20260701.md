# Oportunidades GSC — 2026-07-01

Fuente: revisor-gsc (subagente, corrida auto-diario-20260701-2001), ventana 28 días.

## Rendimiento general
| Métrica | Hoy (28d) | Periodo anterior (28d) | Snapshot diario ayer (30-jun) |
|---|---|---|---|
| Clics | 100 | 102 | 98 |
| Impresiones | 4,558 | 4,409 | 4,490 |
| CTR | 2.19% | — | 2.18% |
| Posición | 7.1 | — | 7.1 |

Estable/plano: las impresiones suben (+3%) pero los clics casi no acompañan (CTR prácticamente igual).
Sin problema de indexación: las 5 URLs clave inspeccionadas (home, colonia infonavit-humaya,
instalacion-contactos, electricista, electricista-precios) están "Enviada e indexada".

## Canibalización "electricista"/"electricista culiacan" (riesgo medio-alto, apuesta de estrategia SEO — NO auto-arreglable)
6 páginas compiten por el mismo término: home (gana, pos 4-7), `/servicios/electricista/` (pos 11,
0 clics), `/servicios/electricista-precios/` (pos 10.1, 0 clics), `/contacto/` (pos 11.2, 0 clics),
2 colonias (infonavit-humaya pos 8.4, tulipanes pos 11.1, ambas 0 clics). Pendiente-humano heredado.

## Sitemap fantasma en Search Console (acción manual, no-código)
`/sitemaps/servicios_colonias_sitemap.xml` sigue registrado con 1 error (sin recrawl desde
2026-06-08) y da 404 real en producción — ya se consolidó en `/sitemap.xml`. El dueño debe
quitarlo manualmente en Search Console → Sitemaps. Pendiente-humano heredado.

## "electrician near me" — decisión ya tomada, NO perseguir
pos 4.3, 32 impr, 0 clics. NEGOCIO.md ya decidió no crear contenido en inglés (2026-06-22). Ignorado.

## Decisión de la corrida de hoy
NO se creó ni optimizó ninguna página en FASE 6: el diff de FASE 5 (regresión ALTA de contraste
WCAG en 18 páginas) ya alcanzó el cap de 18 páginas HTML del candado de publicación. Los hallazgos
nuevos de hoy (12 páginas de servicio con la misma regresión, geo faltante en 40 colonias, fuentes
duplicadas, imágenes 420w faltantes, JS sin versionar, tap-target de navegación, hub
`servicios/index.html` faltante) se encolaron en BACKLOG.jsonl para próximas corridas
(loop-until-dry, nada se pierde). Detalle completo de hallazgos: ver ESTADO.md de hoy.
