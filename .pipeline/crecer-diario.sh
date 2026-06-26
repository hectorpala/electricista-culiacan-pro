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

# launchd arranca con PATH mínimo (sin node) → el MCP de GSC ("command":"node") no
# arrancaba y el agente quedaba "ciego" de GSC (5 días seguidos). Aseguramos node en PATH.
export PATH="/usr/local/bin:/opt/homebrew/bin:$PATH"

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
# --mcp-config: carga el MCP de GSC con node ABSOLUTO (clave para que arranque bajo launchd).
# --strict-mcp-config: usa SOLO ese server (ignora ~/.claude.json: tradingview, etc. no hacen falta aquí).
MCP_GSC="/Users/openclaw/Sitios Web/Electricista Culiacán/.pipeline/mcp-gsc.json"

# ── Clasificación de errores (NO confundir red con cuota) ────────────────────
# TRANSITORIO = se cayó la conexión / el servidor falló a media respuesta. Se REINTENTA:
#   no perdimos cuota, solo se cortó el stream (caso 2026-06-24: "Connection closed mid-response").
# LIMITE = de verdad se agotó el uso del plan. NO se reintenta (inútil hasta que reinicie la cuota).
# El match se hace SOLO sobre lo que imprimió ESE intento (por offset de bytes), así la línea de
# estadística "📊 Uso de la corrida (cuota de suscripción)" nunca cuenta como motivo del fallo.
TRANSIENT_RE='Connection closed mid-response|API Error|Connection error|overloaded|ECONNRESET|ETIMEDOUT|EHOSTUNREACH|ENETUNREACH|fetch failed|socket hang up|terminated|Internal server error|HTTP 5[0-9][0-9]|\b5(00|02|03|29)\b|may be incomplete'
LIMIT_RE='session limit|usage limit|hit your (usage|limit)|rate limit|límite de uso|quota exceeded|resets? at|your limit will reset'

# Espera a que la API de Claude vuelva antes de cada intento. NordVPN (kill switch) bloquea
# la salida al reconectar; sin esto el intento se quema de inmediato (caso plomero 06-25).
# curl a /v1/messages da HTTP 405 (exit 0 = conectó); solo un error de RED da exit != 0.
wait_for_net() {
  local i
  for i in $(seq 1 32); do
    curl -sS -o /dev/null --max-time 6 https://api.anthropic.com/v1/messages 2>/dev/null && return 0
    echo "[$STAMP] red caída (¿NordVPN reconectando?); espero 15s ($i/32)…" >> "$LOG"
    sleep 15
  done
  return 1
}

MAX_ATTEMPTS=3
CLAUDE_OK=0
FAIL_KIND=""          # transitorio | limite | desconocido
for attempt in $(seq 1 "$MAX_ATTEMPTS"); do
  echo "[$STAMP] >>> intento $attempt/$MAX_ATTEMPTS de la corrida @ $(date +%H:%M:%S)" >> "$LOG"
  OFF=$(wc -c < "$LOG")   # byte-offset: leeremos SOLO lo que agregue este intento
  wait_for_net || echo "[$STAMP] red no volvió tras ~8 min; intento igual (puede fallar)." >> "$LOG"
  # Orquestador en SONNET (~5x más barato; el gasto es 67% releer contexto). Los agentes
  # de juicio crítico (page-rebuilder/qa-validator/style-critic/decisor-negocio) llevan
  # model:opus en su frontmatter -> NO se degradan. Ver MODELO-ROUTING.md.
  if "$RUTA_CLAUDE" --model sonnet --permission-mode auto --mcp-config "$MCP_GSC" --strict-mcp-config -p "$(cat .pipeline/crecer-diario-prompt.txt)" >> "$LOG" 2>&1; then
    CLAUDE_OK=1; FAIL_KIND=""; break
  fi
  TAIL=$(tail -c "+$((OFF + 1))" "$LOG" 2>/dev/null || echo "")
  if printf '%s' "$TAIL" | grep -qiE "$LIMIT_RE"; then
    FAIL_KIND="limite"
    echo "[$STAMP] Falla por LÍMITE DE USO real del plan; no tiene caso reintentar." >> "$LOG"
    break
  fi
  if printf '%s' "$TAIL" | grep -qiE "$TRANSIENT_RE"; then
    FAIL_KIND="transitorio"
  else
    FAIL_KIND="desconocido"
  fi
  if [ "$attempt" -lt "$MAX_ATTEMPTS" ]; then
    WAIT=$((attempt * 120))   # backoff: 120s, luego 240s
    echo "[$STAMP] Error $FAIL_KIND (NO de cuota); reintento en ${WAIT}s." >> "$LOG"
    sleep "$WAIT"
  else
    echo "[$STAMP] Agotados los $MAX_ATTEMPTS intentos; la corrida no completó." >> "$LOG"
  fi
