#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check-huecos.py — DETECTOR de páginas FALTANTES (enlaces internos a rutas que no existen).

Decisión del dueño (2026-07-08): cuando falte una página de servicio, el agente la CREA
solo, correctamente (generadores + candados). Este script es el sensor determinista de
"falta una página": encuentra todo destino interno enlazado desde el sitio cuyo archivo
NO existe en disco, rankeado por cuántas páginas lo referencian. La señal complementaria
(demanda GSC sin página) ya vive en la FASE 6 paso 1; la decisión crear-vs-quitar-enlace
la toma el decisor-negocio con NEGOCIO.md; la ejecución usa crear-servicio.py/gen-landing.py
y pasa por gate-pagina.py como siempre.

Cubre los 2 formatos de enlace del sitio: relativo (href="/servicios/x/") y ABSOLUTO del
propio dominio (href="https://electricistaculiacanpro.mx/servicios/" — así enlaza el
breadcrumb al hub; un detector solo-relativo NO lo ve, lección 2026-07-08).

Ignora: fragmentos (/#servicios), literales de plantilla JS (${...}/{{...}}, lección de
check-plantilla), y assets (css/js/img/fonts — esos los vigila check-plantilla; aquí solo
PÁGINAS). Exit 0 siempre (sensor, no candado).

Uso:
  python3 .pipeline/check-huecos.py            # reporte legible
  python3 .pipeline/check-huecos.py --json     # una línea JSON por hueco (para encolar)
"""
import glob
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMINIO = re.compile(r"^https?://(www\.)?electricistaculiacanpro\.mx", re.I)
EXT_ASSET = (".css", ".js", ".mjs", ".json", ".xml", ".txt", ".webmanifest", ".ico",
             ".png", ".jpg", ".jpeg", ".webp", ".avif", ".svg", ".gif",
             ".woff", ".woff2", ".ttf", ".pdf", ".mp4")


def destino_existe(ruta):
    """ruta ya sin dominio, sin / inicial ni final. '' = home."""
    if not ruta:
        return True
    abs_ = os.path.join(ROOT, ruta)
    # OJO: una CARPETA sin index.html es un 404 servido (caso hub servicios/ — 32 breadcrumbs
    # rotos que un os.path.exists() ingenuo daba por buenos). Solo cuenta un ARCHIVO real.
    return (os.path.exists(os.path.join(abs_, "index.html"))
            or os.path.isfile(abs_ + ".html")
            or os.path.isfile(abs_))


def main():
    as_json = "--json" in sys.argv
    referentes = defaultdict(set)
    paginas = [f for f in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)
               if "/node_modules/" not in f and "/.git/" not in f]
    for f in paginas:
        try:
            h = open(f, encoding="utf-8").read()
        except Exception:
            continue
        rel_f = os.path.relpath(f, ROOT)
        for m in re.finditer(r'href=["\']([^"\']+)["\']', h):
            u = m.group(1).strip()
            if "${" in u or "{{" in u:            # literal de plantilla JS, no un enlace real
                continue
            u = DOMINIO.sub("", u)                # absoluto del propio dominio → relativo
            if not u.startswith("/"):             # externo, mailto, tel, fragmento local
                continue
            u = u.split("#", 1)[0].split("?", 1)[0]
            if not u or u == "/":
                continue
            ruta = u.strip("/")
            if ruta.lower().endswith(EXT_ASSET):  # asset: lo vigila check-plantilla
                continue
            if not destino_existe(ruta):
                referentes[u if u.endswith("/") else u + "/"].add(rel_f)

    huecos = sorted(referentes.items(), key=lambda kv: -len(kv[1]))
    if as_json:
        for destino, refs in huecos:
            print(json.dumps({
                "destino": destino,
                "referentes": len(refs),
                "ejemplos": sorted(refs)[:3],
                "es_servicio": destino.startswith("/servicios/"),
            }, ensure_ascii=False))
    else:
        print("Detector de huecos — %d páginas escaneadas, %d destino(s) enlazados que NO existen:" % (
            len(paginas), len(huecos)))
        for destino, refs in huecos:
            print("  %4d páginas → %s   (ej: %s)" % (len(refs), destino, sorted(refs)[0]))
        if not huecos:
            print("  ✅ todos los enlaces internos apuntan a páginas existentes.")
    sys.exit(0)


if __name__ == "__main__":
    main()
