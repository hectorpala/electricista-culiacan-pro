#!/bin/bash
# catchup.sh — Recupera la corrida diaria del ELECTRICISTA si se saltó (Mac apagada/dormida a la hora).
# Lo dispara el LaunchAgent com.electricistaculiacan.catchup con RunAtLoad (al iniciar sesión/boot).
# Regla: si la última corrida fue hace >= 20h, se saltó al menos una diaria -> recuperar ahora.
# El lock de mantener-diario.sh (/tmp/electricista-mantener-sitio.lock) evita doble corrida.
set -uo pipefail

LOG_DIR="$HOME/Library/Logs/mantener-sitio"
mkdir -p "$LOG_DIR"
SCRIPT="/Users/openclaw/Sitios Web/Electricista Culiacán/.pipeline/mantener-diario.sh"
STAMP=$(date "+%Y-%m-%d %H:%M:%S")

NEWEST=$(ls -t "$LOG_DIR"/electricista-2*.log 2>/dev/null | head -1)
if [ -n "$NEWEST" ]; then
  AGE_H=$(( ( $(date +%s) - $(stat -f %m "$NEWEST") ) / 3600 ))
else
  AGE_H=999
fi

if [ "$AGE_H" -ge 20 ]; then
  echo "[$STAMP] catch-up electricista: última corrida hace ${AGE_H}h (>=20) -> RECUPERANDO" >> "$LOG_DIR/electricista-catchup.log"
  bash "$SCRIPT"
  echo "[$STAMP] catch-up electricista: terminado" >> "$LOG_DIR/electricista-catchup.log"
else
  echo "[$STAMP] catch-up electricista: última corrida hace ${AGE_H}h (<20) -> sin acción" >> "$LOG_DIR/electricista-catchup.log"
fi
