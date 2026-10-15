#!/usr/bin/env python3
"""Comprobación de producción tras publicar (corrida 20261014-2100): HTTP 200 en URLs clave
+ UNA evidencia servida por tarea. Reintenta hasta 8 veces (15 s) a que Netlify despliegue.
T1: 4 tarjetas de blog de la home con la raíz/h3 nuevos. T2: contacto/ tel/mailto min-height:44px + 4 spans aria-hidden.
T3: minisplit con el enlace al post 110→220. T4: home tel min-height:44px + 4 li nuevos. Sitemap == worktree.
argv[1] = base alterna (p.ej. http://127.0.0.1:8097) para probar el script antes de publicar."""
import time, urllib.request, sys
B = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "https://electricistaculiacanpro.mx"
WT = "/tmp/equipo-electricista-20261014-2100"
def get(u):
    r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "equipo-check/1.0", "Cache-Control": "no-cache"}), timeout=20)
    return r.status, r.read().decode("utf-8", "replace")
T1 = [("instalacion-electrica-obsoleta-culiacan-420w.webp", "5 Señales de que tu Instalación Eléctrica está Obsoleta</a></h3>"),
      ("mantenimiento-tablero-electrico-culiacan-420w.webp", "Mantenimiento Preventivo de Tablero Eléctrico en Culiacán</a></h3>"),
      ("ahorro-energia-iluminacion-led-culiacan-420w.webp", "Ahorro de Energía con Iluminación LED en Culiacán</a></h3>"),
      ("prevenir-cortocircuitos-culiacan-420w.webp", "Cómo Evitar un Corto Circuito en Casa: 10 Medidas Clave</a></h3>")]
HOME = open(f"{WT}/index.html", encoding="utf-8").read()
checks = [("home 200 == worktree", "/", lambda h: h.strip() == HOME.strip()),
          ("T1 home: 4 tarjetas con raíz + h3 nuevos y 0 textos viejos", "/",
           lambda h: all(h.count(r) >= 1 and h.count(t) == 1 for r, t in T1) and "Ahorra hasta 30%" not in h and "Bajones de luz" not in h and 'alt="¿Cuándo Llamar a un Electricista de Emergencia?"' in h),
          ("T4 home: tel 44px + 4 li nuevos", "/",
           lambda h: 'text-decoration:underline;display:inline-flex;align-items:center;min-height:44px">(667) 392-2273</a>' in h
           and all(h.count(f'href="/servicios/{s}/"') == 1 for s in ["instalacion-minisplit", "mantenimiento-tableros", "instalacion-tierra-fisica", "instalacion-ventiladores-techo"])),
          ("T2 contacto: tel/mailto 44px + 4 spans aria-hidden", "/contacto/",
           lambda h: h.count('text-decoration:none;display:inline-flex;align-items:center;min-height:44px">') == 2 and h.count('<span aria-hidden="true">') >= 4
           and all(f'<span aria-hidden="true">{e}</span>' in h for e in ["📞", "💬", "📧", "📍"])),
          ("T3 minisplit: 1 enlace al post 110→220", "/servicios/instalacion-minisplit/",
           lambda h: h.count('href="/blog/cambio-110-a-220v-culiacan-cfe/"') == 1),
          ("T3 destino 200", "/blog/cambio-110-a-220v-culiacan-cfe/", lambda h: "<title>" in h),
          ("emergencia 200", "/servicios/emergencia-24-7/", lambda h: "<title>" in h),
          ("blog 200", "/blog/", lambda h: "<title>" in h)]
checks += [(f"T1 asset {r}", f"/assets/images/optimizadas/{r}", None) for r, _ in T1]
SITEMAP = open(f"{WT}/sitemap.xml", encoding="utf-8").read()
checks += [("sitemap.xml == worktree", "/sitemap.xml", lambda h: h.strip() == SITEMAP.strip())]
for intento in range(1, 9):
    res = []
    for name, path, fn in checks:
        try:
            if fn is None:
                r = urllib.request.urlopen(urllib.request.Request(B + path, headers={"User-Agent": "equipo-check/1.0"}), timeout=20)
                res.append((name, r.status == 200 and "image/webp" in r.headers.get("Content-Type", ""), r.status))
            else:
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
