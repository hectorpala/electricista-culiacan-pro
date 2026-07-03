# Oportunidades GSC — 2026-07-03

## Métricas (28 días, vs corrida de ayer)
| Métrica | Hoy | Ayer | Cambio |
|---|---|---|---|
| Clics | 104 | 100 | +4% |
| Impresiones | 4,764 | 4,558 | +4.5% |
| CTR | 2.18% | 2.19% | ~estable |
| Posición promedio | 7.1 | 7.1 | sin cambio |

Tendencia estable/ligeramente positiva. Top queries: "electricista culiacan" (pos 6.6, 117 impr,
12 clics), "electricista" (pos 4.0, 108 impr, 5 clics).

## Decisiones (panel decisor-negocio + reglas de NEGOCIO.md)

| Oportunidad | Acción | Riesgo | Motivo |
|---|---|---|---|
| `electricista-precios` CTR 0% pos 9.7 para "electricista" | **NO tocar** | alto → humano | Interferiría con el experimento de título de la home en curso (medir hasta 2026-07-15) y con la canibalización interna ya congelada. Encolado `bk-672de88e` requiere_humano. |
| `instalacion-contactos` CTR 0% pos 5.0 | Ya en backlog | bajo | `bk-f38bd140`, pendiente de próxima corrida (cupo de páginas agotado hoy). |
| Sitemap fantasma `/sitemaps/servicios_colonias_sitemap.xml` en GSC | Sin acción de código | — | Requiere borrado manual en la consola de Search Console (ya documentado, pendiente-humano histórico). |
| Canibalización "electricista" entre home/servicios/colonias | Sin acción | — | Apuesta de estrategia SEO, pendiente-humano histórico (sin cambios hoy). |
| "electrician near me" pos 4.3, 0 clics | Ignorar (decidido) | — | NEGOCIO.md 2026-06-22: no perseguir inglés. |
| "eléctrico automotriz a domicilio" pos 9.1 | Ignorar (decidido) | — | NEGOCIO.md: fuera de giro, no se ofrece. |

## Páginas nuevas hoy: 0

**Motivo:** el diff de la FASE 5 ya llegó al cap de 18 páginas HTML con la corrección de la
regresión de contraste WCAG heredada de ayer (`bk-3d5ba91f`, ALTA) + hallazgos nuevos de los 9
revisores (twitter:url, tap-targets). No hay señal de GSC que justifique forzar una página nueva
hoy sobre ese cupo ya ocupado; el sitio sigue cubriendo la demanda real sin huecos claros de
"electricidad con impresiones altas y sin página propia".

## Backlog nuevo encolado hoy (6 tareas)
- `bk-28159c53` — og:image genérico de emergencia en 20 páginas de servicio no-emergencia (media, bajo riesgo)
- `bk-a4edc2b4` — imágenes hero duplicadas por MD5 en `assets/images/optimizadas/` (bajo riesgo)
- `bk-bacf7108` — 15 páginas sin variante AVIF de su hero (bajo riesgo)
- `bk-a24ec5de` — `instalacion-ventiladores-techo` huérfana, sin enlaces entrantes (bajo riesgo)
- `bk-d0bf38a5` — `contacto/` huérfana, sin enlaces entrantes reales (bajo riesgo)
- `bk-3bd33864` — color muerto `#FBBF24` en `.rating-stars` inline, ~674 páginas (bajo riesgo, latente)
- `bk-672de88e` — `electricista-precios` CTR fix bloqueado por decisión de negocio (alto riesgo, requiere_humano)
- `bk-e8643041` — propagar fix de `.skip-link:focus` tap-target al resto del sitio (bajo riesgo)
