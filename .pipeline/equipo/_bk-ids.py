#!/usr/bin/env python3
"""Muestra estado/firma de ids del backlog. uso: python3 _bk-ids.py id1 id2 ..."""
import json, sys
WT = "/tmp/equipo-electricista-20261014-2100"
ids = set(sys.argv[1:])
for l in open(f"{WT}/BACKLOG.jsonl", encoding="utf-8"):
    d = json.loads(l)
    if d.get("id") in ids:
        print(d["id"], d["estado"], d["tipo"], "|", d["objetivo"][:100])
