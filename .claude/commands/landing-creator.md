# Landing Creator

Crea nuevas landing pages clonando el estilo exacto de electricistaculiacanpro.mx. Solo necesitas proporcionar contenido y fotos.

## 🚨 REGLA #0 ABSOLUTA - COPIA EXACTA O FALLA

**⚠️ CUALQUIER DESVIACIÓN DE index.html = PÁGINA RECHAZADA**

Esta NO es una guía flexible. Es un REQUISITO ABSOLUTO:

### ❌ SI ALGO ES DIFERENTE A index.html → LA PÁGINA NO PASA VALIDACIÓN

- ❌ **Colores diferentes** → FALLA
- ❌ **Tipografías diferentes** → FALLA
- ❌ **Iconos diferentes** → FALLA
- ❌ **Tamaños de texto diferentes** → FALLA
- ❌ **Espaciados diferentes** → FALLA
- ❌ **Gradientes diferentes** → FALLA
- ❌ **Sombras diferentes** → FALLA
- ❌ **Bordes diferentes** → FALLA
- ❌ **Animaciones diferentes** → FALLA

### ✅ ÚNICA FORMA VÁLIDA: COPIA EXACTA

```
index.html === nueva-pagina.html (ESTILOS, COLORES, TIPOGRAFÍA, ICONOS)
```

**NO hay "similar"**
**NO hay "parecido"**
**NO hay "inspirado en"**

**SOLO hay IDÉNTICO o RECHAZADO**

---

## Qué hace este comando

1. **Clona estilos exactos** - Copia BYTE POR BYTE todos los estilos, colores, fuentes, botones de index.html
2. **Estructura idéntica** - Header, hero, secciones, footer EXACTAMENTE iguales
3. **SEO completo** - Meta tags, Open Graph, JSON-LD schemas automáticos
4. **Responsive** - Mobile-first IDÉNTICO a la homepage
5. **Solo pides contenido** - Tú solo das textos y rutas de imágenes (TODO LO DEMÁS ES COPIA EXACTA)

## ⚠️ IMPORTANTE - Fuente de Verdad

**FUENTE DE ESTILOS:** `index.html` (raíz del proyecto)
- Este es el ÚNICO sitio de referencia para TODOS los estilos, CSS, estructura y colores
- CLONAR EXACTAMENTE los estilos de index.html
- **NO interpretar, NO adaptar, NO mejorar - SOLO COPIAR**

## 🎨 VALORES EXACTOS OBLIGATORIOS

### COLORES - CERO TOLERANCIA A DESVIACIONES

**✅ ESTOS SON LOS ÚNICOS COLORES PERMITIDOS:**

#### Colores de Marca (Naranja)
```css
--brand: #E36414           /* Naranja principal - EXACTO, no #E36415 ni #E36413 */
--brand-light: #F97316     /* Naranja claro - EXACTO */
--gradient-brand: linear-gradient(135deg, #F97316 0%, #E36414 100%)
```

