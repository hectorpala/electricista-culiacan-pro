#!/usr/bin/env python3
"""Stage SOLO T1 (bump CSS site-wide): todos los archivos modificados salvo .pipeline/equipo/*;
para los archivos COMPARTIDOS con T2/T3 se stagea HEAD + solo el token ?v= nuevo (hash-object + update-index).
Uso: python3 _stage-T1.py            (stagea y muestra verificación)"""
import subprocess, re, sys
WT = "/tmp/equipo-electricista-20261008-2100"
SHARED = ["blog/ahorro-energia-iluminacion-led/index.html", "blog/seguridad-electrica-temporada-lluvias/index.html",
          "blog/cuando-llamar-electricista-emergencia/index.html", "blog/senales-instalacion-electrica-obsoleta/index.html",
          "blog/mantenimiento-tablero-electrico-preventivo/index.html", "gracias/index.html"]
def git(*a, inp=None):
    return subprocess.run(["git", "-C", WT, *a], input=inp, capture_output=True, text=True, check=True).stdout
home = open(f"{WT}/index.html", encoding="utf-8").read()
tok = sorted(set(re.findall(r"styles[.a-z0-9]*\.css\?v=([0-9]+)", home)))
assert len(tok) == 1 and tok[0] != "20260923", tok
tok = tok[0]
mod = [l[3:] for l in git("status", "--short").splitlines() if l and l[0:2].strip() in ("M", "??", "A") and not l[3:].startswith(".pipeline/equipo/")]
others = [f for f in mod if f not in SHARED]
# shared: HEAD + ?v= replace
for f in SHARED:
    base = git("show", f"HEAD:{f}")
    new = base.replace("css?v=20260923", f"css?v={tok}")
    assert new != base, f
    sha = git("hash-object", "-w", "--stdin", inp=new).strip()
    git("update-index", "--cacheinfo", f"100644,{sha},{f}")
# others: add
for i in range(0, len(others), 200):
    git("add", "--", *others[i:i+200])
# verify
st = git("diff", "--cached", "--stat").splitlines()[-1]
print("cached:", st, "| token", tok, "| others", len(others), "| shared", len(SHARED))
d = git("diff", "--cached", "-U0", "--", *SHARED)
lines = [l for l in d.splitlines() if l and l[0] in "+-" and not l.startswith(("+++", "---"))]
bad = [l for l in lines if "css?v=" not in l]
print("líneas -/+ en compartidos:", len(lines), "| sin ?v= (debe ser 0):", len(bad))
for l in bad[:5]: print("  ", l[:120])
unst = [l for l in git("status", "--short").splitlines() if l and not l.startswith("M ") and not l[3:].startswith(".pipeline/equipo/")]
print("quedan sin stagear (deben ser solo los 6 compartidos con cambios de T2/T3, o nada):")
for l in unst: print("  ", l)
sys.exit(1 if bad else 0)
