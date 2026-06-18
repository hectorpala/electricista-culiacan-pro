#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""diferenciar-colonia.py — Promueve una página de colonia de noindex (doorway)
a indexable, dándole contenido ÚNICO real para que NO sea doorway.

Hace 4 cosas sobre servicios/electricista-colonias-culiacan/<slug>/index.html:
  1) flip  <meta robots noindex> -> index, follow
  2) reemplaza la meta description de plantilla por una ÚNICA de esa colonia
  3) inyecta la sección "Electricidad en <Colonia>: lo que debes saber"
     (3 párrafos propios + "Problemas eléctricos comunes" + "Servicios más solicitados")
  4) arregla el item 3 del BreadcrumbList (le pone su URL propia)

USO:
    python3 scripts/diferenciar-colonia.py spec.json
    python3 scripts/diferenciar-colonia.py --ejemplo > spec.json

DESPUÉS (recordatorio al final):
    1) agregar al sitemap.xml (priority 0.6)
    2) python3 .pipeline/gate-pagina.py servicios/electricista-colonias-culiacan/<slug>/index.html
       (el candado anti-doorway DEBE quedar Jaccard < 0.80 vs hermanas; si no, hazla más única)
    3) rama + merge + push

REGLAS (ver REGLAS.md): el contenido de cada colonia debe ser genuinamente distinto
(zona real, tipo de casas, necesidades eléctricas propias). NO inventes geografía falsa.
Solo diferencia colonias con demanda; NO promuevas 626 doorways de golpe.
"""
import json, os, re, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASEURL = "https://electricistaculiacanpro.mx/servicios/electricista-colonias-culiacan/"
DESC_OLD = re.compile(r'Electricista profesional en [^."]*\. Emergencias 24/7 con llegada en 30-60 min\. Cotización gratis por WhatsApp\. Llama al 667 392 2273\. ★4\.8 en reseñas\.')

EJEMPLO = {
  "slug": "nombre-colonia",
  "nombre": "Nombre Colonia",
  "meta": "Electricista en Nombre Colonia, Culiacán: <servicios clave de esa colonia>. Servicio 24/7, llegada 30-60 min.",
  "p1": "Qué ES la colonia: zona (norte/sur/oriente/poniente/centro), tipo de casas/época, carácter (popular/residencial/comercial). REAL y específico.",
  "p2": "Qué se pide MÁS ahí (según el tipo de casa) y el ETA. Específico de la colonia.",
  "p3": "Un ángulo extra ÚNICO (un problema típico de esa zona, una recomendación, una referencia local segura). NO reciclar p1.",
  "problemas": ["Problema eléctrico típico 1", "Problema 2", "Problema 3", "Problema 4"],
  "servicios": ["Servicio 1", "Servicio 2", "Servicio 3", "Servicio 4"]
}


def seccion(nom, p1, p2, p3, probs, servs):
    pli = "".join("<li>%s</li>" % html.escape(x) for x in probs)
    sli = "".join("<li>%s</li>" % html.escape(x) for x in servs)
    return ('<section class="section">\n  <div class="container">\n'
            '    <h2>Electricidad en %s: lo que debes saber</h2>\n'
            '    <p>%s</p>\n    <p>%s</p>\n    <p>%s</p>\n'
            '    <h3>Problemas eléctricos comunes en %s</h3>\n    <ul class="servicios-zona">%s</ul>\n'
            '    <h3>Servicios más solicitados en %s</h3>\n    <ul class="servicios-zona">%s</ul>\n'
            '  </div>\n</section>\n\n'
            % (html.escape(nom), html.escape(p1), html.escape(p2), html.escape(p3),
               html.escape(nom), pli, html.escape(nom), sli))


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    if sys.argv[1] == "--ejemplo":
        print(json.dumps(EJEMPLO, ensure_ascii=False, indent=2)); sys.exit(0)
    z = json.load(open(sys.argv[1], encoding="utf-8"))
    slug = z["slug"]
    f = os.path.join(ROOT, "servicios/electricista-colonias-culiacan", slug, "index.html")
    if not os.path.isfile(f):
        sys.exit("❌ no existe la colonia: %s" % slug)
    h = open(f, encoding="utf-8").read()
    if "lo que debes saber" in h:
        sys.exit("⚠️ ya diferenciada (tiene 'lo que debes saber'): %s" % slug)

    # 1) robots
    h2 = h.replace('<meta name="robots" content="noindex, follow">',
                   '<meta name="robots" content="index, follow">', 1)
    if h2 == h:
        sys.exit("❌ no se encontró <meta robots noindex> en %s" % slug)
    h = h2
    # 2) meta única (meta + og + twitter, todas las que usen la plantilla)
    n_meta = len(DESC_OLD.findall(h))
    h = DESC_OLD.sub(html.escape(z["meta"]), h)
    # 3) inyectar sección única antes del bloque final-cta
    fc = h.find('class="final-cta"')
    if fc < 0:
        sys.exit("❌ no se encontró el bloque final-cta en %s" % slug)
    ss = h.rfind('<section', 0, fc)
    h = h[:ss] + seccion(z["nombre"], z["p1"], z["p2"], z["p3"], z["problemas"], z["servicios"]) + h[ss:]
    # 4) breadcrumb item 3 con URL propia
    h = re.sub(r'(\{"@type": "ListItem", "position": 3, "name": "[^"]*")\}',
               r'\1, "item": "%s%s/"}' % (BASEURL, slug), h, count=1)

    open(f, "w", encoding="utf-8").write(h)
    print("✅ %s diferenciada e indexable (meta única x%d + sección + breadcrumb)" % (slug, n_meta))
    print("\nSIGUIENTE:")
    print("  1) sitemap.xml + <url><loc>%s%s/</loc> ... priority 0.6" % (BASEURL, slug))
    print("  2) python3 .pipeline/gate-pagina.py servicios/electricista-colonias-culiacan/%s/index.html" % slug)
    print("     (anti-doorway Jaccard < 0.80 vs hermanas; si no, hazla más única)")
    print("  3) rama + merge --no-ff + push")


if __name__ == "__main__":
    main()
