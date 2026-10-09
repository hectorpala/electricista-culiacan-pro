#!/usr/bin/env python3
"""Reproduce las líneas base del plan del pensador (corrida 20261008-2100)."""
import re, os, hashlib, collections, glob
WT = "/tmp/equipo-electricista-20261008-2100/"
def rd(p): return open(WT + p, encoding="utf-8", errors="ignore").read()
print("== T1: 3 hojas CSS")
for f in ["styles.css", "styles.min.css", "styles.7f293647.css"]:
    s = rd(f)
    print(f" {f}: md5={hashlib.md5(s.encode()).hexdigest()} nav-menu={s.count('.nav-menu')} overflow-en-nav-menu={len(re.findall(r'\.nav-menu[^{]*\{[^}]*overflow', s))} contiene-regla-nueva={s.count('overflow-y:auto;overscroll-behavior:contain')}")
print(" sw.js:", re.search(r"CACHE_VERSION\s*=\s*'([^']+)'", rd("sw.js")).group(1))
c = collections.Counter()
inline_overflow = 0
for d, ds, fs in os.walk(WT):
    if any(x in d for x in ("/.git", "/.pipeline", "/node_modules", "/.claude")): continue
    for f in fs:
        if f.endswith(".html"):
            h = open(os.path.join(d, f), encoding="utf-8", errors="ignore").read()
            for t in set(re.findall(r"styles[.a-z0-9]*\.css\?v=([0-9]+)", h)): c[t] += 1
            if re.search(r"\.nav-menu[^{]*\{[^}]*overflow", h): inline_overflow += 1
print(" ?v= por token:", dict(c), "| páginas con overflow inline en .nav-menu:", inline_overflow)
ct = rd("contacto/index.html").split("\n")
print(" contacto l13-14:", [l.strip()[:90] for l in ct[12:14]])
print("== T2: '800w.webp 420w'")
hits = [g.replace(WT, "") for g in glob.glob(WT + "**/index.html", recursive=True) if re.search(r"800w\.webp 420w", open(g, encoding="utf-8", errors="ignore").read())]
print(" páginas:", hits)
for a in ["mantenimiento-tablero-electrico-culiacan", "prevenir-cortocircuitos-culiacan"]:
    for w in ("420w", "800w"):
        p = WT + f"assets/images/optimizadas/{a}-{w}.webp"
        print(f" {a}-{w}.webp:", os.path.getsize(p) if os.path.exists(p) else "NO EXISTE")
print("== T3: gracias/")
g = rd("gracias/index.html")
print(" regla inline presente:", g.count("min-height:44px}.btn-whatsapp{background:#075E54"), "| a.btn-primary:", len(re.findall(r'<a[^>]+class="btn-primary', g)), "| noindex:", g.count('name="robots" content="noindex, follow"'))
print(" termina style l26:", g.split("\n")[25].strip()[-120:] if len(g.split("\n")) > 25 else "?")
cc = rd("contacto/index.html")
print(" contacto tiene la regla:", cc.count("min-height:44px}.btn-whatsapp{background:#075E54"))
