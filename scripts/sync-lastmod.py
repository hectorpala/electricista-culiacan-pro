#!/usr/bin/env python3
"""Sincroniza <lastmod> de sitemap.xml y sitemap_index.xml con la fecha real
del ultimo commit de cada pagina en disco (o con hoy si tiene cambios sin
commitear). Idempotente: correrlo varias veces seguidas no cambia nada mas.

Uso:
    python3 scripts/sync-lastmod.py            # escribe los cambios
    python3 scripts/sync-lastmod.py --check    # solo compara, no escribe

Reglas duras que respeta (REGLAS.md):
- [2026-06-21] OPERACION/MOJIBAKE: edicion con Python + UTF-8 explicito,
  jamas sed/perl con caracteres acentuados.
- [2026-06-23] INFRA/PORT-CHECKER-CIEGO: nunca devolver "todo limpio" en
  silencio si algo no se pudo inspeccionar; cualquier <loc> que no resuelva
  a un archivo en disco (o entrada desconocida en sitemap_index.xml) se
  reporta explicitamente como error, no se ignora.

El script SOLO reescribe el contenido de las etiquetas <lastmod>...</lastmod>
(via regex sobre el texto), preservando byte a byte todo lo demas: no
reordena, ni anade, ni quita <loc>/<changefreq>/<priority>, ni re-serializa
el XML con ElementTree.
"""
from __future__ import annotations

import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
SITEMAP = REPO_ROOT / "sitemap.xml"
SITEMAP_INDEX = REPO_ROOT / "sitemap_index.xml"
SITEMAP_IMAGES_RELPATH = "sitemap-images.xml"

URL_BLOCK_RE = re.compile(r"<url>.*?</url>", re.DOTALL)
SITEMAP_ENTRY_RE = re.compile(r"<sitemap>.*?</sitemap>", re.DOTALL)
LOC_RE = re.compile(r"<loc>(.*?)</loc>")
LASTMOD_RE = re.compile(r"<lastmod>(.*?)</lastmod>")


def loc_to_relpath(loc: str) -> str:
    """https://dominio/<rel>/ -> <rel>/index.html ; la raiz -> index.html"""
    path = urlparse(loc).path
    rel = path.strip("/")
    if rel == "":
        return "index.html"
    return f"{rel}/index.html"


