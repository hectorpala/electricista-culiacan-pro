#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Checker DETERMINISTA de reglas de PLANTILLA para electricistaculiacanpro.mx.

Convierte en comprobaciones mecanicas (grep/parseo, sin juicio) las reglas de
REGLAS.md que hoy dependian de que un revisor LLM "recordara leerlas" (seo, movil,
a11y, perf, links). Lo subjetivo (contraste, intencion de busqueda, similitud de
doorways, calidad de copy) NO esta aqui: se queda en los revisores LLM.

Solo LEE disco y parsea archivos locales. Sin red, sin servidor. Solo REPORTA.
Salida DETERMINISTA: idéntica entre corridas (los hallazgos se ordenan de forma
estable antes de asignar ids).

Emite a stdout SOLO el JSON comun de hallazgos:
  {"hallazgos":[{"id":"plt-001","archivo":"ruta","linea":0,
                 "severidad":"alta|media|baja","categoria":"seo|movil|a11y|perf|links",
                 "descripcion":"...","fix_sugerido":"..."}]}

Reglas mecanicas (todas ancladas en REGLAS.md):
  1. links  (alta)  Enlace/recurso interno (href/src/srcset) a archivo inexistente
                    en disco y sin redirect que lo cubra.            (8a747e6e, f8c72299)
  2. seo    (alta)  og:image / twitter:image apuntando a archivo inexistente.
                                                          (590d3e4a, f8c72299, 26cf9939)
  3. seo    (alta)  aggregateRating / Review self-serving en paginas de /blog/. (08a95902)
  4. seo    (media) Email contaminado de otra plantilla (dominio con "plomero").
  5. a11y   (media) #exit-intent-popup sin role=dialog / aria-modal / aria-labelledby,
                    o su titulo sin id="exit-popup-title".              (a11y-302)
  6. perf   (media) Mas de UNA <img> con fetchpriority="high" (compiten por el LCP).
                                                            (perf-202/203/204)
  7. perf   (media) <img loading="eager"> que NO es el hero (sin fetchpriority=high)
                    ni el logo del nav -> debe ir loading="lazy".       (perf-301..314)
  8. perf   (media) <img> sin width y/o height (CLS).                    (bd9ccadf)
  9. movil  (media) Paridad CSS: una regla critica presente en algun styles*.css pero
                    ausente en otro (los 3 deben tener la misma regla). (f44ef39f + reinc.)
 10. movil  (baja)  <table> sin envoltura <div class="table-wrapper"> (mitigado por el
                    fallback CSS global, por eso baja).                 (f44ef39f)
 11. perf   (baja)  theme-color == #0066cc (placeholder prohibido); o pagina indexable
                    sin meta theme-color alguna.                   (bd9ccadf, fdc89c6c)
 12. links  (alta)  Telefono NO canonico: cualquier wa.me/<digitos>, tel:<...> o
                    "telephone":"<...>" cuyo numero (solo digitos) no sea 526673922273
                    ni 6673922273. Caza el placeholder 6677890000, el corrupto
                    526676673922273 y el tel sin +52.                 (2026-06-17)
 13. seo    (media) Overclaim "certificada/certificacion CFE" o "certificado oficial"+
                    "cfe": solo una UVIE acreditada certifica; nosotros entregamos
                    constancia/a norma NOM-001-SEDE.                  (2026-06-17)
 14. perf   (baja)  Referencia a main.js sin minificar (debe ser main.min.js). (2026-06-17)
 18. movil  (media) Página con markup class="floating-btn ..." pero SIN la regla CSS
                    `.floating-btn{` en su <style> inline -> los botones flotantes CTA
                    se renderizan static/diminutos (CSS critico inline no propagado, misma
                    familia que .sr-only / .hero-cta-buttons).        (2026-06-20)
