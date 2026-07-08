#!/usr/bin/env python3
"""Fix contraste WCAG del badge .hero-availability: verde brillante #22c55e -> teal de marca #075E54.
Solo toca el badge (texto, punto, glow, fondo, borde). NO toca el verde WhatsApp (.bg-whatsapp, style inline)."""
import sys

# Reemplazos seguros (solo badge) para los 3 CSS minificados.
CSS_REPL = [
    ("color:#22c55e", "color:#075E54"),
    ("background:#22c55e", "background:#075E54"),   # en los CSS, el unico background:#22c55e es .availability-dot
    ("0 0 6px #22c55e", "0 0 6px #075E54"),
    ("0 0 12px #22c55e", "0 0 12px #075E54"),
    ("rgba(34,197,94,0.15)", "#E6F4F1"),            # fondo pastilla -> teal claro solido
    ("rgba(34,197,94,0.4)", "rgba(7,94,84,0.35)"),  # borde
]

# Reemplazos para index.html (inline critico): evita .bg-whatsapp y style="" (verde WhatsApp legitimo).
# Ancla el punto por su alto (10px/8px) para no tocar otros background:#22c55e.
HTML_REPL = [
    ("color:#22c55e", "color:#075E54"),
    ("height:10px;background:#22c55e", "height:10px;background:#075E54"),
    ("height:8px;background:#22c55e", "height:8px;background:#075E54"),
    ("0 0 6px #22c55e", "0 0 6px #075E54"),
    ("0 0 12px #22c55e", "0 0 12px #075E54"),
    ("rgba(34,197,94,.15)", "#E6F4F1"),
    ("rgba(34,197,94,0.15)", "#E6F4F1"),
    ("rgba(34,197,94,.4)", "rgba(7,94,84,0.35)"),
    ("rgba(34,197,94,0.4)", "rgba(7,94,84,0.35)"),
]

import os
# Anclado a __file__: con rutas relativas a cwd, desde otro directorio tronaba con
# FileNotFoundError (o pisaría un index.html ajeno si existiera en el cwd).
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def apply(path, repls):
    path = os.path.join(_ROOT, path)
    with open(path, encoding="utf-8") as f:
        s = f.read()
    total = 0
    for a, b in repls:
        n = s.count(a)
        if n:
            s = s.replace(a, b)
            total += n
            print(f"  [{path}] {a!r} -> {b!r} : {n}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    left = s.count("#22c55e")
    print(f"  [{path}] total reemplazos={total} · #22c55e restantes={left}")
    return left

print("== CSS compartidos ==")
for f in ("styles.css", "styles.min.css", "styles.7f293647.css"):
    apply(f, CSS_REPL)

print("== index.html (inline) ==")
left_idx = apply("index.html", HTML_REPL)
print(f"\nEsperado en index.html: 2 restantes (.bg-whatsapp + style inline = verde WhatsApp, intencional).")
sys.exit(0 if left_idx == 2 else 1)
