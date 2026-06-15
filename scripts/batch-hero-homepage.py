#!/usr/bin/env python3
"""
Reemplaza la imagen hero de todas las paginas de servicio
con la misma imagen hero de la homepage.
"""
import re
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERVICIOS_DIR = os.path.join(BASE, "servicios")

SERVICE_PAGES = []
for entry in sorted(os.listdir(SERVICIOS_DIR)):
    path = os.path.join(SERVICIOS_DIR, entry, "index.html")
    if entry == "electricista-colonias-culiacan":
        continue
    if os.path.isfile(path):
        SERVICE_PAGES.append(path)

NEW_PICTURE = '''        <picture class="hero-background">
            <source type="image/avif"
                    srcset="../../assets/images/optimizadas/hero-electricista-culiacan-500w.avif 500w, ../../assets/images/optimizadas/hero-electricista-culiacan-800w.avif 800w, ../../assets/images/optimizadas/hero-electricista-culiacan-1200w.avif 1200w"
                    sizes="100vw">
            <source type="image/webp"
                    srcset="../../assets/images/optimizadas/hero-electricista-culiacan-500w.webp 500w, ../../assets/images/optimizadas/hero-electricista-culiacan-800w.webp 800w, ../../assets/images/optimizadas/hero-electricista-culiacan-1200w.webp 1200w"
                    sizes="100vw">
            <img src="../../assets/images/optimizadas/hero-electricista-culiacan-1200w.webp"
                 srcset="../../assets/images/optimizadas/hero-electricista-culiacan-500w.webp 500w, ../../assets/images/optimizadas/hero-electricista-culiacan-800w.webp 800w, ../../assets/images/optimizadas/hero-electricista-culiacan-1200w.webp 1200w"
                 sizes="100vw"
                 alt="Electricista profesional en Culiacan atendiendo emergencia 24 horas con herramientas especializadas"
                 width="1200"
                 height="800"
                 fetchpriority="high"
                 loading="eager"
                 decoding="async">
        </picture>'''

NEW_PRELOAD = '''    <link rel="preload" as="image"
          href="../../assets/images/optimizadas/hero-electricista-culiacan-1200w.webp"
          imagesrcset="../../assets/images/optimizadas/hero-electricista-culiacan-500w.webp 500w,
                       ../../assets/images/optimizadas/hero-electricista-culiacan-800w.webp 800w,
                       ../../assets/images/optimizadas/hero-electricista-culiacan-1200w.webp 1200w"
          imagesizes="100vw"
          fetchpriority="high">'''

PICTURE_RE = re.compile(
    r'[ \t]*<picture class="hero-background">.*?</picture>',
    re.DOTALL
)

PRELOAD_RE = re.compile(
    r'[ \t]*<link rel="preload" as="image"\s+href="[^"]*"'
    r'\s+imagesrcset="[^"]*"'
    r'\s+imagesizes="[^"]*"'
    r'\s+fetchpriority="high">',
    re.DOTALL
)

changed = 0
for page in SERVICE_PAGES:
    rel = os.path.relpath(page, BASE)
    with open(page, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = content

    match = PICTURE_RE.search(new_content)
    if match:
        new_content = new_content[:match.start()] + NEW_PICTURE + new_content[match.end():]
    else:
        print(f"  WARN: No <picture> hero found in {rel}")

    match = PRELOAD_RE.search(new_content)
    if match:
        new_content = new_content[:match.start()] + NEW_PRELOAD + new_content[match.end():]
    else:
        print(f"  WARN: No preload found in {rel}")

    if new_content != content:
        with open(page, "w", encoding="utf-8") as f:
            f.write(new_content)
        changed += 1
        print(f"  OK: {rel}")
    else:
        print(f"  SKIP (no changes): {rel}")

print(f"\nTotal: {changed} paginas actualizadas")
