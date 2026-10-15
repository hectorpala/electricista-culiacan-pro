#!/usr/bin/env python3
"""Cotejo del coordinador del plan 20261014: T1 (tarjetas de blog de la home) y T5 (lista de servicios)."""
import re, os
WT = "/tmp/equipo-electricista-20261014-2100"
h = open(WT + "/index.html", encoding="utf-8").read()
E = {'senales-instalacion-electrica-obsoleta': 'instalacion-electrica-obsoleta-culiacan',
     'mantenimiento-tablero-electrico-preventivo': 'mantenimiento-tablero-electrico-culiacan',
     'ahorro-energia-iluminacion-led': 'ahorro-energia-iluminacion-led-culiacan',
     'como-prevenir-cortocircuitos-casa': 'prevenir-cortocircuitos-culiacan',
     'cuando-llamar-electricista-emergencia': 'emergencia-electrica-culiacan'}
for s, root in E.items():
    j = h.find('href="./blog/' + s + '/"')
    a = h[h.rfind('<article', 0, j):h.find('</article>', j)]
    srcs = re.findall(r'(?:src|srcset)="([^"]+)"', a)
    post = open(f"{WT}/blog/{s}/index.html", encoding="utf-8").read()
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', post, re.S)
    h1 = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else None
    hero = re.search(r'rel="preload" as="image"[^>]*href="([^"]+)"', post)
    ex = [os.path.exists(f"{WT}/assets/images/optimizadas/{root}-{w}w.webp") for w in (420, 800, 1200)]
    print(s, "\n  card srcs:", srcs, "\n  H1:", h1, "\n  post preload:", hero.group(1) if hero else None, "\n  variantes 420/800/1200:", ex)
bi = open(WT + "/blog/index.html", encoding="utf-8").read()
for s, root in E.items():
    j = bi.find('/blog/' + s + '/')
    a = bi[bi.rfind('<article', 0, j):bi.find('</article>', j)] if j > 0 else ''
    print("blog/index card", s, re.findall(r'src="([^"]+)"', a)[:1], re.findall(r'<h3[^>]*>.*?>(.*?)</a>', a, re.S)[:1])
u = re.search(r'<ul id="lista-servicios-seo">(.*?)</ul>', h, re.S).group(1)
print("lista li:", u.count('<li><a '), "enlaces home a 4 destinos:",
      [h.count('href="/servicios/' + s + '/"') for s in ['instalacion-minisplit', 'mantenimiento-tableros', 'instalacion-tierra-fisica', 'instalacion-ventiladores-techo']])
print(re.findall(r'<li><a href="/servicios/[^"]+">[^<]+</a></li>', u))
