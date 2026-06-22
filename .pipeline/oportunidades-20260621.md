# Oportunidades GSC — 2026-06-21 (primera corrida con GSC FUNCIONAL tras 5 días ciego)

Datos reales `mcp__gsc__*` sobre https://electricistaculiacanpro.mx/ (28 días).
Rendimiento global: 92 clics · 4301 impr · CTR 2.14% · pos 7.0 (estable vs periodo anterior +1%).

## Tabla rankeada (impacto vs riesgo-doorway)

| # | Query | Pos | Impr | Clics | Página que rankea | Diagnóstico | Acción | Riesgo |
|---|-------|-----|------|-------|-------------------|-------------|--------|--------|
| 1 | electricistas 24 horas | 12.3 | 13 | 0 | **/** (home) | Existe `/servicios/emergencia-24-7/` pero rankea el HOME → la dedicada no captura la intención "24 horas" | PIVOTE: optimizar title/meta/H1 de emergencia-24-7 hacia "electricista 24 horas Culiacán" + enlace interno | BAJO (mejora dedicada, no crea página) |
| 2 | electrica cerca de mi ubicación | 2.3 | 27 | 0 | / (home) | Pos 2.3 con 0 clics = problema de CTR del snippet del home | PIVOTE CTR: el home ya rankea muy alto; afinar title/meta es riesgoso (ancla "electricista culiacan" pos 4.5 con clics) | MEDIO (tocar home head-term) |
| 3 | electrician near me | 4.5 | 35 | 0 | / (home) | Query en INGLÉS, near-me; 0 clics | Marginal; el público objetivo es español. No accionar | — |
| 4 | electricista 24 horas | 9.4 | 10 | 2 | (emergencia-24-7) | CTR 20% sano; ya convierte | Se refuerza con acción #1 | BAJO |
| 5 | eléctrico automotriz a domicilio | 2.9 | 22 | 1 | — | OFF-TARGET: el negocio NO hace automotriz (regla 2026-06-17) | IGNORAR | — |

## Decisión FASE 6
- **0 páginas nuevas**: NO hay hueco real. Cada query de alta impresión ya tiene página propia; crear otra canibalizaría/sería doorway.
- **PIVOTE (acción #1, alta confianza/bajo riesgo)**: enrutar la intención "24 horas" a la página dedicada `/servicios/emergencia-24-7/` optimizando su title/meta/H1 + enlace interno, ya que hoy rankea el home en su lugar. Respaldado por datos reales (13+10 impr en "24 horas").
- Acción #2 (CTR del home) queda como observación: tocar el head-term del home es alto riesgo; se deja para decisión con más datos.
