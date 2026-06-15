#!/usr/bin/env python3
"""Ceremonia de cache-busting de CSS — en UN solo paso y verificada.

El CSS se sirve `immutable` en Netlify, así que cambiar su contenido NO llega a
visitantes recurrentes salvo que cambie la URL. La convención del sitio es el
query `?v=YYYYMMDD` en cada referencia + subir CACHE_VERSION del service worker.
Hacerlo a mano en ~670 archivos es propenso a dejar un `?v=` desigual (caché
stale silenciosa en ese archivo). Este script lo hace de una y verifica que
TODAS las referencias queden uniformes.

Uso:
    python3 scripts/bump-css-version.py            # usa la fecha de hoy (YYYYMMDD)
    python3 scripts/bump-css-version.py 20260720   # versión explícita

Qué hace:
  1. Pone `?v=<NEW>` en TODA referencia HTML a styles*.css (añade el query si falta).
  2. Sube CACHE_VERSION en sw.js (vN -> vN+1) y alinea su precache de CSS a `?v=<NEW>`.
  3. Verifica uniformidad: 0 referencias con un `?v=` distinto al nuevo.
"""
import datetime
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

NEW = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().strftime("%Y%m%d")
if not re.fullmatch(r"\d{8}", NEW):
    sys.exit(f"Versión inválida '{NEW}': usa formato YYYYMMDD (ej. 20260720).")

# 1) HTML: styles*.css(?v=NNN)? -> styles*.css?v=NEW
CSS_REF = re.compile(r'(styles[^"\']*?\.css)(\?v=\d+)?(["\'])')
html_changed = 0
refs = 0
for f in glob.glob("**/*.html", recursive=True):
    s = open(f, encoding="utf-8").read()
    if "styles" not in s or ".css" not in s:
        continue
    new, n = CSS_REF.subn(lambda m: f"{m.group(1)}?v={NEW}{m.group(3)}", s)
    if n and new != s:
        open(f, "w", encoding="utf-8").write(new)
        html_changed += 1
        refs += n

# 2) sw.js: CACHE_VERSION + precache de CSS
sw_path = "sw.js"
sw = open(sw_path, encoding="utf-8").read()
m = re.search(r"CACHE_VERSION\s*=\s*'v(\d+)'", sw)
old_v = int(m.group(1)) if m else 0
new_v = old_v + 1
sw = re.sub(r"CACHE_VERSION\s*=\s*'v\d+'", f"CACHE_VERSION = 'v{new_v}'", sw, count=1)
sw = CSS_REF.sub(lambda mm: f"{mm.group(1)}?v={NEW}{mm.group(3)}", sw)
open(sw_path, "w", encoding="utf-8").write(sw)

# 3) Verificación de uniformidad
bad = []
all_versions = set()
for f in glob.glob("**/*.html", recursive=True):
    s = open(f, encoding="utf-8").read()
    for mm in re.finditer(r'styles[^"\']*?\.css\?v=(\d+)', s):
        all_versions.add(mm.group(1))
        if mm.group(1) != NEW:
            bad.append(f)

print(f"Versión nueva: ?v={NEW}  ·  sw.js CACHE_VERSION v{old_v} -> v{new_v}")
print(f"HTML modificados: {html_changed}  ·  referencias CSS actualizadas: {refs}")
print(f"Versiones ?v= presentes ahora: {sorted(all_versions) or ['(ninguna)']}")
if bad:
    print(f"⚠️ {len(set(bad))} archivo(s) con ?v= distinto a {NEW}: {sorted(set(bad))[:5]}")
    sys.exit(1)
print("✅ Uniforme: todas las referencias CSS usan ?v=" + NEW)
print("Recuerda: commitea los 3 CSS si cambiaste su CONTENIDO (paridad styles.css/min/.hash).")
