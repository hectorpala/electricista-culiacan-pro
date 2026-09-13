#!/bin/bash
# Corrida desatendida del Equipo de agentes (coordinador = claude -p con el modelo fuerte).
# Permisos: lista EXPLÍCITA de herramientas (sin saltarse el sistema de permisos).
# Lock compartido con cualquier otra corrida sobre el mismo repo.
set -u
REPO="/Users/openclaw/Sitios Web/Electricista Culiacán"
LOG_DIR="$HOME/Library/Logs/mantener-sitio"; mkdir -p "$LOG_DIR"
STAMP=$(date +%Y%m%d-%H%M); LOG="$LOG_DIR/equipo-$STAMP.log"
LOCK_DIR="/tmp/auto-agente-electricista.lock"
TIMEOUT_MIN="${TIMEOUT_MIN:-60}"
FRENTE="${1:-todo}"
CLAUDE_BIN="${CLAUDE_BIN:-$HOME/.npm-global/bin/claude}"
export PATH="$HOME/.npm-global/bin:/usr/local/bin:/opt/homebrew/bin:$PATH"

log(){ echo "[$(date +%H:%M:%S)] $*" >> "$LOG"; }

# Lock: si el dueño murió (reboot, kill), se toma; si vive, se sale sin hacer nada.
if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  OWNER=$(cat "$LOCK_DIR/pid" 2>/dev/null || true)
  if [ -n "$OWNER" ] && kill -0 "$OWNER" 2>/dev/null; then
    log "Lock ocupado por pid $OWNER (otra corrida viva); salgo."; exit 0
  fi
  log "Lock huérfano (pid ${OWNER:-?}); lo tomo."; rm -rf "$LOCK_DIR"; mkdir "$LOCK_DIR" || exit 0
fi
echo $$ > "$LOCK_DIR/pid"
trap 'rm -rf "$LOCK_DIR"' EXIT

[ -x "$CLAUDE_BIN" ] || { log "No encuentro claude en $CLAUDE_BIN"; exit 1; }
cd "$REPO" || exit 1
log "Inicio corrida frente=$FRENTE timeout=${TIMEOUT_MIN}min"

# Herramientas permitidas al coordinador y a sus subagentes. Todo lo demás se niega.
ALLOWED=(
  "Agent" "SendMessage" "TaskStop" "Read" "Edit" "Write" "Grep" "Glob"
  "Bash(git fetch:*)" "Bash(git worktree:*)" "Bash(git -C:*)" "Bash(git status:*)"
  "Bash(git diff:*)" "Bash(git log:*)" "Bash(git add:*)" "Bash(git commit:*)"
  "Bash(git checkout -- :*)" "Bash(git revert:*)" "Bash(git push -u origin equipo/:*)"
  "Bash(python3:*)" "Bash(node:*)" "Bash(curl:*)" "Bash(grep:*)" "Bash(ls:*)"
  "Bash(cat:*)" "Bash(head:*)" "Bash(tail:*)" "Bash(wc:*)" "Bash(date:*)"
  "Bash(kill:*)" "Bash(xmllint:*)" "Bash(npm run:*)"
  "mcp__gsc__gsc_list_sites" "mcp__gsc__gsc_performance" "mcp__gsc__gsc_keywords"
  "mcp__gsc__gsc_opportunities" "mcp__gsc__gsc_inspect" "mcp__gsc__gsc_sitemaps"
)

"$CLAUDE_BIN" -p "/equipo $FRENTE" \
  --model claude-fable-5-1 \
  --permission-mode acceptEdits \
  --allowedTools "${ALLOWED[@]}" \
  --output-format text < /dev/null >> "$LOG" 2>&1 &
CPID=$!
( sleep $((TIMEOUT_MIN * 60))
  if kill -0 "$CPID" 2>/dev/null; then
    echo "[$(date +%H:%M:%S)] TIMEOUT ${TIMEOUT_MIN}min: matando corrida (pid $CPID)." >> "$LOG"
    kill "$CPID" 2>/dev/null; sleep 10; kill -9 "$CPID" 2>/dev/null
  fi ) &
WPID=$!
wait "$CPID"; RC=$?
kill "$WPID" 2>/dev/null || true
log "Fin corrida rc=$RC. Parte en $REPO/.pipeline/equipo/partes/"
exit $RC
