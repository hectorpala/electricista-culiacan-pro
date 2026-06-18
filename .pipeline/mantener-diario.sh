#!/bin/bash
set -euo pipefail

# Forzar IPv4: el 2026-06-16 fallaron corrida y correo por IPv6 roto (EHOSTUNREACH).
# Hace que node (claude CLI + send-report) prefiera IPv4.
export NODE_OPTIONS="--dns-result-order=ipv4first"

cd "/Users/openclaw/Sitios Web/Electricista Culiacán" || exit 1
LOG_DIR="$HOME/Library/Logs/mantener-sitio"
mkdir -p "$LOG_DIR"
STAMP=$(date +%Y%m%d-%H%M%S)
RUTA_CLAUDE="/Users/openclaw/.npm-global/bin/claude"

# Lock por-REPO COMPARTIDO con crecer-diario.sh (el Auto Agente lo reemplaza; este script
# queda como respaldo manual). Mismo lock = NUNCA dos pipelines a la vez sobre el mismo repo.
LOCK_DIR="/tmp/auto-agente-electricista.lock"
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  OLDPID=$(cat "$LOCK_DIR/pid" 2>/dev/null || echo "")
  if [ -n "$OLDPID" ] && kill -0 "$OLDPID" 2>/dev/null; then
    echo "[$STAMP] Ya hay una corrida activa (pid $OLDPID); saliendo." >> "$LOG_DIR/electricista-$STAMP.log"
    exit 0
  fi
  rm -rf "$LOCK_DIR"; mkdir "$LOCK_DIR" 2>/dev/null || exit 0
fi
echo "$$" > "$LOCK_DIR/pid"
trap 'rm -rf "$LOCK_DIR"' EXIT

# Corrida autónoma del pipeline (auto-permiso → 9 revisores, arregla y publica según candados)
"$RUTA_CLAUDE" --permission-mode auto -p "$(cat .pipeline/mantener-prompt.txt)" >> "$LOG_DIR/electricista-$STAMP.log" 2>&1 \
  || echo "[$STAMP] La corrida de claude terminó con error (continúo para enviar el parte)." >> "$LOG_DIR/electricista-$STAMP.log"

# Parte por email — SIEMPRE, aun si la corrida falló (send-report alerta si el resumen es viejo/ausente).
/usr/local/bin/node /Users/openclaw/gsc-mcp/send-report.mjs \
  "/Users/openclaw/Sitios Web/Electricista Culiacán/.pipeline/ultima-corrida.md" \
  "Electricista Culiacán" "18:20" >> "$LOG_DIR/electricista-$STAMP.log" 2>&1 \
  || echo "[$STAMP] No se pudo enviar el email del parte (electricista)." >> "$LOG_DIR/electricista-$STAMP.log"
