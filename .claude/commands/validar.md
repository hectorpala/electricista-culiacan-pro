# Comando: /validar

Valida una página nueva contra index.html para detectar errores ANTES de hacer commit.

## Uso

```bash
/validar [ruta-relativa-a-la-página]
```

**Ejemplos:**
```bash
/validar blog/como-encontrar-electricista-confiable-culiacan/index.html
/validar electricista-24-horas/index.html
/validar servicios/instalacion-electrica/index.html
```

---

## Instrucciones para Claude

Cuando el usuario ejecute este comando:

### 1. Leer Archivos (en paralelo)
- Lee `index.html` (homepage de referencia)
- Lee la página a validar (ruta proporcionada por usuario)

### 2. Validar Hero (CRÍTICO)

Busca en la página nueva la sección `<header` con clase `hero`:

**✅ DEBE CUMPLIR:**
- [ ] Tiene `<picture class="hero-background">` (NO `<div class="hero-background">`)
- [ ] Dentro del `<picture>` hay `<source type="image/webp">` con atributo `srcset`
- [ ] El `<img>` tiene atributos: `decoding="async"` y `fetchpriority="high"`
- [ ] La imagen es `hero-electricista-trabajo-800w.webp` y `hero-electricista-trabajo-1200w.webp` (o la que especifique usuario)
- [ ] NO usa `hero-electrical-*.webp` (imagen obsoleta)

**Reportar línea exacta si hay error.**

### 3. Validar Botones Flotantes (CRÍTICO)

Busca en la página nueva los botones flotantes (antes del cierre `</body>`):

**✅ DEBE CUMPLIR:**
- [ ] Botón WhatsApp tiene clase `floating-btn floating-whatsapp` (NO `cta-btn`)
- [ ] Botón Teléfono tiene clase `floating-btn floating-call` (NO `cta-btn`)
- [ ] Ambos botones contienen `<svg>` con `<path>` (NO emojis 💬 📞)
- [ ] WhatsApp tiene `background:#22c55e` en CSS (verificar en `<style>`)
- [ ] Teléfono tiene `background:#0f4fa8` en CSS
- [ ] NO están dentro de un `<div class="cta-bar">`

**Reportar línea exacta si hay error.**

### 4. Validar Clases CSS Custom (CRÍTICO)

Busca en el `<style>` de la página nueva:

