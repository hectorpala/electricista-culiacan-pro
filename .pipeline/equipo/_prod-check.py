#!/usr/bin/env python3
"""Comprobación de producción tras publicar (corrida 20261008-2100): HTTP 200 en URLs clave
+ UNA evidencia servida por tarea. Reintenta hasta 8 veces (15 s) a que Netlify despliegue."""
import time, urllib.request, sys
B = "https://electricistaculiacanpro.mx"
def get(u):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "equipo-check/1.0", "Cache-Control": "no-cache"}), timeout=20)
    return r.status, r.read().decode("utf-8", "replace")
RULE = "@media (max-width:768px){.nav-menu{overflow-y:auto;overscroll-behavior:contain}}"
BTN = "min-height:44px}.btn-whatsapp{background:#075E54"
def bump(h): return h.count("styles.7f293647.css?v=20261008") >= 2 and "?v=20260923" not in h
def t2(h): return "800w.webp 420w" not in h and h.count("-420w.webp 420w") >= 1
T2 = ["ahorro-energia-iluminacion-led", "seguridad-electrica-temporada-lluvias", "cuando-llamar-electricista-emergencia",
      "senales-instalacion-electrica-obsoleta", "mantenimiento-tablero-electrico-preventivo"]
checks = [
    ("home 200 + ?v=20261008", "/", bump),
    ("emergencia 200 + ?v=20261008", "/servicios/emergencia-24-7/", bump),
    ("blog 200 + ?v=20261008", "/blog/", bump),
    ("contacto 200 + ?v=20261008", "/contacto/", bump),
    ("T1 CSS servido con la regla", "/styles.7f293647.css?v=20261008", lambda h: h.count(RULE) == 1),
    ("T1 sw.js v37", "/sw.js", lambda h: "CACHE_VERSION = 'v37'" in h and "?v=20261008" in h),
] + [(f"T2 {s}: 420w real", f"/blog/{s}/", lambda h: t2(h) and bump(h)) for s in T2] + [
    ("T3 gracias: regla inline", "/gracias/", lambda h: h.count(BTN) == 1 and bump(h)),
    ("sitemap: 80 lastmod 2026-10-08", "/sitemap.xml", lambda h: h.count("<lastmod>2026-10-08</lastmod>") == 80),
]
for intento in range(1, 9):
    res = []
    for nombre, path, fn in checks:
        try:
            st, h = get(B + path)
            res.append((nombre, st, fn(h)))
        except Exception as e:
            res.append((nombre, "ERR " + str(e)[:60], False))
    ok = all(st == 200 and v for _, st, v in res)
    print(f"intento {intento}: {sum(1 for _, s, v in res if s == 200 and v)}/{len(res)}")
    if ok:
        break
    time.sleep(15)
for r in res:
    print(" ", "OK " if (r[1] == 200 and r[2]) else "FAIL", r[0], r[1])
sys.exit(0 if ok else 1)
