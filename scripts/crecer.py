#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""crecer.py — ORQUESTADOR de crecimiento del sitio (un solo punto de entrada).

Une todas las herramientas en un flujo automatizado y agrega el "plomería" que
antes se hacía a mano: sitemap, enlace entrante, bump del service worker,
publicar (rama+merge+push) y stats.

  python3 scripts/crecer.py estado                 # dashboard del sitio
  python3 scripts/crecer.py servicio spec.json     # crear servicio + sitemap + enlace + sw + gate
  python3 scripts/crecer.py colonia  spec.json     # promover colonia + sitemap + gate
  python3 scripts/crecer.py gate <ruta/index.html> # candado (atajo)
  python3 scripts/crecer.py publicar "mensaje"     # rama + commit + merge --no-ff + push (auto-indexa)

Specs: `python3 scripts/crear-servicio.py --ejemplo`  /  `diferenciar-colonia.py --ejemplo`
Quedan SOLO la auditoría con datos GSC y la indexación por MCP en el skill /expandir-sitio
(necesitan el MCP). Todo lo demás (determinista) lo hace este CLI.
"""
import json, os, re, subprocess, sys, datetime, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://electricistaculiacanpro.mx"
PY = sys.executable


def sh(cmd, **kw):
    return subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, **kw)


def _read(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()
def _write(p, h): open(os.path.join(ROOT, p), "w", encoding="utf-8").write(h)


# ───────────────────────── herramientas de "plomería" ─────────────────────────
def sitemap_add(loc, priority):
    sm = _read("sitemap.xml")
    if loc in sm:
        print("  • sitemap: ya estaba"); return
    today = datetime.date.today().isoformat()
    entry = '  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>%s</priority></url>\n' % (loc, today, priority)
    _write("sitemap.xml", sm.replace("</urlset>", entry + "</urlset>", 1))
    print("  • sitemap: +1 (%s)" % loc)


def home_link_add(slug, label):
    """Añade <li><a> a la lista 'Servicios de Electricidad' de la home."""
    h = _read("index.html")
    href = "/servicios/%s/" % slug
    if href in h:
        print("  • enlace home: ya estaba"); return
    anchor = '</a></li></ul></div></section><!-- SECCION SOCIAL-PROOF'
    if anchor not in h:
        print("  ⚠️ enlace home: no encontré la lista de servicios (enlázalo a mano)"); return
    li = '</a></li><li><a href="%s">%s</a></li></ul></div></section><!-- SECCION SOCIAL-PROOF' % (href, label)
    _write("index.html", h.replace(anchor, li, 1))
    print("  • enlace home: +1 (%s)" % label)


def sw_bump():
    sw = _read("sw.js")
    m = re.search(r"const CACHE_VERSION = 'v(\d+)';", sw)
    if not m:
        print("  ⚠️ sw: no encontré CACHE_VERSION"); return
    n = int(m.group(1)); new = "v%d" % (n + 1)
    _write("sw.js", sw.replace(m.group(0), "const CACHE_VERSION = '%s';" % new, 1))
    print("  • sw: v%s -> %s" % (m.group(1), new))


def gate(paths):
    r = sh([PY, ".pipeline/gate-pagina.py"] + paths)
    print(r.stdout.rstrip())
    return r.returncode == 0


# ───────────────────────── subcomandos ─────────────────────────
def cmd_estado(_):
    serv = [d for d in glob.glob(os.path.join(ROOT, "servicios/*/")) if "colonias" not in d]
    coldir = os.path.join(ROOT, "servicios/electricista-colonias-culiacan")
    cols = glob.glob(os.path.join(coldir, "*/index.html"))
    idx = sum(1 for c in cols if "noindex" not in open(c, encoding="utf-8").read())
    blogs = glob.glob(os.path.join(ROOT, "blog/*/index.html"))
    sm = _read("sitemap.xml").count("<url>")
    last = sh(["git", "log", "--oneline", "-1"]).stdout.strip()
    print("══════ ESTADO DEL SITIO ══════")
    print("  Servicios (páginas):     %d" % len(serv))
    print("  Colonias:                %d total · %d indexables · %d noindex" % (len(cols), idx, len(cols) - idx))
    print("  Blog (posts):            %d" % len(blogs))
    print("  URLs en sitemap.xml:     %d" % sm)
    print("  Service worker:          %s" % (re.search(r"v\d+", _read('sw.js')).group(0)))
    print("  Último commit:           %s" % last)
    print("\n  Candados:")
    cg = sh([PY, ".pipeline/ci-gate.py"])
    for ln in cg.stdout.strip().splitlines():
        if "▶" in ln or "Gate" in ln: print("   ", ln.strip())


def cmd_servicio(args):
    spec = args[0]
    z = json.load(open(spec, encoding="utf-8"))
    slug = z["slug"]
    print("── crear-servicio: %s ──" % slug)
    r = sh([PY, "scripts/crear-servicio.py", spec])
    print(r.stdout.rstrip())
    if r.returncode != 0:
        sys.exit("❌ falló crear-servicio")
    print("── wiring automático ──")
    sitemap_add("%s/servicios/%s/" % (SITE, slug), "0.8")
    home_link_add(slug, z.get("bc", slug))
    sw_bump()
    print("── candado ──")
    ok = gate(["servicios/%s/index.html" % slug])
    print("\n%s" % ("✅ LISTO. Revisa, luego:  python3 scripts/crecer.py publicar \"feat: %s\"" % slug
                    if ok else "❌ candado FALLA — NO publiques; revisa arriba."))


def cmd_colonia(args):
    spec = args[0]
    z = json.load(open(spec, encoding="utf-8"))
    slug = z["slug"]
    print("── diferenciar-colonia: %s ──" % slug)
    r = sh([PY, "scripts/diferenciar-colonia.py", spec])
    print(r.stdout.rstrip())
    if r.returncode != 0:
        sys.exit("❌ falló diferenciar-colonia")
    print("── wiring automático ──")
    sitemap_add("%s/servicios/electricista-colonias-culiacan/%s/" % (SITE, slug), "0.6")
    print("── candado ──")
    ok = gate(["servicios/electricista-colonias-culiacan/%s/index.html" % slug])
    print("\n%s" % ("✅ LISTO. Revisa, luego: publicar" if ok else "❌ candado FALLA — revisa."))


def cmd_gate(args):
    sys.exit(0 if gate(list(args)) else 1)


def cmd_publicar(args):
    if not args:
        sys.exit("uso: crecer.py publicar \"mensaje del commit\"")
    msg = args[0]
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    branch = "auto/crecer-%s" % stamp
    st = sh(["git", "status", "--short"]).stdout.strip()
    if not st:
        sys.exit("nada que publicar (working tree limpio)")
    print("Cambios:\n" + st)
    sh(["git", "checkout", "-b", branch])
    sh(["git", "add", "-A"])
    full = msg + "\n\nCo-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
    c = sh(["git", "commit", "-m", full])
    print(c.stdout.rstrip() + c.stderr.rstrip())
    if "BLOQUEADO" in (c.stdout + c.stderr) or c.returncode != 0:
        print("❌ commit bloqueado por el hook — revisa; quedó en la rama %s" % branch); sys.exit(1)
    sh(["git", "checkout", "main"])
    sh(["git", "merge", "--no-ff", branch, "-m", "Merge: " + msg])
    env = dict(os.environ); env["PATH"] = "/usr/local/bin:" + env.get("PATH", "")
    p = subprocess.run(["git", "push", "origin", "main"], cwd=ROOT, text=True, capture_output=True, env=env)
    print((p.stdout + p.stderr).strip()[-600:])
    sh(["git", "branch", "-d", branch])
    print("\n✅ Publicado. (El pre-push ya encoló la indexación en GSC.)")
    print("   Refuerza la indexación por MCP desde /expandir-sitio si quieres acelerar.")


CMDS = {"estado": cmd_estado, "servicio": cmd_servicio, "colonia": cmd_colonia,
        "gate": cmd_gate, "publicar": cmd_publicar}


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help") or sys.argv[1] not in CMDS:
        print(__doc__); sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help") else 1)
    CMDS[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()
