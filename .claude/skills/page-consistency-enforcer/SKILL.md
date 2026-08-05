---
name: page-consistency-enforcer
description: Garantiza que todas las páginas del sitio usen la misma tipografía, iconos SVG, estructura HTML y SEO que https://electricistaculiacanpro.mx/ (homepage). Se activa automáticamente al crear o revisar páginas.
allowed-tools: Read(*), Edit(*), Write(*), Grep(*), Glob(**), WebFetch(*)
---

# Page Consistency Enforcer

## Cuándo activarme

Actívame AUTOMÁTICAMENTE cuando:
- Usuario dice "crea una página de [servicio/colonia]"
- Usuario dice "revisa la página de [ubicación]"
- Usuario edita archivos `.html` en `servicios/` o `colonias/`
- Usuario pregunta "¿está bien esta página?"
- Usuario menciona "hacer una página" o "revisar otra página"

## Homepage de Referencia

**URL:** https://electricistaculiacanpro.mx/
**Archivo local:** `index.html`

Esta es la **fuente de verdad** para:
- Tipografía
- Iconos SVG
- Estructura HTML
- SEO Meta Tags
- Schema JSON-LD
- Critical CSS
- Clases CSS

---

## Elementos Obligatorios de la Homepage

### 1. TIPOGRAFÍA (CRÍTICO)

**Headings (H1, H2, H3):**
```css
h1,h2,h3{
  font-family:'Montserrat',sans-serif;
  font-weight:800;
  color:var(--text);
  letter-spacing:-0.025em;
  line-height:1.2
}
```

**Body:**
```css
body{
  font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  font-size:16px;
  line-height:1.7;
  color:var(--text)
}
```

**Font-faces obligatorios (en <style> inline):**
```css
@font-face{font-family:'Inter';font-weight:400;src:url('../../assets/fonts/inter-400.woff2')}
@font-face{font-family:'Inter';font-weight:500;src:url('../../assets/fonts/inter-400.woff2')}
@font-face{font-family:'Inter';font-weight:600;src:url('../../assets/fonts/inter-400.woff2')}
@font-face{font-family:'Montserrat';font-weight:700;src:url('../../assets/fonts/montserrat-800.woff2')}
@font-face{font-family:'Montserrat';font-weight:800;src:url('../../assets/fonts/montserrat-800.woff2')}
```
<!-- font-dedup 2026-07-26/2026-08-04: inter-500/inter-600/montserrat-700.woff2 eran duplicados
     byte-a-byte de inter-400/montserrat-800.woff2. Los archivos duplicados se borraron; el
     font-weight declarado se conserva pero la URL apunta al archivo real consolidado. -->

**❌ PROHIBIDO:**
- Usar otras fuentes
- Cambiar font-weight de headings
- Usar font-family diferente

---

### 2. ICONOS SVG (CRÍTICO)

**SIEMPRE usar SVG, NUNCA emojis (⚡💡🛡️🔌💬📞)**

#### Benefits Section - 4 Iconos Obligatorios:

**1. Reloj (Rapidez/Llegada):**
```html
<div class="benefit-icon">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <circle cx="12" cy="12" r="10"/>
    <polyline points="12 6 12 12 16 14"/>
  </svg>
</div>
```

**2. Dinero (Precios/Transparencia):**
```html
<div class="benefit-icon">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
  </svg>
</div>
```

**3. Escudo (Garantía):**
```html
<div class="benefit-icon">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
  </svg>
</div>
```

**4. Documento (Certificación/Factura):**
```html
<div class="benefit-icon">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
    <polyline points="14 2 14 8 20 8"/>
    <line x1="16" y1="13" x2="8" y2="13"/>
    <line x1="16" y1="17" x2="8" y2="17"/>
    <polyline points="10 9 9 9 8 9"/>
  </svg>
</div>
```

#### Botones Flotantes - 2 Iconos Obligatorios:

**WhatsApp:**
```html
<a class="floating-btn floating-whatsapp">
  <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
  </svg>
</a>
```

**Teléfono:**
```html
<a class="floating-btn floating-call">
  <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
    <path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"/>
  </svg>
</a>
```

---

### 3. ESTRUCTURA HTML (CRÍTICO)

