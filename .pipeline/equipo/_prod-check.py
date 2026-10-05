#!/usr/bin/env python3
"""Comprobación de producción tras publicar (corrida 20261004-2100): HTTP 200 en URLs clave
+ UNA evidencia servida por tarea. Reintenta hasta 8 veces (15 s) a que Netlify despliegue."""
import re, time, urllib.request, sys
B = "https://electricistaculiacanpro.mx"
def get(u):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "equipo-check/1.0", "Cache-Control": "no-cache"}), timeout=20)
    return r.status, r.read().decode("utf-8", "replace")
RULE = ".btn-primary{display:inline-block;background:linear-gradient(135deg,#C2410C 0%,#7C2D12 100%);color:#fff;border:none;border-radius:12px;padding:16px 32px;font-weight:600;font-size:1rem;text-decoration:none;text-align:center;cursor:pointer;box-shadow:0 4px 16px rgba(227,100,20,.3);min-height:44px}"
checks = [
    ("home 200", "/", lambda h: True),
    ("emergencia 200", "/servicios/emergencia-24-7/", lambda h: True),
    ("T1 contacto: regla .btn-primary + .btn-whatsapp inline", "/contacto/",
     lambda h: h.count(RULE + ".btn-whatsapp{background:#075E54;") == 1),
    ("T1 /blog/: regla .btn-primary inline", "/blog/", lambda h: h.count(RULE) == 1),
    ("T2 apagones: title nuevo x6, viejo x0, dateModified", "/blog/apagones-culiacan-por-que-se-va-la-luz-que-hacer/",
     lambda h: h.count("Apagón eléctrico en Culiacán: por qué se va la luz y qué hacer") == 6 and "Apagón en Culiacán: por qué" not in h and '"dateModified": "2026-10-04"' in h),
    ("T3 LED: decisiones", "/blog/ahorro-energia-iluminacion-led/",
     lambda h: len(re.findall(r"mejores\s+decisiones para tu economía", h)) == 1 and not re.search(r"mejores\s+decisión ", h)),
    ("sitemap: 77 lastmod 2026-10-04", "/sitemap.xml", lambda h: h.count("<lastmod>2026-10-04</lastmod>") == 77),
]
for intento in range(1, 9):
    res = []
    for nombre, path, fn in checks:
        try:
            st, h = get(B + path)
            ok = st == 200 and fn(h)
        except Exception as e:
            st, ok = f"ERR {e}", False
        res.append((nombre, st, ok))
    bad = [r for r in res if not r[2]]
    print(f"intento {intento}: {len(res)-len(bad)}/{len(res)} OK")
    for r in res: print("  ", "OK " if r[2] else "FALLA", r[1], r[0])
    if not bad: sys.exit(0)
    time.sleep(15)
sys.exit(1)
