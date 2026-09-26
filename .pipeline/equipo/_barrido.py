"""Barrido del coordinador: invariantes servidas + metas en todas las páginas HTML de un rango de commits.
uso: python3 _barrido.py <worktree> <puerto> <rango git, ej. origin/main..HEAD>
"""
import sys, subprocess, re, json, urllib.request, html

wt, port, rango = sys.argv[1], sys.argv[2], sys.argv[3]
files = subprocess.run(["git", "-C", wt, "diff", "--name-only", rango], capture_output=True, text=True).stdout.split()
htmls = [f for f in files if f.endswith(".html")]
ETA_RE = re.compile(r"\b(\d{2})\s*(?:-|a|–)\s*(\d{2,3})\s*min", re.I)
fallas = []
rows = []
for f in htmls:
    url = f"http://127.0.0.1:{port}/" + f[:-len("index.html")] if f.endswith("index.html") else f"http://127.0.0.1:{port}/" + f
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            code, body = r.status, r.read().decode("utf-8", "replace")
    except Exception as e:
        fallas.append((f, f"HTTP {e}")); rows.append((f, "ERR")); continue
    p = []
    if code != 200: p.append(f"http {code}")
    for m in re.finditer(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', body, re.S):
        try: json.loads(m.group(1))
        except Exception as e: p.append(f"jsonld {e}")
    def meta(pat):
        m = re.search(pat, body, re.I); return html.unescape(m.group(1)).strip() if m else None
    canon = meta(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"')
    ogu = meta(r'<meta[^>]+property="og:url"[^>]+content="([^"]+)"')
    twu = meta(r'<meta[^>]+name="twitter:url"[^>]+content="([^"]+)"')
    if not (canon and canon == ogu and (twu is None or twu == canon)): p.append(f"urls canon={canon} og={ogu} tw={twu}")
    if re.search(r"plomer", body, re.I): p.append("plomero")
    for e in set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", body)):
        if e != "contacto@electricistaculiacanpro.mx" and not e.endswith(".webp") and not e.endswith(".png"): p.append(f"email {e}")
    for t in set(re.findall(r"wa\.me/(\d+)", body)):
        if t != "526673922273": p.append(f"wa {t}")
    for t in set(re.findall(r'tel:\+?(\d+)', body)):
        if t not in ("526673922273", "6673922273"): p.append(f"tel {t}")
    for a, b in set(ETA_RE.findall(body)):
        if (a, b) != ("30", "60"): p.append(f"eta {a}-{b}")
    if re.search(r"Ã|Â|�", body): p.append("mojibake")
    title = meta(r"<title>(.*?)</title>")
    desc = meta(r'<meta[^>]+name="description"[^>]+content="([^"]*)"')
    ogt = meta(r'<meta[^>]+property="og:title"[^>]+content="([^"]*)"')
    ogd = meta(r'<meta[^>]+property="og:description"[^>]+content="([^"]*)"')
    twd = meta(r'<meta[^>]+name="twitter:description"[^>]+content="([^"]*)"')
    rows.append((f, "OK" if not p else "FALLA", len(title or ""), len(desc or ""), ogt == title, ogd == desc, twd == desc))
    if p: fallas.append((f, p))
print(f"páginas: {len(htmls)}  fallan: {len(fallas)}")
for r in rows: print(r)
for f, p in fallas: print("FALLA", f, p)
