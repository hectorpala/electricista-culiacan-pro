#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""crear-servicio.py — Genera una página de SERVICIO nueva, con paridad de
plantilla garantizada y contenido único (anti-doorway).

Reusa el esqueleto `servicios/electricista-cerca-de-mi/index.html` (que ya trae
el hero de 2 botones estándar) y delega la sustitución estructural en
`.pipeline/gen-landing.py` (que aborta si algo no calza o hay fuga "plomero").

USO:
    python3 scripts/crear-servicio.py spec.json
    python3 scripts/crear-servicio.py --ejemplo > spec.json   # plantilla de spec

DESPUÉS de generar (lo recuerda al final):
    1) añadir la URL a sitemap.xml (priority 0.8)
    2) enlazarla desde la home (lista "Servicios de Electricidad" en index.html) + bump sw.js
    3) candado:  python3 .pipeline/gate-pagina.py servicios/<slug>/index.html
    4) publicar en rama + merge + push (el pre-push auto-indexa en GSC)

El spec es un JSON con el contenido ÚNICO del servicio (los campos de abajo).
TODO el resto de la página (head, CSS, scripts, footer, popup, botones) se hereda
idéntico del esqueleto.
"""
import json, os, sys, subprocess, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = "servicios/electricista-cerca-de-mi/index.html"

EJEMPLO = {
  "slug": "instalacion-ejemplo",
  "title": "Servicio de Ejemplo en Culiacán | 24/7",
  "desc": "Meta description ≤160 car. que vende y refleja la página.",
  "kw": "keyword1 culiacan, keyword2, keyword3",
  "ogt": "Título Open Graph del Servicio",
  "ogd": "⚡ Descripción OG/Twitter corta y vendedora.",
  "bc": "Nombre Corto (breadcrumb)",
  "svct": "Tipo de servicio (schema serviceType)",
  "svcn": "Nombre completo del servicio en Culiacán",
  "svcd": "Descripción larga del servicio para el JSON-LD (1-2 frases).",
  "h1": "H1 de la página (lo que promete)",
  "hsub": "Subtítulo del hero: el dolor del cliente + qué resolvemos + 24/7.",
  "bintro": "Intro de '¿por qué elegirnos?' (puede llevar <strong>). 4.8★...",
  "b1h": "Título del beneficio #1",
  "b1p": "Párrafo del beneficio #1 (específico del servicio).",
  "sh2": "H2 de la sección de servicios",
  "ctah": "Título del CTA de cierre (pregunta de dolor)",
  "ctap": "Párrafo del CTA de cierre.",
  "appst": "Título del bloque 'lo que hacemos'",
  "appsi": "Intro del bloque 'lo que hacemos'",
  "apps": ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"],
  "appsn": "¿Tu caso no aparece?",
  "testi": [
    ["Testimonio 1 (específico, creíble)", "Nombre A.", "Colonia", "Servicio prestado"],
    ["Testimonio 2", "Nombre B.", "Colonia", "Servicio"],
    ["Testimonio 3", "Nombre C.", "Colonia", "Servicio"]
  ],
  "faqs": [
    ["¿Pregunta real pre-llamada 1?", "Respuesta concreta, sin evasivas."],
    ["¿Pregunta 2?", "Respuesta."],
    ["¿Pregunta 3?", "Respuesta."],
    ["¿Pregunta 4?", "Respuesta."],
    ["¿Atienden de urgencia 24/7?", "Sí, ..."]
  ],
  "maps": "Caption del mapa: servicio en Las Quintas, Tres Ríos, Centro y toda Culiacán.",
  "cob": "Culiacán y zona metropolitana"
}


def _js(s): return json.dumps(s, ensure_ascii=False)


def build_spec(z, skel):
    import re
    def faq_jsonld(faqs):
        items=['            {\n              "@type": "Question",\n              "name": %s,\n              "acceptedAnswer": {\n                "@type": "Answer",\n                "text": %s\n              }\n            }'%(_js(q),_js(a)) for q,a in faqs]
        return '"mainEntity": [\n'+',\n'.join(items)+'\n          ]'
    def faq_html(faqs):
        return '\n'.join('                <details style="background:#fff;padding:1.5rem;margin-bottom:1rem;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1);border-left:4px solid var(--brand)">\n                    <summary style="font-weight:700;color:var(--brand);cursor:pointer;font-size:1.05rem">%s</summary>\n                    <p style="margin-top:1rem;color:#475569;line-height:1.7">%s</p>\n                </details>'%(html.escape(q),html.escape(a)) for q,a in faqs)
    def testi(q,n,col,s):
        return '                <div class="card">\n                    <div class="rating-stars" style="color:#FBBC04;font-size:1.25rem;margin-bottom:1rem">★★★★★</div>\n                    <p style="font-style:italic;margin-bottom:1rem;color:#475569">"%s"</p>\n                    <cite style="font-weight:700;color:var(--brand);font-style:normal">- %s, %s</cite>\n                    <p style="font-size:0.9rem;color:#64748B;margin-top:0.5rem">Servicio: %s</p>\n                </div>'%(html.escape(q),html.escape(n),html.escape(col),html.escape(s))
    def apps_block(t,i,items,n):
        cards='\n                    '.join('<div style="background:#fff;padding:1rem;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.08);color:var(--brand);font-weight:600">%s</div>'%html.escape(x) for x in items)
        return ('    <!-- Zonas de Servicio -->\n    <section class="section" style="background:#F8FAFC">\n        <div class="container">\n            <h2>%s</h2>\n            <div style="max-width:900px;margin:0 auto;text-align:center">\n                <p style="font-size:1.125rem;color:#475569;margin-bottom:2rem">%s</p>\n                <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-bottom:2rem">\n                    %s\n                </div>\n                <p style="color:#64748B;font-size:1rem">%s <a href="https://wa.me/526673922273?text=Hola,%%20necesito%%20cotizar%%20este%%20servicio" style="color:var(--brand);font-weight:600;text-decoration:none" target="_blank" rel="noopener">Contáctanos por WhatsApp</a> y te cotizamos.</p>\n            </div>\n        </div>\n    </section>'%(html.escape(t),html.escape(i),cards,html.escape(n)))
    FAQ_OLD=re.search(r'("mainEntity": \[\n.*?\n          \])\n        \}\n      \]\n    \}\n    </script>',skel,re.S).group(1)
    ZONAS_OLD=re.search(r'    <!-- Zonas de Servicio -->\n.*?\n    </section>',skel,re.S).group(0)
    m3=re.search(r'(    <!-- Testimonios Section -->\n.*?<div class="grid">\n)(.*?)(\n            </div>\n        </div>\n    </section>)',skel,re.S)
    TPRE,TPOST=m3.group(1),m3.group(3); TESTI_OLD=m3.group(1)+m3.group(2)+m3.group(3)
    m4=re.search(r'(            <h2>Preguntas Frecuentes</h2>\n            <div style="max-width:800px;margin:2rem auto">\n)(.*?)(\n            </div>\n        </div>\n    </section>)',skel,re.S)
    FPRE,FPOST=m4.group(1),m4.group(3); FAQH_OLD=m4.group(1)+m4.group(2)+m4.group(3)
    reps=[
     {"old":"electricista-cerca-de-mi","new":z["slug"],"n":8},
     {"old":'<title>Electricista Cerca de Ti en Culiacán 24/7 | 30-60 Min</title>',"new":'<title>%s</title>'%html.escape(z["title"])},
     {"old":'<meta name="description" content="¿Buscas electricista cerca de ti en Culiacán? Vamos a domicilio 24 h con llegada en 30-60 min. Técnico certificado ★4.8. Cotiza gratis por WhatsApp.">',"new":'<meta name="description" content="%s">'%html.escape(z["desc"])},
     {"old":'<meta name="keywords" content="electricista cerca de mi, electricista cerca de mi ubicacion, electricistas cerca de mi ubicación, electricista cerca, electrico cerca de mi ubicacion, electricista a domicilio cerca de mi, tecnico electricista, electricista culiacan">',"new":'<meta name="keywords" content="%s">'%html.escape(z["kw"])},
     {"old":'content="Electricista Cerca de Mí en Culiacán | Servicio Inmediato"',"new":'content="%s"'%html.escape(z["ogt"]),"n":2},
     {"old":'content="⚡ Electricista cerca de ti en Culiacán. Emergencia 24/7, llegada 30-60 min. Cotización gratis por WhatsApp."',"new":'content="%s"'%html.escape(z["ogd"]),"n":2},
     {"old":'"name": "Electricista Cerca de Mí",\n              "item"',"new":'"name": "%s",\n              "item"'%z["bc"]},
     {"old":'"serviceType": "Electricista de Proximidad",',"new":'"serviceType": "%s",'%z["svct"]},
     {"old":'"name": "Electricista Cerca de Mí en Culiacán",',"new":'"name": "%s",'%z["svcn"]},
     {"old":'"description": "Electricista certificado con cobertura completa en todas las colonias de Culiacán. Llegada rápida en 30-60 minutos, atención de emergencias 24/7, servicio profesional cerca de tu ubicación.",',"new":'"description": %s,'%_js(z["svcd"])},
     {"old":FAQ_OLD,"new":faq_jsonld(z["faqs"])},
     {"old":'<span class="breadcrumb-current" itemprop="name">Electricista Cerca de Mí</span>',"new":'<span class="breadcrumb-current" itemprop="name">%s</span>'%html.escape(z["bc"])},
     {"old":'<h1>¿Buscas Electricista Cerca de Ti en Culiacán? Llegamos Rápido</h1>',"new":'<h1>%s</h1>'%html.escape(z["h1"])},
     {"old":'<p class="hero-subtitle">Electricista certificado con cobertura completa en todas las colonias de Culiacán. Llegada en 30-60 minutos para emergencias, servicio 24/7, atención inmediata por WhatsApp. Estamos cerca de Las Quintas, Tres Ríos, Chapultepec, Guadalupe, Montebello, Centro y toda la ciudad.</p>',"new":'<p class="hero-subtitle">%s</p>'%html.escape(z["hsub"])},
     {"old":'Electricista certificado cerca de ti en Culiacán. <strong>4.8★ en Google</strong> • Servicio 24/7 todos los días.',"new":z["bintro"]},
     {"old":'<h3>Cobertura Completa en Culiacán</h3>',"new":'<h3>%s</h3>'%html.escape(z["b1h"])},
     {"old":'<p>Electricista cerca de ti en más de 30 colonias de Culiacán. Zona norte, centro, sur y oriente. Sin importar tu ubicación, llegamos rápido: Las Quintas 30-40 min, Centro 25-35 min, Villa Universidad 35-45 min.</p>',"new":'<p>%s</p>'%html.escape(z["b1p"])},
     {"old":'<h2>Servicios de Electricista Cerca de Ti</h2>',"new":'<h2>%s</h2>'%html.escape(z["sh2"])},
     {"old":'<h2 style="color:#FFF;margin-bottom:1.5rem">¿Necesitas un Electricista Cerca de Ti AHORA?</h2>',"new":'<h2 style="color:#FFF;margin-bottom:1.5rem">%s</h2>'%html.escape(z["ctah"])},
     {"old":'<p style="font-size:1.125rem;margin-bottom:2rem;line-height:1.7">Si tienes una emergencia eléctrica, no esperes más. Contáctanos por WhatsApp y te confirmamos tiempo exacto de llegada a tu ubicación. Electricista certificado en camino en menos de 60 minutos a la mayoría de las colonias de Culiacán.</p>',"new":'<p style="font-size:1.125rem;margin-bottom:2rem;line-height:1.7">%s</p>'%html.escape(z["ctap"])},
     {"old":'📍 Solicitar Electricista Cerca de Mí',"new":'📍 Solicitar Servicio'},
     {"old":ZONAS_OLD,"new":apps_block(z["appst"],z["appsi"],z["apps"],z["appsn"])},
     {"old":TESTI_OLD,"new":TPRE+'\n'.join(testi(*t) for t in z["testi"])+TPOST},
     {"old":FAQH_OLD,"new":FPRE+faq_html(z["faqs"])+FPOST},
     {"old":'<p style="text-align:center;margin-top:1.5rem;color:#64748B">Electricista cerca de ti en Las Quintas, Tres Ríos, Guadalupe, Centro y todas las colonias de Culiacán.</p>',"new":'<p style="text-align:center;margin-top:1.5rem;color:#64748B">%s</p>'%html.escape(z["maps"])},
     {"old":'<br>Culiacán y zona metropolitana',"new":'<br>%s'%html.escape(z["cob"])},
    ]
    return {"skeleton":SK,"output":"servicios/%s/index.html"%z["slug"],"replacements":reps}


def main():
    if len(sys.argv)<2 or sys.argv[1] in ("-h","--help"):
        print(__doc__); sys.exit(0)
    if sys.argv[1]=="--ejemplo":
        print(json.dumps(EJEMPLO, ensure_ascii=False, indent=2)); sys.exit(0)
    z=json.load(open(sys.argv[1],encoding="utf-8"))
    skel=open(os.path.join(ROOT,SK),encoding="utf-8").read()
    spec=build_spec(z,skel)
    r=subprocess.run([sys.executable,os.path.join(ROOT,".pipeline/gen-landing.py"),"-"],
                     input=json.dumps(spec),capture_output=True,text=True,cwd=ROOT)
    print(r.stdout.strip() or r.stderr.strip())
    if r.returncode==0:
        print("\nSIGUIENTE:")
        print("  1) sitemap.xml  + <url><loc>.../servicios/%s/</loc> ... priority 0.8"%z["slug"])
        print("  2) enlazar desde index.html (lista Servicios de Electricidad) + bump sw.js")
        print("  3) python3 .pipeline/gate-pagina.py servicios/%s/index.html"%z["slug"])
        print("  4) rama + merge --no-ff + PATH=/usr/local/bin git push  (auto-indexa)")
    sys.exit(r.returncode)


if __name__=="__main__":
    main()
