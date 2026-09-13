# Equipo de agentes (13-sep-2026) — el ÚNICO equipo del sitio

Coordinador = sesión Claude con el modelo fuerte → `/equipo [frente]` (`.claude/skills/equipo/SKILL.md`).
Agentes en `.claude/agents/equipo-*.md`:

| Rol | Modelo | Puede editar | Qué hace |
|---|---|---|---|
| equipo-pensador | opus | no | audita (checkers + GSC real) y entrega plan de ≤5 tareas verificables |
| equipo-ejecutor | sonnet | sí | implementa UNA tarea, cambio mínimo, con evidencia |
| equipo-arreglador | sonnet | sí | causa raíz de una falla reportada, corrige lo mínimo |
| equipo-probador | haiku | no | intenta demostrar que la tarea falló; PASA/FALLA con comandos |

Archivos:
- `calificaciones.jsonl` — una línea por reporte (rúbrica 4×3 puntos; <7 reprueba).
- `partes/parte-<stamp>.md` — parte en español para Héctor, una por corrida.
- `correr.sh` — corrida desatendida (`claude -p "/equipo todo"`), lock + tiempo límite,
  herramientas permitidas por lista explícita. Log en `~/Library/Logs/mantener-sitio/equipo-*.log`.
- `com.electricistaculiacan.equipo.plist` — job launchd diario 21:00 (se instala copiándolo a
  `~/Library/LaunchAgents/` y `launchctl bootstrap gui/$UID <ruta>`).

Reglas de oro:
- Trabajo SIEMPRE en worktree `/tmp/electricista-equipo-<stamp>` desde `origin/main`, rama
  `equipo/<stamp>`. Publicar a `main` (= producción en Netlify) lo hace Héctor.
- Reforzamiento: el coordinador escribe lecciones fechadas en la sección "Lecciones" del agente
  que reprobó y sube `model:` un escalón a la 2ª reprobación por capacidad. Nunca baja solo.
- Los checkers deterministas de `.pipeline/check-*.py`, `ci-gate.py`, `gate-pagina.py`,
  `auto-fixers.py` y `gestor-backlog.py` siguen siendo la vara de verdad; el equipo los usa.
