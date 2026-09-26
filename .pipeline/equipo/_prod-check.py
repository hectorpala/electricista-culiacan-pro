"""Comprueba producción tras publicar: espera el despliegue (sonda) y luego una evidencia por tarea.
uso: python3 _prod-check.py <sonda_url> <texto_esperado_en_sonda> [checks.json]
checks.json: lista de {"url":..., "debe":[regex...], "no_debe":[regex...]}
"""
import sys, time, re, json, urllib.request

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "equipo-check", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.status, r.read().decode("utf-8", "replace")

sonda, esperado = sys.argv[1], sys.argv[2]
t0 = time.time()
ok = False
while time.time() - t0 < 150:
    try:
        code, body = get(sonda)
        if esperado in body:
            ok = True; break
    except Exception as e:
        print("sonda error", e)
    time.sleep(10)
print(f"despliegue visible: {ok} a los {int(time.time()-t0)} s")
if len(sys.argv) > 3:
    checks = json.load(open(sys.argv[3]))
    fallos = 0
    for c in checks:
        try:
            code, body = get(c["url"])
        except Exception as e:
            print("FALLA", c["url"], e); fallos += 1; continue
        probs = []
        if code != 200: probs.append(f"http {code}")
        for rx in c.get("debe", []):
            if not re.search(rx, body): probs.append(f"falta /{rx}/")
        for rx in c.get("no_debe", []):
            if re.search(rx, body): probs.append(f"sobra /{rx}/")
        print("OK  " if not probs else "FALLA", c["url"], probs)
        fallos += bool(probs)
    print(f"fallos: {fallos}/{len(checks)}")
