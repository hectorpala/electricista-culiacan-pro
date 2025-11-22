# Documentacion Tecnica - Electricista Culiacan Pro

**Sitio Web**: electricistaculiacanpro.mx  
**Fecha de creacion**: Noviembre 2024  
**Ultima actualizacion**: 22 de Noviembre, 2025  
**Version**: 2.1

---

## Tabla de Contenidos

1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Tipografia y Fuentes](#tipografia-y-fuentes)
3. [Sistema de Colores](#sistema-de-colores)
4. [Variables CSS](#variables-css)
5. [Componentes Principales](#componentes-principales)
6. [Optimizaciones de Performance](#optimizaciones-de-performance)
7. [SEO y Metadatos](#seo-y-metadatos)
8. [Estructura de Paginas](#estructura-de-paginas)

---

## Estructura del Proyecto

```
electricista website/
├── index.html                          # Pagina principal
├── styles.css                          # Estilos globales
├── script.js                           # JavaScript principal
│
├── fonts/                              # Fuentes autohospedadas
│   ├── inter-400.woff2
│   ├── inter-500.woff2
│   ├── inter-600.woff2
│   ├── montserrat-700.woff2
│   └── montserrat-800.woff2
│
├── img/                                # Imagenes optimizadas WebP
│   ├── instalacion-electrica-420w.webp
│   ├── instalacion-electrica-800w.webp
│   ├── tablero-electrico-420w.webp
│   ├── tablero-electrico-800w.webp
│   ├── contactos-apagadores-420w.webp
│   └── iluminacion-led-800w.webp
│
├── servicios/                          # Landing pages de servicios
│   ├── instalacion-electrica/
│   ├── reparacion-cortocircuitos/
│   ├── instalacion-contactos/
│   ├── iluminacion-led/
│   ├── mantenimiento-tableros/
│   ├── tierra-fisica/
│   └── electricista/
│       ├── 24-7/index.html
│       ├── cerca-de-mi/index.html
│       ├── a-domicilio/index.html
│       ├── precios/index.html
│       └── colonias/index.html
│
├── blog/                               # Blog de contenido
│   ├── index.html
│   ├── como-detectar-fallas-electricas-casa/
│   ├── problemas-comunes-electricidad-culiacan/
│   ├── cuando-llamar-electricista-profesional/
│   └── certificacion-cfe-instalacion-electrica/
│
├── sitemaps/
│   └── main_sitemap.xml
│
└── images/                             # Assets del sitio
    ├── favicon.ico
    ├── favicon.png
    └── logo-blue.svg
```

**Total de paginas HTML**: 24 archivos

---

## Sistema de Colores

### Paleta de Colores Principal

```css
:root {
  /* Colores de marca (Brand) */
  --brand: #1E40AF;              /* Azul principal */
  --brand-light: #3B82F6;        /* Azul claro (hover/accent) */
  --brand-dark: #1E3A8A;         /* Azul oscuro (pressed) */

  /* Accion especial */
  --accent: #FCD34D;             /* Amarillo electricidad */
  --whatsapp: #25D366;           /* Verde WhatsApp oficial */

  /* Textos */
  --text: #0F172A;               /* Texto principal (negro azulado) */
  --text-light: #475569;         /* Texto secundario (gris) */
  --text-muted: #475569;         /* Texto desenfatizado */

  /* Fondos */
  --bg: #FFFFFF;                 /* Fondo blanco puro */
  --bg-soft: #F8FAFC;            /* Fondo suave (gris muy claro) */
  --bg-card: #FFFFFF;            /* Fondo de tarjetas */

  /* Bordes y sombras */
  --border: #E2E8F0;             /* Bordes sutiles */
  --shadow: rgba(15,23,42,0.1);  /* Sombra suave */
  --shadow-lg: rgba(15,23,42,0.15); /* Sombra pronunciada */

  /* Gradientes */
  --gradient-brand: linear-gradient(135deg, #3B82F6 0%, #1E40AF 100%);
  --gradient-overlay: linear-gradient(135deg, rgba(15,23,42,0.9) 0%, rgba(30,41,59,0.8) 100%);
}
```

### Uso de Colores

| Elemento | Color | Variable CSS | Codigo Hex |
|----------|-------|--------------|------------|
| Boton principal | Azul | `var(--brand)` | `#1E40AF` |
| Hover de boton | Azul claro | `var(--brand-light)` | `#3B82F6` |
| Enlace activo | Azul oscuro | `var(--brand-dark)` | `#1E3A8A` |
| Acento amarillo | Amarillo | `var(--accent)` | `#FCD34D` |
| Boton WhatsApp | Verde | `var(--whatsapp)` | `#25D366` |

---

## Componentes Principales

### 1. Navegacion (Nav)

```html
<nav class="nav">
    <div class="container">
        <div class="nav-wrapper">
            <a href="/" class="logo">Electricista Culiacan Pro</a>
            <button class="mobile-menu-btn" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <ul class="nav-menu">
                <li><a href="#inicio" class="nav-link">Inicio</a></li>
                <li><a href="#servicios" class="nav-link">Servicios</a></li>
                <li><a href="#sobre-nosotros" class="nav-link">Sobre Nosotros</a></li>
                <li><a href="/blog/" class="nav-link">Blog</a></li>
                <li><a href="#contacto" class="nav-link">Contacto</a></li>
            </ul>
        </div>
    </div>
</nav>
```

**Caracteristicas**:
- Sticky position (fijo al hacer scroll)
- Responsive con menu hamburguesa en movil
- Height: 80px
- Background: Blanco con sombra sutil

### 2. Hero Section

```html
<header id="inicio" class="hero">
    <div class="container">
        <div class="hero-content">
            <h1 class="fade-in">Electricista Profesional en Culiacan, Sinaloa</h1>
            <p class="hero-subtitle fade-in">Soluciones electricas rapidas y confiables...</p>
            <p class="hero-contact">WhatsApp: 52 667 000 0000 · Llamadas: 667 000 0000</p>
            <a href="#contacto" class="btn-primary hover-lift">Solicitar Cotizacion</a>
        </div>
    </div>
</header>
```

---

## Optimizaciones de Performance

### 1. Imagenes

**Formato**: 100% WebP (no PNG/JPG)

**Estrategia de tamanos**:
- `420w`: Para moviles y thumbnails
- `800w`: Para tablets y desktop

**Ejemplo de implementacion**:
```html
<picture>
    <source type="image/webp" srcset="img/nombre-420w.webp 420w, img/nombre-800w.webp 800w">
    <img src="img/nombre-420w.webp" width="420" height="420" loading="lazy">
</picture>
```

**Beneficios**:
- Reduccion del 93% en peso vs PNG
- LCP mejorado (carga 10-15x mas rapida)
- Width/height explicitos previenen CLS

### 2. Core Web Vitals

| Metrica | Objetivo | Estado Actual |
|---------|----------|---------------|
| LCP (Largest Contentful Paint) | < 2.5s | ✅ Optimizado (WebP + preload) |
| FID (First Input Delay) | < 100ms | ✅ Vanilla JS ligero |
| CLS (Cumulative Layout Shift) | < 0.1 | ✅ Width/height explicitos |

---

## SEO y Metadatos

### 1. Meta Tags Basicos

```html
<title>Electricista en Culiacan a domicilio 24/7 | Electricista Culiacan Pro</title>
<meta name="description" content="Electricista en Culiacan 24/7: a domicilio, instalaciones, cortocircuitos y emergencias. Atencion rapida y precios claros. WhatsApp y telefono.">
<link rel="canonical" href="https://electricistaculiacanpro.mx/" />
```

### 2. JSON-LD Structured Data

**Electrician Schema**:
```json
{
  "@context": "https://schema.org",
  "@type": "Electrician",
  "name": "Electricista Culiacan Pro",
  "url": "https://electricistaculiacanpro.mx/",
  "telephone": "+52 667 000 0000",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Culiacan",
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
}
```

---

## Estructura de Paginas

### Pagina Principal (index.html)

**Secciones en orden**:

1. **Nav** - Navegacion sticky
2. **Hero** - Titulo principal + CTA
3. **Beneficios** - 3 iconos con beneficios clave
4. **Servicios** - Grid de 6 tarjetas con imagenes
5. **Enlaces SEO** - 5 enlaces a landings genericas
6. **Urgencias 24/7** - CTA de emergencia
7. **Zonas de Servicio** - Colonias atendidas
8. **Preguntas Frecuentes** - 6 FAQs
9. **Blog de Electricidad** - 3 articulos recientes
10. **Testimonios** - 6 resenas con estrellas + enlaces a Google/Facebook
11. **Servicios (Footer)** - Lista de enlaces
12. **Contacto** - Formulario + WhatsApp
13. **Footer** - Info de contacto + enlaces

---

## Checklist de Deploy

Antes de publicar cambios a produccion:

- [ ] Todas las imagenes estan en WebP
- [ ] Todas las imagenes tienen width/height
- [ ] Links internos funcionan correctamente
- [ ] Sitemap actualizado con nuevas paginas
- [ ] JSON-LD validado sin errores
- [ ] Open Graph tags completos en todas las paginas
- [ ] Branding consistente ("Electricista Culiacan Pro")
- [ ] Formularios de contacto funcionando
- [ ] Enlaces de WhatsApp con formato correcto
- [ ] Probado en Chrome, Firefox, Safari
- [ ] Probado en movil (iOS y Android)
- [ ] Core Web Vitals en verde (PageSpeed)
- [ ] Archivos CSS/JS minificados (opcional)

---

**Fin de Documentacion Tecnica**
*Version: 2.1 - 22 de Noviembre, 2025*
