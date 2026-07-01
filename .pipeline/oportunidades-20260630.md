# Oportunidades GSC — 2026-06-30

Fuente: revisor-gsc (subagente, corrida auto-diario-20260630-2000), ventana 28 días.

## Rendimiento general
| Métrica | Hoy | 2026-06-29 | Δ |
|---|---|---|---|
| Clics | 98 | 92 | +6.5% |
| Impresiones | 4490 | 4483 | +0.2% |
| CTR | 2.18% | 2.05% | +0.13pp |
| Posición | 7.1 | 7.1 | = |

Tendencia positiva y estable.

## Striking distance / canibalización (riesgo medio-alto, requiere decisión de negocio)
- `electricista` compite en 3 URLs propias (home pos 4, `/servicios/electricista/` pos 11, `/servicios/electricista-precios/` pos 10.1) — posible canibalización interna. **NO auto-arreglar**: es apuesta de estrategia SEO (prohibido en automático). Pendiente-humano.
- `electricista culiacan` disperso en 4 URLs (home, `infonavit-humaya`, `contacto/`, `tulipanes`) — mismo patrón.

## CTR-fix (riesgo bajo, mecánico) — YA ENCOLADOS al backlog
- `bk-f38bd140`: `/servicios/instalacion-contactos/` — "contactos culiacan" pos 5.1, 18 impr, 0 clics.
- `bk-9d8c6176` (previo): `/servicios/emergencia-24-7/` — "electricistas 24 horas" pos 13.7.
- `electricista` pos 4, 104 impr, CTR 4.8% (home) — candidato a próxima ronda de CTR-fix de meta.
- `electrician near me` pos 4.2, 33 impr, CTR 0% — decisión ya tomada en NEGOCIO.md: NO perseguir inglés.

## Indexación de las 16 colonias diferenciadas (2026-06-29)
Muestra de 8: 3 indexadas (tres-rios, santa-aynes, infonavit-humaya), 4 rastreadas-sin-indexar, 1 con noindex-cache-vieja (recursos-hidraulicos — HTML ya correcto, es lag de recrawl de Google). Comportamiento esperado por REGLAS.md 2026-06-17 (Google prioriza colonias prominentes). Seguir midiendo a 3-4 semanas.

## Acción externa (no-código, pendiente-humano)
- Sitemap fantasma en Search Console: `/sitemaps/servicios_colonias_sitemap.xml` sigue registrado (1 error, última descarga 2026-06-08) pero el archivo ya no existe en disco (se consolidó en `/sitemap.xml`, commit `e1839586`). Acción: el dueño debe quitarlo manualmente en Search Console > Sitemaps (no hay tool MCP para esto).

## Decisión de la corrida de hoy
NO se creó ni optimizó ninguna página nueva en FASE 6: el diff de FASE 5 (correcciones de accesibilidad ALTA + performance ALTA + link roto) ya alcanzó el cap de 18 páginas HTML del candado de publicación. Los 4 hallazgos de bajo riesgo se encolaron en BACKLOG.jsonl para la próxima corrida (loop-until-dry sin pérdida de trabajo).
