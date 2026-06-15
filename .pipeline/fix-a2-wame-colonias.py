#!/usr/bin/env python3
"""A2 — Personaliza el texto del wa.me que quedó con la fuga "10 de Abril".
Deriva el nombre real de cada colonia desde areaServed.name del JSON-LD y
reemplaza SOLO el fragmento del texto del wa.me. Nada más se toca."""
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path("servicios/electricista-colonias-culiacan")
LEAK = "electricista%20en%2010%20de%20Abril"
AREA = re.compile(r'"areaServed":\s*\{[^}]*?"name":\s*"([^"]+?),\s*Culiac[aá]n"')

changed, skipped = [], []

for f in sorted(ROOT.glob("*/index.html")):
    src = f.read_text(encoding="utf-8")
    if LEAK not in src:
        continue
    m = AREA.search(src)
    if not m:
        skipped.append((f, "no se pudo derivar areaServed.name"))
        continue
    name = m.group(1).strip()
    enc = quote(name, safe="")
    repl = f"electricista%20en%20{enc}"
    new = src.replace(LEAK, repl)
    if LEAK in new:
        skipped.append((f, "quedó fuga residual"))
        continue
    if new == src:
        # mismo texto (sería la propia 10-de-abril): no-op legítimo
        continue
    f.write_text(new, encoding="utf-8")
    changed.append((f, name, enc))

print(f"Cambiados: {len(changed)}")
print(f"Saltados:  {len(skipped)}")
for f, name, enc in changed[:5]:
    print(f"  ej {f.parent.name}: -> en {name}  ({enc})")
for f, why in skipped:
    print(f"  SKIP {f}: {why}")
sys.exit(1 if skipped else 0)
