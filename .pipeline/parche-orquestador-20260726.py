#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Porta al Electricista los 4 arreglos del orquestador hechos en el Plomero el 2026-07-26.

Problema que cierran (visto en plomero el 07-11 y el 07-26): el CLI en modo -p mata las
tareas en background a los 600s y AUN ASI sale con codigo 0. El driver leia ese 0 como
exito -> mandaba por correo el parte del dia ANTERIOR diciendo "publicado", marcaba
last-run-day (el catch-up ya no rescataba nada) y el trabajo quedaba sin commitear.

Es IDEMPOTENTE: si un parche ya esta aplicado lo salta. Verifica la sintaxis con `bash -n`
y RESTAURA el respaldo si algo queda mal.

  python3 parche-orquestador-20260726.py --dry-run   # dice que haria, no escribe
  python3 parche-orquestador-20260726.py             # aplica
"""
import datetime
import os
import shutil
import subprocess
import sys

SH = "/Users/openclaw/Sitios Web/Electricista Culiacán/.pipeline/crecer-diario.sh"
PARTE = "/Users/openclaw/Sitios Web/Electricista Culiacán/.pipeline/ultima-corrida.md"

PARCHES = [
    (
        "1/4 no cortar las tareas en background a los 600s",
        'export NODE_OPTIONS="--dns-result-order=ipv4first"',
        'export NODE_OPTIONS="--dns-result-order=ipv4first"\n'
        '\n'
        '# NO cortar las tareas en background a los 600s. El CLI en modo -p espera por defecto\n'
        '# solo 10 min a los subagentes lanzados en background y luego imprime "Background tasks\n'
        '# still running after 600s; terminating" y SALE CON CODIGO 0, con el verificador a medias.\n'
        '# Con 0 espera indefinidamente; el freno real es el TIMEOUT_MIN de abajo.\n'
        'export CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0',
        "CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS",
    ),
    (
        "2/4 codigo de salida 0 no prueba que la corrida termino",
        '    CLAUDE_OK=1; FAIL_KIND=""; break',
        '    # Codigo de salida 0 NO prueba que la corrida termino: el CLI tambien sale 0 cuando MATA\n'
        '    # las tareas en background vivas (tipicamente el verificador). Si eso paso, las fases\n'
        '    # finales (publicar, aprender, escribir el parte) nunca corrieron -> NO es exito.\n'
        '    OUTATT=$(tail -c "+$((OFF + 1))" "$LOG" 2>/dev/null || echo "")\n'
        '    if printf \'%s\' "$OUTATT" | grep -q "Background tasks still running"; then\n'
        '      FAIL_KIND="incompleta"\n'
        '      echo "[$STAMP] Salio con codigo 0 pero corto tareas en background: las fases finales '
        '(verificar/publicar/parte) NO terminaron; no cuenta como exito." >> "$LOG"\n'
        '      break\n'
        '    fi\n'
        '    CLAUDE_OK=1; FAIL_KIND=""; break',
        "Background tasks still running",
    ),
    (
        "3/4 candado de frescura del parte",
        '# Parte por email. Si la corrida tuvo ÉXITO (Claude o respaldo Codex) → manda el parte nuevo.',
        '# CANDADO DE FRESCURA (independiente del LLM): el parte solo vale si lo escribio ESTA corrida.\n'
        '# Si su fecha de modificacion es anterior al arranque, la corrida murio antes de la ultima fase\n'
        '# y mandarlo seria un correo FALSO (caso plomero 2026-07-26: llego el parte del dia anterior\n'
        '# diciendo "publicado" mientras el trabajo seguia sin commitear).\n'
        'if [ "${CLAUDE_OK:-0}" = 1 ] || [ "${CODEX_OK:-0}" = 1 ]; then\n'
        '  PARTE_MTIME=$(stat -f %m "' + PARTE + '" 2>/dev/null || echo 0)\n'
        '  if [ "$PARTE_MTIME" -lt "$RUN_START" ]; then\n'
        '    echo "[$STAMP] El parte no se reescribio en esta corrida (mtime $PARTE_MTIME < inicio '
        '$RUN_START): no llego a la fase final; NO mando el parte viejo." >> "$LOG"\n'
        '    CLAUDE_OK=0; CODEX_OK=0; FAIL_KIND="incompleta"\n'
        '  fi\n'
        'fi\n'
        '\n'
        '# Parte por email. Si la corrida tuvo ÉXITO (Claude o respaldo Codex) → manda el parte nuevo.',
        "CANDADO DE FRESCURA",
    ),
    (
        "4/4 motivo honesto para la corrida incompleta",
        '    timeout)',
        '    incompleta)\n'
        '      MOTIVO="la corrida hizo trabajo pero NO llego a terminarlo (se corto en la revision final, '
        'antes de publicar y de escribir el parte del dia)"\n'
        '      SUGERENCIA="El trabajo NO se perdio: quedo guardado en la rama de la corrida. La proxima '
        'corrida lo retoma. Log: $LOG" ;;\n'
        '    timeout)',
        "incompleta)",
    ),
]


def corrida_viva():
    r = subprocess.run(["pgrep", "-fl", "crecer-diario.sh"], capture_output=True, text=True)
    return [l for l in r.stdout.splitlines() if "Electricista" in l]


def main():
    dry = "--dry-run" in sys.argv
    if not os.path.exists(SH):
        sys.exit("no encuentro %s" % SH)

    vivas = corrida_viva()
    if vivas and not dry:
        sys.exit("ABORTO: la corrida del Electricista sigue viva (%s). Editar el .sh mientras "
                 "bash lo lee por offset lo corrompe." % vivas[0].split()[0])

    original = open(SH, encoding="utf-8").read()
    h = original
    hechos, saltados = [], []
    for nombre, ancla, reemplazo, marca in PARCHES:
        if marca in h:
            saltados.append(nombre)
            continue
        if h.count(ancla) != 1:
            sys.exit("ABORTO: el ancla de '%s' aparece %d veces (esperaba 1). El script cambio; "
                     "reviso a mano." % (nombre, h.count(ancla)))
        h = h.replace(ancla, reemplazo, 1)
        hechos.append(nombre)

    if not hechos:
        print("Nada que hacer: los 4 parches ya estaban aplicados.")
        return 0

    if dry:
        print("DRY-RUN. Aplicaria:")
        for n in hechos:
            print("   + " + n)
        for n in saltados:
            print("   = ya aplicado: " + n)
        print("(%d bytes -> %d bytes)" % (len(original), len(h)))
        return 0

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    respaldo = SH + ".respaldo-" + stamp
    shutil.copy2(SH, respaldo)
    open(SH, "w", encoding="utf-8").write(h)

    chk = subprocess.run(["bash", "-n", SH], capture_output=True, text=True)
    if chk.returncode != 0:
        shutil.copy2(respaldo, SH)
        sys.exit("SINTAXIS ROTA -> restaure el respaldo. Error: %s" % chk.stderr.strip())

    for n in hechos:
        print("   + " + n)
    for n in saltados:
        print("   = ya aplicado: " + n)
    print("OK: sintaxis valida. Respaldo en %s" % respaldo)
    return 0


if __name__ == "__main__":
    sys.exit(main())
