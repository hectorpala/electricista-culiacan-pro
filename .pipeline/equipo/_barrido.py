#!/usr/bin/env python3
"""Barrido del coordinador: invariantes servidas por página (EQUIPO.md → invariantes).
Uso: python3 _barrido.py <ruta/index.html> [...]   (rutas relativas al worktree)
Comprueba: HTTP 200 en :8097, JSON-LD parsea (nº bloques, nº Question), canonical==og:url==twitter:url,
0 'plomero', email solo contacto@electricistaculiacanpro.mx, teléfono canónico, ETA única 30-60,
0 colores prohibidos (#0066cc/#0284c7/#0369a1, rojo #b91c1c/#dc2626/#ef4444), 0 mojibake (Ã/Â/�).
"""
import sys, re, json, urllib.request
BASE = "http://127.0.0.1:8097/"
WT = "/tmp/equipo-electricista-20261009-2100/"
rows = []
for rel in sys.argv[1:]:
    rel = rel.replace(WT, "")
    url = BASE + rel.replace("index.html", "")
    fallas = []
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            code = r.status
            html = r.read().decode("utf-8", "replace")
    except Exception as e:
        rows.append((rel, f"HTTP ERROR {e}")); continue
    if code != 200: fallas.append(f"http {code}")
    blocks = re.findall(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.S)
    nq = 0
    for i, b in enumerate(blocks):
        try:
            d = json.loads(b)
            nq += len(re.findall(r'"@type"\s*:\s*"Question"', b))
        except Exception as e:
            fallas.append(f"jsonld#{i} no parsea: {str(e)[:40]}")
    def meta(pat):
        m = re.search(pat, html, re.I)
        return m.group(1).rstrip("/") if m else None
    can = meta(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)')
    og = meta(r'<meta[^>]+property=["\']og:url["\'][^>]+content=["\']([^"\']+)')
    tw = meta(r'<meta[^>]+name=["\']twitter:url["\'][^>]+content=["\']([^"\']+)')
    if not (can and can == og == tw): fallas.append(f"url-mismatch can={can} og={og} tw={tw}")
    if re.search(r'plomer', html, re.I): fallas.append(f"plomero x{len(re.findall(r'plomer', html, re.I))}")
    emails = set(re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', html))
    bad = [e for e in emails if e.lower() != "contacto@electricistaculiacanpro.mx" and not e.endswith(("schema.org", "w3.org"))]
    if bad: fallas.append(f"email {bad}")
    nums = set(re.findall(r'(?:wa\.me/|tel:\+?|"telephone"\s*:\s*"\+?)([\d\s-]{8,})', html))
    badn = [n for n in nums if re.sub(r'\D', '', n) not in ("526673922273", "6673922273")]
    if badn: fallas.append(f"tel {badn}")
    etas = set(re.findall(r'(\d{2})\s*[-–a]\s*(\d{2})\s*min', html))
    bade = [f"{a}-{b}" for a, b in etas if (a, b) != ("30", "60")]
    if bade: fallas.append(f"eta {sorted(set(bade))}")
    badc = re.findall(r'#(?:0066cc|0284c7|0369a1|b91c1c|dc2626|ef4444)\b', html, re.I)
    if badc: fallas.append(f"color-off-brand {sorted(set(badc))}")
    if re.search(r'Ã|Â|�', html): fallas.append("mojibake")
    rows.append((rel, "OK" if not fallas else "FALLA " + "; ".join(fallas), len(blocks), nq))
ok = 0
for r in rows:
    print(" | ".join(str(x) for x in r))
    if len(r) > 1 and r[1] == "OK": ok += 1
print(f"TOTAL {ok}/{len(rows)} OK")
