#!/bin/bash
set -euo pipefail

# ════════════════════════════════════════════════════════════════════════════
#  AUTO AGENTE ELECTRICISTA — corrida diaria autónoma (todo el sistema junto):
#  CORRIGE errores (mecánicos + humanos) · CRECE +3 páginas/día según GSC ·
#  VERIFICA que todo quedó bien · APRENDE cada error · publica solo si pasa candados.
#  Reemplaza a mantener-diario.sh (lo incluye y le suma crecimiento, verificación y aprendizaje).
# ════════════════════════════════════════════════════════════════════════════

# Forzar IPv4: el 2026-06-16 fallaron corrida y correo por IPv6 roto (EHOSTUNREACH).
export NODE_OPTIONS="--dns-result-order=ipv4first"

cd "/Users/openclaw/Sitios Web/Electricista Culiacán" || exit 1
LOG_DIR="$HOME/Library/Logs/mantener-sitio"
mkdir -p "$LOG_DIR"
STAMP=$(date +%Y%m%d-%H%M%S)
RUTA_CLAUDE="/Users/openclaw/.npm-global/bin/claude"

# Lock por-REPO (lo comparten crecer-diario.sh y mantener-diario.sh para que NUNCA corran
# dos pipelines a la vez sobre el mismo repo). Resistente a cuelgues: si el dueño del lock
# ya murió (SIGKILL/corte de luz/reboot), se roba el lock en vez de quedar apagado en silencio.
LOCK_DIR="/tmp/auto-agente-electricista.lock"
LOG="$LOG_DIR/auto-agente-$STAMP.log"
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  OLDPID=$(cat "$LOCK_DIR/pid" 2>/dev/null || echo "")
  if [ -n "$OLDPID" ] && kill -0 "$OLDPID" 2>/dev/null; then
    echo "[$STAMP] Ya hay una corrida activa (pid $OLDPID); saliendo." >> "$LOG"
    exit 0
  fi
  echo "[$STAMP] Lock huérfano (pid '$OLDPID' ya no vive) -> lo robo y continúo." >> "$LOG"
  rm -rf "$LOCK_DIR"
  mkdir "$LOCK_DIR" 2>/dev/null || { echo "[$STAMP] No pude tomar el lock; saliendo." >> "$LOG"; exit 0; }
fi
echo "$$" > "$LOCK_DIR/pid"
trap 'rm -rf "$LOCK_DIR"' EXIT

# Corrida autónoma del sistema completo (auto-permiso). El prompt orquesta las 10 fases.
"$RUTA_CLAUDE" --permission-mode auto -p "$(cat .pipeline/crecer-diario-prompt.txt)" >> "$LOG_DIR/auto-agente-$STAMP.log" 2>&1 \
  || echo "[$STAMP] La corrida de claude terminó con error (continúo para enviar el parte)." >> "$LOG_DIR/auto-agente-$STAMP.log"

# Parte por email — SIEMPRE, aun si la corrida falló (send-report alerta si el resumen es viejo/ausente).
/usr/local/bin/node /Users/openclaw/gsc-mcp/send-report.mjs \
  "/Users/openclaw/Sitios Web/Electricista Culiacán/.pipeline/ultima-corrida.md" \
  "Auto Agente Electricista" "18:20" >> "$LOG_DIR/auto-agente-$STAMP.log" 2>&1 \
  || echo "[$STAMP] No se pudo enviar el email del parte (Auto Agente Electricista)." >> "$LOG_DIR/auto-agente-$STAMP.log"

# A3: marca que YA corrió hoy (el catch-up lo lee para no duplicar corrida el mismo día).
date +%Y%m%d > "$LOG_DIR/auto-agente-last-run-day"
