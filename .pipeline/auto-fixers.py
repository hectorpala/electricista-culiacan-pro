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
  python3 .pipeline/auto-fixers.py verify --base main        # certifica LOTE MECÁNICO (FASE 8)
"""
import datetime
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CORRECT_EMAIL = "contacto@electricistaculiacanpro.mx"
BRAND_THEME = "#E36414"   # theme-color de la home (fuente de verdad)

# ── CUARENTENA (bk pendiente: contenido delgado / fuera de plantilla) ─────────────────────
# Estas páginas FALLAN gate-pagina.py por razones PREEXISTENTES (<150 tokens visibles únicos,
# o contacto/: 7 errores de plantilla). Si un fixer las toca, el verificador de FASE 7 las
# inspecciona, falla, y la corrida ENTERA no publica. Se saltan aquí hasta que el agente las
# enriquezca (diferenciar-colonia.py / decisor-negocio); al cerrar su tarea de backlog,
# QUITARLAS de esta lista para que los fixers pendientes (skip-link, etc.) las alcancen.
CUARENTENA = {
    "blog/index.html",
    "contacto/index.html",
    "servicios/electricista-colonias-culiacan/bachigualato/index.html",
    "servicios/electricista-colonias-culiacan/campestre/index.html",
    "servicios/electricista-colonias-culiacan/colinas-de-san-miguel/index.html",
    "servicios/electricista-colonias-culiacan/el-vallado/index.html",
    "servicios/electricista-colonias-culiacan/hacienda-del-valle/index.html",
    "servicios/electricista-colonias-culiacan/jorge-almada/index.html",
    "servicios/electricista-colonias-culiacan/juntas-de-humaya/index.html",
    "servicios/electricista-colonias-culiacan/las-americas/index.html",
    "servicios/electricista-colonias-culiacan/lazaro-cardenas/index.html",
    "servicios/electricista-colonias-culiacan/libertad/index.html",
    "servicios/electricista-colonias-culiacan/los-pinos/index.html",
    "servicios/electricista-colonias-culiacan/nuevo-culiacan/index.html",
    "servicios/electricista-colonias-culiacan/pemex/index.html",
    "servicios/electricista-colonias-culiacan/prados-de-la-conquista/index.html",
    "servicios/electricista-colonias-culiacan/rafael-buelna/index.html",
    "servicios/electricista-colonias-culiacan/recursos-hidraulicos/index.html",
    "servicios/electricista-colonias-culiacan/valle-alto/index.html",
}


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

def _sin_svg(h):
    """Quita los bloques <svg>…</svg> (para detectar sin tocar arte vectorial)."""
    return re.sub(r"<svg\b.*?</svg>", " ", h, flags=re.S | re.I)

def _det_color(h):
    low = _sin_svg(h).lower()
    return any(c in low for c in _COLOR_OFFBRAND)

def _fix_color(h):
    # PROTEGER los <svg>: el reemplazo global ciego podía repintar un fill legítimo
    # dentro de arte vectorial — se apartan los bloques svg, se sanan los colores del
    # resto, y se restauran intactos. (La CALIBRACIÓN de la denylist se conserva: aquí
    # el AZUL SÍ es de marca — azul-stray → #1e40af, NO a naranja.)
    n = 0
    svgs = []
    def _stash(m):
        svgs.append(m.group(0))
        return "\x00SVG%d\x00" % (len(svgs) - 1)
    h = re.sub(r"<svg\b.*?</svg>", _stash, h, flags=re.S | re.I)
    for c in _COLOR_LIGHT_BG:
        h, k = re.subn(re.escape(c), "#FFF7ED", h, flags=re.I); n += k
    for c in _COLOR_BLUE:
        h, k = re.subn(re.escape(c), "#1e40af", h, flags=re.I); n += k
    for c in _COLOR_RED_PURPLE:
        h, k = re.subn(re.escape(c), "#C2410C", h, flags=re.I); n += k
    for c in _COLOR_GREEN:
        h, k = re.subn(re.escape(c), "#22c55e", h, flags=re.I); n += k
    h = re.sub(r"\x00SVG(\d+)\x00", lambda m: svgs[int(m.group(1))], h)
    return h, n


# ── tercer tono latente de estrellitas (bk-3bd33864 / REGLAS.md color-muerto-FBBF24):
#    el <style> crítico inline de ~674 páginas trae .rating-stars{color:#FBBF24} (1.67:1).
#    Hoy lo tapa styles.<hash>.css (#B45309, ya corregido), pero es bomba latente (flash de
#    carga / reorden de hojas). Mismo destino que la remediación FBBC04/FFA000 → #B45309. ──
def _det_star(h):
    return "fbbf24" in _sin_svg(h).lower()

def _fix_star(h):
    n = 0
    svgs = []
    def _stash(m):
        svgs.append(m.group(0))
        return "\x00SVG%d\x00" % (len(svgs) - 1)
    h = re.sub(r"<svg\b.*?</svg>", _stash, h, flags=re.S | re.I)
    h, n = re.subn(r"#FBBF24", "#B45309", h, flags=re.I)
    h = re.sub(r"\x00SVG(\d+)\x00", lambda m: svgs[int(m.group(1))], h)
    return h, n


# ── SVG decorativo sin aria-hidden en los botones flotantes (bk-08a2d9d5 / REGLAS.md
#    svg-aria-hidden-cta-20260628): el <a class="floating-btn"> ya trae aria-label; el svg
#    interior debe llevar aria-hidden="true" (patrón ya aplicado en la home). ──
_FLOAT_SVG = re.compile(r'(<a[^>]*class="[^"]*floating-btn[^"]*"[^>]*>\s*)<svg(?![^>]*aria-hidden)', re.I)

def _det_svg_float(h):
    return bool(_FLOAT_SVG.search(h))

def _fix_svg_float(h):
    return _FLOAT_SVG.subn(r'\g<1><svg aria-hidden="true"', h)


# ── skip-link de accesibilidad (bk-e8643041): réplica EXACTA del de la home (fuente de
#    verdad) en las páginas que no lo tienen. Receta estrecha: (1) <a> pegado tras <body>,
#    (2) regla .skip-link:focus en el <style> crítico, (3) ancla: id="main-content" en el
#    primer <main>/<section> tras </header> — si ese elemento ya tiene id, se apunta el
#    href al id existente en vez de duplicar. Páginas sin </header> NO se tocan (quedan
#    para edición normal: son 4, caben en el cap de 18). ──
_SKIP_A = ('<a href="#main-content" class="skip-link" style="position:absolute;top:-40px;left:0;'
           'background:#1e40af;color:#fff;padding:8px 16px;z-index:100;font-size:14px;'
           'transition:top .2s">Saltar al contenido</a>')
_SKIP_CSS = '.skip-link:focus{top:0;min-height:44px;display:flex;align-items:center;box-sizing:border-box}'

def _det_skiplink(h):
    return ("skip-link" not in h) and ("</header>" in h) and ("<body" in h) and ("</style>" in h)

def _fix_skiplink(h):
    i = h.find("</header>")
    m = re.search(r"<(main|section)\b([^>]*)>", h[i:i + 600], re.I)
    if not m:
        return h, 0
    tag_attrs = m.group(2)
    mid = re.search(r'id=["\']([^"\']+)["\']', tag_attrs)
    if mid:
        ancla = mid.group(1)          # ya tiene id → el href apunta ahí
        skip_a = _SKIP_A.replace("#main-content", "#" + ancla)
    else:                             # sin id → se le pone main-content (como la home)
        abs_start = i + m.start()
        h = h[:abs_start] + "<%s id=\"main-content\"%s>" % (m.group(1), tag_attrs) + h[i + m.end():]
        skip_a = _SKIP_A
    h2, n1 = re.subn(r"(<body[^>]*>)", r"\g<1>" + skip_a.replace("\\", "\\\\"), h, count=1, flags=re.I)
    if not n1:
        return h, 0
    h3 = h2.replace("</style>", _SKIP_CSS + "</style>", 1)
    return h3, 1


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
    ("star-color-inline", "tercer tono latente #FBBF24 de .rating-stars en el <style>/style inline → #B45309 (paridad con styles*.css, WCAG AA)",
     "mecanico", _det_star, _fix_star),
    ("svg-aria-float", "svg decorativo sin aria-hidden dentro de <a class=floating-btn aria-label=…> → aria-hidden=true (patrón de la home)",
     "mecanico", _det_svg_float, _fix_svg_float),
    ("skip-link", "página sin skip-link → réplica exacta del de la home tras <body> + regla :focus en el CSS crítico + ancla en el primer main/section tras el header",
     "mecanico", _det_skiplink, _fix_skiplink),
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
    """Sube el token `styles*.css?v=…` a `version` en TODAS las páginas HTML **y en el
    precache de sw.js** (llevaba la URL ?v= vieja hardcodeada → el SW nuevo precacheaba
    CSS stale aunque CACHE_VERSION subiera). OBLIGATORIO al cambiar un CSS: se sirve
    `immutable`. Acepta tokens de 8-12 dígitos (fecha o fecha+hora). Devuelve
    (páginas tocadas, fallos de escritura)."""
    n_files, fallos = 0, 0
    targets = sorted(set(glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True)))
    targets.append(os.path.join(ROOT, SW_FILE))
    for p in targets:
        if "/node_modules/" in p or "/.git/" in p:
            continue
        try:
            s = open(p, encoding="utf-8").read()
        except Exception:
            continue
        s2, k = re.subn(r'(styles[\w.]*\.css\?v=)\d{8,12}', r'\g<1>' + version, s)
        if k and s2 != s:
            try:
                open(p, "w", encoding="utf-8").write(s2)
                n_files += 1
            except Exception:
                fallos += 1
    return n_files, fallos


# Estado del cache-busting: hash de los 3 CSS registrado DESPUÉS del último bump exitoso.
# Si al arrancar difiere, un cambio de CSS quedó SIN bump (fixer muerto a medias) → se
# repara aquí mismo. Sin esto, CSS viejo cacheado 1 año sin ningún sensor.
BUMP_STATE = os.path.join(ROOT, ".pipeline", "css-bump-state.json")

def _css_hash():
    import hashlib
    hh = hashlib.sha256()
    for css_name in CSS_FILES:
        try:
            hh.update(open(os.path.join(ROOT, css_name), "rb").read())
        except Exception:
            hh.update(b"(ausente)")
    return hh.hexdigest()

def _token_version():
    """Token ?v= nuevo: fecha (AAAAMMDD); si las páginas YA traen el de hoy, fecha+hora
    (AAAAMMDDHHMM) para que el segundo cambio del día también rompa el cache."""
    hoy = datetime.date.today().strftime("%Y%m%d")
    try:
        home = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
        if re.search(r'styles[\w.]*\.css\?v=' + hoy + r'(?!\d)', home):
            return datetime.datetime.now().strftime("%Y%m%d%H%M")
    except Exception:
        pass
    return hoy

def _do_full_bump(motivo):
    """Bump completo (?v= en páginas+sw + CACHE_VERSION) y registro del estado."""
    version = _token_version()
    np, nf = _bump_css_version_html(version)
    print("  ✅ ?v=%s bumpeado en %d archivo(s)%s [%s]" % (
        version, np, (" · ⚠️ %d fallo(s) de escritura" % nf) if nf else "", motivo))
    nb = _bump_sw()
    print("  ✅ %s → CACHE_VERSION +1" % SW_FILE if nb else "  ⚠️  no pude bumpear %s" % SW_FILE)
    ok = (nf == 0 and nb > 0)
    if ok:
        import json as _json
        try:
            open(BUMP_STATE, "w", encoding="utf-8").write(
                _json.dumps({"css_sha256": _css_hash(), "token": version,
                             "fecha": datetime.datetime.now().isoformat(timespec="seconds")}) + "\n")
        except Exception:
            print("  ⚠️  no pude escribir %s (el auto-reparo del próximo run re-bumpeará)" % BUMP_STATE)
    return ok


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
    """Corre los ASSET_FIXERS sobre los 3 CSS; si alguno toca CSS y se aplica, corre el bump
    completo. AUTO-REPARO previo: si el hash de los CSS difiere del registrado tras el último
    bump (fixer muerto a medias), se re-bumpea aunque hoy no haya nada que arreglar.
    Devuelve (total, bump_fallido)."""
    fixers = [f for f in ASSET_FIXERS if (solo is None or f[0] == solo)]
    if not fixers:
        return 0, False
    bump_fallido = False

    import json as _json
    try:
        estado = _json.loads(open(BUMP_STATE, encoding="utf-8").read())
    except Exception:
        estado = None
    if estado and estado.get("css_sha256") and estado["css_sha256"] != _css_hash():
        if apply:
            print("ASSET fixers: ⚠️ los CSS cambiaron SIN bump registrado (corrida anterior muerta a medias) → re-bump:")
            if not _do_full_bump("auto-reparo"):
                bump_fallido = True
        else:
            print("ASSET fixers: ⚠️ los CSS difieren del último bump registrado — con --apply se auto-repara (re-bump).")

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
            if not _do_full_bump("fix aplicado"):
                bump_fallido = True
        elif css_tocado:
            print("  (con --apply: bumpea ?v= en las páginas + sw.js — necesario por el cache immutable)")
    elif apply and estado is None:
        # Primer run con el estado nuevo: registrar la línea base sin bumpear nada.
        try:
            open(BUMP_STATE, "w", encoding="utf-8").write(
                _json.dumps({"css_sha256": _css_hash(), "token": "(baseline)",
                             "fecha": datetime.datetime.now().isoformat(timespec="seconds")}) + "\n")
            print("ASSET fixers: línea base de bump registrada (%s)." % os.path.relpath(BUMP_STATE, ROOT))
        except Exception:
            pass
    return total, bump_fallido


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
    saltadas = 0
    for p in paths:
        if os.path.relpath(p, ROOT) in CUARENTENA:
            saltadas += 1
            continue
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
    if saltadas:
        print("⏸  %d página(s) en CUARENTENA saltadas (contenido delgado preexistente; ver backlog)." % saltadas)
    if total == 0:
        print("✅ Nada que arreglar: el sitio ya está limpio para estos fixers.")
    else:
        print("%s %d página(s) con fix mecánico%s." % (
            "✅ Arregladas" if apply else "○ Arreglaría", total, "" if apply else " (corre con --apply)"))

    # ASSET fixers (CSS compartido): en barrido completo, o si --solo nombra uno de asset.
    if full_run or (solo in asset_ids):
        _, bump_fallido = cmd_run_assets(apply, solo=solo if solo in asset_ids else None)
        if bump_fallido:
            # Exit ≠ 0: un CSS cambiado sin bump completo es un estado inconsistente que
            # el orquestador DEBE ver (antes solo se imprimía un ⚠️ y exit 0).
            print("❌ bump de cache-busting INCOMPLETO — revisar antes de publicar.")
            sys.exit(1)


def cmd_verify(args):
    """LOTE MECÁNICO VERIFICADO (candado de FASE 8): certifica qué archivos HTML del diff
    vs --base fueron producidos ÍNTEGRAMENTE por los FIXERS registrados. Para cada HTML
    cambiado: toma su contenido en el ref base, le aplica SOLO los fixers (mismo orden que
    `run`) y exige igualdad BYTE A BYTE con el working tree; además exige idempotencia
    (ningún detector debe seguir disparando sobre el resultado). Un archivo que no calza
    es edición LIBRE: no invalida el lote, pero cuenta contra el cap de 18.
    Salida: JSON {mecanicos, libres, archivos_libres} + exit 0 (exit 2 solo si git falla)."""
    import json as _json
    import subprocess
    base = args[args.index("--base") + 1] if "--base" in args else "main"

    def _git(*a):
        return subprocess.run(["git"] + list(a), capture_output=True, cwd=ROOT)

    diff = _git("diff", "--name-only", base, "--")
    if diff.returncode != 0:
        print("❌ git diff falló: %s" % diff.stderr.decode("utf-8", "replace").strip()); sys.exit(2)
    cambiados = [f for f in diff.stdout.decode("utf-8").splitlines() if f.strip()]
    html = [f for f in cambiados if f.endswith(".html")]
    no_html = [f for f in cambiados if not f.endswith(".html")]

    mecanicos, libres = [], []
    for rel in html:
        show = _git("show", "%s:%s" % (base, rel))
        if show.returncode != 0:
            libres.append((rel, "nuevo en el diff (no existe en %s)" % base)); continue
        try:
            h = show.stdout.decode("utf-8")
            actual = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        except Exception as e:
            libres.append((rel, "ilegible: %s" % e)); continue
        for fid, _, _, det, fix in FIXERS:
            if det(h):
                h2, n = fix(h)
                if n:
                    h = h2
        if h != actual:
            libres.append((rel, "no equivale a base+fixers (hay edición manual)")); continue
        residuo = [fid for fid, _, _, det, fix in FIXERS if det(actual) and fix(actual)[1]]
        if residuo:
            libres.append((rel, "no idempotente: %s sigue disparando" % ",".join(residuo))); continue
        mecanicos.append(rel)

    for rel, motivo in libres:
        print("  ✋ LIBRE  %s — %s" % (rel, motivo))
    if no_html:
        print("  ℹ️  fuera del lote (no HTML, los juzga el candado normal): %s" % ", ".join(no_html))
    print(_json.dumps({"base": base, "mecanicos": len(mecanicos), "libres": len(libres),
                       "archivos_libres": [r for r, _ in libres], "no_html": no_html},
                      ensure_ascii=False))


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); sys.exit(0)
    cmd = sys.argv[1]
    if cmd == "list":
        cmd_list()
    elif cmd == "run":
        cmd_run(sys.argv[2:])
    elif cmd == "verify":
        cmd_verify(sys.argv[2:])
    else:
        print("comando desconocido: %s" % cmd); sys.exit(2)


if __name__ == "__main__":
    main()
