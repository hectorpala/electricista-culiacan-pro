#!/usr/bin/env python3
"""A1 — Quita SOLO la propiedad aggregateRating del JSON-LD de cada colonia.
Mecánico y validado: regex puntual + json.loads para garantizar que el JSON-LD
siga parseando. No toca nada más (ni el nodo Electrician, ni el hero visible)."""
import json
import re
import sys
from pathlib import Path

ROOT = Path("servicios/electricista-colonias-culiacan")
# coincide con: , "aggregateRating": {...sin llaves anidadas...}
PAT = re.compile(r',\s*"aggregateRating"\s*:\s*\{[^{}]*\}')
LDJSON = re.compile(
    r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL
)

changed, skipped, untouched = [], [], []

for f in sorted(ROOT.glob("*/index.html")):
    src = f.read_text(encoding="utf-8")
    if '"aggregateRating"' not in src:
        untouched.append(f)
        continue
    new = PAT.sub("", src)
    if new == src:
        skipped.append((f, "patrón no coincidió pese a contener aggregateRating"))
        continue
    # validar que TODOS los bloques ld+json del archivo sigan parseando
    ok = True
    for block in LDJSON.findall(new):
        try:
            json.loads(block)
        except Exception as e:
            ok = False
            skipped.append((f, f"JSON-LD no parsea tras el cambio: {e}"))
            break
    if not ok:
        continue
    if '"aggregateRating"' in new:
        skipped.append((f, "quedó un aggregateRating residual"))
        continue
    f.write_text(new, encoding="utf-8")
    changed.append(f)

print(f"Cambiados:   {len(changed)}")
print(f"Saltados:    {len(skipped)}")
print(f"Sin tocar:   {len(untouched)}")
for f, why in skipped:
    print(f"  SKIP {f}: {why}")
sys.exit(1 if skipped else 0)
