#!/bin/bash
set -euo pipefail

cd "/Users/openclaw/Sitios Web/Electricista Culiacán" || exit 1
LOG_DIR="$HOME/Library/Logs/mantener-sitio"
mkdir -p "$LOG_DIR"
STAMP=$(date +%Y%m%d-%H%M%S)
RUTA_CLAUDE="/Users/openclaw/.npm-global/bin/claude"

# Lock propio de electricista (independiente del de plomero)
LOCK_DIR="/tmp/electricista-mantener-sitio.lock"
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  echo "[$STAMP] Ya hay una corrida de mantenimiento (electricista) activa; saliendo." >> "$LOG_DIR/electricista-$STAMP.log"
  exit 0
fi
trap 'rmdir "$LOCK_DIR"' EXIT

# Corrida autónoma del pipeline (auto-permiso → 9 revisores, arregla y publica según candados)
"$RUTA_CLAUDE" --permission-mode auto -p "$(cat .pipeline/mantener-prompt.txt)" >> "$LOG_DIR/electricista-$STAMP.log" 2>&1 \
  || echo "[$STAMP] La corrida de claude terminó con error (continúo para enviar el parte)." >> "$LOG_DIR/electricista-$STAMP.log"

# Parte por email — SIEMPRE, aun si la corrida falló (send-report alerta si el resumen es viejo/ausente).
/usr/local/bin/node /Users/openclaw/gsc-mcp/send-report.mjs \
  "/Users/openclaw/Sitios Web/Electricista Culiacán/.pipeline/ultima-corrida.md" \
  "Electricista Culiacán" "18:20" >> "$LOG_DIR/electricista-$STAMP.log" 2>&1 \
  || echo "[$STAMP] No se pudo enviar el email del parte (electricista)." >> "$LOG_DIR/electricista-$STAMP.log"
