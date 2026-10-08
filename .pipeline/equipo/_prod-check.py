#!/usr/bin/env python3
"""Comprobación de producción tras publicar (corrida 20261007-2101): HTTP 200 en URLs clave
+ UNA evidencia servida por tarea. Reintenta hasta 8 veces (15 s) a que Netlify despliegue."""
import time, urllib.request, sys
B = "https://electricistaculiacanpro.mx"
def get(u):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "equipo-check/1.0", "Cache-Control": "no-cache"}), timeout=20)
    return r.status, r.read().decode("utf-8", "replace")
TEL = '<a href="tel:+526673922273" class="btn-secondary hover-lift" style="display:inline-flex;align-items:center;justify-content:center;gap:.5rem;background:#fff;color:#C2410C;border:2px solid #C2410C;padding:15px 32px;border-radius:14px;text-decoration:none;font-weight:700;min-height:48px;margin:.75rem .5rem 0"><span><strong>Llamar:</strong> 667 392 2273</span></a>'
HREF = 'href="/blog/apagones-culiacan-por-que-se-va-la-luz-que-hacer/"'
def t1(h):
    hdr = h[h.find('<header'):h.find('</header>')]
    return hdr.count(TEL) == 1 and hdr.count('wa.me/526673922273') == 1
def t2(h): return h.count(HREF) == 1
def t3(h):
    return (h.count("generalmente el mismo día.</p>") == 1 and h.count("factura electrónica (CFDI).</p>") == 1
            and h.count("Ver cómo cotizamos →") == 1 and "con llegada inmediata" not in h and "Ver precios →" not in h)
T3 = ["electricista-cerca-de-mi", "electricista-zona-norte-culiacan", "electricista-zona-sur-culiacan", "electricista-zona-oriente-culiacan",
      "electricista-zona-poniente-culiacan", "electricista-centro-culiacan", "electricista-comercial", "instalacion-calentador-electrico",
      "instalacion-porton-electrico", "contrato-luz-medidor-cfe", "instalacion-planta-luz-generador", "instalacion-paneles-solares",
      "instalacion-cercas-electricas", "reparacion-minisplit", "dictamen-electrico", "no-hay-luz-en-parte-casa"]
checks = [
    ("home 200", "/", lambda h: True),
    ("emergencia 200", "/servicios/emergencia-24-7/", lambda h: True),
    ("blog 200", "/blog/", lambda h: True),
    ("T1 apagones: Llamar en el hero", "/blog/apagones-culiacan-por-que-se-va-la-luz-que-hacer/", t1),
    ("T1 cuanto-cuesta: Llamar en el hero", "/blog/cuanto-cuesta-electricista-culiacan/", t1),
    ("T1 breaker: Llamar en el hero", "/blog/por-que-se-bota-el-breaker-pastilla-culiacan/", t1),
    ("T2 cuando-llamar: href apagones x1", "/blog/cuando-llamar-electricista-emergencia/", t2),
    ("T2 lluvias: href apagones x1", "/blog/seguridad-electrica-temporada-lluvias/", t2),
] + [(f"T3 {s}: tarjetas nuevas", f"/servicios/{s}/", t3) for s in T3] + [
    ("sitemap: 21 lastmod 2026-10-07", "/sitemap.xml", lambda h: h.count("<lastmod>2026-10-07</lastmod>") == 21),
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
