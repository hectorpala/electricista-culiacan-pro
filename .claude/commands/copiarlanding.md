# Copiar Landing v2.0.0 (Método Manual)

Crea landings nuevas clonando `reparacion-cortos-circuitos` y cambiando SOLO el contenido.

---

## 🤖 ¿Método automático o manual?

Ahora tienes **2 opciones** para crear landings:

### Opción 1: **Semi-automatizado** ⚡ (Recomendado)
```
/automatizaciondelanding "Nombre del Servicio"
```
- ✅ Crea estructura base automáticamente
- ✅ Genera slug y copia template v2.0.0
- ✅ Valida imágenes automáticamente
- ⚠️ Requiere imagen base 800w
- ⚠️ Requiere generar contenido SEO manualmente
- ⚠️ Requiere aplicar contenido con @agentconstructor
- ⏱️ 10-15 minutos totales

### Opción 2: **Manual** 🔧 (Este documento)
```
cp -r servicios/reparacion-cortos-circuitos servicios/nuevo-slug
# + edición manual de 21 secciones
```
- ✅ Control total sobre cada texto
- ✅ No requiere generación de contenido
- ✅ Útil para ediciones específicas
- ⏱️ Más lento (10-15 minutos)

**💡 Usa el método manual cuando:**
- Quieras control total sobre cada palabra
- Tengas el contenido ya preparado
- Necesites copiar de una landing existente diferente

**Usa el método semi-automatizado cuando:**
- Quieras que se genere la estructura base automáticamente
- Prefieras usar @agentconstructor para aplicar el contenido
- Necesites validación automática de imágenes

---

## 🎯 Proceso (3 pasos)

### Paso 1: Copiar carpeta

```bash
cp -r servicios/reparacion-cortos-circuitos servicios/[nuevo-slug]

# Ejemplos:
cp -r servicios/reparacion-cortos-circuitos servicios/instalacion-minisplit
cp -r servicios/reparacion-cortos-circuitos servicios/reparacion-apagadores
```

### Paso 2: Editar SOLO el contenido

Abre `servicios/[nuevo-slug]/index.html` y cambia **SOLO** estos textos:

#### A) `<head>` (líneas 6-8):

```html
<title>[Nuevo título 50-60 chars]</title>
<meta name="description" content="[Nueva descripción 120-155 chars]">
<meta name="keywords" content="[keywords separadas por comas]">
```

#### B) Canonical (línea 45):

```html
<link rel="canonical" href="https://electricistaculiacanpro.mx/servicios/[nuevo-slug]/">
```

#### C) Open Graph (líneas 133-137):

```html
<meta property="og:url" content="https://electricistaculiacanpro.mx/servicios/[nuevo-slug]/" />
<meta property="og:title" content="[Nuevo título]" />
<meta property="og:description" content="[Nueva descripción]" />
<meta property="og:image" content="https://electricistaculiacanpro.mx/assets/images/optimizadas/[nueva-imagen]-800w.webp" />
```

#### D) Twitter Card (líneas 142-145):

```html
<meta name="twitter:url" content="https://electricistaculiacanpro.mx/servicios/[nuevo-slug]/" />
<meta name="twitter:title" content="[Nuevo título]" />
<meta name="twitter:description" content="[Nueva descripción]" />
<meta name="twitter:image" content="https://electricistaculiacanpro.mx/assets/images/optimizadas/[nueva-imagen]-800w.webp" />
```

#### E) Schema Breadcrumb (líneas 174-177):

```javascript
{
  "@type": "ListItem",
  "position": 3,
  "name": "[Nombre del servicio]"
}
```

#### F) Schema Service (líneas 213-223):

```javascript
{
  "@type": "Service",
  "serviceType": "[Tipo de servicio]",
  "provider": {
    "@id": "https://electricistaculiacanpro.mx/#business"
  },
  "areaServed": {
    "@type": "City",
    "name": "Culiacán"
  },
  "description": "[Descripción del servicio en 1-2 frases]"
}
```

#### G) Breadcrumb HTML (línea 296):

```html
<span class="breadcrumb-current" itemprop="name">[Nombre Servicio]</span>
```

#### H) Hero imagen (líneas 307-318):

```html
<picture class="hero-background">
    <source type="image/webp"
            srcset="../../assets/images/optimizadas/[nueva-imagen]-culiacan-800w.webp 800w, ../../assets/images/optimizadas/[nueva-imagen]-culiacan-1200w.webp 1200w"
            sizes="100vw">
    <img src="../../assets/images/optimizadas/[nueva-imagen]-culiacan-1200w.webp"
         srcset="../../assets/images/optimizadas/[nueva-imagen]-culiacan-800w.webp 800w, ../../assets/images/optimizadas/[nueva-imagen]-culiacan-1200w.webp 1200w"
         sizes="100vw"
         alt="[Descripción de la imagen para SEO]"
         width="1200"
         height="655"
         fetchpriority="high"
         loading="eager"
         decoding="async">
</picture>
```

#### I) Hero H1 (línea 323):

```html
<h1 class="fade-in">[Nuevo H1 con keyword principal en Culiacán]</h1>
```

#### J) Hero subtitle (línea 339):

