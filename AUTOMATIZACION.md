# Sistema de automatización — Electricista Culiacán

## 🤖 Auto Agente Electricista (todo el sistema junto, 1 corrida diaria)

**Auto Agente Electricista** es el sistema completo corriendo solo, sin supervisión, una vez
al día (18:20). En una sola corrida hace CUATRO trabajos:

| Fase | Qué hace |
|---|---|
| **A) Corrige** | Errores **mecánicos** (CSS, links/imágenes rotas, schema, CLS…) **y humanos/de contenido** (ortografía, caracteres mal codificados, claims que violan reglas, email contaminado) — reescritos bien y por completo. |
| **B) Crece** | Hasta **3 páginas nuevas al día según Google Search Console** (MCP): detecta huecos con datos reales (impresiones sin página propia) y los llena. 0 si no hay señal — nunca fuerza doorways. |
| **C) Verifica** | Un **agente verificador** independiente y escéptico re-corre los candados y carga cada página tocada para demostrar que **todo quedó bien** ANTES de publicar. Si algo falla, no publica. |
| **D) Aprende** | Un **agente aprendiz** convierte cada error en una **regla permanente** (REGLAS.md) y, si es mecanizable, en un **checker** — para que ese error no se repita. El sistema se vuelve más inteligente con cada corrida. |

Solo publica si pasa TODOS los candados (verificador ok + diff acotado + sin borrados raros) y
sincronizando con el remoto (jamás `git push --force`). Te manda el **parte por email** siempre.

**Piezas:** `.pipeline/crecer-diario-prompt.txt` (las 10 fases) · `.pipeline/crecer-diario.sh` (driver) ·
`.pipeline/launchd/com.electricistaculiacan.autoagente.plist` (horario 18:20).

**Activar** (reemplaza al viejo job de solo-mantenimiento para no correr ambos):
```bash
launchctl unload ~/Library/LaunchAgents/com.electricistaculiacan.mantener.plist 2>/dev/null
cp ".pipeline/launchd/com.electricistaculiacan.autoagente.plist" ~/Library/LaunchAgents/
launchctl load  ~/Library/LaunchAgents/com.electricistaculiacan.autoagente.plist
launchctl start com.electricistaculiacan.autoagente   # opcional: probar una corrida YA
```

---

## Mapa técnico

Hay **dos capas**: el **cerebro** (un skill LLM que decide y usa el MCP de Google) y el
**motor determinista** (scripts que garantizan calidad y hacen el trabajo mecánico).

```
  /expandir-sitio (SKILL)          ← decide QUÉ hacer (audita GSC, prioriza)  [LLM + MCP]
        │
        ▼
  scripts/crecer.py (ORQUESTADOR)  ← hace el flujo de punta a punta            [determinista]
        ├── scripts/crear-servicio.py ──┐
        ├── scripts/diferenciar-colonia.py ─┤→ .pipeline/gen-landing.py  (genera con anti-drift)
        ├── wiring: sitemap + enlace home + sw.js
        ├── .pipeline/gate-pagina.py    ← candado (validate + checkers + anti-doorway)
        └── publicar: rama → commit → merge → push
                                          │
                                          ▼
                            hooks/pre-commit (gate) · hooks/pre-push (auto-indexa GSC)
                                          │
                                          ▼
                            ESTADO.md · HISTORIAL.jsonl · REGLAS.md  (memoria)
```

## El orquestador: `scripts/crecer.py` (punto de entrada)
Un solo CLI que une todo y automatiza el "plomería" que antes era manual.

| Comando | Qué hace |
|---|---|
| `python3 scripts/crecer.py estado` | Dashboard: nº de servicios, colonias (total/indexables), blogs, URLs en sitemap, sw, último commit, candados. |
| `python3 scripts/crecer.py servicio spec.json` | Crea servicio **+ sitemap + enlace en la home + bump sw + candado**, todo automático. |
| `python3 scripts/crecer.py colonia spec.json` | Promueve colonia noindex→indexable **+ sitemap + candado**. |
| `python3 scripts/crecer.py gate <ruta>` | Atajo al candado. |
| `python3 scripts/crecer.py publicar "msg"` | Rama → commit → merge `--no-ff` → push (el pre-push **auto-indexa** en Google). |

Specs de contenido (qué editar):
- `python3 scripts/crear-servicio.py --ejemplo > spec.json`
- `python3 scripts/diferenciar-colonia.py --ejemplo > spec.json`

## Las piezas (todas versionadas en el repo)

**Cerebro (decide):**
- `.claude/skills/expandir-sitio/SKILL.md` — agente de crecimiento (`/expandir-sitio`). Audita huecos con datos reales de GSC (MCP), prioriza con tope `MAX_PAGINAS=3`, y dispara el orquestador. **La auditoría GSC y la indexación por MCP viven aquí** (necesitan el MCP).
- `.claude/skills/mantener-sitio/SKILL.md` — hermano que *arregla* lo existente (`/mantener-sitio`).

**Motor determinista (hace y garantiza):**
- `.pipeline/gen-landing.py` — genera una página copiando un esqueleto byte a byte + sustituciones afirmadas (aborta ante drift o fuga "plomero").
- `.pipeline/gate-pagina.py` — candado: validate-landing + ci-gate (0 ALTA) + anti-doorway (Jaccard < 0.80).
- `.pipeline/ci-gate.py` + `check-plantilla.py` + `check-indexabilidad.py` — checkers.
- `scripts/crear-servicio.py` · `scripts/diferenciar-colonia.py` — generadores de contenido reusables (specs JSON).

**Guardas y publicación:**
- `hooks/pre-commit` — corre ci-gate + valida landings de servicio (omite blogs y colonias).
- `hooks/pre-push` — auto-indexa en Google las URLs nuevas (encola lo que rebasa la cuota diaria, reintenta solo).

**Memoria:**
- `REGLAS.md` (errores que NO repetir + estándares: hero-CTA, garantía 30-90 días, alcance del negocio) · `ESTADO.md` (estado de cada corrida) · `HISTORIAL.jsonl` (un hallazgo por línea).

## Flujo típico (cómo se usa todo junto)
1. **Decidir:** `/expandir-sitio` audita GSC y propone el hueco de mayor valor (o tú decides un servicio/colonia).
2. **Spec:** `crear-servicio.py --ejemplo > spec.json` y lo llenas con el contenido único.
3. **Construir+gatear (1 comando):** `crecer.py servicio spec.json` → crea, cablea (sitemap/enlace/sw) y pasa el candado.
4. **Publicar (1 comando):** `crecer.py publicar "feat: ..."` → rama+merge+push, y el hook auto-indexa.
5. **Medir:** a las 2-3 semanas, revisar en GSC (vía el skill) qué quedó indexado y qué jala llamadas.

## Reglas duras que el sistema respeta siempre
- **Anti-doorway:** el candado bloquea cualquier página con Jaccard ≥ 0.80 vs una hermana.
- **Paridad de plantilla:** toda página replica `index.html` (hero de 2 botones, etc.) — garantizado por construcción.
- **Solo servicios reales:** no se crean páginas de servicios que el negocio no ofrece (decisión del dueño; ver REGLAS.md, p.ej. NO automotriz).
- **Sin claims engañosos:** garantía 30-90 días, sin "se pagan solos"/"sin riesgos", dictamen no promete certificado de UVIE.