#### Hero Section (Obligatorio):
```html
<header id="inicio" class="hero">
  <picture class="hero-background">
    <source type="image/webp"
            srcset="...800w.webp 800w, ...1200w.webp 1200w"
            sizes="100vw">
    <img src="...1200w.webp"
         srcset="...800w.webp 800w, ...1200w.webp 1200w"
         width="1200" height="800"
         fetchpriority="high"
         loading="eager"
         decoding="async"
         alt="...">
  </picture>
  <div class="container">
    <div class="hero-content">
      <h1>Título Principal</h1>
      <p class="hero-subtitle">Subtítulo descriptivo</p>
      <div class="hero-rating">
        <svg class="google-logo">...</svg>
        <span class="rating-stars">★★★★★</span>
        <span class="rating-score">4.8/5</span>
      </div>
      <div class="hero-features">
        <div class="feature-item">
          <svg>...</svg>
          <span>Llegada en 30-60 min</span>
        </div>
        <!-- más features -->
      </div>
      <a href="#contacto" class="btn-primary">CTA Principal</a>
    </div>
  </div>
</header>
```

#### Benefits Section (Obligatorio):
```html
<section class="section" id="beneficios">
  <div class="container">
    <h2>Título de Beneficios</h2>
    <div class="grid benefits-grid">
      <!-- 4 Benefits -->
      <div class="card benefit">
        <div class="benefit-icon">
          <svg>...</svg>
        </div>
        <div class="benefit-content">
          <h3>Título Beneficio</h3>
          <p>Descripción...</p>
          <ul class="service-list">
            <li>Punto 1</li>
            <li>Punto 2</li>
          </ul>
        </div>
      </div>

      <!-- WhatsApp CTA Box (OBLIGATORIO) -->
      <div class="whatsapp-cta-box">
        <svg class="whatsapp-icon-large" viewBox="0 0 24 24" fill="currentColor">
          <path d="M17.472 14.382c..."/>
        </svg>
        <h3>¿Tienes dudas? Respondemos en 10 minutos</h3>
        <p>Chatea con nosotros y recibe atención personalizada</p>
        <a href="https://wa.me/526673922273?text=..."
           class="whatsapp-cta-button"
           target="_blank"
           rel="noopener">Abrir Chat</a>
      </div>
    </div>
  </div>
</section>
```

#### Service Cards (Obligatorio):
```html
<a href="..." class="card card--img">
  <div class="service-card">
    <figure class="media-box">
      <picture>
        <source type="image/webp"
                srcset="...420w.webp 420w, ...800w.webp 800w"
                sizes="(max-width:768px) 100vw, 420px">
        <img src="...420w.webp"
             width="420" height="420"
             loading="lazy"
             decoding="async"
             alt="...">
      </picture>
    </figure>
  </div>
  <h3>Título del Servicio</h3>
  <p>Descripción breve del servicio...</p>
  <span class="service-cta">Más Información →</span>
</a>
```

**❌ PROHIBIDO en Service Cards:**
- Emojis en H3: `<h3>⚡ Instalación</h3>`
- Imágenes NO cuadradas: `width="800" height="600"`
- Falta `service-cta`: debe tener `<span class="service-cta">Más Información →</span>`
- Estilos inline: `style="text-decoration:none"`

#### Botones Flotantes (Obligatorio):
```html
<!-- Antes del cierre </body> -->
<div style="position:fixed;bottom:20px;right:20px;z-index:100;display:flex;flex-direction:column;gap:10px">
  <a href="https://wa.me/526673922273?text=..."
     class="floating-btn floating-whatsapp"
     target="_blank"
     rel="noopener"
     aria-label="Contactar por WhatsApp">
    <svg width="24" height="24">...</svg>
  </a>
  <a href="tel:+526673922273"
     class="floating-btn floating-call"
     aria-label="Llamar ahora">
    <svg width="24" height="24">...</svg>
  </a>
</div>
```

---

### 4. SEO META TAGS (OBLIGATORIO)

```html
<head>
  <!-- Title y Description -->
  <title>[Servicio/Colonia] en Culiacán | [Beneficio] 24/7</title>
  <meta name="description" content="...descripción optimizada 120-155 chars...">
  <meta name="keywords" content="electricista, culiacán, [variaciones]">

  <!-- Canonical -->
  <link rel="canonical" href="https://electricistaculiacanpro.mx/[ruta]/">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://electricistaculiacanpro.mx/[ruta]/">
  <meta property="og:title" content="[Título SEO]">
  <meta property="og:description" content="[Descripción]">
  <meta property="og:image" content="https://electricistaculiacanpro.mx/assets/images/...">
  <meta property="og:locale" content="es_MX">
  <meta property="og:site_name" content="Electricista Culiacán Pro">

  <!-- Twitter Cards -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://electricistaculiacanpro.mx/[ruta]/">
  <meta name="twitter:title" content="[Título]">
  <meta name="twitter:description" content="[Descripción]">
  <meta name="twitter:image" content="https://electricistaculiacanpro.mx/assets/images/...">
</head>
```