**❌ PROHIBIDO:** Usar otros naranjas (#FF6B35, #FF7A3D, #E36514, etc.)

#### Colores de Texto
```css
--text: #0F172A            /* Texto principal - EXACTO */
--text-light: #475569      /* Texto secundario - EXACTO */
```

**❌ PROHIBIDO:** Usar #000000, #333333, #1E40AF, u otros negros/grises

#### Colores de Fondo
```css
--bg: #FFFFFF              /* Fondo blanco - EXACTO */
--bg-soft: #F8FAFC         /* Fondo suave - EXACTO */
```

**❌ PROHIBIDO:** Usar #F5F5F5, #FAFAFA, #F9FAFB u otros blancos/grises

#### Colores de UI
```css
--border: #E2E8F0          /* Bordes - EXACTO */
--shadow: rgba(15,23,42,0.1)  /* Sombras - EXACTO */
```

**❌ PROHIBIDO:** Usar rgba(0,0,0,0.1), #DDD, u otras sombras/bordes

#### Theme Color
```css
theme-color: #0066cc       /* EXACTO - NO #0066CC ni #0066cd */
```

#### Colores de Botones Flotantes
```css
WhatsApp: #22c55e          /* EXACTO - NO #25D366 (viejo WhatsApp green) */
Teléfono: #0f4fa8          /* EXACTO - NO #0066cc */
```

**❌ ERRORES COMUNES:**
- ❌ Usar #25D366 para WhatsApp (es el color viejo)
- ❌ Usar #0066cc para botón de teléfono (es theme-color, no botón)
- ❌ Usar #1E40AF para textos (es un azul, no está en la paleta)

---

### TIPOGRAFÍAS - CERO TOLERANCIA A DESVIACIONES

**✅ ESTAS SON LAS ÚNICAS FUENTES PERMITIDAS:**

#### Fuentes de Títulos (Montserrat)
```css
h1, h2, h3 {
  font-family: 'Montserrat', sans-serif;
  font-weight: 800;          /* EXACTO - NO 700, NO 900 */
  letter-spacing: -0.025em;  /* EXACTO */
  line-height: 1.2;          /* EXACTO */
}
```

**Pesos disponibles de Montserrat:**
- 700 (Bold) - Para algunos encabezados secundarios
- 800 (ExtraBold) - Para H1, H2, H3

**❌ PROHIBIDO:** Usar font-weight: 600, 900, o cualquier otro peso

#### Fuentes de Cuerpo (Inter)
```css
body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  font-size: 16px;           /* EXACTO - NO 15px, NO 17px */
  line-height: 1.7;          /* EXACTO - NO 1.6, NO 1.8 */
}
```

**Pesos disponibles de Inter:**
- 400 (Regular) - Texto normal
- 500 (Medium) - Texto destacado
- 600 (SemiBold) - Texto en negritas

**❌ PROHIBIDO:** Usar Roboto, Open Sans, Lato, u otras fuentes

---

### ICONOS - CERO TOLERANCIA A DESVIACIONES

**✅ ESTOS SON LOS ÚNICOS ICONOS PERMITIDOS:**

#### ❌ PROHIBIDO: Usar Emojis
```html
<!-- ❌ MAL -->
<button>💬 WhatsApp</button>
<button>📞 Llamar</button>

<!-- ✅ BIEN -->
<button>
  <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
    <path d="M17.472 14.382c-.297-.149..."/>
  </svg>
</button>
```

**Razón:** Los emojis se ven diferentes en cada plataforma (iOS, Android, Windows). Los SVGs son IDÉNTICOS en todas partes.

#### Iconos SVG Permitidos (de index.html)

**1. WhatsApp Icon (EXACTO):**
```html
<svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
  <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
</svg>
```

**2. Teléfono Icon (EXACTO):**
```html
<svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
  <path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"/>
</svg>
```

**3. Google Logo (para rating badge):**
```html
<svg class="google-logo" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
  <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
  <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
  <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
  <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
</svg>
```

**❌ PROHIBIDO:**
- Font Awesome icons
- Material Icons
- Heroicons
- Bootstrap Icons
- Cualquier librería de iconos externa

**✅ PERMITIDO:**
- SOLO los SVG que ya están en index.html (copiados EXACTAMENTE)

---

### GRADIENTES - CERO TOLERANCIA A DESVIACIONES

**✅ Gradiente de Botones Principal:**
```css
background: linear-gradient(135deg, #fba336 0%, #f97316 45%, #e36414 100%);
```

**❌ PROHIBIDO:** Cambiar ángulo (NO 90deg, NO 180deg), cambiar colores, cambiar stops

**✅ Gradiente del Hero Overlay:**
```css
background: linear-gradient(180deg, rgba(10,18,36,0.75) 0%, rgba(10,18,36,0.5) 60%, transparent 100%);
```

**❌ PROHIBIDO:** Cambiar opacidades, cambiar dirección, cambiar colores

---

### TAMAÑOS - CERO TOLERANCIA A DESVIACIONES

**✅ Tamaños de Texto:**
```css
h1: clamp(2.5rem, 5vw, 4rem)     /* EXACTO */
h2: 2.5rem                        /* EXACTO */
body: 16px                        /* EXACTO - NO 15px, NO 18px */
line-height: 1.7                  /* EXACTO - NO 1.5, NO 1.8 */
```

**✅ Tamaños de Logo:**
```css
Nav: height: 140px, width: auto   /* EXACTO */
Mobile: height: 90px, width: auto /* EXACTO */
```

**✅ Tamaños de Botones:**
```css
padding: 17px 34px                /* EXACTO */
border-radius: 14px               /* EXACTO - NO 12px, NO 16px */
min-height: 48px                  /* EXACTO (accesibilidad) */
min-width: 48px                   /* EXACTO (accesibilidad) */
```

**✅ Tamaños de Botones Flotantes:**
```css
width: 54px                       /* EXACTO - NO 50px, NO 60px */
height: 54px                      /* EXACTO */
border-radius: 50%                /* EXACTO (círculo perfecto) */
```

---

### SOMBRAS - CERO TOLERANCIA A DESVIACIONES

**✅ Sombra de Botones:**
```css
box-shadow: 0 10px 24px rgba(227,100,20,0.28);
```

**✅ Sombra de Botones Flotantes:**
```css
box-shadow: 0 10px 28px rgba(0,0,0,0.16);
```

**✅ Sombra de Cards:**
```css
box-shadow: 0 2px 10px rgba(15,23,42,0.1);
```

**❌ PROHIBIDO:** Cambiar blur, spread, opacidad, color

---

### SERVICE CARDS - ESTRUCTURA OBLIGATORIA

**✅ Imágenes de Service Cards DEBEN SER CUADRADAS (420x420):**

Todas las tarjetas de servicios DEBEN usar imágenes cuadradas, NO rectangulares.

```html
<img src="...420w.webp"
     srcset="...420w.webp 420w, ...800w.webp 800w"
     sizes="(max-width:768px) 100vw, 420px"
     alt="..."
     width="420" height="420"
     loading="lazy" decoding="async">
```

**ESTRUCTURA CORRECTA (de plomero culiacan pro):**
```html
<a href="..." class="card card--img">
    <div class="service-card">
        <figure class="media-box">
            <picture>
                <source type="image/webp" srcset="...420w.webp 420w, ...800w.webp 800w">
                <img src="...420w.webp" width="420" height="420" loading="lazy" decoding="async">
            </picture>
        </figure>
    </div>
    <h3>Título del Servicio</h3>
    <p>Descripción...</p>
</a>
```

**✅ REQUISITOS OBLIGATORIOS:**
- Imágenes: width="420" height="420" (CUADRADAS)
- DEBE usar `<div class="service-card">` + `<figure class="media-box">`
- NO usar emojis en títulos `<h3>`
- Srcset: 420w y 800w (NO 800w/1200w)

**❌ PROHIBIDO:**
- Imágenes rectangulares (420x235) - FALLA AUTOMÁTICA
- Imágenes grandes (800x600, 1200x800) - FALLA AUTOMÁTICA
- Emojis en títulos - FALLA AUTOMÁTICA

---

### BENEFITS SECTION - ESTRUCTURA OBLIGATORIA

**✅ Sección "¿Por qué elegirnos?" DEBE usar SVG icons, NO emojis:**

La sección de beneficios DEBE usar la estructura EXACTA de plomero culiacan pro con iconos SVG.

**ESTRUCTURA CORRECTA (minificada, de plomero culiacan pro línea 1154):**
```html
<section class="section section-alt"><div class="container benefits-container"><h2>¿Por qué elegirnos?</h2><div class="benefits-grid"><div class="benefit"><div class="benefit-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><div class="benefit-content"><h3>Llegamos hoy mismo</h3><p>Atendemos emergencias en 30-60 min...</p></div></div>...</div></section>
```

**REQUISITOS ESTRICTOS:**
- DEBE usar `<div class="benefit-icon">` con SVG dentro
- DEBE usar `<div class="benefit-content">` para h3 y p
- DEBE incluir `.whatsapp-cta-box` al final de `.benefits-grid`
- DEBE tener `<p class="benefits-cta">` con CTA final
- HTML minificado (sin indentación extra)
- 4 benefits + 1 WhatsApp CTA box

**❌ PROHIBIDO (FALLA AUTOMÁTICA):**
```html
<!-- ❌ INCORRECTO: Usa emojis en vez de SVG -->
<div class="benefit">
    <div style="font-size:3rem">⚡</div>
    <h3>Servicio Rápido</h3>
</div>

<!-- ✅ CORRECTO: Usa SVG en benefit-icon -->
<div class="benefit">
    <div class="benefit-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor">...</svg>
    </div>
    <div class="benefit-content">
        <h3>Servicio Rápido</h3>
        <p>Descripción...</p>
    </div>
</div>
```

**ICONOS SVG PERMITIDOS (de plomero culiacan pro):**
- Reloj (circle + polyline) - "Llegamos hoy mismo"
- Dinero (dollar sign) - "Precios claros"
- Herramienta (wrench path) - "Garantía 6 meses"
- Documento (document + lines) - "Factura SAT"

**ERRORES CRÍTICOS:**
- Usar emojis (⚡💡🛡️⚙️) en vez de SVG - FALLA
- NO usar `.benefit-icon` + `.benefit-content` - FALLA
- Faltar `.whatsapp-cta-box` - FALLA
- Estructura con indentación excesiva (debe ser minificada) - FALLA

---

## 🚨 VALIDACIÓN AUTOMÁTICA

**Antes de hacer commit, verificar CADA UNO de estos valores:**

```bash
# Buscar colores incorrectos
grep -r "#1E40AF" servicios/  # NO debe existir (es azul viejo)
grep -r "#25D366" servicios/  # NO debe existir (WhatsApp viejo)
grep -r "font-weight: 900" servicios/  # NO debe existir
grep -r "font-family: Roboto" servicios/  # NO debe existir

# Buscar emojis en botones (PROHIBIDO)
grep -r "💬" servicios/  # NO debe existir en HTML
grep -r "📞" servicios/  # NO debe existir en HTML

# Verificar colores correctos
grep -r "#E36414" servicios/  # DEBE existir (brand)
grep -r "#F97316" servicios/  # DEBE existir (brand-light)
grep -r "#22c55e" servicios/  # DEBE existir (WhatsApp nuevo)
```

---

✅ **Mantener IDÉNTICOS:**
- Gradientes de botones
- Colores de fondos
- Colores de texto
- Estilos de sombras
- Animaciones y transiciones
- Layout y espaciado

❌ **NO CAMBIAR:**
- Paleta de colores
- Variables CSS en `:root`
- Estilos visuales
- Fuentes (Inter + Montserrat)

## Uso

```
/landing-creator
```

El comando te pedirá la información necesaria paso a paso.

## Instrucciones para Claude

### REGLAS CRÍTICAS - Leer primero

**⚠️ REGLA #0 - PROHIBIDO AGREGAR ELEMENTOS CUSTOM:**

Esta es la regla MÁS IMPORTANTE. NUNCA, bajo ninguna circunstancia:

- ❌ **PROHIBIDO:** Crear clases CSS que NO existan en index.html
- ❌ **PROHIBIDO:** Agregar `.highlight-box`, `.warning-box`, `.info-box`, `.note-box` o cualquier caja con color de fondo
- ❌ **PROHIBIDO:** Crear elementos amarillos, rojos, azules, verdes con bordes de colores
- ❌ **PROHIBIDO:** Inventar nuevos estilos más allá de los que están en index.html
- ❌ **PROHIBIDO:** Agregar divs decorativos con fondos de colores (#fef3c7, #fee2e2, etc.)

✅ **SOLO PERMITIDO:** Usar clases que YA EXISTEN en index.html:
  - `.hero`, `.hero-background`, `.hero-content`
  - `.section`, `.section-alt`
  - `.benefits-grid`, `.benefit-card`
  - `.grid`, `.card`
  - `.faq`, `.faq-item`
  - `.footer`
  - `.btn-primary`, `.btn-secondary`
  - `.floating-btn`, `.floating-whatsapp`, `.floating-call`

Si necesitas resaltar contenido, usa SOLO:
  - Párrafos con `<strong>` o `<em>`
  - Listas `<ul>` o `<ol>` sin estilos custom
  - Encabezados `<h2>`, `<h3>` que ya tienen estilos en index.html

**Fuente de verdad:** index.html en raíz del proyecto
**Clona ESTRICTAMENTE** - No agregues, no inventes, no mejores.

**⚠️ REGLA #0.1 - ESTRUCTURA HERO (CRÍTICO):**

El hero DEBE usar EXACTAMENTE esta estructura (index.html línea 2815):

```html
<header id="inicio" class="hero">
    <picture class="hero-background">
        <source type="image/webp"
                srcset="assets/images/optimizadas/NOMBRE-800w.webp 800w, assets/images/optimizadas/NOMBRE-1200w.webp 1200w"
                sizes="100vw">
        <img src="assets/images/optimizadas/NOMBRE-1200w.webp"
             srcset="assets/images/optimizadas/NOMBRE-800w.webp 800w, assets/images/optimizadas/NOMBRE-1200w.webp 1200w"
             sizes="100vw"
             alt="..."
             width="1200"
             height="655"
             fetchpriority="high"
             loading="eager"
             decoding="async">
    </picture>
    <div class="container">
        <div class="hero-content">...</div>
    </div>
</header>
```

❌ **ERRORES COMUNES A EVITAR:**
- ❌ NO usar `<div class="hero-background">` - DEBE ser `<picture class="hero-background">`
- ❌ NO omitir el elemento `<source type="image/webp">`
- ❌ NO omitir `decoding="async"` en el `<img>`
- ❌ NO usar imágenes diferentes a las de index.html sin verificar
- ❌ NO omitir `content-visibility:auto` en el CSS de `.hero-background img`

**Imagen hero por defecto:**
- USAR: `emergencia-electrica-culiacan-800w.webp` y `emergencia-electrica-culiacan-1200w.webp` (igual que index.html)
- NO USAR: hero-electrical-*.webp u otras imágenes obsoletas a menos que el usuario las especifique

**⚠️ REGLA #0.2 - BOTONES FLOTANTES (CRÍTICO):**

Los botones flotantes (WhatsApp + Llamar) DEBEN usar EXACTAMENTE esta estructura (index.html línea 3862-3876):

```html
<a href="https://wa.me/526673922273?text=Hola%2C%20necesito%20informaci%C3%B3n%20sobre%20servicios%20de%20electricidad%20en%20Culiac%C3%A1n"
   id="cta-whatsapp"
   class="floating-btn floating-whatsapp"
   target="_blank"
   rel="noopener noreferrer"
   aria-label="Contactar por WhatsApp - Respuesta inmediata">
    <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    <span class="online-badge" aria-label="En línea"></span>
</a>

<a href="tel:+526673922273"
   id="cta-llamar"
   class="floating-btn floating-call"
   aria-label="Llamar ahora">
    <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"/></svg>
</a>
```

**CSS de botones flotantes (index.html línea 125-128):**
```css
.floating-btn{position:fixed;right:18px;width:54px;height:54px;border-radius:50%;display:grid;place-items:center;color:#fff;font-size:1.1rem;box-shadow:0 10px 28px rgba(0,0,0,0.16);transition:transform .12s ease,box-shadow .12s ease,filter .12s ease;z-index:60;text-decoration:none}
.floating-btn:hover{transform:translateY(-2px);box-shadow:0 14px 34px rgba(0,0,0,0.2);filter:brightness(1.05)}
.floating-call{background:#0f4fa8;bottom:18px}
.floating-whatsapp{background:#22c55e;bottom:78px}
```

❌ **ERRORES COMUNES A EVITAR:**
- ❌ NO usar emojis (💬 📞) - DEBE usar SVG icons completos
- ❌ NO usar `<div class="cta-bar">` - Botones van directos sin contenedor
- ❌ NO usar clases incorrectas - DEBE usar `.floating-btn`, `.floating-whatsapp`, `.floating-call`
- ❌ NO usar colores incorrectos - WhatsApp: #22c55e (NO #25D366), Tel: #0f4fa8 (NO #0066cc)
- ❌ NO usar teléfonos diferentes - WhatsApp: +526673922273, Tel: +526673922273

**⚠️ REGLA #0.3 - CRITICAL CSS COMPLETO (CRÍTICO):**

Cada página DEBE incluir el bloque COMPLETO de Critical CSS. NO es suficiente copiar solo CSS individual de componentes.

**✅ DEBE incluir TODO el Critical CSS (COPIAR DE index.html líneas 77-172):**
```css
<style>
    /* 5 Fonts Web (Inter + Montserrat) */
    @font-face{font-family:'Inter';font-style:normal;font-weight:400;font-display:swap;src:url('assets/fonts/inter-400.woff2') format('woff2')}
    @font-face{font-family:'Inter';font-style:normal;font-weight:500;font-display:swap;src:url('assets/fonts/inter-500.woff2') format('woff2')}
    @font-face{font-family:'Inter';font-style:normal;font-weight:600;font-display:swap;src:url('assets/fonts/inter-600.woff2') format('woff2')}
    @font-face{font-family:'Montserrat';font-style:normal;font-weight:700;font-display:swap;src:url('assets/fonts/montserrat-700.woff2') format('woff2')}
    @font-face{font-family:'Montserrat';font-style:normal;font-weight:800;font-display:swap;src:url('assets/fonts/montserrat-800.woff2') format('woff2')}

    /* CSS Variables */
    :root{--brand:#E36414;--brand-light:#F97316;--text:#0F172A;--text-light:#475569;--bg:#FFFFFF;--bg-soft:#F8FAFC;--border:#E2E8F0;--shadow:rgba(15,23,42,0.1);--gradient-brand:linear-gradient(135deg,#F97316 0%,#E36414 100%);--container-max-width:1200px;--container-gutter:24px}

    /* Base styles */
    *{margin:0;padding:0;box-sizing:border-box}
    body{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;font-size:16px;line-height:1.7;color:var(--text);background-color:var(--bg-soft);padding-top:80px}
    .container{max-width:var(--container-max-width);margin:0 auto;padding:0 var(--container-gutter)}
    h1,h2,h3{font-family:'Montserrat',sans-serif;font-weight:800;color:var(--text);letter-spacing:-0.025em;line-height:1.2}
    h1{font-size:clamp(2.5rem,5vw,4rem);margin-bottom:1.5rem}

    /* Nav */
    .nav{position:fixed;top:0;left:0;right:0;z-index:50;background:transparent;border-bottom:none;padding:22px 0}
    .nav-wrapper{display:flex;align-items:center;justify-content:space-between}
    .logo{display:block;text-decoration:none;transition:opacity .2s ease;contain:layout}
    .logo img{height:140px;width:auto;display:block;max-height:160px;mix-blend-mode:multiply;aspect-ratio:512/195}
    .logo:hover{opacity:0.9}
    @media (max-width:768px){.logo img{height:90px;max-height:100px}}

    /* Hero (CRÍTICO para centrado) */
    .hero{min-height:85vh;display:grid;place-items:center;text-align:center;padding:140px 16px;position:relative;overflow:hidden}
    .hero-background{position:absolute;inset:0;z-index:0}
    .hero-background img{width:100%;height:100%;object-fit:cover;object-position:center center;content-visibility:auto}
    @media (max-width:768px){.hero{min-height:75vh;padding-top:85px!important;align-items:flex-start!important}.hero-background img{object-position:20% 35%}.hero-content{margin-top:0!important;padding:1.5rem 1.25rem!important;background:rgba(255,255,255,0.12)!important;backdrop-filter:blur(2px)!important;-webkit-backdrop-filter:blur(2px)!important}.hero h1{margin-top:0!important;margin-bottom:0.5rem!important;font-size:clamp(1.5rem,5vw,2rem)!important;line-height:1.2!important}.hero-subtitle{display:none!important}.hero .btn-primary{width:100%!important;max-width:100%!important;font-size:1rem!important;padding:0.875rem 1.5rem!important}}
    .hero::after{content:"";position:absolute;top:-80px;left:0;right:0;height:100px;z-index:1;background:linear-gradient(180deg,rgba(10,18,36,0.75) 0%,rgba(10,18,36,0.5) 60%,transparent 100%);pointer-events:none}
    .hero-content{position:relative;z-index:2;max-width:900px;width:min(90vw,840px);margin:0 auto;background:rgba(255,255,255,0.15);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-radius:24px;padding:3rem 2.5rem;border:1px solid rgba(255,255,255,0.2);box-shadow:0 8px 32px rgba(0,0,0,0.1);contain:layout paint}

    /* Buttons */
    .btn-primary{display:inline-block;background:linear-gradient(135deg,#fba336 0%,#f97316 45%,#e36414 100%);color:#fff;border:none;border-radius:14px;padding:17px 34px;font-weight:700;font-size:1rem;text-decoration:none;cursor:pointer;box-shadow:0 10px 24px rgba(227,100,20,0.28);min-height:48px;min-width:48px;transition:transform .12s ease,box-shadow .12s ease,filter .12s ease;contain:layout style;will-change:transform}
    .btn-primary:hover{transform:translateY(-1px);box-shadow:0 14px 32px rgba(227,100,20,0.34);filter:brightness(1.04)}
    .btn-primary:active{transform:translateY(0);box-shadow:0 10px 20px rgba(227,100,20,0.28)}

    /* Floating buttons */
    .floating-btn{position:fixed;right:18px;width:54px;height:54px;border-radius:50%;display:grid;place-items:center;color:#fff;font-size:1.1rem;box-shadow:0 10px 28px rgba(0,0,0,0.16);transition:transform .12s ease,box-shadow .12s ease,filter .12s ease;z-index:60;text-decoration:none}
    .floating-btn:hover{transform:translateY(-2px);box-shadow:0 14px 34px rgba(0,0,0,0.2);filter:brightness(1.05)}
    .floating-call{background:#0f4fa8;bottom:18px}
    .floating-whatsapp{background:#22c55e;bottom:78px}
</style>
```

❌ **ERROR COMÚN (causa problemas de alineación):**
Solo copiar CSS de botones flotantes sin incluir el resto del Critical CSS.

**Consecuencias de Critical CSS incompleto:**
- ❌ Hero desalineado (título muy a la derecha o muy arriba)
- ❌ Fuentes web no cargan (se ve fuente del sistema)
- ❌ Variables CSS no definidas (colores rotos)
- ❌ Layout roto en mobile
- ❌ Nav mal posicionado

**⚠️ REGLA #0.4 - VERIFICACIÓN MÓVIL Y ESCRITORIO (CRÍTICO):**

🚨 **TODAS las adecuaciones DEBEN funcionar perfectamente en AMBAS versiones:**

✅ **VERIFICACIÓN OBLIGATORIA después de CADA cambio:**
1. **Versión Desktop (1920px, 1440px, 1280px):**
   - Hero centrado perfectamente
   - Imágenes con dimensiones correctas
   - Textos legibles
   - Botones flotantes visibles (derecha inferior)

2. **Versión Móvil (375px, 390px, 428px):**
   - Hero responsive con `align-items:flex-start!important`
   - `.hero-content` con backdrop-filter y padding reducido
   - Textos legibles sin scroll horizontal
   - Botones flotantes NO obstruyen contenido

**REGLA DE ORO:**
> **"Si no funciona PERFECTAMENTE en MÓVIL Y ESCRITORIO, NO está terminado."**

**⚠️ REGLA #0.5 - OPTIMIZACIÓN SEO OBLIGATORIA (CRÍTICO):**

🚨 **TODAS las landing pages DEBEN incluir:**

**1. Title Tag Optimizado:**
- ✅ Longitud: 50-60 caracteres (óptimo), máximo 70
- ✅ Formato: `[Keyword Principal] | Electricista Culiacán Pro`
- ✅ Keyword al inicio del title

**2. Meta Description Optimizada:**
- ✅ Longitud: 120-155 caracteres (óptimo), máximo 160
- ✅ Incluir keyword principal + call-to-action

**3. Breadcrumb HTML Navegable (OBLIGATORIO):**
- ✅ DEBE aparecer VISUALMENTE en la página
- ✅ Ubicación: Entre `</nav>` y `<header class="hero">`
- ✅ Enlaces funcionales a Inicio y secciones padre

**4. Logo con Dimensiones (OBLIGATORIO):**
- ✅ DEBE incluir atributos width y height
- ✅ Nav: width="140" height="140"
- ✅ Footer: width="200" height="76"

## Proceso Interactivo

### Paso 1: Solicitar información básica

```
🎨 Vamos a crear tu landing page con el estilo de electricistaculiacanpro.mx

1️⃣ ¿Cuál es el slug de la página? (ejemplo: electricista-urgente)
   Se creará en: /<slug>/index.html
```

### Paso 2-4: Keyword, H1, Meta Description

[Continúa igual que antes]

### Paso 5-8: Contenido del hero, Beneficios, FAQs

[Continúa igual que antes]

## Reglas importantes

1. **NUNCA modificar estilos** - Copiar exactamente de index.html
2. **NUNCA inventar contenido** - Usar solo lo que el usuario proporciona
3. **NUNCA crear clases CSS custom** - SOLO usar clases de index.html
4. **SIEMPRE crear backup** - Antes de sobrescribir archivos
5. **SIEMPRE validar imágenes** - Verificar que existan las rutas proporcionadas
6. **SIEMPRE generar schemas completos** - WebSite, Service, FAQPage, BreadcrumbList
7. **AL REHACER páginas existentes:**
   - ELIMINAR hero custom antiguo
   - ELIMINAR todos los estilos custom
   - USAR SOLO estructura de index.html
   - CREAR backup automático

**Teléfonos oficiales:**
- WhatsApp: +526673922273
- Llamadas: +526673922273

**Imágenes hero por defecto:**
- emergencia-electrica-culiacan-800w.webp
- emergencia-electrica-culiacan-1200w.webp

**Theme color:** #0066cc

## Notas finales

- El estilo es 100% idéntico a index.html (copiar, no modificar)
- Solo el contenido cambia (textos, imágenes del usuario)
- Responsive automático (mismo CSS que homepage)
- SEO completo automático (schemas, meta tags, OG, canonical)
- El usuario solo necesita: textos + fotos
- **Al rehacer páginas: ELIMINAR hero custom, USAR hero con imagen de fondo**
- **Siempre crear backup antes de sobrescribir**
- 🚨 **CRÍTICO: SIEMPRE verificar resultado en MÓVIL Y ESCRITORIO antes de commit**
- 🚨 **NO hacer commit hasta que AMBAS versiones se vean perfectas**
- 🚨 **60%+ usuarios son móvil - mobile DEBE funcionar perfecto**

---

## ✅ CHECKLIST DE VALIDACIÓN OBLIGATORIO

**Ejecuta ESTE checklist COMPLETO antes de hacer commit de cualquier landing page.**

### 📋 1. Critical CSS (OBLIGATORIO)

- [ ] **Critical CSS inline presente** - Bloque `<style>` completo en `<head>` (líneas 77-172 de index.html)
- [ ] **5 fuentes web @font-face** - Inter (400, 500, 600) + Montserrat (700, 800)
- [ ] **Variables CSS :root** - Todas las variables definidas (--brand, --brand-light, --text, etc.)
- [ ] **Base styles** - *, body, .container, h1/h2/h3 definidos
- [ ] **Nav styles** - .nav, .nav-wrapper, .logo, .logo img completos
- [ ] **Hero styles** - .hero, .hero-background, .hero-content, .hero::after, media queries móvil
- [ ] **Button styles** - .btn-primary con gradientes y transiciones
- [ ] **Floating buttons** - .floating-btn, .floating-call, .floating-whatsapp

**❌ SI FALTA CRITICAL CSS → La página NO funciona correctamente**

### 📋 2. Estructura Hero (OBLIGATORIO)

- [ ] **`<header id="inicio" class="hero">`** - Tag correcto
- [ ] **`<picture class="hero-background">`** - NO div, DEBE ser picture
- [ ] **`<source type="image/webp">`** - Elemento source presente
- [ ] **srcset con 800w y 1200w** - Dos variantes de imagen
- [ ] **`<img>` con todos los atributos:**
  - [ ] `src="...emergencia-electrica-culiacan-1200w.webp"`
  - [ ] `srcset="...800w.webp 800w, ...1200w.webp 1200w"`
  - [ ] `sizes="100vw"`
  - [ ] `alt="..."` descriptivo
  - [ ] `width="1200"`
  - [ ] `height="655"`
  - [ ] `fetchpriority="high"`
  - [ ] `loading="eager"`
  - [ ] `decoding="async"` ← CRÍTICO, se olvida frecuentemente

**❌ SI FALTA decoding="async" → Hero puede causar layout shift**

### 📋 3. Botones Flotantes (OBLIGATORIO)

- [ ] **Botón WhatsApp presente** con:
  - [ ] `href="https://wa.me/526673922273?text=..."`
  - [ ] `id="cta-whatsapp"`
  - [ ] `class="floating-btn floating-whatsapp"`
  - [ ] SVG icon completo (NO emoji 💬)
  - [ ] `<span class="online-badge"></span>`

- [ ] **Botón Llamar presente** con:
  - [ ] `href="tel:+526673922273"`
  - [ ] `id="cta-llamar"`
  - [ ] `class="floating-btn floating-call"`
  - [ ] SVG icon completo (NO emoji 📞)

- [ ] **NO usa `<div class="cta-bar">`** - Botones van directos sin contenedor

**❌ SI USA EMOJIS EN VEZ DE SVG → Inconsistencia visual entre plataformas**

### 📋 4. Logo con Dimensiones (OBLIGATORIO)

- [ ] **Logo en nav:**
  - [ ] `<img src="../../logo-electricista-culiacan-pro.webp"`
  - [ ] `width="140"`
  - [ ] `height="140"`
  - [ ] `alt="Electricista Culiacán Pro"`

- [ ] **Logo en footer (si aplica):**
  - [ ] `width="200"`
  - [ ] `height="76"`

**❌ SI FALTAN DIMENSIONES → CLS (Cumulative Layout Shift) alto**

### 📋 5. SEO Meta Tags (OBLIGATORIO)

- [ ] **Title:** 50-60 caracteres (óptimo), máximo 70
- [ ] **Meta description:** 120-155 caracteres (óptimo), máximo 160
- [ ] **Canonical URL:** `<link rel="canonical" href="https://..." />`
- [ ] **Theme color:** `<meta name="theme-color" content="#0066cc">`
- [ ] **Open Graph:** og:type, og:url, og:title, og:description, og:image
- [ ] **Twitter Card:** twitter:card, twitter:title, twitter:description, twitter:image

**❌ SI META DESCRIPTION FUERA DE RANGO → SEO audit FALLA**

### 📋 6. Breadcrumb HTML (OBLIGATORIO)

- [ ] **Breadcrumb visible** presente después de `</nav>` y antes de `<header class="hero">`
- [ ] **Enlaces funcionales** a Inicio y secciones padre
- [ ] **Estilos aplicados:** .breadcrumb, .breadcrumb-link, .breadcrumb-separator, .breadcrumb-current

**Ejemplo correcto:**
```html
<nav class="breadcrumb" aria-label="Breadcrumb">
    <div class="container">
        <a href="/" class="breadcrumb-link">Inicio</a>
        <span class="breadcrumb-separator">›</span>
        <a href="/#servicios" class="breadcrumb-link">Servicios</a>
        <span class="breadcrumb-separator">›</span>
        <span class="breadcrumb-current">Precios</span>
    </div>
</nav>
```

**❌ SI FALTA BREADCRUMB VISUAL → UX pobre, usuario se pierde**

### 📋 7. Google Tag Manager (OBLIGATORIO)

- [ ] **Google Analytics (gtag.js)** en `<head>`:
  ```html
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-NSV2K9N2ZD"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-NSV2K9N2ZD');
  </script>
  ```

- [ ] **GTM lazy load** después de `<body>`:
  ```html
  <script>
  window.dataLayer = window.dataLayer || [];
  (function() {
    var loadGTM = function() {
      var script = document.createElement('script');
      script.async = true;
      script.src = 'https://www.googletagmanager.com/gtm.js?id=GTM-W75CRTX5';
      document.head.appendChild(script);
    };
    if (window.requestIdleCallback) {
      requestIdleCallback(loadGTM);
    } else {
      setTimeout(loadGTM, 1);
    }
  })();
  </script>
  ```

- [ ] **GTM noscript** después del script anterior:
  ```html
  <noscript>
    <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W75CRTX5"
            height="0" width="0" style="display:none;visibility:hidden"></iframe>
  </noscript>
  ```

**❌ SI FALTA GTM → Deployment FALLA en SEO audit**

### 📋 8. Teléfonos Correctos (OBLIGATORIO)

- [ ] **TODOS los teléfonos son 667 392 2273**
- [ ] **WhatsApp:** `https://wa.me/526673922273`
- [ ] **Tel links:** `tel:+526673922273`
- [ ] **NO hay 667 000 0000** en ninguna parte
- [ ] **NO hay 667 163 1231** en ninguna parte

**❌ SI HAY TELÉFONOS VIEJOS → Cliente no puede contactar correctamente**

### 📋 9. Imágenes Hero Correctas (OBLIGATORIO)

- [ ] **USA:** `emergencia-electrica-culiacan-800w.webp` y `emergencia-electrica-culiacan-1200w.webp`
- [ ] **NO USA:** hero-electricista-culiacan-*.webp (obsoletas)
- [ ] **Rutas correctas** según profundidad:
  - Servicios: `../../assets/images/optimizadas/`
  - Colonias: `../../assets/images/optimizadas/`

**❌ SI USA IMÁGENES OBSOLETAS → Inconsistencia visual**

### 📋 10. JSON-LD Schemas (OBLIGATORIO)

- [ ] **WebSite schema** presente
- [ ] **BreadcrumbList schema** presente y coincide con breadcrumb HTML
- [ ] **Service schema** presente
- [ ] **LocalBusiness/Electrician schema** presente con:
  - [ ] Teléfono correcto: +52 667 392 2273
  - [ ] Email: contacto@electricistaculiacanpro.mx
  - [ ] Coordenadas: 24.7903, -107.3878
- [ ] **FAQPage schema** presente (si aplica)

**❌ SI FALTAN SCHEMAS → SEO degradado, rich snippets no aparecen**

### 📋 11. Responsive Mobile (OBLIGATORIO)

- [ ] **Media query móvil** presente en Critical CSS:
  ```css
  @media (max-width:768px){
    .hero{min-height:75vh;padding-top:85px!important;align-items:flex-start!important}
    .hero-background img{object-position:20% 35%}
    .hero-content{margin-top:0!important;padding:1.5rem 1.25rem!important;
      background:rgba(255,255,255,0.12)!important;
      backdrop-filter:blur(2px)!important}
    .hero h1{margin-bottom:0.5rem!important;font-size:clamp(1.5rem,5vw,2rem)!important}
    .hero-subtitle{display:none!important}
    .hero .btn-primary{width:100%!important;font-size:1rem!important;padding:0.875rem 1.5rem!important}
  }
  ```

- [ ] **Logo responsive** con media query:
  ```css
  @media (max-width:768px){.logo img{height:90px;max-height:100px}}
  ```

**❌ SI FALTA CSS MÓVIL → 60%+ usuarios tienen experiencia rota**

### 📋 12. Estilos CSS Inline (PROHIBIDO)

- [ ] **NO usa CSS inline custom** tipo `style="color:#1E40AF"` en elementos
- [ ] **SOLO usa clases existentes** de index.html: .hero, .card, .benefit, .btn-primary, etc.
- [ ] **NO inventa clases nuevas** como .highlight-box, .warning-box, .info-box

**✅ PERMITIDO:** `style="display:grid;gap:2rem"` para layouts específicos
**❌ PROHIBIDO:** Crear divs con colores de fondo custom (#fef3c7, #fee2e2, etc.)

### 📋 13. Enlaces styles.css (OBLIGATORIO)

- [ ] **styles.css enlazado** después de Critical CSS:
  ```html
  <!-- Non-critical CSS -->
  <link rel="stylesheet" href="../../styles.css">
  ```

- [ ] **Comentario presente** para claridad

**❌ SI FALTA styles.css → Estilos de cards, grids, footer rotos**

### 📋 14. Verificación Visual (OBLIGATORIO)

**Desktop (1920px, 1440px, 1280px):**
- [ ] Hero centrado perfectamente vertical y horizontalmente
- [ ] Textos hero legibles sobre imagen de fondo
- [ ] Logo con tamaño correcto (140x140px)
- [ ] Botones flotantes visibles en esquina inferior derecha
- [ ] Cards alineadas en grid responsive
- [ ] Footer con todos los elementos visibles

**Mobile (375px, 390px, 428px):**
- [ ] Hero con `align-items:flex-start` (contenido arriba)
- [ ] `.hero-content` con backdrop-filter funcionando
- [ ] Título hero legible (tamaño reducido)
- [ ] `.hero-subtitle` oculto (display:none)
- [ ] Logo reducido a 90px altura
- [ ] Botones flotantes NO obstruyen contenido
- [ ] NO hay scroll horizontal
- [ ] Formularios y tablas responsive

**❌ SI NO SE VE PERFECTO EN AMBOS → NO hacer commit**

---

## 🚨 PROCEDIMIENTO DE VALIDACIÓN

**ANTES de hacer commit:**

1. ✅ **Ejecutar checklist completo** (los 14 puntos anteriores)
2. ✅ **Abrir página local** en navegador
3. ✅ **Verificar en DevTools:**
   - Desktop: 1440px width
   - Mobile: 375px width
4. ✅ **Validar en ambas versiones:**
   - Hero centrado/alineado correctamente
   - Botones flotantes visibles
   - Imágenes cargando
   - Teléfonos clickeables
5. ✅ **Verificar meta tags:**
   - Title: 50-60 chars
   - Description: 120-155 chars
6. ✅ **Verificar consola:**
   - NO errores 404 (imágenes/fuentes faltantes)
   - NO errores JavaScript
   - GTM cargando correctamente

**SOLO SI TODOS LOS CHECKS PASAN → Hacer commit**

---

## 📝 Template de Commit con Validación

Cuando hagas commit de una landing page, incluye ESTE template en el mensaje:

```
feat(landing): [nombre-de-la-pagina] - implementación completa

✅ VALIDACIÓN COMPLETADA:
- [x] Critical CSS completo (fonts + vars + styles)
- [x] Hero structure con picture + decoding="async"
- [x] Botones flotantes con SVG icons
- [x] Logo 140x140 con dimensiones
- [x] SEO: Title 50-60 chars, Description 120-155 chars
- [x] Breadcrumb HTML visible
- [x] GTM: gtag.js + GTM lazy load + noscript
- [x] Teléfonos: 667 392 2273 (todos)
- [x] Imagen hero: emergencia-electrica-culiacan
- [x] JSON-LD schemas: WebSite + Breadcrumb + Service + FAQ
- [x] Responsive mobile: media queries OK
- [x] NO CSS inline custom
- [x] styles.css enlazado
- [x] Verificado visualmente: Desktop 1440px + Mobile 375px

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## ⚠️ ERRORES COMUNES A EVITAR

Estos son los errores MÁS FRECUENTES encontrados en auditorías:

1. **❌ Olvidar `decoding="async"` en hero `<img>`** → Layout shift
2. **❌ Usar emojis en botones flotantes en vez de SVG** → Inconsistencia visual
3. **❌ Logo sin width/height** → CLS alto
4. **❌ Teléfonos viejos (667 000 0000)** → Cliente no puede llamar
5. **❌ Hero usa hero-electricista en vez de emergencia-electrica** → Imagen obsoleta
6. **❌ NO incluir Critical CSS inline** → FOUC (Flash of Unstyled Content)
7. **❌ GTM con ID placeholder (GTM-XXXXXXX)** → Tracking roto
8. **❌ Meta description fuera de 120-155 chars** → SEO audit FALLA
9. **❌ Breadcrumb solo en JSON-LD, NO HTML visible** → UX pobre
10. **❌ Mobile no probado** → 60% usuarios con experiencia rota
