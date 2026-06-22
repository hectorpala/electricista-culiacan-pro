#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""auto-fixers.py — REGISTRO de arreglos MECÁNICOS conocidos (la apuesta del 90%).

Portado del sitio hermano y CALIBRADO a la marca de electricistaculiacanpro.mx
(NARANJA + AZUL): el azul es de marca aquí, así que un azul fuera-de-marca se
remapea al AZUL DE MARCA (#1e40af), NO a naranja. Email/theme-color son los de
este sitio.

Filosofía: detectar ya lo hacen los check-*.py; lo que faltaba es APLICAR el fix en vez de
diferirlo. Cada fixer es una receta ESTRECHA y determinista (NO "que el LLM arregle lo que sea"):
detecta un patrón conocido → aplica el fix exacto. Lo MECÁNICO se drena sin límite; lo grande
(reestructuras, claims de negocio, precios, borrar páginas) NO vive aquí.

Cada fixer respeta el SCOPE: p.ej. og:url solo en páginas INDEXABLES (una noindex no lo necesita).

Uso:
  python3 .pipeline/auto-fixers.py list                      # lista los fixers
  python3 .pipeline/auto-fixers.py run                       # DRY-RUN sobre todo el sitio (no escribe)
  python3 .pipeline/auto-fixers.py run --apply               # aplica y escribe
  python3 .pipeline/auto-fixers.py run --solo og-url [paths] # un fixer / rutas concretas
"""
import datetime
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CORRECT_EMAIL = "contacto@electricistaculiacanpro.mx"
BRAND_THEME = "#E36414"   # theme-color de la home (fuente de verdad)


def es_noindex(h):
    return bool(re.search(r'<meta[^>]+name=["\']robots["\'][^>]*noindex', h, re.I))


def canonical_de(h):
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', h, re.I)
    return m.group(1) if m else None


# ── Cada fixer: (id, descripcion, riesgo, detecta(h)->bool, arregla(h)->(h, n)) ──

def _det_ogurl(h):
    return (not es_noindex(h)) and canonical_de(h) and 'property="og:url"' not in h and "property='og:url'" not in h

def _fix_ogurl(h):
    can = canonical_de(h)
    def repl(m):
        return m.group(0) + "\n" + m.group(1) + '<meta property="og:url" content="%s">' % can
    return re.subn(r'(^[ \t]*)<link[^>]+rel=["\']canonical["\'][^>]*>', repl, h, count=1, flags=re.I | re.M)


def _det_theme(h):
    return '#0066cc' in h and 'name="theme-color"' in h

def _fix_theme(h):
    return re.subn(r'(name=["\']theme-color["\'][^>]*content=["\'])#0066cc', r'\g<1>' + BRAND_THEME, h, flags=re.I)


# Email contaminado de la plantilla ORIGEN (cualquier email con "plomero" en el dominio)
def _det_email(h):
    return bool(re.search(r'[\w.%+-]+@[\w.-]*plomero[\w.-]*', h, re.I))

def _fix_email(h):
    return re.subn(r'[\w.%+-]+@[\w.-]*plomero[\w.-]*', CORRECT_EMAIL, h, flags=re.I)


_ROBOTS = '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">'

def _det_robots(h):
    return (not es_noindex(h)) and canonical_de(h) and not re.search(r'<meta[^>]+name=["\']robots["\']', h, re.I)

def _fix_robots(h):
    def repl(m):
        return m.group(1) + _ROBOTS + "\n" + m.group(0)
    return re.subn(r'(^[ \t]*)<link[^>]+rel=["\']canonical["\'][^>]*>', repl, h, count=1, flags=re.I | re.M)


# ── color off-brand → paleta de marca (NARANJA + AZUL). CALIBRADO: el azul que NO es de
#    marca se remapea al AZUL DE MARCA (#1e40af); rojo/morado → naranja #C2410C; verde
#    decorativo → verde de marca #22c55e; fondos claros → tinte naranja #FFF7ED.
#    CONSERVA: azules de marca #1e40af/#0f4fa8/#1a73e8/#0d3f8a, #22c55e, WhatsApp
#    #25d366/#128c7e, logo Google #4285f4/#ea4335/#34a853/#fbbc05, grises slate.
#    Espejo del check 11b de check-plantilla.py. ──
_COLOR_LIGHT_BG = ("#e0f2fe", "#f0f9ff", "#bae6fd", "#e8f4fd", "#f0f8ff",
                   "#fef2f2", "#dcfce7", "#f0fdf4", "#ecfdf5")                 # → tinte naranja
_COLOR_BLUE = ("#0066cc", "#0284c7", "#0369a1", "#004499", "#0c4a6e",
               "#0ea5e9", "#075985", "#1a5276", "#2c3e50")                    # azul-no-marca → azul de marca
_COLOR_RED_PURPLE = ("#667eea", "#764ba2", "#dc2626", "#dc3545", "#b91c1c", "#991b1b")  # → naranja
_COLOR_GREEN = ("#059669", "#166534", "#16a34a", "#28a745", "#10b981")        # verde decorativo → verde de marca
_COLOR_OFFBRAND = _COLOR_LIGHT_BG + _COLOR_BLUE + _COLOR_RED_PURPLE + _COLOR_GREEN

def _det_color(h):
    low = h.lower()
    return any(c in low for c in _COLOR_OFFBRAND)

def _fix_color(h):
    n = 0
    for c in _COLOR_LIGHT_BG:
        h, k = re.subn(re.escape(c), "#FFF7ED", h, flags=re.I); n += k
    for c in _COLOR_BLUE:
        h, k = re.subn(re.escape(c), "#1e40af", h, flags=re.I); n += k
    for c in _COLOR_RED_PURPLE:
        h, k = re.subn(re.escape(c), "#C2410C", h, flags=re.I); n += k
    for c in _COLOR_GREEN:
        h, k = re.subn(re.escape(c), "#22c55e", h, flags=re.I); n += k
    return h, n


FIXERS = [
    ("og-url", "og:url faltante en página indexable → copia el canonical (scope: solo indexables)",
     "mecanico", _det_ogurl, _fix_ogurl),
    ("theme-color", "theme-color placeholder #0066cc → color de marca " + BRAND_THEME,
     "mecanico", _det_theme, _fix_theme),
    ("email", "email contaminado con 'plomero' → " + CORRECT_EMAIL,
     "mecanico", _det_email, _fix_email),
    ("meta-robots", "página indexable sin <meta name=robots> → añade el estándar index,follow (scope: indexables)",
     "mecanico", _det_robots, _fix_robots),
    ("color-off-brand", "color off-brand (azul-no-marca/morado/rojo/verde decorativo) → paleta de marca; azul→#1e40af, rojo→#C2410C, verde→#22c55e; conserva azul de marca/WhatsApp/Google",
     "mecanico", _det_color, _fix_color),
]


# ──────────────────── ASSET FIXERS (CSS/JS COMPARTIDO, no por página) ────────────────────
# Operan UNA vez sobre los assets compartidos (los 3 CSS) en vez de por página HTML. Cuando
# tocan CSS, bumpean el ?v= en las páginas que lo referencian + CACHE_VERSION de sw.js — el CSS
# se sirve `immutable`, así que cambiar el contenido NO basta: hay que cambiar la URL (el ?v=).
# Riesgo mecánico → auto, sin límite.
CSS_FILES = ["styles.css", "styles.min.css", "styles.7f293647.css"]
SW_FILE = "sw.js"

# Selectores interactivos que DEBEN ser tap-target ≥44px en móvil. Ampliar cuando un revisor a11y
# encuentre uno nuevo. El electricista usa `.breadcrumb-link`; se incluye el del hermano por si acaso.
TAP_SELECTORS = [".breadcrumb-link", ".breadcrumb-item a"]


def _bump_sw():
    """Sube CACHE_VERSION 'vN' → 'vN+1' en sw.js (cache-busting de 1 archivo)."""
    p = os.path.join(ROOT, SW_FILE)
    try:
        s = open(p, encoding="utf-8").read()
    except Exception:
        return 0
    def repl(m):
        return "%s%d%s" % (m.group(1), int(m.group(2)) + 1, m.group(3))
    nuevo, n = re.subn(r"(CACHE_VERSION\s*=\s*['\"]v)(\d+)(['\"])", repl, s, count=1)
    if n:
        open(p, "w", encoding="utf-8").write(nuevo)
    return n


def _bump_css_version_html(version):
    """Sube el token `styles*.css?v=AAAAMMDD` a `version` en TODAS las páginas HTML. OBLIGATORIO
    al cambiar un CSS: se sirve `immutable`, el visitante que regresa solo re-pide el CSS si CAMBIA
    la URL. Reemplazo literal del token de fecha → seguro. Devuelve nº de páginas tocadas."""
    n_files = 0
    htmls = sorted(set(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)))
    for p in htmls:
        if "/node_modules/" in p or "/.git/" in p:
            continue
        try:
            s = open(p, encoding="utf-8").read()
        except Exception:
            continue
        s2, k = re.subn(r'(styles[\w.]*\.css\?v=)\d{8}', r'\g<1>' + version, s)
        if k:
            open(p, "w", encoding="utf-8").write(s2)
            n_files += 1
    return n_files


def _fix_tap_target(css):
    """Garantiza min-height:44px + inline-flex centrado en cada TAP_SELECTORS. Idempotente.
    Solo toca reglas STANDALONE (inicio o tras `}`), nunca un selector embebido en un grupo."""
    n = 0
    for sel in TAP_SELECTORS:
        pat = re.compile(r"(^|\})(" + re.escape(sel) + r")\{([^}]*)\}", re.M)
        m = pat.search(css)
        if not m:
            continue
        decl = m.group(3)
        if "min-height:44px" in decl.replace(" ", ""):
            continue
        nuevo = decl
        if "display:inline-flex" not in nuevo.replace(" ", ""):
            nuevo = re.sub(r"display:\s*inline-block", "display:inline-flex;align-items:center", nuevo)
            if "display:inline-flex" not in nuevo.replace(" ", ""):
                nuevo = "display:inline-flex;align-items:center;" + nuevo
        nuevo = "min-height:44px;" + nuevo
        css = css[:m.start()] + m.group(1) + sel + "{" + nuevo + "}" + css[m.end():]
        n += 1
    return css, n


ASSET_FIXERS = [
    ("tap-target-44",
     "tap target <44px en selectores interactivos compartidos (migas) → min-height:44px en los 3 CSS + bump ?v=/sw.js",
     "mecanico", _fix_tap_target),
]


def cmd_run_assets(apply, solo=None):
    """Corre los ASSET_FIXERS sobre los 3 CSS; si alguno toca CSS y se aplica, bumpea ?v= + sw.js."""
    fixers = [f for f in ASSET_FIXERS if (solo is None or f[0] == solo)]
    if not fixers:
        return 0
    total, css_tocado, lineas = 0, False, []
    for fid, _, _, fix in fixers:
        for css_name in CSS_FILES:
            p = os.path.join(ROOT, css_name)
            try:
                s = open(p, encoding="utf-8").read()
            except Exception:
                continue
            s2, n = fix(s)
            if n:
                total += n
                css_tocado = True
                if apply:
                    open(p, "w", encoding="utf-8").write(s2)
                lineas.append("  %s %s → %s×%d%s" % (
                    "✅" if apply else "○", css_name, fid, n, "" if apply else " (dry-run)"))
    if lineas:
        print("ASSET fixers (CSS compartido):")
        for ln in lineas:
            print(ln)
        if css_tocado and apply:
            hoy = datetime.date.today().strftime("%Y%m%d")
            np = _bump_css_version_html(hoy)
            print("  ✅ ?v=%s bumpeado en %d página(s) (rompe el cache immutable del CSS)" % (hoy, np))
            nb = _bump_sw()
            print("  ✅ %s → CACHE_VERSION +1" % SW_FILE if nb else "  ⚠️  no pude bumpear %s" % SW_FILE)
        elif css_tocado:
            print("  (con --apply: bumpea ?v= en las páginas + sw.js — necesario por el cache immutable)")
    return total


def paginas_default():
    pats = [
        "index.html",
        "*/index.html",                        # secciones top-level (contacto, precios, blog…)
        "servicios/*/index.html",
        "servicios/*/*/index.html",            # colonias bajo cualquier subdir de servicios
        "blog/*/index.html",
    ]
    out = []
    for p in pats:
        out += glob.glob(os.path.join(ROOT, p))
    return sorted(set(out))


def cmd_list():
    print("Auto-fixers registrados (todos riesgo MECÁNICO → auto, sin límite):")
    print(" PÁGINA (HTML, por archivo):")
    for fid, desc, riesgo, _, _ in FIXERS:
        print("  • %-14s %s" % (fid, desc))
    print(" ASSET (CSS/JS compartido, una vez + bump ?v=/sw.js):")
    for fid, desc, riesgo, _ in ASSET_FIXERS:
        print("  • %-14s %s" % (fid, desc))
    print("\nBorrar huérfanos: .pipeline/limpiar-huerfanos.py (no vive aquí: es borrado, no edición).")


def cmd_run(args):
    apply = "--apply" in args
    solo = args[args.index("--solo") + 1] if "--solo" in args else None
    paths = [a for a in args if not a.startswith("--") and a != solo]
    full_run = not paths   # sin rutas explícitas → barrido de todo el sitio
    if not paths:
        paths = paginas_default()
    fixers = [f for f in FIXERS if (solo is None or f[0] == solo)]
    asset_ids = {f[0] for f in ASSET_FIXERS}

    total = 0
    for p in paths:
        try:
            h = open(p, encoding="utf-8").read()
        except Exception:
            continue
        orig = h
        aplicados = []
        for fid, _, _, det, fix in fixers:
            if det(h):
                h2, n = fix(h)
                if n:
                    h = h2
                    aplicados.append("%s×%d" % (fid, n))
        if aplicados:
            total += 1
            rel = os.path.relpath(p, ROOT)
            if apply and h != orig:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(h)
                print("  ✅ %s → %s" % (rel, ", ".join(aplicados)))
            else:
                print("  ○ %s → %s (dry-run)" % (rel, ", ".join(aplicados)))

    print("")
    if total == 0:
        print("✅ Nada que arreglar: el sitio ya está limpio para estos fixers.")
    else:
        print("%s %d página(s) con fix mecánico%s." % (
            "✅ Arregladas" if apply else "○ Arreglaría", total, "" if apply else " (corre con --apply)"))

    # ASSET fixers (CSS compartido): en barrido completo, o si --solo nombra uno de asset.
    if full_run or (solo in asset_ids):
        cmd_run_assets(apply, solo=solo if solo in asset_ids else None)


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    cmd = sys.argv[1]
    if cmd == "list":
        cmd_list()
    elif cmd == "run":
        cmd_run(sys.argv[2:])
    else:
        print("comando desconocido: %s" % cmd); sys.exit(2)


if __name__ == "__main__":
    main()
