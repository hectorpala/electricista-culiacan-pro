#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tripwire de COSTO/CUOTA. Lee .pipeline/costos.jsonl (lo escribe registrar-costo.mjs desde el
driver — portado del plomero 2026-07-07: antes NADA escribía el ledger y este tripwire estuvo
MUERTO desde el origen). Emite hallazgos si la última corrida se pasó de presupuesto, si hay
señales de corrida desbocada/enana, o si el ledger deja de recibir filas (continuidad).
Solo VISIBILIDAD: no corta nada. Emite el JSON común {"hallazgos":[...]}. Sin argumentos.
"""
import os, json
from datetime import date, datetime

ROOT   = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COSTOS = os.path.join(ROOT, ".pipeline", "costos.jsonl")
UMBRAL_TOKENS = 28_000_000   # ~2x una corrida diaria normal
UMBRAL_USD    = 70           # usd_equiv_api_ref (referencia; corre por suscripción)

def main():
    hallazgos, filas = [], []
    if os.path.isfile(COSTOS):
        for ln in open(COSTOS, encoding="utf-8", errors="replace"):
            ln = ln.strip()
            if ln:
                try: filas.append(json.loads(ln))
                except Exception: pass
    # ── LEDGER VACÍO/AUSENTE: el registro de consumo no está corriendo (así estuvo este
    #    sitio desde el origen hasta 2026-07-07 sin que nadie lo notara).
    if not filas:
        hallazgos.append({
            "id": "costo-ledger-vacio", "archivo": ".pipeline/costos.jsonl", "linea": 0,
            "severidad": "media", "categoria": "costo",
            "descripcion": "El ledger de consumo está vacío o no existe: registrar-costo.mjs no está corriendo (o el driver no lo invoca) — el consumo de cuota NO se está vigilando.",
            "fix_sugerido": "Verificar que crecer-diario.sh invoque registrar-costo.mjs tras la corrida y que el archivo se esté anexando.",
        })
        print(json.dumps({"hallazgos": hallazgos, "analizadas": 0}, ensure_ascii=False, indent=2))
        return
    # ── Detector de CORRIDA DESBOCADA: output_tokens y nº de mensajes vs mediana móvil
    #    (excluyendo filas de 0 tokens, que son corridas fallidas y deprimen la mediana).
    FACTOR = 5
    MIN_HIST = 4
    def _mediana(xs):
        s = sorted(xs); n = len(s)
        if not n: return 0
        return s[n//2] if n % 2 else (s[n//2-1] + s[n//2]) / 2
    if len(filas) > MIN_HIST:
        u = filas[-1]; prev = filas[:-1]
        for campo, etiqueta in (("output_tokens", "output"), ("mensajes", "mensajes")):
            cur = u.get(campo, 0) or 0
            med = _mediana([f.get(campo, 0) or 0 for f in prev if (f.get("total_tokens", 0) or 0) > 0])
            if med > 0 and cur > FACTOR * med:
                hallazgos.append({
                    "id": "costo-runaway-%s" % etiqueta, "archivo": ".pipeline/costos.jsonl", "linea": 0,
                    "severidad": "alta", "categoria": "costo",
                    "descripcion": "CORRIDA DESBOCADA: la última (%s) generó %s=%s, ~%.0f× la mediana (%s). Firma de loop sin freno, no de día grande." % (
                        u.get("etiqueta", "?"), etiqueta, f"{cur:,}", cur/med, f"{int(med):,}"),
                    "fix_sugerido": "Auditar la corrida: ¿loop-until-dry sin tope o fan-out sin lote? El timeout duro del driver la corta a los 90 min.",
                })
    u   = filas[-1]
    tok = u.get("total_tokens", 0)
    usd = u.get("usd_equiv_api_ref", 0)
    if tok > UMBRAL_TOKENS or usd > UMBRAL_USD:
        hallazgos.append({
            "id": "costo-001", "archivo": ".pipeline/costos.jsonl", "linea": 0,
            "severidad": "media", "categoria": "costo",
            "descripcion": "La última corrida (%s) consumió %.1fM tokens (~$%.0f api-ref), sobre presupuesto (%.0fM / $%.0f)." % (
                u.get("etiqueta", "?"), tok/1e6, usd, UMBRAL_TOKENS/1e6, UMBRAL_USD),
            "fix_sugerido": "Auditar la corrida: ¿demasiados revisores en paralelo, lote grande, o un loop sin freno? Bajar fan-out o usar modelo más barato en revisores deterministas.",
        })
    # ── Fila de 0 tokens: NO es una corrida barata, es un fallo silencioso.
    if (u.get("total_tokens", 0) or 0) == 0:
        hallazgos.append({
            "id": "costo-000", "archivo": ".pipeline/costos.jsonl", "linea": 0,
            "severidad": "media", "categoria": "costo",
            "descripcion": "La última corrida (%s) registró 0 tokens: el medidor falló o la corrida no ejecutó." % u.get("etiqueta", "?"),
            "fix_sugerido": "Revisar el log de la corrida y el failnote; un 0 oculta tanto una corrida caída como un medidor roto.",
        })
    # ── CONTINUIDAD: día(s) sin fila = el auto-agente no corrió (o no registró) y nadie
    #    avisó (caso plomero 04→07-jul). Umbral 2: la fila de HOY puede no existir aún.
    fechas = [f.get("fecha", "") for f in filas if f.get("fecha")]
    try:
        ultima = max(datetime.strptime(x, "%Y-%m-%d").date() for x in fechas)
        dias = (date.today() - ultima).days
        if dias >= 2:
            hallazgos.append({
                "id": "costo-continuidad", "archivo": ".pipeline/costos.jsonl", "linea": 0,
                "severidad": "alta", "categoria": "costo",
                "descripcion": "CONTINUIDAD ROTA: la última fila del ledger es del %s (%d días sin corrida registrada)." % (ultima.isoformat(), dias),
                "fix_sugerido": "Revisar launchctl (com.electricistaculiacan.autoagente), el log más reciente y los failnotes; el catch-up debería recuperar al siguiente arranque.",
            })
    except ValueError:
        pass
    # ── CORRIDA ENANA: pocos mensajes = arrancó y murió a los minutos.
    msj = u.get("mensajes", 0) or 0
    if 0 < msj <= 5:
        hallazgos.append({
            "id": "costo-enana", "archivo": ".pipeline/costos.jsonl", "linea": 0,
            "severidad": "media", "categoria": "costo",
            "descripcion": "CORRIDA ENANA: la última (%s) registró solo %d mensaje(s) — arrancó y murió casi de inmediato." % (u.get("etiqueta", "?"), msj),
            "fix_sugerido": "Revisar el log de esa corrida y el failnote; causa típica: error temprano del CLI (red/credenciales).",
        })
    print(json.dumps({"hallazgos": hallazgos, "analizadas": len(filas)}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
