#!/usr/bin/env python3
"""Comprobación de producción tras publicar (corrida 20261009-2100): HTTP 200 en URLs clave
+ UNA evidencia servida por tarea. Reintenta hasta 8 veces (15 s) a que Netlify despliegue."""
import time, urllib.request, sys
B = "https://electricistaculiacanpro.mx"
def get(u, binary=False):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "equipo-check/1.0", "Cache-Control": "no-cache"}), timeout=20)
    b = r.read()
    return r.status, (b if binary else b.decode("utf-8", "replace")), r.headers.get("Content-Type", "")
LOGO = 'src="/assets/images/optimizadas/logo-256w.webp" srcset="/assets/images/optimizadas/logo-128w.webp 128w, /assets/images/optimizadas/logo-256w.webp 256w" sizes="(max-width:768px) 96px, 140px"'
T1 = {"por-que-se-bota-el-breaker-pastilla-culiacan": "mantenimiento-tablero-electrico-culiacan-1200w", "mantenimiento-tablero-electrico-preventivo": "mantenimiento-tablero-electrico-culiacan-1200w",
      "apagones-culiacan-por-que-se-va-la-luz-que-hacer": "emergencia-electrica-culiacan-1200w", "cuando-llamar-electricista-emergencia": "emergencia-electrica-culiacan-1200w",
      "cuanto-cuesta-electricista-culiacan": "instalacion-minisplit-culiacan-800w", "recibo-luz-alto-culiacan-como-bajarlo": "instalacion-minisplit-culiacan-800w", "como-elegir-buen-electricista-culiacan": "instalacion-minisplit-culiacan-800w"}
T2 = ["", "ahorro-energia-iluminacion-led", "cambio-110-a-220v-culiacan-cfe", "como-prevenir-cortocircuitos-casa", "olor-a-quemado-en-casa-que-hacer", "por-que-parpadean-las-luces-de-mi-casa", "seguridad-electrica-temporada-lluvias", "senales-instalacion-electrica-obsoleta"]
AVIF = {"mantenimiento-tablero-electrico-culiacan-800w": 21935, "mantenimiento-tablero-electrico-culiacan-1200w": 35568, "emergencia-electrica-culiacan-800w": 16722, "emergencia-electrica-culiacan-1200w": 27681, "instalacion-minisplit-culiacan-800w": 19668}
checks = [("home 200", "/", lambda h, ct: True), ("emergencia 200", "/servicios/emergencia-24-7/", lambda h, ct: True)]
checks += [(f"T1 {s}: avif ×2 + logo", f"/blog/{s}/", (lambda base: (lambda h, ct: h.count("image/avif") == 2 and f"{base}.avif" in h and h.count(LOGO) == 1 and 'src="/assets/images/electricista-culiacan-pro-logo.webp"' not in h))(b)) for s, b in T1.items()]
checks += [(f"T2 /blog/{s}: logo 256w", f"/blog/{s}/" if s else "/blog/", lambda h, ct: h.count(LOGO) == 1 and 'src="/assets/images/electricista-culiacan-pro-logo.webp"' not in h) for s in T2]
checks += [(f"T1 asset {n}.avif {sz} B image/avif", f"/assets/images/optimizadas/{n}.avif", (lambda sz: (lambda b, ct: len(b) == sz and "avif" in ct))(sz), True) for n, sz in AVIF.items()]
checks += [("T3 home: 30 candidatos 420w + 3 tarjetas -420w", "/", lambda h, ct: h.count("420w.webp 420w") == 30 and 'srcset="/assets/images/optimizadas/mantenimiento-tablero-electrico-culiacan-800w.webp 800w" sizes=' not in h)]
checks += [("sitemap: 16 lastmod 2026-10-09", "/sitemap.xml", lambda h, ct: h.count("<lastmod>2026-10-09</lastmod>") == 16)]
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
