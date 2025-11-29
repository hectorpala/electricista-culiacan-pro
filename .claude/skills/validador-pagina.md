# Skill: Validador de Página

Soy un asistente especializado en validar páginas web contra las reglas de [@.claude/commands/landing-creator.md](.claude/commands/landing-creator.md).

## Cuándo activarme

El usuario me activa escribiendo `@validador-pagina` o mencionándome en cualquier parte del mensaje.

## Mi trabajo

Cuando me activan, sigo estos pasos EXACTAMENTE:

## IMPORTANTE - Qué valido y qué NO valido

**SÍ valido (estructura técnica):**
- Estructura HTML (`<picture>`, `<source>`, atributos correctos)
- Clases CSS correctas (`.floating-btn`, `.hero-background`, etc.)
- Presencia de elementos críticos (botones flotantes con SVG, Critical CSS completo)
- Atributos técnicos (`fetchpriority`, `decoding`, `srcset`, `sizes`)
- Prohibiciones (NO custom classes, NO emojis en botones)

**NO valido (diseño/branding):**
- Colores específicos en variables CSS (`:root`)
- Valores de gradientes
- Tamaños de fuente
- Espaciado (padding, margin)
- Contenido textual

**Branding - NO se valida ni se cambia:**

Electricista Culiacán Pro y Plomero Culiacán Pro son empresas hermanas con IDENTIDAD VISUAL IDÉNTICA:
- Colores naranja (#E36414, #F97316) son CORRECTOS para ambas empresas
- Gradientes son IDÉNTICOS por diseño corporativo
- Logos tienen el mismo estilo visual
- Solo cambia el contenido textual (plomero → electricista)

**Por lo tanto, este validador:**
- Verifica que los botones flotantes tengan las clases correctas
- Verifica que exista el Critical CSS completo
- NO cambia los colores (ya son los correctos)
- NO modifica variables CSS de branding

### Paso 1: Preguntar qué validar

```
Validador de Página Activado

¿Qué página quieres validar?

Ejemplos:
  - blog/como-encontrar-electricista-confiable-culiacan/index.html
  - electricista-24-horas/index.html
  - servicios/instalacion-electrica/index.html
```

Esperar la respuesta del usuario.

### Paso 2: Leer archivos necesarios

Una vez que el usuario proporcione la ruta, leer en paralelo:
1. `index.html` (homepage de referencia)
2. La página proporcionada por el usuario

### Paso 3: Validar según reglas críticas

Verificar las 14 áreas siguientes (basadas en @.claude/commands/validar.md y landing-creator.md):

#### 3.1 Hero - Estructura (CRÍTICO)

Buscar `<header` con clase `hero` en la página nueva:

**REQUISITOS OBLIGATORIOS:**
- DEBE usar `<picture class="hero-background">` (NO `<div>`)
- DEBE tener `<source type="image/webp">` con srcset
- DEBE tener `fetchpriority="high"` y `decoding="async"` en `<img>`
- Imagen DEBE ser `hero-electricista-trabajo-800w.webp` y `1200w.webp` (o la que especifique usuario)

**Si encuentra error:** Anotar línea exacta y qué está mal. FALLA AUTOMÁTICA.

#### 3.2 Hero - CSS (CRÍTICO)

Buscar en el `<style>` la regla `.hero-background img`:

**OBLIGATORIO:**
- DEBE incluir `content-visibility:auto`

**Si falta:** Anotar línea y CSS faltante. FALLA AUTOMÁTICA.

#### 3.3 Botones Flotantes - HTML (CRÍTICO)

Buscar antes del cierre `</body>`:

**REQUISITOS ESTRICTOS:**
- Botón WhatsApp DEBE tener clase `floating-btn floating-whatsapp`
- Botón Teléfono DEBE tener clase `floating-btn floating-call`
- Ambos DEBEN contener `<svg>` con `<path>` (PROHIBIDO usar emojis)
- PROHIBIDO que estén dentro de `<div class="cta-bar">`

**Si encuentra error:** Anotar línea exacta. FALLA AUTOMÁTICA.

#### 3.4 Botones Flotantes - CSS (CRÍTICO)

Buscar en el `<style>`:

**COLORES OBLIGATORIOS:**
- `.floating-whatsapp` DEBE ser `background:#22c55e`
- `.floating-call` DEBE ser `background:#0f4fa8`

**COLORES PROHIBIDOS (FALLA AUTOMÁTICA):**
- PROHIBIDO: #25D366 (WhatsApp incorrecto)
- PROHIBIDO: #0066cc (Tel incorrecto)

**Si encuentra error:** Anotar línea y color incorrecto. FALLA AUTOMÁTICA.

#### 3.5 Clases CSS Custom Prohibidas

Buscar en el `<style>`:

**ESTRICTAMENTE PROHIBIDO (FALLA AUTOMÁTICA SI EXISTE):**
- `.highlight-box`
- `.warning-box`
- `.info-box`
- `.note-box`
- `.alert-box`
- Cualquier clase con `background:#fef3c7` (amarillo)
- Cualquier clase con `background:#fee2e2` (rojo)
- Cualquier clase con `border-left: 4px solid`

**Si encuentra alguna:** Anotar línea exacta. FALLA AUTOMÁTICA.

#### 3.6 HTML con Cajas de Colores

Buscar en el `<body>`:

**ESTRICTAMENTE PROHIBIDO (FALLA AUTOMÁTICA SI EXISTE):**
- `<div class="highlight-box">`
- `<div class="warning-box">`
- Divs con `style="background:#fef3c7"` inline

**Si encuentra alguna:** Anotar línea exacta. FALLA AUTOMÁTICA.

#### 3.7 Critical CSS Completo (CRÍTICO)

Buscar en el `<style>` del `<head>`:

**OBLIGATORIO - DEBE incluir TODO (mínimo 40+ líneas):**
- `@font-face` para Inter (400, 500, 600)
- `@font-face` para Montserrat (700, 800)
- `:root` con variables CSS
- Reset CSS (`*{margin:0;padding:0;...}`)
- `body` con font-family, padding-top
- `.container` con max-width, margin
- `.nav` con position:fixed
- `.logo` y `.logo img`
- `.hero{display:grid;place-items:center;text-align:center;...}`
- `.hero-background` con position:absolute
- `.hero-background img` con object-fit, content-visibility
- `.hero-content{margin:0 auto;...}`
- `.btn-primary` con gradient
- `.floating-btn`, `.floating-call`, `.floating-whatsapp`
- `@media (max-width:768px)` con responsive completo

**ERRORES QUE CAUSAN FALLA AUTOMÁTICA:**
- Solo 3-10 líneas de CSS (incompleto) - FALLA
- Falta `@font-face` (fuentes no cargan) - FALLA
- Falta `:root` (variables no definidas) - FALLA
- Falta `.hero{display:grid;place-items:center}` (desalineación) - FALLA
- Falta `@media` queries (roto en mobile) - FALLA

**Si falta CSS crítico:** Anotar que falta bloque completo de index.html. FALLA AUTOMÁTICA.

#### 3.8 Service Cards - Estructura (CRÍTICO)

Buscar en las secciones de servicios (id="servicios" o similares):

**ESTRUCTURA OBLIGATORIA (de index.html):**
```html
<a href="..." class="card card--img">
    <div class="service-card">
        <figure class="media-box">
            <picture>
                <source type="image/webp"
                        srcset="...420w.webp 420w, ...800w.webp 800w"
                        sizes="(max-width:768px) 100vw, 420px">
                <img src="...420w.webp"
                     srcset="...420w.webp 420w, ...800w.webp 800w"
                     sizes="(max-width:768px) 100vw, 420px"
                     alt="..."
                     width="420" height="420"
                     loading="lazy" decoding="async">
            </picture>
        </figure>
    </div>
    <h3>Título del Servicio</h3>
    <p>Descripción del servicio...</p>
    <ul class="service-list">
        <li>Punto 1</li>
        <li>Punto 2</li>
    </ul>
    <span class="service-cta">Más Información →</span>
</a>
```

**REQUISITOS ESTRICTOS (CERO TOLERANCIA):**
- DEBE usar `<div class="service-card">` como contenedor de la imagen
- DEBE usar `<figure class="media-box">` para envolver el picture
- Imágenes DEBEN ser 420w y 800w (PROHIBIDO 800w y 1200w)
- DEBE ser width="420" height="420" - IMÁGENES CUADRADAS (PROHIBIDO 420x235, 800x600 u otros tamaños)
- sizes DEBE ser "(max-width:768px) 100vw, 420px" (EXACTO, sin variaciones)
- `<h3>` PROHIBIDO usar emojis (NO: "Instalación", SI: "Instalación")
- DEBE usar `<ul class="service-list">` (PROHIBIDO estilos inline)
- DEBE tener `<span class="service-cta">Más Información →</span>` al final
- PROHIBIDO `style="text-decoration:none;color:inherit;display:block"` en `<a>`
- PROHIBIDO `style="padding:1.5rem"` en divs custom
- PROHIBIDO `style="color:var(--brand)"` en h3
- PROHIBIDO `style="border-radius:12px..."` en imágenes

**ESTRUCTURA INCORRECTA (FALLA AUTOMÁTICA):**
```html
<!-- INCORRECTO: Sin service-card/media-box, con emojis, estilos inline -->
<a href="..." class="card card--img" style="text-decoration:none;color:inherit">
    <picture>
        <img src="...800w.webp" width="800" height="600"
             style="border-radius:12px;width:100%;height:auto">
    </picture>
    <div style="padding:1.5rem">
        <h3 style="color:var(--brand)">⚡ Instalación Eléctrica</h3>
        <ul style="margin-top:1rem;color:#475569">
            <li>Punto 1</li>
        </ul>
    </div>
</a>
```

**ERRORES CRÍTICOS (FALLA AUTOMÁTICA):**
- Falta `<div class="service-card">` y `<figure class="media-box">` - FALLA
- Usa emojis en títulos h3 - FALLA
- Imágenes con tamaño incorrecto (NO CUADRADAS: 420x235, 800x600 en vez de 420x420 SQUARE) - FALLA
- Srcset incorrecto (usa 800w/1200w en vez de 420w/800w) - FALLA
- Falta `<span class="service-cta">` al final - FALLA
- Usa estilos inline custom en vez de clases - FALLA
- NO usa class="service-list" en las `<ul>` - FALLA

**Si encuentra error:** Anotar línea exacta y mostrar estructura incorrecta vs correcta. FALLA AUTOMÁTICA.

#### 3.9 Benefits Section y Barra WhatsApp CTA (OBLIGATORIO)

Buscar en el `<body>` la sección "¿Por qué elegirnos?" con clase `.benefits-grid`:

**BENEFITS STRUCTURE - OBLIGATORIO:**
- Cada benefit DEBE usar `<div class="benefit-icon">` con SVG dentro (NO emojis)
- Cada benefit DEBE usar `<div class="benefit-content">` para h3 y p
- PROHIBIDO usar emojis grandes (⚡💡🛡️⚙️) con `style="font-size:3rem"`
- DEBE usar iconos SVG de plomero culiacan pro (reloj, dinero, herramienta, documento)
- HTML debe estar minificado (sin indentación extra)

**WHATSAPP CTA BOX - OBLIGATORIO:**
- Tiene `<div class="whatsapp-cta-box">` presente
- Contiene heading: "¿Tienes dudas? Respondemos en 10 minutos"
- Tiene botón con clase `whatsapp-cta-button` y texto "Abrir Chat"
- Link apunta a: `https://wa.me/526673922273?text=...` (electricista)
- Está ubicado dentro de `.benefits-grid` (después de los 4 benefits)
- Usa SVG para iconos (NO emojis)

**ERRORES CRÍTICOS (FALLA AUTOMÁTICA):**
- Benefits usan emojis (⚡💡🛡️) en vez de SVG icons - FALLA
- NO usa estructura `.benefit-icon` + `.benefit-content` - FALLA
- Falta completamente el elemento `.whatsapp-cta-box` - FALLA
- Texto del heading incorrecto o abreviado - FALLA
- Botón no dice "Abrir Chat" - FALLA
- Link no apunta a WhatsApp correcto (526673922273) - FALLA
- Ubicado fuera de `.benefits-grid` - FALLA

**Si falta o está mal:** Anotar línea exacta y qué falta/está incorrecto.

#### 3.10 Sección Blog (OBLIGATORIO en homepage)

Buscar en el `<body>` la sección con `id="blog"`:

**OBLIGATORIO - DEBE cumplir:**
- Tiene `<section id="blog" class="section">`
- Usa estructura `service-card` (NO `news-card`)
- Cada artículo es un `<a href="/blog/.../" class="card card--img">`
- Dentro tiene `<div class="service-card">` con `<figure class="media-box">`
- Imágenes usan `<picture>` con `<source type="image/webp">`
- Tiene `<span class="service-cta">Leer artículo completo →</span>`
- Mínimo 3 artículos de blog

**ERRORES CRÍTICOS (FALLA AUTOMÁTICA):**
- Usa estructura `news-card` antigua - FALLA
- No tiene `service-cta` en los artículos - FALLA
- Imágenes no usan picture/source - FALLA
- Menos de 3 artículos - FALLA

**Si falta o está mal:** Anotar línea exacta.

#### 3.11 Sección Testimoniales (OBLIGATORIO en homepage)

Buscar en el `<body>` la sección "Lo que dicen nuestros clientes":

**OBLIGATORIO - DEBE cumplir:**
- Tiene sección con clase `testimonials`
- Usa grid con `testimonial-grid`
- Cada testimonio es `testimonial-card`
- Tiene estrellas (⭐⭐⭐⭐⭐ o SVG stars)
- Incluye nombre del cliente y colonia
- Mínimo 3 testimonios

**CSS DEBE incluir:**
```css
.testimonials{padding:4rem 0;background:#ffffff}
.testimonial-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:2rem}
.testimonial-card{background:#ffffff;padding:2rem;border-radius:16px;box-shadow:0 4px 24px rgba(0,0,0,0.1);border-left:4px solid var(--brand)}
```

**Si falta o está mal:** Anotar línea exacta.

#### 3.12 Sección Social Proof (OBLIGATORIO en homepage)

Buscar la sección "Prueba Real de Nuestro Servicio":

**OBLIGATORIO - DEBE cumplir:**
- Tiene `<section class="social-proof">`
- Subsección "Reseñas Verificadas Google" con `google-reviews-grid`
- Subsección "Resultados Reales: Antes y Después" con `before-after-grid`
- Usa imágenes WebP optimizadas
- Tiene badges/labels en cada imagen

**CSS DEBE incluir:**
```css
.social-proof{background:linear-gradient(135deg,#f8fafc 0%,#e0f2fe 100%);padding:4rem 1.5rem;margin:3rem 0}
.google-reviews-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:2rem}
.before-after-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:2rem}
```

**Si falta o está mal:** Anotar línea exacta.

#### 3.13 Formulario Contacto con Validación (CRÍTICO)

Buscar formulario con `id="contact-form"`:

**HTML DEBE cumplir:**
- Form tiene atributos: `id="contact-form"` `method="POST"` `netlify`
- Campos: `nombre`, `telefono`, `email`, `mensaje` (con IDs correctos)
- Cada campo envuelto en `<div class="form-field">`
- Cada campo tiene `<span class="error-message">` y `<span class="success-message">`
- Botón submit tiene `disabled` inicial
- Tiene `<p class="form-note">` con texto respuesta 30 minutos

**CSS DEBE incluir (en head styles):**
```css
.form-field{position:relative;margin-bottom:1.25rem}
.form-field.valid input,.form-field.valid textarea{border-color:#28a745;background-image:url("data:image/svg+xml,%3Csvg...")}
.form-field.invalid input,.form-field.invalid textarea{border-color:#dc3545;background-image:url("data:image/svg+xml,%3Csvg...")}
.error-message{display:none;color:#dc3545}
.form-field.invalid .error-message{display:block}
.success-message{display:none;color:#28a745}
.form-field.valid .success-message{display:block}
```

**JAVASCRIPT (main.js) DEBE incluir:**
- Función `validateField(field, validatorKey)`
- Validators para: nombre (≥2 chars), telefono (10 dígitos), email (formato), mensaje (≥10 chars)
- Event listeners en `input` y `blur` para cada campo
- Función `updateSubmitButton()` que habilita/deshabilita submit
- Multi-layer lead capture (Netlify + localStorage + GA4 + WhatsApp)

**Si falta validación JS:** Anotar que main.js no tiene validación en tiempo real.

#### 3.14 Sección Contacto - CSS Completo (CRÍTICO)

Buscar en `<style>` del head:

**DEBE incluir TODOS estos estilos:**
```css
.final-cta{text-align:center;max-width:600px;margin:0 auto 3rem;padding:2rem;background:var(--bg-card);border-radius:20px;box-shadow:0 8px 32px var(--shadow-lg);border:2px solid var(--brand)}
.cta-text{font-size:1.25rem;color:var(--text);font-weight:600;margin-bottom:0.5rem}
.cta-subtitle{font-size:1rem;color:var(--text-light);margin-bottom:2rem}
.cta-buttons{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.contact-content{display:grid;grid-template-columns:1fr 1fr;gap:3rem;max-width:900px;margin:0 auto}
.map-container{margin-top:3rem}
.map-embed{position:relative;padding-bottom:56.25%;height:0;overflow:hidden}
.whatsapp-link{color:#22c55e;text-decoration:none;font-weight:600}
```

**Media queries mobile:**
```css
@media (max-width:768px){
  .contact-content{grid-template-columns:1fr;gap:2rem}
  .cta-buttons{flex-direction:column;align-items:center}
  .cta-buttons .btn-primary,.cta-buttons .btn-secondary{width:100%;max-width:320px}
}
```

**Si falta CSS:** Anotar bloques faltantes.

### Paso 4: Generar Reporte

Presentar resultado en este formato:

```markdown
## Validación de [nombre-página]

### APROBADAS (X/14)

- Hero estructura correcta
- Hero CSS correcto
- Botones flotantes HTML correcto
- Botones flotantes CSS correcto
- Sin clases CSS custom prohibidas
- Sin cajas de colores en HTML
- Critical CSS completo incluido
- Service Cards con estructura correcta (service-card + media-box)
- Barra WhatsApp CTA presente
- Sección Blog con estructura service-card
- Sección Testimoniales completa
- Sección Social Proof completa
- Formulario Contacto con validación JS
- CSS Contacto completo (.final-cta, .contact-content, etc.)

---

### ERRORES DETECTADOS (X)

#### Error 1: [Descripción clara]
- **Archivo:** [ruta]
- **Línea:** [número exacto]
- **Encontrado:** `[código incorrecto]`
- **Debe ser:** `[código correcto]`

#### Error 2: [...]

---

## Resultado Final

**Estado:** LISTO PARA COMMIT | REQUIERE CORRECCIONES (X errores)
```

### Paso 5: Ofrecer Corrección Automática

**Si hay errores (≥1):**

```
¿Quieres que corrija los errores automáticamente? (s/n)
```

Esperar respuesta del usuario.

**Si usuario responde "s" o "si" o "sí":**

1. Usar herramienta Edit para corregir cada error
2. Después de corregir todos, volver a validar
3. Mostrar resultado de la segunda validación
4. **Abrir página localmente** usando Bash tool con comando `open` para que el usuario vea los cambios en Safari
5. **VERIFICAR VISUALMENTE en MÓVIL Y ESCRITORIO** (Paso 6)

**Si usuario responde "n" o "no":**

```
Entendido. Los errores quedan documentados arriba.
Puedes corregirlos manualmente o pedirme "corrige" cuando estés listo.
```

**Si NO hay errores (0):**

1. **Abrir página localmente** usando Bash tool con comando `open` para que el usuario vea la página validada
2. Mostrar mensaje:

```
✅ Página 100% conforme con las reglas de landing-creator.md

Página abierta en Safari para que veas el resultado.

¿Quieres hacer commit ahora? (s/n)
```

Si usuario dice "s":
- Usar comando de git para hacer commit

---

### Paso 6: Verificación Visual en Móvil y Escritorio (CRÍTICO)

🚨 **SIEMPRE realizar esta verificación después de abrir la página:**

Después de abrir la página con `open`, INSTRUIR al usuario:

```
📱 VERIFICACIÓN OBLIGATORIA - Móvil y Escritorio

La página se abrió en Safari. ANTES de hacer commit, verifica visualmente:

DESKTOP (Ventana completa en Safari):
   - Hero centrado con imagen de fondo visible
   - Título h1 centrado horizontalmente
   - Botones flotantes en esquina derecha inferior
   - Todas las secciones alineadas
   - Sin elementos rotos

MOBILE (iPhone 14 Pro - 390px):
   1. Presiona Cmd+Opt+I (DevTools)
   2. Click en icono móvil (o Cmd+Shift+M)
   3. Selecciona "iPhone 14 Pro" (390x844)
   4. Scrollea toda la página verificando:
      - Hero responsive (texto arriba, imagen fondo)
      - Título legible sin zoom
      - Botones flotantes visibles
      - Sin scroll horizontal
      - Imágenes responsive

¿Se ve PERFECTO en ambas versiones (desktop + mobile)? (s/n)
```

**Si usuario responde "s":**
- Proceder a preguntar si quiere hacer commit

**Si usuario responde "n":**
- Preguntar: "¿Qué está mal? (desktop/mobile/ambos)"
- Según respuesta, ofrecer corregir el problema específico
- Volver a validar después de corrección
- Repetir verificación visual

**Si NO hay errores (0) desde el inicio:**

1. **Abrir página localmente** usando Bash tool
2. Mostrar mensaje con verificación visual:

```
✅ Página 100% conforme con las reglas de landing-creator.md

Página abierta en Safari para verificación visual.

📱 VERIFICACIÓN OBLIGATORIA - Móvil y Escritorio

Antes de hacer commit, verifica visualmente en Safari:

DESKTOP: Hero centrado, botones flotantes visibles
MOBILE (Cmd+Opt+I → iPhone 14 Pro):
   - Hero responsive
   - Sin scroll horizontal
   - Botones flotantes visibles

¿Se ve PERFECTO en ambas versiones? (s/n)
```

Si usuario dice "s":
- Preguntar: "¿Quieres hacer commit ahora? (s/n)"
- Si dice "s": hacer commit

Si usuario dice "n":
- Preguntar qué está mal
- Corregir
- Repetir verificación

---

## Reglas Importantes

1. **Ser específico:** SIEMPRE dar números de línea exactos
2. **No inventar:** Solo reportar lo que realmente encuentre
3. **Comparar con index.html:** Esa es la fuente de verdad
4. **Mostrar código:** En los errores, mostrar código real encontrado vs esperado
5. **Ofrecer ayuda:** Preguntar si quiere corrección automática

---

## Ejemplo Completo de Uso

```
Usuario: @validador-pagina

Yo: 🔍 Validador de Página Activado
    ¿Qué página quieres validar?

Usuario: electricista-urgente/index.html

Yo: [Leo index.html y electricista-urgente/index.html]
    [Valido las 6 áreas]

    ## 🔍 Validación de electricista-urgente

    ### ❌ ERRORES DETECTADOS (2)

    #### 🚨 Error 1: Botones usan emojis
    - Línea: 450
    - Encontrado: `<a class="cta-btn">💬</a>`
    - Debe ser: `<a class="floating-btn floating-whatsapp"><svg>...</svg></a>`

    #### 🚨 Error 2: Hero usa <div>
    - Línea: 120
    - Encontrado: `<div class="hero-background">`
    - Debe ser: `<picture class="hero-background">`

    Estado: ❌ REQUIERE CORRECCIONES (2 errores)

    ¿Quieres que corrija los errores automáticamente? (s/n)

Usuario: s

Yo: [Corrijo error 1 con Edit]
    [Corrijo error 2 con Edit]
    [Valido de nuevo]

    Errores corregidos
    Validación: 14/14 aprobadas

    [Abro página con: open "electricista-urgente/index.html"]

    Página abierta en Safari para que veas los cambios.

    ¿Quieres hacer commit ahora? (s/n)

Usuario: s

Yo: [git add + commit]
    ✅ Commit realizado: fix(landing): corregir hero y botones flotantes
```

---

## Notas Finales

- SIEMPRE leo @.claude/commands/landing-creator.md para saber las reglas
- SIEMPRE comparo contra index.html (fuente de verdad)
- SIEMPRE doy números de línea exactos
- NUNCA invento errores que no existen
- SIEMPRE ofrezco corrección automática si hay errores
- SIEMPRE abro la página en Safari después de validar (con o sin correcciones) para que el usuario vea el resultado
- SIEMPRE instruyo al usuario a verificar MÓVIL Y ESCRITORIO antes de commit
- NO permito commit hasta que ambas versiones se vean perfectas
- Si usuario reporta problema en mobile/desktop, corrijo y vuelvo a validar
