#!/usr/bin/env python3
"""Comprobación de producción tras publicar (corrida 20261015-2100): HTTP 200 en URLs clave
+ UNA evidencia servida por tarea. Reintenta hasta 8 veces (15 s) a que Netlify despliegue.
T1: home con la regla color:#1e40af en #lista-servicios-seo y #zonas. T2: 30 páginas con los 6 enlaces del mini-nav con min-height:44px.
T3: 3 servicios con el enlace al post (quemado / parpadean). T4: post LED sin "recibo de luz hasta 80%", blog/index, iluminacion-led, home l.857.
T5: minisplit con "garantía por escrito de 30 a 90 días" y sin "certificada". Sitemap == worktree.
argv[1] = base alterna (p.ej. http://127.0.0.1:8097) para probar el script antes de publicar."""
import time, urllib.request, sys, re
B = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "https://electricistaculiacanpro.mx"
WT = "/tmp/equipo-electricista-20261015-2100"
def get(u):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "equipo-check/1.0", "Cache-Control": "no-cache"}), timeout=20)
    return r.status, r.read().decode("utf-8", "replace")
T2 = ["mantenimiento-electrico-industrial", "correccion-factor-de-potencia", "instalacion-electrica-bombeo-agricola", "electricista-centro-culiacan", "reparacion-minisplit", "electricista-zona-norte-culiacan", "instalacion-calentador-electrico", "instalacion-camaras-seguridad", "proyecto-electrico-obra-nueva", "electricista-comercial", "no-hay-luz-en-parte-casa", "instalacion-bomba-agua", "planta-emergencia-empresas", "instalacion-planta-luz-generador", "contratacion-media-tension-cfe", "instalaciones-electricas-industriales", "instalacion-cercas-electricas", "instalacion-paneles-solares", "dictamen-electrico", "subestaciones-electricas", "electricista-zona-oriente-culiacan", "instalacion-porton-electrico", "electricista-cerca-de-mi", "contrato-luz-medidor-cfe", "paneles-solares-empresas", "electricista-zona-sur-culiacan", "electricista-zona-poniente-culiacan", "pararrayos-tierras-nom-022"]
MN = re.compile(r'<!-- Mini Nav -->.*?</nav>', re.S)
def mininav_ok(h):
    m = MN.search(h)
    if not m: return False
    seg = m.group(0)
    return len(re.findall(r'<a ', seg)) == 6 and seg.count("min-height:44px;min-width:44px") == 6
checks = [("T1 home: regla color #1e40af en lista + zonas", "/",
           lambda h: '#lista-servicios-seo li a{display:inline-flex;align-items:center;min-height:44px;color:#1e40af}#zonas .zones-content p:not(.zones-question) a{color:#1e40af}' in h),
          ("T4 home: tarjeta LED sin 'recibo de luz'", "/",
           lambda h: "Focos LED de calidad que consumen hasta 80% menos energía que los incandescentes." in h and "Ahorra hasta 80% en tu recibo de luz" not in h),
          ("T3 cortocircuitos: enlace al post quemado", "/servicios/reparacion-cortocircuitos/", lambda h: h.count('href="/blog/olor-a-quemado-en-casa-que-hacer/"') == 1),
          ("T3 emergencia: enlace al post quemado", "/servicios/emergencia-24-7/", lambda h: h.count('href="/blog/olor-a-quemado-en-casa-que-hacer/"') == 1),
          ("T3 tableros: enlace al post parpadean", "/servicios/mantenimiento-tableros/", lambda h: h.count('href="/blog/por-que-parpadean-las-luces-de-mi-casa/"') == 1),
          ("T3 destino quemado 200", "/blog/olor-a-quemado-en-casa-que-hacer/", lambda h: "<title>" in h),
          ("T3 destino parpadean 200", "/blog/por-que-parpadean-las-luces-de-mi-casa/", lambda h: "<title>" in h),
          ("T4 post LED", "/blog/ahorro-energia-iluminacion-led/",
           lambda h: "recibo de luz hasta 80" not in h and h.count("mano de obra profesional y garantía por escrito") == 2 and '"dateModified": "2026-10-15"' in h and "<h3>Hasta 80% menos consumo en iluminación</h3>" in h),
          ("T4 blog/index tarjeta LED", "/blog/", lambda h: "recibo de luz hasta 80" not in h and "Cuánto puedes reducir tu recibo de luz con iluminación LED, qué focos elegir" in h),
          ("T4 iluminacion-led hero", "/servicios/iluminacion-led/", lambda h: "Consume hasta 80% menos energía que un foco incandescente" in h and "Ahorra hasta 80% en tu recibo de luz" not in h),
          ("T5 minisplit", "/servicios/instalacion-minisplit/",
           lambda h: h.count("con garantía por escrito de 30 a 90 días</span>") == 1 and "Instalación a norma en 3 horas promedio" in h and len(re.findall("certificad", h)) == 2)]
checks += [(f"T2 mininav 44 {s}", f"/servicios/{s}/", mininav_ok) for s in T2]
checks += [(f"T2 mininav 44 blog {s}", f"/blog/{s}/", mininav_ok) for s in ["como-prevenir-cortocircuitos-casa", "senales-instalacion-electrica-obsoleta"]]
SITEMAP = open(f"{WT}/sitemap.xml", encoding="utf-8").read()
checks += [("sitemap.xml == worktree", "/sitemap.xml", lambda h: h.strip() == SITEMAP.strip())]
for intento in range(1, 9):
    res = []
    for name, path, fn in checks:
        try:
            st, body = get(B + path)
            res.append((name, st == 200 and bool(fn(body)), st))
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
