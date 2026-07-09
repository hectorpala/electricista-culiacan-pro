#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check-relleno.py — DETECTOR de páginas de relleno (contenido delgado o clonado).

Decisión del dueño (2026-07-08): el agente detecta SOLO, en su loop diario, qué páginas
son de relleno y las REGENERA él mismo en páginas de verdad (o las manda a noindex si la
estrategia 2b dice que Google no las quiere). Este script es el sensor; la decisión
enriquecer-vs-noindex la toma el decisor-negocio con señales GSC; la ejecución la drena
el loop del backlog con los candados de siempre.

Usa EXACTAMENTE la misma vara que gate-pagina.py (visible_tokens/jaccard importados de
ahí): lo que este detector marca es lo mismo que el candado bloquearía — cero criterios
divergentes entre sensor y candado.

Criterios (solo páginas INDEXABLES; una noindex deliberada no es "relleno", es estrategia):
  VACIA      <150 tokens visibles únicos  → ya bloquea el candado si alguien la toca
  CASI_VACIA <200 tokens                  → pasará a VACIA con cualquier recorte; delgada
  CLON       Jaccard ≥0.72 vs una hermana → texto casi calcado (banda de advertencia del
                                            anti-doorway; las viejas nunca pasaron por el gate)

Uso:
  python3 .pipeline/check-relleno.py            # reporte legible
  python3 .pipeline/check-relleno.py --json     # una línea JSON por página (para encolar)
Exit 0 siempre (es un sensor, no un candado — el candado sigue siendo gate-pagina.py).
"""
import glob
import importlib.util
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_spec = importlib.util.spec_from_file_location("gate", os.path.join(ROOT, ".pipeline", "gate-pagina.py"))
_gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gate)

UMBRAL_CASI = 200
UMBRAL_CLON = _gate.UMBRAL_WARN   # 0.72 — la misma banda del anti-doorway


def paginas_indexables():
    pats = [
        os.path.join(ROOT, "servicios", "*", "index.html"),
        os.path.join(ROOT, "servicios", "electricista-colonias-culiacan", "*", "index.html"),
        os.path.join(ROOT, "blog", "*", "index.html"),
        os.path.join(ROOT, "blog", "index.html"),
        os.path.join(ROOT, "contacto", "index.html"),
    ]
    out, seen = [], set()
    for pat in pats:
        for f in sorted(glob.glob(pat)):
            af = os.path.abspath(f)
            if af not in seen:
                seen.add(af)
                out.append(f)
    return out


def main():
    as_json = "--json" in sys.argv
    hallazgos = []
    paginas = paginas_indexables()
    tokens_de = {}
    for p in paginas:
        tokens_de[p] = _gate.visible_tokens(p)   # None si es noindex

    indexables = [p for p in paginas if tokens_de[p] is not None]
    for p in indexables:
        tv = tokens_de[p]
        rel = os.path.relpath(p, ROOT)
        motivos = []
        if len(tv) < 150:
            motivos.append("VACIA")
        elif len(tv) < UMBRAL_CASI:
            motivos.append("CASI_VACIA")
        worst, worst_sib = 0.0, None
        for s in indexables:
            if s == p:
                continue
            j = _gate.jaccard(tv, tokens_de[s])
            if j > worst:
                worst, worst_sib = j, s
        if worst >= UMBRAL_CLON:
            motivos.append("CLON")
        if motivos:
            hallazgos.append({
                "pagina": rel,
                "motivos": motivos,
                "tokens_unicos": len(tv),
                "jaccard_max": round(worst, 2),
                "gemela": os.path.relpath(worst_sib, ROOT) if worst_sib and worst >= UMBRAL_CLON else None,
                "es_colonia": "/electricista-colonias-culiacan/" in rel,
            })

    hallazgos.sort(key=lambda x: (x["tokens_unicos"], -x["jaccard_max"]))
    if as_json:
        for x in hallazgos:
            print(json.dumps(x, ensure_ascii=False))
    else:
        print("Detector de relleno — %d indexables revisadas, %d con señal:" % (len(indexables), len(hallazgos)))
        for x in hallazgos:
            extra = (" · gemela %s" % x["gemela"]) if x["gemela"] else ""
            print("  %-12s %-70s %4d tokens · Jaccard %.2f%s" % (
                "/".join(x["motivos"]), x["pagina"], x["tokens_unicos"], x["jaccard_max"], extra))
        if not hallazgos:
            print("  ✅ ninguna página indexable parece de relleno.")
    sys.exit(0)


if __name__ == "__main__":
    main()