"""
import os
import re
import json
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # raiz del repo
BASE = "https://electricistaculiacanpro.mx"

# Telefono canonico UNICO del sitio (solo digitos). Se aceptan dos formas:
# con lada nacional 52 (526673922273, p.ej. wa.me/tel/JSON-LD) y sin ella
# (6673922273, p.ej. un tel: nacional). Cualquier otro numero = fuga/placeholder/
# corrupcion. Patrones malos vistos el 2026-06-17: placeholder de plantilla
# 6677890000, corrupto por digitos duplicados 526676673922273, tel sin +52.
PHONE_CANONICAL = {"526673922273", "6673922273"}

# Directorios que NUNCA son paginas servidas del sitio (mismo criterio que
# check-indexabilidad.py).
SKIP_DIRS = ("/node_modules/", "/.git/", "/partials/", "/docs/", "/.netlify/",
             "/reivision de sitio/", "/site-check/", "/keyword-volume-tool/",
             "/mcp-local-seo/", "/scripts/")

# Extensiones que son RECURSOS en disco (un href/src a esto debe existir tal cual).
RESOURCE_EXT = (".css", ".js", ".mjs", ".webp", ".png", ".jpg", ".jpeg", ".gif",
                ".svg", ".ico", ".webmanifest", ".json", ".xml", ".pdf", ".txt",
                ".woff", ".woff2", ".ttf", ".otf", ".mp4", ".webm", ".avif")

# ---------------------------------------------------------------- hallazgos
_findings = []  # se ordenan y se les asigna id al final (determinismo)


def add(sev, archivo, categoria, desc, fix):
    _findings.append({
        "archivo": archivo, "linea": 0, "severidad": sev,
        "categoria": categoria, "descripcion": desc, "fix_sugerido": fix,
    })


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def read(p):
    try:
        return open(p, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""


# ---------------------------------------------------------------- redirects (para no
# marcar como roto un enlace que Netlify resuelve via 301/200 rewrite)
def _mk_redirect(frm, status):
    if frm.endswith("*"):
        return (frm[:-1], True, status)   # "/foo/*" -> prefijo "/foo/"
    return (frm, False, status)


def load_redirects():
    rules = []  # (prefijo_o_ruta, es_prefijo, status)
    rp = os.path.join(ROOT, "_redirects")
    if os.path.isfile(rp):
        for line in read(rp).splitlines():
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            parts = s.split()
            if len(parts) < 2:
                continue
            status = parts[-1] if parts[-1].isdigit() else "301"
            rules.append(_mk_redirect(parts[0], status))
    nt = os.path.join(ROOT, "netlify.toml")
    if os.path.isfile(nt):
        txt = read(nt)
        for blk in re.split(r"\[\[redirects\]\]", txt)[1:]:
            mf = re.search(r'from\s*=\s*"([^"]+)"', blk)
            ms = re.search(r'status\s*=\s*(\d+)', blk)
            if mf:
                rules.append(_mk_redirect(mf.group(1), ms.group(1) if ms else "301"))
    return rules


def redirect_covers(path, rules):
    """True solo si una regla ESPECIFICA reescribe/redirige el path a un destino real
    (2xx/3xx). Se ignoran: el comodin raiz "/" (demasiado amplio) y las reglas 4xx/5xx
    como el fallback `/* -> /404.html 404` (que ES el caso de enlace roto, no lo tapa)."""
    for pref, is_prefix, status in rules:
        if status[:1] in ("4", "5"):
            continue
        if is_prefix and pref in ("", "/"):
            continue  # catch-all: no cuenta como redirect intencional de un enlace
        if is_prefix:
            if path.startswith(pref):
                return True
        elif path == pref:
            return True
    return False


# ---------------------------------------------------------------- helpers de parseo
def attr(tag, name):
    m = re.search(name + r'\s*=\s*["\']([^"\']*)["\']', tag, re.I)
    return m.group(1) if m else None


def imgs(t):
    return re.findall(r'<img\b[^>]*>', t, re.I)


def is_stub(t):
    return bool(re.search(r'<meta[^>]*http-equiv=["\']refresh["\']', t, re.I))


def has_noindex(t):
    for m in re.finditer(r'<meta[^>]*name=["\'](?:robots|googlebot)["\'][^>]*>', t, re.I):
        c = re.search(r'content=["\']([^"\']*)["\']', m.group(0), re.I)
        if c and "noindex" in c.group(1).lower():
            return True
    return False


# ---------------------------------------------------------------- recoleccion de paginas
def collect_pages():
    pages = []
    for dirpath, dirnames, files in os.walk(ROOT):
        dn = "/" + os.path.relpath(dirpath, ROOT).replace(os.sep, "/") + "/"
        if any(s in dn for s in SKIP_DIRS):
            dirnames[:] = []
            continue
        for fn in files:
            if not fn.endswith(".html"):
                continue
            if fn.endswith(".min.html") or ".backup" in fn:
                continue
            pages.append(os.path.join(dirpath, fn))
    pages.sort()
    return pages


# ---------------------------------------------------------------- mapeo enlace -> disco
def resolve_to_disk(value, page_dir):
    """Devuelve (ruta_disco_o_None, url_path_normalizada) para un href/src interno.
    None en ruta -> no es un enlace interno verificable (externo/anchor/etc.)."""
    v = value.strip()
    if not v:
        return None, None
    low = v.lower()
    if (low.startswith(("http://", "https://", "//", "mailto:", "tel:", "#",
                        "data:", "javascript:", "sms:", "geo:"))):
        return None, None
    # quitar query y fragmento
    clean = v.split("#")[0].split("?")[0]
    if not clean:
        return None, None
    # ruta URL normalizada (para redirects): siempre absoluta desde la raiz del sitio
    if clean.startswith("/"):
        disk = os.path.normpath(os.path.join(ROOT, clean.lstrip("/")))
        url_path = clean
    else:
        disk = os.path.normpath(os.path.join(page_dir, clean))
        url_path = "/" + os.path.relpath(disk, ROOT).replace(os.sep, "/")
    # mapear a archivo concreto
    if clean.endswith("/"):
        return os.path.join(disk, "index.html"), url_path
    _, ext = os.path.splitext(disk)
    ext = ext.lower()
    if ext in RESOURCE_EXT or ext in (".html", ".htm"):
        return disk, url_path  # referencia directa a un archivo concreto
    # sin extension y sin slash final: ruta "bonita" -> dir/index.html, luego .html
    cand = os.path.join(disk, "index.html")
    if os.path.isfile(cand):
        return cand, url_path
    if os.path.isfile(disk + ".html"):
        return disk + ".html", url_path
    return cand, url_path  # se reportara como inexistente (index.html del dir)


def _is_template_literal(v):
    """href/src construido dinámicamente en JS (`${...}`) o plantillas (`{{...}}`):
    no es una ruta estática, no se valida como archivo en disco."""
    return "${" in v or "{{" in v


def link_candidates(t):
    """Lista de valores de href/src/srcset del documento."""
    vals = []
    for m in re.finditer(r'(?:href|src)\s*=\s*["\']([^"\']+)["\']', t, re.I):
        if not _is_template_literal(m.group(1)):
            vals.append(m.group(1))
    for m in re.finditer(r'srcset\s*=\s*["\']([^"\']+)["\']', t, re.I):
        for piece in m.group(1).split(","):
            url = piece.strip().split()[0] if piece.strip() else ""
            if url and not _is_template_literal(url):
                vals.append(url)
    return vals


# ================================================================ CHECKS por pagina
def check_page(fpath, t, noindex, redirects):
    r = rel(fpath)
    page_dir = os.path.dirname(fpath)

    # --- 1. enlaces/recursos internos rotos (alta, links)
    seen = set()
    for val in link_candidates(t):
        disk, url_path = resolve_to_disk(val, page_dir)
        if disk is None:
            continue
        key = (disk, url_path)
        if key in seen:
            continue
        seen.add(key)
        if os.path.isfile(disk):
            continue
        if url_path and redirect_covers(url_path, redirects):
            continue  # lo cubre un redirect/rewrite: no es 404
        add("alta", r, "links",
            "Enlace/recurso interno a archivo inexistente: %s" % val,
            "Corregir la ruta a un archivo que exista en disco, o eliminar el enlace; "
            "si la URL depende de un redirect, añadir la regla en _redirects/netlify.toml")

    # --- 2. og:image / twitter:image a archivo inexistente (alta, seo)
    for m in re.finditer(r'<meta\b[^>]*>', t, re.I):
        tag = m.group(0)
        prop = (attr(tag, "property") or attr(tag, "name") or "").lower()
        if prop not in ("og:image", "twitter:image"):
            continue
        content = attr(tag, "content")
        if not content:
            continue
        disk, _ = resolve_to_disk(content, page_dir)
        if disk is None:
            continue  # imagen externa (CDN): no verificable en disco
        if not os.path.isfile(disk):
            add("alta", r, "seo",
                "%s apunta a un archivo inexistente: %s" % (prop, content),
                "Apuntar %s a una imagen que exista en disco (ej. un .webp del repo)" % prop)

    # --- 3. aggregateRating / Review en /blog/ (alta, seo)
    if r.startswith("blog/"):
        if re.search(r'"aggregateRating"', t) or re.search(r'"@type"\s*:\s*"Review"', t):
            add("alta", r, "seo",
                "Schema con aggregateRating/Review self-serving en página de blog",
                "Quitar aggregateRating/Review del JSON-LD del blog (política self-serving "
                "de Google); las reseñas solo en páginas de negocio")

    # --- 4. email/dominio contaminado de otra plantilla (media, seo)
    #        Un email cuyo dominio contiene "plomero" en el sitio de electricista
    #        es una fuga de copy-paste de la plantilla origen.
    m_mail = re.search(r'[\w.%+-]+@[\w.-]*plomero[\w.-]*', t, re.I)
    if m_mail:
        add("media", r, "seo",
            "Email contaminado de otra plantilla (dominio con 'plomero'): %s" % m_mail.group(0),
            "Reemplazar por el email correcto de electricistaculiacanpro.mx")

    # --- 5. exit-intent-popup sin ARIA (media, a11y)
    mp = re.search(r'<div\b[^>]*id=["\']exit-intent-popup["\'][^>]*>', t, re.I)
    if mp:
        tag = mp.group(0)
        falta = []
        if not re.search(r'role=["\']dialog["\']', tag, re.I):
            falta.append('role="dialog"')
        if not re.search(r'aria-modal=["\']true["\']', tag, re.I):
            falta.append('aria-modal="true"')
        if not re.search(r'aria-labelledby=', tag, re.I):
            falta.append('aria-labelledby')
        if not re.search(r'id=["\']exit-popup-title["\']', t, re.I):
            falta.append('título con id="exit-popup-title"')
        if falta:
            add("media", r, "a11y",
                "#exit-intent-popup sin atributos de diálogo modal: falta %s" % ", ".join(falta),
                'Igualar al patrón correcto (index.html): <div id="exit-intent-popup" '
                'role="dialog" aria-modal="true" aria-labelledby="exit-popup-title"> y el '
                '<h3> con id="exit-popup-title"')

    # --- 6/7/8. checks sobre <img>
    img_tags = imgs(t)
    high = 0
    for tag in img_tags:
        is_high = bool(re.search(r'fetchpriority=["\']high["\']', tag, re.I))
        if is_high:
            high += 1
        # 7. loading=eager que no es hero ni logo
        if re.search(r'loading=["\']eager["\']', tag, re.I):
            src = (attr(tag, "src") or "")
            if not is_high and "logo" not in src.lower():
                add("media", r, "perf",
                    "<img> con loading=\"eager\" que no es el hero LCP ni el logo: %s"
                    % (src or tag[:60]),
                    'Cambiar a loading="lazy" (solo el hero con fetchpriority="high" va eager)')
        # 8. sin width y/o height
        if not re.search(r'\bwidth\s*=', tag, re.I) or not re.search(r'\bheight\s*=', tag, re.I):
            src = (attr(tag, "src") or "")
            add("media", r, "perf",
                "<img> sin width y/o height (CLS): %s" % (src or tag[:60]),
                "Declarar width y height explícitos en la imagen para reservar espacio (evitar CLS)")
    # 6. mas de una img high
    if high > 1:
        add("media", r, "perf",
            "%d imágenes con fetchpriority=\"high\" (solo el hero LCP debe llevarlo)" % high,
            "Dejar fetchpriority=\"high\" en UNA sola imagen (el hero); quitarlo del resto")

    # --- 10. tabla sin table-wrapper (baja, movil)
    for tm in re.finditer(r'<table\b', t, re.I):
        start = tm.start()
        window = t[max(0, start - 200):start]
        if "table-wrapper" not in window:
            add("baja", r, "movil",
                "<table> sin envoltura <div class=\"table-wrapper\"> (scroll horizontal móvil)",
                'Envolver la <table> en <div class="table-wrapper"> (patrón establecido); '
                'el fallback CSS global mitiga, pero el wrapper es el patrón correcto')

    # --- 11. theme-color (baja, perf)
    tc_metas = re.findall(r'<meta\b[^>]*name=["\']theme-color["\'][^>]*>', t, re.I)
    if tc_metas:
        for tag in tc_metas:
            val = (attr(tag, "content") or "").strip().lower()
            if val == "#0066cc":
                add("baja", r, "perf",
                    "theme-color usa el placeholder prohibido #0066cc",
                    "Cambiar theme-color al color de marca vigente del sitio (no el placeholder #0066cc)")
    elif not noindex:
        add("baja", r, "perf",
            "Página indexable sin <meta name=\"theme-color\">",
            "Añadir <meta name=\"theme-color\" content=\"#...\"> con el color de marca en el <head>")

    # --- 11b. marca/color: hex off-brand prohibidos (seo)
    # La marca de ESTE sitio es NARANJA + AZUL (la home la usa): naranja #E36414/#F97316/#C2410C
    # y AZUL DE MARCA #1e40af/#0f4fa8/#1a73e8/#0d3f8a. LEGÍTIMOS además: #22c55e (disponibilidad),
    # WhatsApp #25d366/#128c7e, logo Google #4285f4/#ea4335/#34a853/#fbbc05, neutros slate, ámbar
    # de avisos. PROHIBIDO: azules que NO son los de marca, morado, rojo y verde decorativo (se
    # colaban por clonación del sitio hermano). OJO: NO incluir aquí los azules de marca.
    # Casos color-elec-20260620. Si aparece un tono nuevo off-brand, añádelo aquí.
    OFFBRAND_HEX = (
        # azules NO-marca (los de marca #1e40af/#0f4fa8/#1a73e8/#0d3f8a NO van aquí)
        "#0066cc", "#0284c7", "#0369a1", "#004499", "#0c4a6e", "#0ea5e9", "#075985",
        "#1a5276", "#bae6fd", "#e8f4fd", "#f0f8ff", "#f0f9ff", "#e0f2fe", "#2c3e50",
        # morado / rojo
        "#667eea", "#764ba2", "#dc2626", "#dc3545", "#b91c1c", "#991b1b", "#fef2f2",
        # verde decorativo (NO el #22c55e de marca, NI WhatsApp #25d366/#128c7e, NI Google #34a853)
        "#059669", "#166534", "#16a34a", "#28a745", "#10b981", "#dcfce7", "#f0fdf4", "#ecfdf5",
    )
    offb = {h: len(re.findall(h, t, re.I)) for h in OFFBRAND_HEX}
    offb = {h: n for h, n in offb.items() if n}
    if offb:
        detalle = ", ".join("%s×%d" % (h, n) for h, n in offb.items())
        add("media", r, "seo",
            "Color off-brand (azul-no-marca/morado/rojo/verde) en la página: %s — la marca es NARANJA+AZUL como la home" % detalle,
            "Reemplazar por la paleta: naranja #C2410C / azul de marca #1e40af; verde→#22c55e; "
            "fondos claros #FFF7ED. No tocar el logo de Google (#4285f4/#ea4335 en <path fill> de SVG).")

    # --- 12. telefono NO canonico (alta, links) — contacto roto = leads perdidos
    #         Normaliza a solo digitos (ignora +, espacios y guiones). Si el numero
    #         no es 526673922273 ni 6673922273 -> fuga/placeholder/corrupcion.
    seen_phones = set()
    for m in re.finditer(
            r'wa\.me/(\+?[\d\s\-]+)'                       # wa.me/<numero>
            r'|tel:(\+?[\d\s\-]+)'                          # tel:<numero>
            r'|"telephone"\s*:\s*"(\+?[\d\s\-]+)"',         # JSON-LD telephone
            t, re.I):
        raw = m.group(1) or m.group(2) or m.group(3) or ""
        digits = re.sub(r'\D', "", raw)
        if not digits:
            continue
        if digits in PHONE_CANONICAL:
            continue
        if digits in seen_phones:
            continue
        seen_phones.add(digits)
        add("alta", r, "links",
            "Teléfono no canónico (%s); el único número del sitio es 526673922273"
            % m.group(0).strip(),
            "Reemplazar por el teléfono canónico: wa.me/526673922273 · tel:+526673922273 · "
            '"telephone":"+526673922273" (display "667 392 2273"). Patrones malos: placeholder '
            "6677890000, corrupto 526676673922273, tel sin +52")

    # --- 13. overclaim certificación CFE (media — NO bloquea; visibiliza el lote)
    #         Solo una UVIE acreditada emite la verificación oficial para CFE; el
    #         negocio entrega "constancia de instalación / a norma NOM-001-SEDE".
    #   Análisis por ORACIÓN (no por documento): se ignora la oración si atribuye
    #   el certificado a una UVIE acreditada (deslinde honesto, p.ej. dictamen-electrico)
    #   y se cazan TODAS las variantes "certificad{a,o,os,as} ... CFE" (cualquier orden,
    #   ventana de 40 car.) + "certificación CFE". Antes solo cazaba 3 frases exactas y
    #   se le escapaba "Certificado CFE" / "tableros certificados CFE" / "conforme a CFE"
    #   (los cazó el revisor LLM el 2026-06-18; ahora son deterministas).
    #   Heurística de deslinde: si la página menciona "UVIE" en cualquier parte, fue
    #   redactada con el entendimiento correcto (el certificado oficial lo emite una
    #   Unidad de Verificación), p.ej. dictamen-electrico → se confía y NO se marca.
    overclaim = None
    if "uvie" not in t.lower():
        for frase in re.split(r"[.\n]", t):
            fl = frase.lower()
            if "cfe" not in fl:
                continue
            m = (re.search(r"certificad[oa]s?\b[^.]{0,40}\bcfe\b", fl)
                 or re.search(r"\bcfe\b[^.]{0,40}\bcertificad[oa]s?\b", fl)
                 or re.search(r"certificaci[oó]n\s+cfe", fl))
            if m:
                overclaim = m.group(0).strip()[:50]
                break
    if overclaim:
        add("media", r, "seo",
            "Overclaim certificación CFE (\"%s\"): solo una UVIE acreditada certifica para CFE"
            % overclaim,
            'Reescribir a "constancia de instalación" / "a norma NOM-001-SEDE" (NO "certificada/'
            'certificación/certificado(s) CFE"). Las oraciones que atribuyen el certificado a una '
            "UVIE acreditada NO se marcan (deslinde honesto)")

    # --- 14. main.js sin minificar (baja, perf)
    for m in re.finditer(r'src\s*=\s*["\']([^"\']*main\.js)["\']', t, re.I):
        add("baja", r, "perf",
            "Referencia a main.js sin minificar: %s (debe ser main.min.js)" % m.group(1),
            "Cambiar el src a main.min.js (mismo path, versión minificada que usa index.html). "
            "Tras el cambio verificar que las URLs wa.me no quedaron truncadas")

    # --- 15. rating visible 5.0 (media, seo): el estándar de marca es 4.8 (coherente con
    #         el aggregateRating del schema). Un span.rating-score ">5.0/5" visible —sobre
    #         todo en blogs SIN aggregateRating propio— contradice el estándar y se cuela al
    #         copiar bloques de prueba social. Regresión vista 2026-06-17/18 (servicios) y
    #         2026-06-19 (6 blogs). OJO: no confundir con "ratingValue":"5" de reviews
    #         individuales ni con "5.0" dentro de paths SVG (este patrón solo caza el span).
    if re.search(r'rating-score"\s*>\s*5\.0', t):
        add("media", r, "seo",
            'Rating visible "5.0" en span.rating-score (el estándar del sitio es 4.8)',
            'Cambiar el "5.0" del span.rating-score a "4.8" (el ratingValue del JSON-LD y todo '
            '"N.N" visible deben coincidir en 4.8). NO tocar "5.0" que sean coordenadas en SVG')

    # --- 16. overclaim absoluto / garantía financiera (media, seo): claims no sostenibles
    #         tipo "cero riesgo", "retorno garantizado", "se pagan solos" — familia de los ya
    #         prohibidos ("sin riesgos para tu familia"/"se pagan solos", remediados 2026-06-17).
    #         NO se incluye "sin riesgo" a secas: tiene usos legítimos (instrucción de
    #         seguridad, "sin riesgo de descarga" tras instalar tierra física).
    for pat_oc, etiqueta in (
        (r"cero\s+riesgo", "cero riesgo"),
        (r"riesgo\s+cero", "riesgo cero"),
        (r"retorno\s+garantizado", "retorno garantizado"),
        (r"se\s+pagan\s+solos?", "se pagan solos"),
        (r"se\s+paga\s+solo\b", "se paga solo"),
    ):
        if re.search(pat_oc, t, re.I):
            add("media", r, "seo",
                'Overclaim absoluto/garantía financiera ("%s"): claim no sostenible' % etiqueta,
                'Suavizar a algo verificable: "minimiza/reduce el riesgo", "suele recuperarse en '
                'pocos meses según el consumo". Evitar "cero riesgo"/"garantizado"/"se pagan solos"')
            break

    # --- 17. tarjeta card--img sin wrapper media-box (media, movil): si un <a class="card
    #         card--img"> contiene <picture> SIN el <figure class="media-box"> de la homepage
    #         (fuente de verdad), la imagen se renderiza a su ancho intrínseco (~420px) y se
    #         recorta ~77px en móvil. Pasó en 11 blogs (remediado 2026-06-19).
    if re.search(r'class="card card--img"[^>]*>\s*<picture', t):
        add("media", r, "movil",
            "Tarjeta card--img con <picture> sin envolver en figure.media-box (la imagen se "
            "recorta en móvil)",
            'Envolver el <picture> en <div class="service-card"><figure class="media-box">...'
            '</figure></div> replicando la estructura de index.html (fuente de verdad)')

    # --- 18. floating-btn sin CSS inline (media, movil): la regla `.floating-btn{...}`
    #         (+ .floating-call/.floating-whatsapp/.floating-btn--phone/--whatsapp/.floating-cta)
    #         que posiciona los botones flotantes WhatsApp/Llamar vive SOLO en el <style>
    #         critico inline (NO en el CSS servido hasheado). Si una pagina lleva el markup
    #         class="floating-btn ..." pero NO trae la regla `.floating-btn{` en su mismo
    #         <style>, los botones se renderizan static/diminutos (~20x26px) = CTA movil roto.
    #         Misma familia que .sr-only (2026-06-16) y .hero-cta-buttons (2026-06-17). Pasaron
    #         13 paginas (11 blogs + contacto + gracias), remediadas 2026-06-20. El check ignora
    #         espacios entre `.floating-btn` y la llave. NO marca index.html ni las paginas que
    #         SI tienen la regla. OJO: hay DOS convenciones de markup (floating-whatsapp/-call
    #         y floating-btn--whatsapp/-phone); el markup que dispara este check es `class="floating-btn`
    #         (literal), presente en AMBAS porque comparten la clase base.
    if re.search(r'class="floating-btn\b', t) and not re.search(r'\.floating-btn\s*\{', t):
        add("media", r, "movil",
            "Markup class=\"floating-btn\" presente pero SIN la regla CSS .floating-btn{ en el "
            "<style> inline -> los botones flotantes WhatsApp/Llamar se renderizan static y "
            "diminutos (CTA móvil roto)",
            'Replicar el bloque CSS inline de los botones flotantes (de index.html) en el <style> '
            'de esta página, cubriendo AMBAS variantes de markup: .floating-btn/.floating-call/'
            '.floating-whatsapp y .floating-btn--phone/.floating-btn--whatsapp/.floating-cta. NO se '
            'arregla por el CSS servido (es hasheado: obligaría a re-versionar cientos de HTML)')


# ================================================================ CHECK global: paridad CSS
# PARIDAD TOTAL (no solo firmas): las 689 paginas sirven styles.7f293647.css (el VIVO, =
# index.html FUENTE DE VERDAD); styles.min.css esta huerfana (nadie la sirve) y styles.css
# es la fuente. Las tres DEBEN tener las mismas reglas: si la fuente/min se desvian del
# vivo, son una bomba latente (si algun build reconstruye el servido desde ahi, el sitio
# cambia de colores/logo sin querer; caso real 20260619: la fuente traia otro esquema de
# marca y otro .logo). El checker viejo solo comparaba 3 firmas hardcodeadas.
#
# Se descompone cada styles*.css en ATOMOS (selector individual + bloque de declaraciones
# normalizado, con su contexto @media) y se reporta todo atomo presente en alguna hoja pero
# ausente en otra. Ignora minificacion (espacios) y agrupacion de selectores -> sin falsos
# positivos. (Logica espejo de .pipeline/check-css-paridad.py.)
def _css_norm_sel(s):
    s = re.sub(r"\s+", " ", s).strip()  # conserva el combinador descendiente (' '), semantico
    return re.sub(r"\s*([>+~,])\s*", r"\1", s)


def _css_norm_decls(body):
    b = re.sub(r"\s+", " ", body).strip()
    b = re.sub(r"\s*([;:,])\s*", r"\1", b)
    return ";".join(sorted(d.strip() for d in b.split(";") if d.strip()))


def _css_split_rules(css):
    rules, depth, prelude, buf, prelude_s = [], 0, [], [], ""
    for ch in css:
        if ch == "{":
            if depth == 0:
                prelude_s, prelude, depth = "".join(prelude), [], 1
            else:
                depth += 1
                buf.append(ch)
        elif ch == "}":
            depth -= 1
            if depth == 0:
                rules.append((prelude_s.strip(), "".join(buf)))
                buf = []
            else:
                buf.append(ch)
        else:
            (prelude if depth == 0 else buf).append(ch)
    return rules


def _css_style_atoms(prelude, body, ctx=""):
    decls = _css_norm_decls(body)
    return ["%s%s{%s}" % (ctx, sel, decls)
            for sel in _css_norm_sel(prelude).split(",") if sel]


def _css_atoms(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out = set()
    for prelude, body in _css_split_rules(css):
        p = _css_norm_sel(prelude)
        head = p.split("(")[0].lower()
        if head.startswith("@media") or head.startswith("@supports"):
            ctx = re.sub(r"\s+", "", p) + "||"
            for ip, ib in _css_split_rules(body):
                out.update(_css_style_atoms(ip, ib, ctx))
        elif p.startswith("@"):
            out.add(re.sub(r"\s+", "", p) + "{" + re.sub(r"\s+", "", body) + "}")
        else:
            out.update(_css_style_atoms(prelude, body))
    return out


def check_css_parity():
    css_files = sorted(glob.glob(os.path.join(ROOT, "styles*.css")))
    if len(css_files) < 2:
        return  # nada que comparar
    A = {c: _css_atoms(read(c)) for c in css_files}
    union = set().union(*A.values())
    for atom in sorted(union):
        tienen = [c for c in css_files if atom in A[c]]
        if len(tienen) == len(css_files):
            continue
        nombres = ", ".join(sorted(os.path.basename(c) for c in tienen))
        for c in css_files:
            if atom not in A[c]:
                add("media", rel(c), "movil",
                    "Paridad CSS rota: la regla '%s' existe en %s pero falta aquí" % (atom, nombres),
                    "Unificar las 3 hojas al VIVO (styles.7f293647.css = index.html fuente de verdad). "
                    "Si el cambio toca el archivo servido, versionar ?v= y subir CACHE_NAME en sw.js.")


# ================================================================ MAIN
def main():
    redirects = load_redirects()
    for fpath in collect_pages():
        t = read(fpath)
        if is_stub(t):
            continue  # stub de redireccion (meta-refresh): no es pagina de contenido
        check_page(fpath, t, has_noindex(t), redirects)
    check_css_parity()

    # orden estable + asignacion de ids deterministas
    sev_rank = {"alta": 0, "media": 1, "baja": 2}
    _findings.sort(key=lambda h: (h["archivo"], sev_rank.get(h["severidad"], 9),
                                  h["categoria"], h["descripcion"]))
    out = []
    for i, h in enumerate(_findings, 1):
        out.append({
            "id": "plt-%03d" % i, "archivo": h["archivo"], "linea": h["linea"],
            "severidad": h["severidad"], "categoria": h["categoria"],
            "descripcion": h["descripcion"], "fix_sugerido": h["fix_sugerido"],
        })
    print(json.dumps({"hallazgos": out}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
