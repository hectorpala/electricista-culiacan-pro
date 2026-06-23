# Routing de modelos por agente — política (decidir bien SIN despilfarrar tokens)

Cada agente declara su `model:` en el frontmatter. La regla NO es "todo a Haiku": es **el modelo
justo según dónde vive la inteligencia de la tarea.** Bajar de modelo solo donde el modelo NO
cambia el resultado; mantener el fuerte donde su juicio ES el producto.

## El principio (3 preguntas)
1. **¿La verdad la produce un checker determinista y el agente solo lo corre y relaya el JSON?**
   → **haiku.** Ejecuta el comando y devuelve el JSON igual que Opus. Cero pérdida de efectividad.
2. **¿Juicio ligero, medición headless, o sensible pero mecánico?** → **sonnet.**
3. **¿El JUICIO del modelo ES el entregable (calidad, doorway, decisión de negocio)?** → **opus.**

## Asignación actual (electricista)
| Modelo | Agentes | Por qué |
|---|---|---|
| **haiku** | revisor-indexabilidad · revisor-plantilla · revisor-produccion | Cada uno corre un checker (`check-*.py`); el JSON es la verdad. |
| **sonnet** | revisor-gsc · revisor-a11y · revisor-movil · revisor-perf · revisor-seo · revisor-links · verificador | Juicio ligero / medición headless / verificación de solo-lectura. |
| **opus** | decisor-negocio | La decisión de negocio (qué crear/escalar) ES el producto; un error es caro. |

## Roles que heredan el modelo de SESIÓN (= Opus)
El orquestador diario (la corrida principal) y el constructor/fixer de páginas se quedan en Opus:
ahí la inteligencia ES el producto. Solo los REVISORES se bajan de modelo (es donde estaba el despilfarro).

## Dormidos (NO los invoca el prompt diario → no gastan)
page-rebuilder, qa-validator, style-critic, style-extractor, image-size-auditor, revisor (equipo
feb-2026 sin frontmatter). Si algún día se activan, asignarles modelo con este mismo criterio.

## Regla para un agente NUEVO
Si solo corre un `check-*` → **haiku**. Si juzga calidad/intención → **opus**. En medio → **sonnet**.
Ante la duda, sube un escalón: el ahorro no vale perder efectividad.
