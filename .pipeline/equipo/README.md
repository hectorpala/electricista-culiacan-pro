# Equipo de agentes — este proyecto usa los agentes GLOBALES (13-sep-2026)

- Agentes: `~/.claude/agents/equipo-{pensador,ejecutor,arreglador,probador}.md` (genéricos).
- Coordinador: skill global `~/.claude/skills/equipo/SKILL.md` → `/equipo [frente]`.
- Perfil de ESTE proyecto: `EQUIPO.md` en la raíz del repo (checkers, intocables, publicación,
  lecciones por rol). Es lo único específico; los agentes lo leen al arrancar.
- Lanzador global: `~/.claude/equipo/correr.sh <repo> [frente]`; aquí lo invoca
  `.pipeline/launchd/bin/EquipoElectricista` (job launchd `com.electricistaculiacan.equipo`, 21:00).
  Log en `~/Library/Logs/equipo/`.
- Por corrida, en este repo: `calificaciones.jsonl` (rúbrica 4×3, <7 reprueba) y `partes/parte-<stamp>.md`.

Para usar el equipo en OTRO proyecto: copiar la plantilla de `EQUIPO.md` (está al final del
SKILL.md global), llenarla, y correr `/equipo` desde ese repo o programar el lanzador global.
