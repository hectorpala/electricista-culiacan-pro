# Auditoría de crecimiento (GSC) — 2026-06-17 (corrida supervisada)

Propiedad: `https://electricistaculiacanpro.mx/` · ventana 28 días.

## Veredicto: 0 páginas NUEVAS justificadas hoy. La ganancia es ENRIQUECER lo existente.
El sitio ya cubre con página propia cada servicio y query comercial con demanda. Forzar
páginas nuevas sobre esta demanda canibalizaría páginas existentes (doorway) → el candado
`gate-pagina.py` las bloquearía con razón. Lo de alto valor y bajo riesgo es optimización.

## Tabla rankeada
| # | Oportunidad | Tipo | Dato GSC | Acción | Riesgo doorway |
|---|---|---|---|---|---|
| 1 | "electricista 24 horas / urgente" rankea en el HOME, no en `emergencia-24-7` | Enriquecer página existente | "electricista 24 horas" pos 9.4 (2 clics), "electricistas 24 horas" pos 11, "electricista urgente" pos 9.3/15 impr/0 clics | Optimizar title/meta/H1 de `servicios/emergencia-24-7/` hacia 24h+urgente + enlace interno desde home | Bajo (mejora, no crea) |
| 2 | Cluster "cómo evitar cortocircuitos" pos 8-12 | Enriquecer blog existente | "como evitar un corto circuito en casa" pos 8.2/13 impr, +3 variantes | Añadir las variantes "evitar" al blog `como-prevenir-cortocircuitos-casa` (H2/FAQ) | Bajo |
| 3 | CTR 0 en queries top-3 del HOME | Optimización CTR | "electrica cerca de mi ubicación" pos 2.2/30 impr/0 clics; "electricista a domicilio cerca de mi ubicación" pos 2/23 impr/0 clics | Revisar title/meta del home para esas variantes (decisión de copy del dueño) | N/A |
| — | "eléctrico automotriz a domicilio" pos 2.6/21 impr | DESCARTADO | off-target | NO crear (REGLAS: el negocio no ofrece automotriz) | — |

## Recomendación
NO crear páginas hoy (correcto por datos). Ejecutar la **Oportunidad #1** (optimizar
`emergencia-24-7` + enlace desde home) como enriquecimiento de bajo riesgo y alta intención.
La #2 y #3 son ediciones de copy menores que el Auto Agente diario puede ir tomando.
