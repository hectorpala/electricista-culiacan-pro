# NEGOCIO.md — Fuente única de verdad del negocio

Este archivo existe para que el Auto Agente **derive** las decisiones de negocio en vez de
preguntarte cada corrida. Tú lo curas de vez en cuando (servicios, precios, políticas); la
computadora lo ejecuta continuamente. **Si algo cambia, edítalo AQUÍ y queda autónomo para
siempre.** Lo lee en la FASE 0 y lo aplica al decidir qué crear (crecimiento) y qué corregir.

> Regla madre: **"deriva, no inventes".** Si una decisión se puede resolver con ESTE archivo +
> los datos (repo/GSC), la máquina decide sola. Si NO, va a humano (cola `requiere_humano`).

## Giro
Servicios **eléctricos** residenciales y comerciales en Culiacán, Sinaloa. Todo lo que sea
ELECTRICIDAD (instalación, reparación, mantenimiento eléctrico) cae en el giro.

## Servicios que SÍ ofreces — auto-creables si hay DEMANDA real en GSC
(derivados de las páginas existentes en `servicios/`)
- Instalación eléctrica y cambio de cableado
- Instalación de contactos, apagadores e iluminación LED
- Centros de carga, tableros (mantenimiento), tierra física
- Reparación de cortocircuitos / "no hay luz en parte de la casa"
- Dictamen eléctrico y trámite de contrato de luz / medidor CFE
- Calentador eléctrico, ventiladores de techo
- **Minisplit / aire acondicionado** (instalación y reparación — parte eléctrica)
- Cámaras de seguridad, cercas eléctricas, portón eléctrico
- Paneles solares, planta de luz / generador
- Instalación eléctrica de bomba de agua (la parte eléctrica)
- Emergencias eléctricas 24/7

## Decisión de PÁGINA NUEVA  ("auto si es electricidad")
1. Query de GSC con demanda real (≥ UMBRAL_DEMANDA) que cae CLARAMENTE en ELECTRICIDAD (lista de
   arriba o un vecino directo del giro, p.ej. "regulador de voltaje", "no-break", "timbre/interfón")
   → **CREAR sola** (riesgo medio, auto). Pasa por todos los candados.
2. Query FUERA de electricidad (plomería de tubo/agua, albañilería, herrería, jardinería…) o
   **ambigua** → **NO crear**: encólala riesgo **alto** (`requiere_humano`) para que el dueño decida.
3. Ante la duda de si algo "es electricidad" → trátalo como ambiguo (riesgo alto), nunca lo fuerces.

## Servicios que NO ofreces  (jamás crear; si hay demanda, va a humano)
<!-- Curado por el dueño. Agrega aquí lo que NO haces aunque la gente lo busque. -->
- **Eléctrico AUTOMOTRIZ** (instalación/reparación eléctrica de autos). Confirmado por el dueño
  2026-06-22: NO se ofrece, aunque GSC muestre demanda ("eléctrico automotriz a domicilio" ~32 impr,
  pos 2.9). JAMÁS crear página de este servicio; si aparece la query, ignorar (no escalar a humano,
  ya está decidido).

## ANTI-FUGA (este sitio es CLON adaptado — al revés que el plomero)
- La palabra **"plomero"/"plomería"** y cualquier branding/GTM/email de plomería **JAMÁS** deben
  aparecer en este sitio. El email correcto es **contacto@electricistaculiacanpro.mx** (NUNCA un
  email con "plomero"). Si una query es de plomería pura (agua/tubería) → humano, no es tu giro.

## Precios
- **NUNCA** precio visible en el cuerpo. Lenguaje: "cotización sin costo / cotización clara".
  Las cifras solo en JSON-LD (priceRange/offers). No inventar precios nuevos.

## Contenido / año
- Unificar el año visible al **año actual** es seguro por defecto (freshness), SIEMPRE que no
  implique afirmar precios nuevos. `datePublished` NO se toca; `dateModified` = hoy si editas.

## Datos fijos (derivados, no inventar)
- Contacto: **contacto@electricistaculiacanpro.mx** · tel/WhatsApp = el de la home (NAP).
- Anti-doorway: Jaccard < 0.80 (lo bloquea `gate-pagina.py`).
- Marca: azul eléctrico (la home `index.html` es la fuente de verdad del estilo).
