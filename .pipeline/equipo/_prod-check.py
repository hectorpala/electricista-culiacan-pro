#!/usr/bin/env python3
"""Comprobación de producción tras publicar (corrida 20261011-2246): HTTP 200 en URLs clave
+ UNA evidencia servida por tarea. Reintenta hasta 8 veces (15 s) a que Netlify despliegue."""
import time, urllib.request, sys, os
B = "https://electricistaculiacanpro.mx"
WT = "/tmp/equipo-electricista-20261011-2246"
def get(u, binary=False):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "equipo-check/1.0", "Cache-Control": "no-cache"}), timeout=20)
    b = r.read()
    return r.status, (b if binary else b.decode("utf-8", "replace")), r.headers.get("Content-Type", "")
LOGO = 'src="/assets/images/optimizadas/logo-256w.webp" srcset="/assets/images/optimizadas/logo-128w.webp 128w, /assets/images/optimizadas/logo-256w.webp 256w" sizes="(max-width:768px) 96px, 140px"'
FOOT = '<div class="footer-logo"><img loading="lazy" decoding="async" src="/assets/images/electricista-culiacan-pro-logo.webp" alt="Electricista Culiacán Pro" width="200" height="76"></div>'
TAP = ';display:inline-flex;align-items:center;min-height:44px'
T1 = {"ahorro-energia-iluminacion-led": "ahorro-energia-iluminacion-led-culiacan", "cambio-110-a-220v-culiacan-cfe": "blog-220v-culiacan",
      "como-prevenir-cortocircuitos-casa": "prevenir-cortocircuitos-culiacan", "olor-a-quemado-en-casa-que-hacer": "blog-olor-quemado-casa",
      "por-que-parpadean-las-luces-de-mi-casa": "blog-luces-parpadean", "seguridad-electrica-temporada-lluvias": "seguridad-electrica-temporada-lluvias-culiacan",
      "senales-instalacion-electrica-obsoleta": "instalacion-electrica-obsoleta-culiacan"}
T2 = ["gracias/", "contacto/", "servicios/", "servicios/electricista-colonias-culiacan/"]
T3 = ["contratacion-media-tension-cfe", "contrato-luz-medidor-cfe", "correccion-factor-de-potencia", "dictamen-electrico", "electricista-centro-culiacan",
      "electricista-cerca-de-mi", "electricista-comercial", "electricista-zona-norte-culiacan", "electricista-zona-oriente-culiacan", "electricista-zona-poniente-culiacan",
      "electricista-zona-sur-culiacan", "instalacion-bomba-agua", "instalacion-calentador-electrico", "instalacion-camaras-seguridad", "instalacion-cercas-electricas",
      "instalacion-electrica-bombeo-agricola", "instalacion-paneles-solares", "instalacion-planta-luz-generador", "instalacion-porton-electrico",
      "instalaciones-electricas-industriales", "mantenimiento-electrico-industrial", "no-hay-luz-en-parte-casa", "paneles-solares-empresas", "pararrayos-tierras-nom-022",
      "planta-emergencia-empresas", "proyecto-electrico-obra-nueva", "reparacion-minisplit", "subestaciones-electricas"]
checks = [("home 200", "/", lambda h, ct: True), ("emergencia 200", "/servicios/emergencia-24-7/", lambda h, ct: True), ("blog 200", "/blog/", lambda h, ct: True)]
checks += [(f"T1 /blog/{s}: avif ×2 en preload+source", f"/blog/{s}/", (lambda base: (lambda h, ct: h.count('type="image/avif"') == 2 and f"{base}-1200w.avif" in h and f"{base}-800w.avif 800w" in h))(b)) for s, b in T1.items()]
for b in T1.values():
    for w in ("800w", "1200w"):
        sz = os.path.getsize(f"{WT}/assets/images/optimizadas/{b}-{w}.avif")
        checks.append((f"T1 asset {b}-{w}.avif {sz} B image/avif", f"/assets/images/optimizadas/{b}-{w}.avif", (lambda sz: (lambda body, ct: len(body) == sz and "avif" in ct))(sz), True))
checks += [(f"T2 /{p}: nav logo 128/256w, 0 grande en nav", f"/{p}", lambda h, ct: h.count(LOGO) == 1 and 'src="/assets/images/electricista-culiacan-pro-logo.webp" alt' not in h.split("</nav>")[0]) for p in T2]
checks += [(f"T2 /{p}: footer-logo de la home", f"/{p}", lambda h, ct: h.count(FOOT) == 1) for p in ("contacto/", "servicios/")]
checks += [(f"T3 /servicios/{s}: 3 anclas tap44 en bloque contacto", f"/servicios/{s}/", lambda h, ct: h.split("<!-- Información de Contacto -->")[1].split("<!-- Formulario de Contacto -->")[0].count(TAP) == 3) for s in T3]
checks += [(f"T3 /blog/{s}: 3 anclas tap44", f"/blog/{s}/", lambda h, ct: h.split("<!-- Información de Contacto -->")[1].split("<!-- Formulario de Contacto -->")[0].count(TAP) == 3) for s in ("como-prevenir-cortocircuitos-casa", "senales-instalacion-electrica-obsoleta")]
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