done
[ "$CLAUDE_OK" = 1 ] || echo "[$STAMP] La corrida de claude terminó con error ($FAIL_KIND); continúo para enviar el parte." >> "$LOG"

# Parte por email. Si la corrida tuvo ÉXITO → manda el parte nuevo. Si FALLÓ (cuota/error) →
# NO mandes el parte viejo (sería un correo engañoso "encontré N" de una corrida anterior);
# manda un aviso honesto de que no se completó.
if [ "${CLAUDE_OK:-0}" = 1 ]; then
  /usr/local/bin/node /Users/openclaw/gsc-mcp/send-report.mjs \
    "/Users/openclaw/Sitios Web/Electricista Culiacán/.pipeline/ultima-corrida.md" \
    "Auto Agente Electricista" "20:00" >> "$LOG_DIR/auto-agente-$STAMP.log" 2>&1 \
    || echo "[$STAMP] No se pudo enviar el email del parte (Auto Agente Electricista)." >> "$LOG_DIR/auto-agente-$STAMP.log"
else
  FAILNOTE="$LOG_DIR/fail-$STAMP.md"
  # Motivo HONESTO según el tipo de falla (no asumir cuota). La línea de evidencia se saca del
  # log EXCLUYENDO la estadística "📊 Uso ... (cuota de suscripción)" para no confundirla con un error.
  ERRLINE=$(grep -iE "$TRANSIENT_RE|$LIMIT_RE" "$LOG" 2>/dev/null | grep -viE '📊 Uso|cuota de suscripción|equiv-API' | head -1 | sed 's/^[[:space:]]*//')
  [ -n "$ERRLINE" ] || ERRLINE="(sin línea de error reconocible; revisa el log completo)"
  case "$FAIL_KIND" in
    transitorio)
      MOTIVO="se cayó la conexión con el servidor a media respuesta — error TRANSITORIO de red, NO de cuota (corrió con tu plan, no se facturó nada)"
      SUGERENCIA="El sistema ya reintentó $MAX_ATTEMPTS veces sin éxito. No requiere acción: el catch-up o la corrida de mañana lo recuperan." ;;
    limite)
      MOTIVO="se alcanzó el límite de uso del plan"
      SUGERENCIA="Reintenta cuando se restablezca la cuota." ;;
    *)
      MOTIVO="error no reconocido de la corrida"
      SUGERENCIA="Revisa el log: $LOG" ;;
  esac
  printf '# Auto Agente Electricista — corrida NO completada\n**Motivo:** %s.\n**Evidencia (del log):** `%s`\n**Qué sigue:** %s\n\nNo se hizo ni publicó ningún cambio en esta corrida.\n' \
    "$MOTIVO" "$ERRLINE" "$SUGERENCIA" > "$FAILNOTE"
  /usr/local/bin/node /Users/openclaw/gsc-mcp/send-report.mjs \
    "$FAILNOTE" "Auto Agente Electricista" "no completada" >> "$LOG" 2>&1 \
    || echo "[$STAMP] No se pudo enviar el aviso de falla (Auto Agente Electricista)." >> "$LOG"
fi

# A3: marca que YA corrió hoy SOLO si la corrida tuvo éxito. Si falló, NO se marca → el
# catch-up sí podrá recuperarla hoy (si se marcara siempre, una corrida fallida quedaría sin recuperar).
[ "${CLAUDE_OK:-0}" = 1 ] && date +%Y%m%d > "$LOG_DIR/auto-agente-last-run-day"
