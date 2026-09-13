#!/bin/bash
# Delegado: el lanzador real es global (~/.claude/equipo/correr.sh <repo> [frente]).
exec /bin/bash "$HOME/.claude/equipo/correr.sh" "/Users/openclaw/Sitios Web/Electricista Culiacán" "$@"