---

### 5. SCHEMA JSON-LD (OBLIGATORIO)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://electricistaculiacanpro.mx/#website",
      "url": "https://electricistaculiacanpro.mx/",
      "name": "Electricista Culiacán Pro",
      "inLanguage": "es-MX"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://electricistaculiacanpro.mx/[ruta]/#breadcrumb",
      "itemListElement": [...]
    },
    {
      "@type": "Electrician",
      "@id": "https://electricistaculiacanpro.mx/#business",
      "name": "Electricista Culiacán Pro",
      "telephone": "+52 667 392 2273",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Culiacán",
        "addressRegion": "Sinaloa",
        "addressCountry": "MX"
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "reviewCount": "150",
        "bestRating": "5",
        "worstRating": "1"
      }
    },
    {
      "@type": "Service",
      "serviceType": "[Tipo de Servicio]",
      "provider": {"@id": "https://electricistaculiacanpro.mx/#business"}
    },
    {
      "@type": "FAQPage",
      "mainEntity": [...]
    }
  ]
}
```

---

### 6. CRITICAL CSS INLINE (OBLIGATORIO)

```html
<style>
  /* Font-faces */
  @font-face{font-family:'Inter';font-weight:400;src:url('../../assets/fonts/inter-400.woff2')}
  @font-face{font-family:'Inter';font-weight:500;src:url('../../assets/fonts/inter-400.woff2')}
  @font-face{font-family:'Inter';font-weight:600;src:url('../../assets/fonts/inter-400.woff2')}
  @font-face{font-family:'Montserrat';font-weight:700;src:url('../../assets/fonts/montserrat-800.woff2')}
  @font-face{font-family:'Montserrat';font-weight:800;src:url('../../assets/fonts/montserrat-800.woff2')}

  /* Variables CSS */
  :root{
    --brand:#0047AB;
    --brand-light:#0066FF;
    --accent:#FF6600;
    --text:#0F172A;
    --text-light:#475569;
    --bg:#FFFFFF;
    --bg-soft:#F8FAFC
  }

  /* Reset */
  *{margin:0;padding:0;box-sizing:border-box}

  /* Body */
  body{
    font-family:'Inter',-apple-system,sans-serif;
    font-size:16px;
    line-height:1.7;
    color:var(--text);
    padding-top:80px
  }

  /* Container */
  .container{max-width:1200px;margin:0 auto;padding:0 24px}

  /* Headings */
  h1,h2,h3{
    font-family:'Montserrat',sans-serif;
    font-weight:800;
    color:var(--text)
  }

  /* Nav */
  .nav{
    position:fixed;
    top:0;left:0;right:0;
    z-index:50;
    background:rgba(0,71,171,0.98);
    padding:16px 0
  }

  /* Hero */
  .hero{
    min-height:85vh;
    display:grid;
    place-items:center;
    text-align:center;
    position:relative
  }

  .hero-background{position:absolute;inset:0;z-index:0}
  .hero-background img{
    width:100%;
    height:100%;
    object-fit:cover;
    content-visibility:auto
  }

  .hero-content{
    position:relative;
    z-index:2;
    max-width:900px;
    margin:0 auto
  }

  /* Mobile */
  @media (max-width:768px){
    .hero{min-height:75vh}
    .hero-content{padding:1.5rem 1.25rem}
  }
</style>

<!-- Load full CSS -->
<link rel="stylesheet" href="../../styles.min.css">
```

---

## Proceso de Validación

Cuando creo o reviso una página:

### Paso 1: Leer homepage de referencia
```
Leo index.html local O uso WebFetch para obtener https://electricistaculiacanpro.mx/
```

### Paso 2: Leer página objetivo

### Paso 3: Validar 14 áreas críticas

1. ✅ **Tipografía**: Montserrat (headings) + Inter (body)
2. ✅ **Icons Benefits**: 4 SVG icons (NO emojis ⚡💡🛡️🔌)
3. ✅ **Icons Botones**: 2 SVG (NO emojis 💬📞)
4. ✅ **Hero**: `<picture>` con fetchpriority="high"
5. ✅ **Hero CSS**: `content-visibility:auto` en img
6. ✅ **Benefits**: Estructura `benefit-icon + benefit-content`
7. ✅ **WhatsApp CTA Box**: Presente en benefits-grid
8. ✅ **Service Cards**: Estructura `service-card + media-box`
9. ✅ **Service Cards**: Imágenes 420x420 (cuadradas)
10. ✅ **Service Cards**: Sin emojis en H3
11. ✅ **Service Cards**: `<span class="service-cta">` presente
12. ✅ **Botones Flotantes**: Clases `floating-btn floating-whatsapp/call`
13. ✅ **SEO**: Meta tags completos (title, description, OG, Twitter)
14. ✅ **Schema**: JSON-LD completo (WebSite, BreadcrumbList, Electrician, Service, FAQPage)

### Paso 4: Generar reporte

```markdown
## 📋 Validación de Consistencia con Homepage

