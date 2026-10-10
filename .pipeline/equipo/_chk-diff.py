#!/usr/bin/env python3
"""Cotejo del coordinador (corrida 20261009-2100): clasifica cada línea -/+ del diff (árbol vs HEAD)
por tarea y comprueba metas/JSON-LD intactos. Uso: python3 _chk-diff.py"""
import subprocess, re, os, json
WT = "/tmp/equipo-electricista-20261009-2100"
T1 = ["blog/por-que-se-bota-el-breaker-pastilla-culiacan/index.html", "blog/mantenimiento-tablero-electrico-preventivo/index.html",
      "blog/apagones-culiacan-por-que-se-va-la-luz-que-hacer/index.html", "blog/cuando-llamar-electricista-emergencia/index.html",
      "blog/cuanto-cuesta-electricista-culiacan/index.html", "blog/recibo-luz-alto-culiacan-como-bajarlo/index.html",
      "blog/como-elegir-buen-electricista-culiacan/index.html"]
T2 = ["blog/index.html", "blog/ahorro-energia-iluminacion-led/index.html", "blog/cambio-110-a-220v-culiacan-cfe/index.html",
      "blog/como-prevenir-cortocircuitos-casa/index.html", "blog/olor-a-quemado-en-casa-que-hacer/index.html",
      "blog/por-que-parpadean-las-luces-de-mi-casa/index.html", "blog/seguridad-electrica-temporada-lluvias/index.html",
      "blog/senales-instalacion-electrica-obsoleta/index.html"]
T3 = ["index.html"]
AVIF = ["mantenimiento-tablero-electrico-culiacan-800w", "mantenimiento-tablero-electrico-culiacan-1200w", "emergencia-electrica-culiacan-800w",
        "emergencia-electrica-culiacan-1200w", "instalacion-minisplit-culiacan-800w"]
def git(*a): return subprocess.run(["git", "-C", WT, *a], capture_output=True, text=True).stdout
def lines(f):
    out = git("diff", "-U0", "--", f)
    return [l for l in out.split("\n") if l and l[0] in "+-" and not l.startswith(("+++", "---"))]
def metas(txt):
    g = lambda p: re.findall(p, txt, re.S)
    return {"title": g(r"<title>.*?</title>"), "desc": g(r'<meta name="description"[^>]*>'), "og": g(r'<meta property="og:[^>]*>'),
            "tw": g(r'<meta name="twitter:[^>]*>'), "ld": g(r'<script type="application/ld\+json">.*?</script>'), "dm": g(r'"dateModified"\s*:\s*"[^"]*"')}
status = [l for l in git("status", "--short").split("\n") if l and not l[3:].startswith(".pipeline/equipo/")]
print("== status (sin .pipeline/equipo):", len(status))
for l in status: print("  ", l)
print("\n== T1 (7 HTML):")
for f in T1:
    ls = lines(f); plus = [l for l in ls if l[0] == "+"]; minus = [l for l in ls if l[0] == "-"]
    bad_p = [l for l in plus if not (".avif" in l or "image/avif" in l or "logo-256w.webp" in l)]
    bad_m = [l for l in minus if not (".webp" in l)]
    cur = open(f"{WT}/{f}", encoding="utf-8").read(); head = git("show", f"HEAD:{f}")
    print(f"  {f.split('/')[1][:38]:38} +{len(plus)} -{len(minus)} malas+{len(bad_p)} malas-{len(bad_m)} avif={cur.count('image/avif')} logo512={cur.count('src=\"/assets/images/electricista-culiacan-pro-logo.webp\"')} metas_igual={metas(cur)==metas(head)} hero_webp_source={cur.count('<source type=\"image/webp\"')}")
    for l in bad_p + bad_m: print("     !!", l[:160])
print("  AVIF:")
d = f"{WT}/assets/images/optimizadas/"
for n in AVIF:
    a, w = d + n + ".avif", d + n + ".webp"
    print(f"   {n:48} avif={os.path.getsize(a) if os.path.exists(a) else 'NO'} webp={os.path.getsize(w)} ok={os.path.exists(a) and os.path.getsize(a) < os.path.getsize(w)}")
print("\n== T2 (8 HTML):")
for f in T2:
    ls = lines(f); cur = open(f"{WT}/{f}", encoding="utf-8").read(); head = git("show", f"HEAD:{f}")
    exp = len(ls) == 2 and ls[0][0] == "-" and ls[1][0] == "+" and 'logo-128w.webp 128w, /assets/images/optimizadas/logo-256w.webp 256w' in ls[1] and 'electricista-culiacan-pro-logo.webp' in ls[0]
    print(f"  {f[5:45]:40} lineas={len(ls)} par_esperado={exp} logo512={cur.count('src=\"/assets/images/electricista-culiacan-pro-logo.webp\"')} metas_igual={metas(cur)==metas(head)}")
print("\n== T3 (index.html):")
ls = lines("index.html"); cur = open(f"{WT}/index.html", encoding="utf-8").read(); head = git("show", "HEAD:index.html")
print(f"  lineas={len(ls)} 420w={len(re.findall(r'420w\.webp 420w', cur))} (HEAD {len(re.findall(r'420w\.webp 420w', head))}) metas_igual={metas(cur)==metas(head)}")
if len(ls) == 2:
    a, b = ls[0][1:], ls[1][1:]
    exp = b
    for base, alt in [("mantenimiento-tablero-electrico-culiacan", "Por qué se bota el breaker"), ("emergencia-electrica-culiacan", "Apagón eléctrico en Culiacán"), ("instalacion-minisplit-culiacan", "Recibo de luz alto")]:
        exp = exp.replace(f'srcset="/assets/images/optimizadas/{base}-420w.webp 420w, /assets/images/optimizadas/{base}-800w.webp 800w" sizes=', f'srcset="/assets/images/optimizadas/{base}-800w.webp 800w" sizes=')
        exp = exp.replace(f'<img src="/assets/images/optimizadas/{base}-420w.webp" alt="{alt}', f'<img src="/assets/images/optimizadas/{base}-800w.webp" alt="{alt}')
    print("  nueva línea con los 6 reemplazos deshechos == vieja:", exp == a)