```html
<p class="hero-subtitle fade-in">[Nueva descripción del servicio - 1-2 líneas]</p>
```

#### K) Hero CTAs WhatsApp (líneas 369, 389):

```html
<a href="https://wa.me/526673922273?text=Hola,%20necesito%20[servicio]%20en%20Culiacán"
```

#### L) Benefits H2 (línea 399):

```html
<h2>¿Por qué somos el mejor servicio de [servicio] en Culiacán?</h2>
```

#### M) Benefits párrafo intro (líneas 400-403):

```html
<p style="text-align: center; max-width: 800px; margin: 0 auto 3rem; font-size: 1.1rem; color: #475569;">
    Más de <strong>150 clientes satisfechos</strong> en Las Quintas, Tres Ríos, Chapultepec, Montebello y Centro nos respaldan.
    <strong style="color: #E36414;">4.8★ en Google</strong> • [Descripción breve del servicio].
</p>
```

#### N) Benefits (4 tarjetas - líneas 405-457):

Reescribe cada benefit con:
```html
<div class="benefit">
    <div class="benefit-icon">
        <!-- Mantén el SVG o cámbialo según necesites -->
    </div>
    <div class="benefit-content">
        <h3>[Nuevo título benefit]</h3>
        <p>[Nueva descripción específica del servicio]</p>
    </div>
</div>
```

#### O) WhatsApp CTA box (líneas 459-475):

```html
<div class="whatsapp-cta-box">
    <div class="whatsapp-cta-icon">
        <!-- Mantén el SVG -->
    </div>
    <div class="whatsapp-cta-content">
        <h3>¿Tienes dudas? Respondemos en 10 minutos</h3>
        <p>Cotiza, agenda o reporta [tipo de servicio] por WhatsApp - cualquier hora del día</p>
    </div>
    <a href="https://wa.me/526673922273?text=Hola,%20necesito%20[servicio]%20en%20Culiacán" class="whatsapp-cta-button">
        <!-- Mantén el SVG -->
        Abrir Chat
    </a>
</div>
```

#### P) Benefits CTA final (líneas 478-481):

```html
<p class="benefits-cta">
    <strong>Agenda tu [servicio] hoy mismo desde WhatsApp o llamada al <a href="tel:6673922273">667 392 2273</a></strong><br>
    <span class="benefits-cta-subtitle">Servicio de [servicio] más confiable de Culiacán</span>
</p>
```

#### Q) Nuestros Servicios (líneas 486-579):

**NO CAMBIAR NADA** - Esta sección se copia TAL CUAL.

#### R) Floating CTAs (líneas 600, 609):

Actualizar solo el texto del WhatsApp:
```html
<a href="https://wa.me/526673922273?text=Hola%2C%20necesito%20[servicio]%20en%20Culiac%C3%A1n"
```

### Paso 3: Validar

```bash
# Validar estructura
./validate-landing.sh servicios/[nuevo-slug]/index.html

# Abrir en navegador
open servicios/[nuevo-slug]/index.html
```

## ✅ Checklist Final

- [ ] Title: 50-60 caracteres
- [ ] Meta description: 120-155 caracteres
- [ ] Canonical URL actualizado
- [ ] Open Graph URLs actualizadas
- [ ] Schema breadcrumb actualizado
- [ ] Schema Service actualizado
- [ ] Breadcrumb HTML actualizado
- [ ] Hero imagen paths actualizados
- [ ] H1 actualizado
- [ ] Hero subtitle actualizado
- [ ] Benefits H2 y contenido actualizados
- [ ] WhatsApp CTAs actualizados (4 lugares)
- [ ] Nuestros Servicios **SIN CAMBIOS**
- [ ] Validador pasa: `./validate-landing.sh` → ✅
- [ ] Se ve bien en desktop y mobile

## ❌ NO CAMBIES

- Estructura HTML (clases, IDs, divs)
- Colores, estilos CSS
- SVG icons
- Navegación, footer
- **Sección "Nuestros Servicios" COMPLETA**
- Floating CTAs (estructura, solo texto WhatsApp)
- Teléfonos (667 392 2273)
- GTM/GA IDs
- Critical CSS
- data-template-version="v2.0.0"

## 💡 Ejemplo

```bash
# 1. Copiar
cp -r servicios/reparacion-cortos-circuitos servicios/instalacion-minisplit

# 2. Editar contenido en index.html
# - Title: "Instalación Minisplit Culiacán | Clima Profesional"
# - Description: "⚡ Instalación minisplit en Culiacán. Inverter y estándar. Instalación certificada. ¡Llama: 667 392 2273!"
# - H1: "Instalación de Minisplit en Culiacán | Clima Profesional"
# - Hero image: emergencia-electrica-culiacan → instalacion-minisplit-culiacan
# - Benefits: 4 beneficios sobre instalación de clima

# 3. Validar
./validate-landing.sh servicios/instalacion-minisplit/index.html
open servicios/instalacion-minisplit/index.html
```

## ⚡ Regla de Oro

**SOLO cambia TEXTOS.**
**NUNCA cambies estructura, clases, estilos o IDs.**
**La sección "Nuestros Servicios" se copia IDÉNTICA.**

Si lo haces bien, el validador pasará a la primera ✅