**❌ PROHIBIDO (NO deben existir):**
- [ ] `.highlight-box` con background amarillo (#fef3c7)
- [ ] `.warning-box` con background rojo (#fee2e2)
- [ ] `.info-box`, `.note-box`, `.alert-box` o similar
- [ ] Cualquier clase con `border-left: 4px solid`
- [ ] Fondos de colores que NO existan en index.html

**Reportar línea exacta si encuentra alguna.**

### 5. Validar HTML de Cajas de Colores

Busca en el `<body>` de la página nueva:

**❌ PROHIBIDO (NO deben existir):**
- [ ] `<div class="highlight-box">`
- [ ] `<div class="warning-box">`
- [ ] Divs con `style="background:#fef3c7"` o similar inline

**Reportar línea exacta si encuentra alguna.**

### 6. Validar Barra WhatsApp CTA (OBLIGATORIO)

Busca en el `<body>` dentro de la sección `.benefits-grid`:

**✅ DEBE CUMPLIR:**
- [ ] Tiene `<div class="whatsapp-cta-box">` presente
- [ ] Contiene heading `<h3>` con texto exacto: "¿Tienes dudas? Respondemos en 10 minutos"
- [ ] Tiene botón con clase `whatsapp-cta-button` y texto "Abrir Chat"
- [ ] Link apunta a: `https://wa.me/526671631231?text=...` (electricista)
- [ ] Está ubicado dentro de `.benefits-grid` (después de los 4 benefits)
- [ ] Usa SVG para iconos (NO emojis)

**❌ ERROR COMÚN:**
- Falta completamente el elemento `.whatsapp-cta-box`
- Texto del heading incorrecto o abreviado
- Botón no dice "Abrir Chat"
- Link no apunta a WhatsApp correcto (526671631231)
- Ubicado fuera de `.benefits-grid`

**Reportar línea exacta si falta o está incorrecto.**

### 7. Validar Sección Blog (HOMEPAGE)

Busca la sección `id="blog"`:

**✅ DEBE CUMPLIR:**
- [ ] Usa estructura `service-card` (NO `news-card`)
- [ ] Cada artículo: `<a href="/blog/.../" class="card card--img">`
- [ ] Contiene `<div class="service-card">` con `<figure class="media-box">`
- [ ] Imágenes con `<picture>` + `<source type="image/webp">`
- [ ] Tiene `<span class="service-cta">Leer artículo completo →</span>`
- [ ] Mínimo 3 artículos

**Reportar si usa estructura incorrecta.**

### 8. Validar Sección Testimoniales (HOMEPAGE)

Busca "Lo que dicen nuestros clientes":

**✅ DEBE CUMPLIR:**
- [ ] Sección con clase `testimonials`
- [ ] Grid: `testimonial-grid`
- [ ] Cards: `testimonial-card`
- [ ] Estrellas ⭐⭐⭐⭐⭐ o SVG
- [ ] Nombre + colonia en cada testimonio
- [ ] Mínimo 3 testimonios
- [ ] CSS: `.testimonial-card{border-left:4px solid var(--brand)}`

**Reportar si faltan elementos.**

### 9. Validar Sección Social Proof (HOMEPAGE)

Busca "💯 Prueba Real de Nuestro Servicio":

**✅ DEBE CUMPLIR:**
- [ ] `<section class="social-proof">`
- [ ] Reseñas Google: `google-reviews-grid`
- [ ] Antes/Después: `before-after-grid`
- [ ] Imágenes WebP optimizadas
- [ ] Badges/labels en imágenes
- [ ] CSS: `background:linear-gradient(135deg,#f8fafc 0%,#e0f2fe 100%)`

**Reportar si falta subsección.**

### 10. Validar Formulario Contacto + Validación (CRÍTICO)

Busca `id="contact-form"`:

**HTML:**
- [ ] Atributos: `id="contact-form"` `method="POST"` `netlify`
- [ ] Campos con IDs: `nombre`, `telefono`, `email`, `mensaje`
- [ ] Wrapeados en `<div class="form-field">`
- [ ] Cada uno con `<span class="error-message">` y `<span class="success-message">`
- [ ] Botón `disabled` inicial
- [ ] `<p class="form-note">` presente

**CSS (en head):**
- [ ] `.form-field.valid input{border-color:#28a745;background-image:url("data:image/svg+xml...")}`
- [ ] `.form-field.invalid input{border-color:#dc3545;background-image:url("data:image/svg+xml...")}`
- [ ] `.form-field.invalid .error-message{display:block}`
- [ ] `.form-field.valid .success-message{display:block}`

**JAVASCRIPT (main.js):**
- [ ] Función `validateField(field, validatorKey)`
- [ ] Validators: nombre ≥2, telefono 10 dígitos, email formato, mensaje ≥10
- [ ] Event listeners `input` y `blur` en cada campo
- [ ] `updateSubmitButton()` enable/disable
- [ ] Multi-layer lead capture (Netlify + localStorage + GA4 + WhatsApp)

**Reportar si falta validación JS.**

### 11. Validar CSS Sección Contacto (CRÍTICO)

Busca en `<style>`:

**DEBE INCLUIR:**
- [ ] `.final-cta{max-width:600px;border-radius:20px;box-shadow:0 8px 32px var(--shadow-lg);border:2px solid var(--brand)}`
- [ ] `.cta-text{font-weight:600}`
- [ ] `.cta-subtitle{margin-bottom:2rem}`
- [ ] `.contact-content{display:grid;grid-template-columns:1fr 1fr;gap:3rem}`
- [ ] `.map-container{margin-top:3rem}`
- [ ] `.map-embed{padding-bottom:56.25%}`
- [ ] `.whatsapp-link{color:#22c55e}`
- [ ] Media queries mobile para `.contact-content` y `.cta-buttons`

**Reportar bloques CSS faltantes.**

### 12. Validar Estructura General

**✅ DEBE TENER (comparar con index.html):**
- [ ] `<nav class="nav">` idéntico
- [ ] `<footer class="footer">` idéntico
- [ ] Mismo `<link>` a `styles.min.css`
- [ ] Mismo `<script>` de `main.js`
- [ ] Paths correctos (absolutos `/` en raíz, relativos `../../` en subdirectorios)

### 13. Formato del Reporte

Presenta el resultado en este formato:

```markdown
## 🔍 Validación de [nombre-página]

### ✅ APROBADAS (X/12)

- ✅ Hero estructura correcta
- ✅ Botones flotantes con SVG
- ✅ Sin clases CSS custom
- ✅ Sin cajas de colores en HTML
- ✅ Barra WhatsApp CTA presente
- ✅ Sección Blog (service-card structure)
- ✅ Sección Testimoniales completa
- ✅ Sección Social Proof completa
- ✅ Formulario con validación JS en tiempo real
- ✅ CSS Contacto completo (.final-cta, .contact-content, etc.)
- ✅ Estructura general correcta
- ✅ Paths correctos

### ❌ ERRORES DETECTADOS (X)

#### 🚨 Error 1: [Descripción]
- **Archivo:** [ruta]
- **Línea:** [número]
- **Encontrado:** `[código incorrecto]`
- **Debe ser:** `[código correcto]`
- **Fix:** [instrucción específica]

#### 🚨 Error 2: [...]

---

## 📊 Resultado Final

**Estado:** ✅ LISTO PARA COMMIT | ❌ REQUIERE CORRECCIONES

**Acción recomendada:**
- Si TODO ✅: Puedes proceder con `git commit`
- Si HAY ❌: Corrígelos primero ejecutando: [comandos específicos]
```

### 8. Ser Específico

**NO digas:** "El hero está mal"
**SÍ di:** "Línea 145: Hero usa `<div class="hero-background">` pero debe ser `<picture class="hero-background">`"

**NO digas:** "Los botones están incorrectos"
**SÍ di:** "Línea 627-635: Botones usan emojis 💬 📞, deben usar SVG con path d='M17.472...'"

---

## Ejemplo de Uso Completo

```bash
Usuario: /validar blog/articulo-nuevo/index.html

Claude: [Lee ambos archivos]
Claude: [Valida las 6 áreas]
Claude: [Genera reporte]

## 🔍 Validación de articulo-nuevo

### ✅ APROBADAS (5/7)
- ✅ Estructura general correcta
- ✅ Paths correctos
- ✅ Sin cajas de colores en HTML
- ✅ Hero estructura correcta
- ✅ Barra WhatsApp CTA presente

### ❌ ERRORES DETECTADOS (2)

#### 🚨 Error 1: Botones flotantes usan emojis
- **Archivo:** blog/articulo-nuevo/index.html
- **Línea:** 450-455
- **Encontrado:** `<a class="cta-btn">💬</a>`
- **Debe ser:** `<a class="floating-btn floating-whatsapp"><svg>...</svg></a>`
- **Fix:** Reemplazar con estructura de index.html línea 1356-1373

#### 🚨 Error 2: Clase CSS custom prohibida
- **Archivo:** blog/articulo-nuevo/index.html
- **Línea:** 85
- **Encontrado:** `.highlight-box{background:#fef3c7;...}`
- **Debe ser:** NO debe existir esta clase
- **Fix:** Eliminar línea 85 y líneas 320-325 (HTML que la usa)

---

## 📊 Resultado Final

**Estado:** ❌ REQUIERE CORRECCIONES

**Acción recomendada:**
Por favor corrígelos primero. ¿Quieres que los corrija automáticamente?
```

---

## Notas Importantes

- Este comando NO modifica archivos, solo reporta
- Siempre compara contra index.html como fuente de verdad
- Reporta TODAS las diferencias, no solo la primera
- Usa números de línea exactos para facilitar corrección
- Prioriza errores críticos (hero, botones) sobre warnings menores