def _run_git(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


def git_last_commit_date(relpath: str) -> str | None:
    """Fecha (YYYY-MM-DD, %cs) del ultimo commit que toco relpath, o None
    si el archivo nunca se ha commiteado."""
    result = _run_git(["log", "-1", "--format=%cs", "--", relpath])
    date = result.stdout.strip()
    return date or None


def has_uncommitted_changes(relpath: str) -> bool:
    result = _run_git(["status", "--porcelain", "--", relpath])
    return bool(result.stdout.strip())


def resolve_lastmod(relpath: str, today: str) -> tuple[str | None, str | None]:
    """Devuelve (fecha, error). Si error no es None, no se pudo resolver
    una fecha confiable (nunca se devuelve una fecha inventada junto a un
    error silencioso)."""
    abspath = REPO_ROOT / relpath
    if not abspath.exists():
        return None, f"no existe en disco: {relpath}"
    if has_uncommitted_changes(relpath):
        return today, None
    date = git_last_commit_date(relpath)
    if date is None:
        # Existe pero nunca se ha commiteado: usar hoy (no hay historial real).
        return today, None
    return date, None


def sync_sitemap_xml(text: str, today: str) -> tuple[str, list[dict]]:
    resultados: list[dict] = []

    def repl(match: re.Match) -> str:
        block = match.group(0)
        loc_match = LOC_RE.search(block)
        if not loc_match:
            resultados.append(
                {
                    "loc": None,
                    "relpath": None,
                    "actual": None,
                    "esperado": None,
                    "error": "bloque <url> sin <loc>",
                }
            )
            return block

        loc = loc_match.group(1)
        relpath = loc_to_relpath(loc)
        esperado, error = resolve_lastmod(relpath, today)
        lastmod_match = LASTMOD_RE.search(block)
        actual = lastmod_match.group(1) if lastmod_match else None

        resultados.append(
            {
                "loc": loc,
                "relpath": relpath,
                "actual": actual,
                "esperado": esperado,
                "error": error or (None if lastmod_match else "bloque <url> sin <lastmod>"),
            }
        )

        if error is not None or lastmod_match is None or esperado is None:
            return block
        return block[: lastmod_match.start(1)] + esperado + block[lastmod_match.end(1) :]

    nuevo_texto = URL_BLOCK_RE.sub(repl, text)
    return nuevo_texto, resultados


def sync_sitemap_index(
    text: str, max_lastmod_sitemap: str, images_lastmod: str | None, images_error: str | None
) -> tuple[str, list[dict]]:
    resultados: list[dict] = []

    def repl(match: re.Match) -> str:
        block = match.group(0)
        loc_match = LOC_RE.search(block)
        loc = loc_match.group(1) if loc_match else None
        lastmod_match = LASTMOD_RE.search(block)
        actual = lastmod_match.group(1) if lastmod_match else None

        if loc and loc.endswith("/sitemap.xml"):
            esperado, error = max_lastmod_sitemap, None
        elif loc and loc.endswith("/sitemap-images.xml"):
            esperado, error = images_lastmod, images_error
        elif loc is None:
            esperado, error = None, "bloque <sitemap> sin <loc>"
        else:
            # PORT-CHECKER-CIEGO: entrada desconocida -> se reporta, no se
            # ignora en silencio ni se le inventa una fecha.
            esperado, error = None, f"entrada de sitemap_index.xml no reconocida: {loc}"

        resultados.append(
            {"loc": loc, "relpath": None, "actual": actual, "esperado": esperado, "error": error}
        )

        if error is not None or lastmod_match is None or esperado is None:
            return block
        return block[: lastmod_match.start(1)] + esperado + block[lastmod_match.end(1) :]

    nuevo_texto = SITEMAP_ENTRY_RE.sub(repl, text)
    return nuevo_texto, resultados


def _desync(resultados: list[dict]) -> list[dict]:
    return [r for r in resultados if r["error"] or r["actual"] != r["esperado"]]


def _print_resultado(nombre_archivo: str, resultados: list[dict]) -> bool:
    """Imprime el resumen de un archivo y devuelve True si esta al dia."""
    desync = _desync(resultados)
    total = len(resultados)
    ok = total - len(desync)
    if not desync:
        print(f"OK {ok}/{total} lastmod al dia ({nombre_archivo})")
        return True
    print(f"DESINCRONIZADO {ok}/{total} lastmod al dia ({nombre_archivo}):")
    for r in desync:
        print(
            f"  {r['loc']} -> actual={r['actual']!r} esperado={r['esperado']!r}"
            + (f" error={r['error']}" if r["error"] else "")
        )
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="solo compara, no escribe; sale 1 si algo esta desincronizado"
    )
    args = parser.parse_args()

    today = datetime.date.today().isoformat()

    sitemap_text = SITEMAP.read_text(encoding="utf-8")
    nuevo_sitemap_text, resultados_sitemap = sync_sitemap_xml(sitemap_text, today)

    fechas_validas = [r["esperado"] for r in resultados_sitemap if r["esperado"]]
    max_lastmod_sitemap = max(fechas_validas) if fechas_validas else today

    images_lastmod, images_error = resolve_lastmod(SITEMAP_IMAGES_RELPATH, today)

    index_text = SITEMAP_INDEX.read_text(encoding="utf-8")
    nuevo_index_text, resultados_index = sync_sitemap_index(
        index_text, max_lastmod_sitemap, images_lastmod, images_error
    )

    if args.check:
        ok_sitemap = _print_resultado("sitemap.xml", resultados_sitemap)
        ok_index = _print_resultado("sitemap_index.xml", resultados_index)
        return 0 if (ok_sitemap and ok_index) else 1

    for r in resultados_sitemap + resultados_index:
        if r["error"]:
            print(f"AVISO: {r['loc']}: {r['error']}", file=sys.stderr)

    SITEMAP.write_text(nuevo_sitemap_text, encoding="utf-8")
    SITEMAP_INDEX.write_text(nuevo_index_text, encoding="utf-8")

    escritos_sitemap = sum(1 for r in resultados_sitemap if not r["error"])
    escritos_index = sum(1 for r in resultados_index if not r["error"])
    print(f"sitemap.xml: {escritos_sitemap}/{len(resultados_sitemap)} lastmod sincronizados")
    print(f"sitemap_index.xml: {escritos_index}/{len(resultados_index)} lastmod sincronizados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
