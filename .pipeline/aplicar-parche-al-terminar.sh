#!/bin/bash
# Espera a que la corrida del Electricista termine y aplica los 4 arreglos del orquestador
# portados del Plomero (2026-07-26). NO toca nada mientras la corrida viva: editar un .sh
# que bash esta leyendo por offset lo corrompe a media ejecucion.
LOG="$HOME/Library/Logs/mantener-sitio/parche-orquestador-electricista.log"
DIR="/Users/openclaw/Sitios Web/Electricista Culiacán/.pipeline"
echo "[$(date '+%F %T')] vigilante armado; espero a que libere la corrida." >> "$LOG"
# Tope de 2h: la corrida tiene un timeout duro de 90 min, asi que si a las 2h sigue viva
# es que algo raro pasa y prefiero no tocar nada y dejar rastro.
for i in $(seq 1 240); do
  if ! pgrep -fl "crecer-diario.sh" 2>/dev/null | grep -q "Electricista"; then
    sleep 20   # margen para que el driver cierre el correo y suelte el lock
    echo "[$(date '+%F %T')] corrida terminada; aplico el parche." >> "$LOG"
    python3 "$DIR/parche-orquestador-20260726.py" >> "$LOG" 2>&1
    echo "[$(date '+%F %T')] resultado: exit=$?" >> "$LOG"
    exit 0
  fi
  sleep 30
done
echo "[$(date '+%F %T')] la corrida seguia viva tras 2h; NO parcheo, lo dejo para revision." >> "$LOG"
exit 1
