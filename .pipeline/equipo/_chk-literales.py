#!/usr/bin/env python3
"""Cotejo del coordinador: cada literal viejo de T2/T3/T4/T5 aparece exactamente 1 vez."""
WT = "/tmp/equipo-electricista-20261014-2100"
C = {
    "contacto/index.html": [
        '<a href="tel:+526673922273" style="color:#C2410C;text-decoration:none">667 392 2273</a>',
        '<a href="mailto:contacto@electricistaculiacanpro.mx" style="color:#C2410C;text-decoration:none">',
        '>📞 Teléfono</h3>', '>💬 WhatsApp</h3>', '>📧 Email</h3>', '>📍 Ubicación</h3>'],
    "servicios/instalacion-minisplit/index.html": [
        'Evita gastos innecesarios por instalaciones mal dimensionadas.</p>',
        'href="/blog/cambio-110-a-220v-culiacan-cfe/"'],
    "servicios/contrato-luz-medidor-cfe/index.html": ['href="/blog/cambio-110-a-220v-culiacan-cfe/"'],
    "index.html": [
        '<p><strong>Teléfono:</strong> <a href="tel:+526673922273" style="color:inherit;font-weight:600;text-decoration:underline">(667) 392-2273</a></p>',
        '<li><a href="/servicios/reparacion-minisplit/">Reparación de minisplit</a></li>',
        '#lista-servicios-seo li a{display:inline-flex;align-items:center;min-height:44px}'],
}
for f, lits in C.items():
    h = open(f"{WT}/{f}", encoding="utf-8").read()
    for l in lits:
        print(h.count(l), f, l[:70])
import re
h = open(f"{WT}/servicios/contrato-luz-medidor-cfe/index.html", encoding="utf-8").read()
m = re.search(r'<p>[^<]*<a href="/blog/cambio-110-a-220v-culiacan-cfe/"[^>]*>[^<]*</a>[^<]*</p>', h)
print("precedente:", m.group(0) if m else None)
