"""Añade una calificación. uso: python3 _calificar.py '<json de una línea>'"""
import sys, json
WT = "/tmp/equipo-electricista-20260925-2101"
d = json.loads(sys.argv[1])
d["total"] = d["cumplio"] + d["alcance"] + d["honestidad"] + d["evidencia"]
d["aprobado"] = d["total"] >= 7
with open(f"{WT}/.pipeline/equipo/calificaciones.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(d, ensure_ascii=False) + "\n")
print("calificado", d["agente"], d["tarea"], d["total"], "/12")
