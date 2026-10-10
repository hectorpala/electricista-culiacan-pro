#!/usr/bin/env python3
"""Reproduce las líneas base del plan del pensador (corrida 20261009-2100)."""
import re, os, glob, shutil, subprocess
WT = "/tmp/equipo-electricista-20261009-2100/"
def rd(p): return open(WT + p, encoding="utf-8", errors="ignore").read()
print("== herramientas:", {t: shutil.which(t) for t in ["dwebp", "avifenc", "magick", "sips", "avifdec"]})
home = rd("index.html")
print("== home preload (l.5-12):")
for l in home.split("\n")[4:12]: print("  ", l.strip()[:200])
print("== home <source avif>:", re.findall(r'<source type="image/avif"[^>]*>', home)[:2])
m = re.search(r'<img[^>]*logo-256w\.webp[^>]*>', home); print("== home logo:", m.group(0)[:300] if m else None)
d = WT + "assets/images/optimizadas/"
for n in ["logo-128w.webp", "logo-256w.webp"] + [f"{b}-{w}.webp" for b in ["mantenimiento-tablero-electrico-culiacan", "emergencia-electrica-culiacan", "instalacion-minisplit-culiacan"] for w in ("420w", "800w", "1200w")]:
    print(f"  {n}: {os.path.getsize(d+n) if os.path.exists(d+n) else 'NO EXISTE'}")
print("== avif existentes:", len(glob.glob(d + "*.avif")), glob.glob(d + "*.avif")[:6])
print("== sw.js precache logo:", rd("sw.js").count("logo-128w"), rd("sw.js").count("logo-256w"))
print("== home '420w.webp 420w':", len(re.findall(r"420w\.webp 420w", home)))
print("== news-grid en una línea:", home.count('class="news-grid"'), [i for i, l in enumerate(home.split("\n"), 1) if 'class="news-grid"' in l])
for s in ['srcset="/assets/images/optimizadas/mantenimiento-tablero-electrico-culiacan-800w.webp 800w" sizes=',
          '<img src="/assets/images/optimizadas/mantenimiento-tablero-electrico-culiacan-800w.webp" alt="Por qué se bota el breaker',
          'srcset="/assets/images/optimizadas/emergencia-electrica-culiacan-800w.webp 800w" sizes=',
          '<img src="/assets/images/optimizadas/emergencia-electrica-culiacan-800w.webp" alt="Apagón eléctrico en Culiacán',
          'srcset="/assets/images/optimizadas/instalacion-minisplit-culiacan-800w.webp 800w" sizes=',
          '<img src="/assets/images/optimizadas/instalacion-minisplit-culiacan-800w.webp" alt="Recibo de luz alto']:
    print("  T3 count", home.count(s), s[:70])
print("== blogs: logo-literal / image-avif / preload-webp-hero")
for f in sorted(glob.glob(WT + "blog/**/index.html", recursive=True)):
    h = open(f, encoding="utf-8", errors="ignore").read()
    pre = re.findall(r'<link rel="preload" as="image"[^>]*>', h)
    print(f"  {h.count('src=\"/assets/images/electricista-culiacan-pro-logo.webp\"')} {h.count('image/avif')} {len(pre)} {f.replace(WT,'')} :: {pre[0][:150] if pre else '-'}")
print("== otras páginas con el logo 512:", sum(1 for f in glob.glob(WT + "**/index.html", recursive=True) if 'src="/assets/images/electricista-culiacan-pro-logo.webp"' in open(f, encoding="utf-8", errors="ignore").read()))
