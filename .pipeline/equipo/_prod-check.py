#!/usr/bin/env python3
"""Comprobación de producción tras publicar (corrida 20261012-2100): HTTP 200 en URLs clave
+ UNA evidencia servida por tarea. Reintenta hasta 8 veces (15 s) a que Netlify despliegue.
T1: main.min.js servido == disco (parche del popup, 0 pushState) + ?v=20261012 en páginas + sw v40.
T2: 4 B2B con href a emergencia-24-7. T3: garantías 30-90 en tableros y LED. Sitemap == worktree."""
import time, urllib.request, sys, hashlib
B = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "https://electricistaculiacanpro.mx"   # argv[1] = base alterna (p.ej. http://127.0.0.1:8097) para probar el script
WT = "/tmp/equipo-electricista-20261012-2100"
def get(u, binary=False):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "equipo-check/1.0", "Cache-Control": "no-cache"}), timeout=20)
    b = r.read()
    return r.status, (b if binary else b.decode("utf-8", "replace")), r.headers.get("Content-Type", "")
JS = open(f"{WT}/main.min.js", "rb").read()
T2 = ["contratacion-media-tension-cfe", "correccion-factor-de-potencia", "paneles-solares-empresas", "proyecto-electrico-obra-nueva"]
TOK = lambda h: "main.min.js?v=20261012" in h and "main.min.js?v=20261004" not in h
checks = [("home 200 + main.min.js?v=20261012", "/", lambda h, ct: TOK(h)),
          ("emergencia 200 + ?v=20261012", "/servicios/emergencia-24-7/", lambda h, ct: TOK(h)),
          ("blog 200 (no carga main.min.js desde la base)", "/blog/", lambda h, ct: "main.min.js" not in h),
          ("contacto ?v=20261012 (ruta ../)", "/contacto/", lambda h, ct: TOK(h)),
          ("T1 main.min.js servido == disco, 0 pushState/popstate, wa.me ok", "/main.min.js?v=20261012",
           lambda b, ct: b == JS and b"pushState" not in b and b"popstate" not in b and b"wa.me/526673922273" in b and "javascript" in ct, True),
          ("T1 sw.js CACHE_VERSION v40 + precache ?v=20261012", "/sw.js", lambda h, ct: "CACHE_VERSION = 'v40'" in h and "main.min.js?v=20261012" in h)]
checks += [(f"T2 /servicios/{s}: 1 href a emergencia-24-7", f"/servicios/{s}/", lambda h, ct: h.count('href="/servicios/emergencia-24-7/"') == 1 and "Electricista 24 Horas" in h) for s in T2]
checks += [("T3 tableros: garantía 90 días, 0 '2 años'/'Extendida'", "/servicios/mantenimiento-tableros/",
            lambda h, ct: h.count("Sí, garantía de 90 días en mantenimiento, ajustes, cambio de breakers y cambio completo de tablero.") == 2 and "Garantía Extendida" not in h and "2 años" not in h and "<h3>Garantía por Escrito</h3>" in h),
           ("T3 LED: 30 a 90 días ×2, dateModified 2026-10-12", "/blog/ahorro-energia-iluminacion-led/",
            lambda h, ct: h.count("garantía por escrito de 30 a 90 días en mano de obra de instalación") == 2 and '"dateModified": "2026-10-12"' in h and "1 año de garantía" not in h)]
SITEMAP = open(f"{WT}/sitemap.xml", encoding="utf-8").read()
checks += [("sitemap.xml == worktree", "/sitemap.xml", lambda h, ct: h.strip() == SITEMAP.strip())]
for intento in range(1, 9):
    res = []
    for c in checks:
        name, path, fn = c[0], c[1], c[2]
        binary = len(c) > 3
        try:
            st, body, ct = get(B + path, binary)
            res.append((name, st == 200 and bool(fn(body, ct)), st))
        except Exception as e:
            res.append((name, False, str(e)[:60]))
    ok = sum(1 for r in res if r[1])
    print(f"intento {intento}: {ok}/{len(res)} OK")
    if ok == len(res): break
    for r in res:
        if not r[1]: print("   FALLA", r[0], r[2])
    time.sleep(15)
for r in res: print(("OK   " if r[1] else "FALLA"), r[0])
sys.exit(0 if ok == len(res) else 1)
