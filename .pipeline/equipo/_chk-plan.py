#!/usr/bin/env python3
"""Reproduce las líneas base del plan del pensador (corrida 20261007-2101)."""
import re, glob
WT = "/tmp/equipo-electricista-20261007-2101/"
TEL = 'href="tel:+526673922273" class="btn-secondary hover-lift"'
def rd(p): return open(WT + p, encoding="utf-8").read()
def hero(h): return h[h.find("<header"):h.find("</header>")]
print("== T1: tel en hero (debe ser 0) y wa.me en hero (1)")
for p in ["blog/apagones-culiacan-por-que-se-va-la-luz-que-hacer/index.html",
          "blog/cuanto-cuesta-electricista-culiacan/index.html",
          "blog/breaker-se-bota-causas-soluciones-culiacan/index.html"]:
    try:
        h = rd(p)
    except FileNotFoundError:
        print("  NO EXISTE", p); continue
    hh = hero(h)
    print(f"  {p}: tel-hero={hh.count(TEL)} wa-hero={hh.count('wa.me/526673922273')} btn-whatsapp={hh.count('btn-primary btn-whatsapp')} hero-content={hh.count('hero-content')}")
ref = [l for l in rd("blog/olor-a-quemado-en-casa-que-hacer/index.html").split("\n") if TEL in l]
print("  ref olor líneas con TEL:", len(ref), "| strip:", ref[0].strip()[:80] if ref else None)
print("== blogs breaker: slug real")
print("  ", [g.replace(WT, "") for g in glob.glob(WT + "blog/*breaker*")])
print("== T2: cadenas (deben ser 1 en visible; apagones href 0)")
a = rd("blog/cuando-llamar-electricista-emergencia/index.html")
b = rd("blog/seguridad-electrica-temporada-lluvias/index.html")
print("  emergencia: '<p>Una emergencia eléctrica real involucra'", a.count("<p>Una emergencia eléctrica real involucra"),
      "| 'apagones totales sin explicación'", a.count("apagones totales sin explicación"),
      "| href apagones", a.count('href="/blog/apagones-culiacan-por-que-se-va-la-luz-que-hacer/"'))
print("  lluvias: '<p>Sí, los apagones y fluctuaciones de voltaje'", b.count("<p>Sí, los apagones y fluctuaciones de voltaje"),
      "| href apagones", b.count('href="/blog/apagones-culiacan-por-que-se-va-la-luz-que-hacer/"'))
print("== T3: 3 cadenas en servicios/*")
S1 = '<p style="color:#475569;margin-bottom:1.5rem">Electricista a domicilio con llegada inmediata. Atención profesional en tu hogar o negocio.</p>'
S2 = '<p style="color:#475569;margin-bottom:1.5rem">Consulta los precios de servicios eléctricos. Cotizaciones claras y justas con factura incluida.</p>'
S3 = '<span style="color:#C2410C;font-weight:600">Ver precios →</span>'
rows = []
for p in sorted(glob.glob(WT + "servicios/*/index.html")):
    h = open(p, encoding="utf-8").read()
    c = (h.count(S1), h.count(S2), h.count(S3))
    if any(c): rows.append((p.replace(WT, ""), c))
for r in rows: print("  ", r)
print("  total páginas con alguna:", len(rows))
print("== respaldo destinos")
d = rd("servicios/electricista-a-domicilio/index.html"); pz = rd("servicios/electricista-precios/index.html")
print("  a-domicilio 'generalmente el mismo día':", d.count("generalmente el mismo día"))
print("  precios 'costo total antes de iniciar':", len(re.findall(r"costo total antes de iniciar", pz, re.I)), "| 'sin cargos ocultos':", len(re.findall(r"sin cargos ocultos", pz, re.I)), "| CFDI:", pz.count("CFDI"))
print("  'llegada inmediata' site-wide (html):", sum(open(g, encoding='utf-8').read().count('con llegada inmediata') for g in glob.glob(WT + '**/index.html', recursive=True)))
