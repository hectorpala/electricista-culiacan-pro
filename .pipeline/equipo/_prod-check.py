#!/usr/bin/env python3
"""Comprobación de producción tras publicar (corrida 20260930-2100): HTTP 200 en URLs clave
+ UNA evidencia servida por tarea. Reintenta hasta 8 veces (15 s) a que Netlify despliegue."""
import re, time, urllib.request, sys
B = "https://electricistaculiacanpro.mx"
def get(u):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "equipo-check/1.0", "Cache-Control": "no-cache"}), timeout=20)
    return r.status, r.read().decode("utf-8", "replace")
checks = [
    ("home 200", "/", lambda h: True),
    ("emergencia 200", "/servicios/emergencia-24-7/", lambda h: True),
    ("T1 cuando-llamar: FAQ nueva x2, 0 garantizad, 0 20-40", "/blog/cuando-llamar-electricista-emergencia/",
     lambda h: h.count("30-60 minutos a emergencias eléctricas reales") == 2 and "garantizad" not in h and not re.search(r"20-40|40-60", h)),
    ("T1 cuando-llamar: dateModified 2026-09-30", "/blog/cuando-llamar-electricista-emergencia/", lambda h: '"dateModified": "2026-09-30"' in h),
    ("T1 lluvias: 0 garantizad + dateModified", "/blog/seguridad-electrica-temporada-lluvias/", lambda h: "garantizad" not in h and '"dateModified": "2026-09-30"' in h),
    ("T2 cerca-de-mi: 30-60 a Las Quintas, 0 cifras viejas", "/servicios/electricista-cerca-de-mi/",
     lambda h: "llegamos en 30-60 min a Las Quintas" in h and not re.search(r"30-40 min|25-35 min|35-45 min", h)),
    ("T2 a-domicilio: 30-60 según tráfico, 0 cifras viejas", "/servicios/electricista-a-domicilio/",
     lambda h: "con llegada en 30-60 minutos, según el tráfico y la zona" in h and not re.search(r"20 y 30|45-60", h)),
    ("T3 /blog/: 2 wa.me + ?text= propio + tel en header", "/blog/",
     lambda h: h.count("wa.me/526673922273") == 2 and "vengo%20del%20blog" in h and h.count('href="tel:+526673922273"') == 2),
    ("sitemap: 5 lastmod 2026-09-30", "/sitemap.xml", lambda h: h.count("<lastmod>2026-09-30</lastmod>") == 5),
]
for intento in range(1, 9):
    res = []
    for name, path, fn in checks:
        try:
            st, h = get(B + path)
            res.append((name, st == 200 and bool(fn(h)), st))
        except Exception as e:
            res.append((name, False, str(e)[:40]))
    ok = sum(1 for r in res if r[1])
    print(f"intento {intento}: {ok}/{len(res)} OK")
    if ok == len(res):
        for r in res: print("  ✅", r[0])
        sys.exit(0)
    if intento < 8: time.sleep(15)
for r in res: print("  ✅" if r[1] else "  ❌", r[0], r[2])
sys.exit(1)
