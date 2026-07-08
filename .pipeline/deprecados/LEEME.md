# Deprecados (archivados 2026-07-07, port de la auditoría infra del plomero)

- **mantener-diario.sh** — reemplazado por `crecer-diario.sh` (que incluye el mantenimiento).
  Se archiva porque era footgun residual: corre con el prompt viejo `mantener-prompt.txt`,
  sin reintentos/wait_for_net/timeout, y escribía el marcador del día compartido, pudiendo
  hacer que el catch-up se saltara una recuperación legítima. NO estaba en launchd
  (verificado 2026-07-07: solo autoagente, catchup y meta cargados).