**Página:** colonias/tres-rios/index.html
**Referencia:** https://electricistaculiacanpro.mx/

### ✅ APROBADAS (12/14)

- Tipografía correcta (Montserrat + Inter)
- Hero estructura `<picture>` correcta
- SEO completo (meta tags + schema)
- Service cards estructura correcta

### ❌ ERRORES (2/14)

1. **Benefits usan emojis en vez de SVG**
   - Líneas: 359, 368, 377, 386
   - Encontrado: `<div style="font-size:3rem">⚡</div>`
   - Debe ser: `<div class="benefit-icon"><svg>...</svg></div>`

2. **Falta whatsapp-cta-box**
   - Línea: 394
   - Debe agregarse dentro de `.benefits-grid`

**Estado:** ❌ REQUIERE CORRECCIONES (2 errores)
```

### Paso 5: Corregir (si usuario autoriza)

Si usuario dice "s", "corrige", "corrígelos":
1. Aplico correcciones usando Edit tool
2. Revalido página (debe quedar 14/14)
3. Abro en navegador local
4. Pido verificación visual mobile + desktop

---

## Reglas de Corrección

### Tipografía:
```html
<!-- ❌ Incorrecto -->
<style>h1{font-family:'Arial'}</style>

<!-- ✅ Correcto -->
<style>
h1,h2,h3{font-family:'Montserrat',sans-serif;font-weight:800}
body{font-family:'Inter',-apple-system,sans-serif}
</style>
```

### Icons Benefits:
```html
<!-- ❌ Incorrecto -->
<div style="font-size:3rem">⚡</div>

<!-- ✅ Correcto -->
<div class="benefit-icon">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <circle cx="12" cy="12" r="10"/>
    <polyline points="12 6 12 12 16 14"/>
  </svg>
</div>
```

### Botones Flotantes:
```html
<!-- ❌ Incorrecto -->
<a class="btn-primary">💬 WhatsApp</a>

<!-- ✅ Correcto -->
<a class="floating-btn floating-whatsapp">
  <svg width="24" height="24">...</svg>
</a>
```

---

## NO hacer

- NO cambiar colores del branding
- NO modificar contenido textual (solo estructura)
- NO cambiar tamaños de fuente personalizados
- Solo garantizar CONSISTENCIA con homepage

---

## Ejemplo Completo

```
Usuario: "Crea una página para la colonia Chapultepec"

Yo (skill activado automáticamente):
1. Leo https://electricistaculiacanpro.mx/ como referencia
2. Creo colonias/chapultepec/index.html con:
   - Misma tipografía (Montserrat + Inter)
   - Mismos iconos SVG (NO emojis)
   - Misma estructura HTML
   - Mismo SEO completo
   - Mismo Critical CSS inline
3. Valido 14/14 áreas ✅
4. Entrego página lista

Usuario: "Revisa servicios/instalacion-electrica/"

Yo (skill activado automáticamente):
1. Leo homepage https://electricistaculiacanpro.mx/
2. Leo servicios/instalacion-electrica/index.html
3. Valido y encuentro:
   - ❌ Usa emojis (⚡🔧) en H3 de service cards
   - ❌ Falta whatsapp-cta-box
   - ❌ Botones flotantes con clase incorrecta
4. Pregunto: "¿Corrijo automáticamente? (s/n)"
5. Si s: Aplico correcciones, revalido (14/14), abro en navegador
```

---

## Referencias

- **Homepage de producción:** https://electricistaculiacanpro.mx/
- **Homepage local:** `index.html`
- **Validador de páginas:** `.claude/skills/validador-pagina.md`
- **Landing Creator:** `.claude/commands/landing-creator.md`
