# Landing Creator

Crea nuevas landing pages clonando el estilo exacto de electricistaculiacanpro.mx. Solo necesitas proporcionar contenido y fotos.

## Qué hace este comando

1. **Clona estilos exactos** - Copia todos los estilos, colores, fuentes, botones de index.html
2. **Estructura idéntica** - Header, hero, secciones, footer iguales
3. **SEO completo** - Meta tags, Open Graph, JSON-LD schemas automáticos
4. **Responsive** - Mobile-first como la homepage
5. **Solo pides contenido** - Tú solo das textos y rutas de imágenes

## ⚠️ IMPORTANTE - Fuente de Verdad

**FUENTE DE ESTILOS:** `index.html` (raíz del proyecto)
- Este es el sitio de referencia para TODOS los estilos, CSS, estructura y colores
- CLONAR EXACTAMENTE los estilos de index.html

🎨 **COLORES Y ESTILOS - MANTENER EXACTOS:**

✅ **Usar EXACTAMENTE los mismos colores que index.html:**
- `--brand: #E36414` (naranja principal)
- `--brand-light: #F97316` (naranja claro)
- `--gradient-brand: linear-gradient(135deg, #F97316 0%, #E36414 100%)`
- `--text: #0F172A`
- `--text-light: #475569`
- `--bg: #FFFFFF`
- `--bg-soft: #F8FAFC`
- `--border: #E2E8F0`
- `--shadow: rgba(15,23,42,0.1)`
- `--container-max-width: 1200px`
- `--container-gutter: 24px`

✅ **Theme color:** `#0066cc`

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
