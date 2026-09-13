#!/bin/bash
# catchup.sh — Recupera la corrida diaria del ELECTRICISTA si se saltó (Mac apagada/dormida a la hora).
# Lo dispara el LaunchAgent com.electricistaculiacan.catchup con RunAtLoad (al iniciar sesión/boot).
# Regla: si la última corrida fue hace >= 20h, se saltó al menos una diaria -> recuperar ahora.
# El lock de crecer-diario.sh (/tmp/auto-agente-electricista.lock) evita doble corrida.
set -uo pipefail

LOG_DIR="$HOME/Library/Logs/mantener-sitio"
mkdir -p "$LOG_DIR"
# Apunta al sistema unificado (Auto Agente Electricista), no al viejo de solo-mantenimiento.
SCRIPT="/Users/openclaw/Sitios Web/Electricista Culiacán/.pipeline/crecer-diario.sh"
STAMP=$(date "+%Y-%m-%d %H:%M:%S")

# A3 — anti doble-corrida: si YA hubo una corrida HOY (marca datada que escribe el driver al
# terminar), no dispares otra aunque hayan pasado >=20h (evita 1 corrida por reinicio + 1 por launchd).
TODAY=$(date +%Y%m%d)
# Marcador NAMESPACEADO (el viejo auto-agente-last-run-day era COMPARTIDO con el plomero).
# Fallback una sola vez al nombre viejo para no perder la marca del día de la transición.
MARK=$(cat "$LOG_DIR/auto-agente-electricista-last-run-day" 2>/dev/null || cat "$LOG_DIR/auto-agente-last-run-day" 2>/dev/null || echo "")
if [ "$MARK" = "$TODAY" ]; then
  echo "[$STAMP] catch-up electricista: ya corrió hoy ($TODAY) -> sin acción" >> "$LOG_DIR/electricista-catchup.log"
  exit 0
fi

# SOLO logs del ELECTRICISTA (namespaceados): el glob viejo auto-agente-2*.log matcheaba
# también los del PLOMERO (misma carpeta) → dead-man's switch contaminado (infra-009 del
# plomero: sitio muerto pasaba por vivo). electricista-2*.log = logs del job viejo.
NEWEST=$(ls -t "$LOG_DIR"/auto-agente-electricista-2*.log "$LOG_DIR"/electricista-2*.log 2>/dev/null | head -1)
if [ -n "$NEWEST" ]; then
  AGE_H=$(( ( $(date +%s) - $(stat -f %m "$NEWEST") ) / 3600 ))
else
  AGE_H=999
fi

# La última corrida FALLÓ si trae el marcador propio del DRIVER ("terminó con error").
# "API Error" aparece en el STREAM de corridas exitosas (reintentos relatados) → falso FAILED.
FAILED=0
[ -n "$NEWEST" ] && grep -qiE "termin. con error" "$NEWEST" && FAILED=1

if [ "$AGE_H" -ge 20 ]; then
  echo "[$STAMP] catch-up electricista: última corrida hace ${AGE_H}h (>=20, ausente) -> RECUPERANDO" >> "$LOG_DIR/electricista-catchup.log"
  bash "$SCRIPT"
  echo "[$STAMP] catch-up electricista: terminado" >> "$LOG_DIR/electricista-catchup.log"
elif [ "$FAILED" = 1 ]; then
  echo "[$STAMP] catch-up electricista: última corrida (hace ${AGE_H}h) FALLÓ -> RECUPERANDO" >> "$LOG_DIR/electricista-catchup.log"
  bash "$SCRIPT"
  echo "[$STAMP] catch-up electricista: terminado" >> "$LOG_DIR/electricista-catchup.log"
else
  echo "[$STAMP] catch-up electricista: última corrida hace ${AGE_H}h, OK -> sin acción" >> "$LOG_DIR/electricista-catchup.log"
fi
