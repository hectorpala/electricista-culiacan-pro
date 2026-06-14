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

### 📌 VERSIÓN DE REFERENCIA OFICIAL

**Última actualización:** [ACTUALIZAR AL SUBIR CAMBIOS]
**Versión de plantilla:** v2.0.0
**Commit/Hash:** [ACTUALIZAR CON ÚLTIMO COMMIT]

#### Archivos de Referencia

**FUENTE DE ESTILOS:** `index.html` (raíz del proyecto)
- **Ruta oficial:** `index.html`
- **Critical CSS:** Extraído a `assets/css/critical.css` (95 líneas, líneas 78-172 de index.html)
- **Hero structure:** Líneas 2815-2904
- **Botones flotantes:** Líneas 3862-3876
- **GTM scripts:** Líneas 19-26 (gtag.js) + 2744-2767 (GTM lazy load)
- **Breadcrumb:** Líneas 2790-2814
- Este es el ÚNICO sitio de referencia para TODOS los estilos, CSS, estructura y colores
- CLONAR EXACTAMENTE los estilos de index.html
- **NO interpretar, NO adaptar, NO mejorar - SOLO COPIAR**

**ESTILOS ADICIONALES:** `styles.css` (estilos no críticos)
- **Ruta oficial:** `styles.css`
- **Última modificación:** [ACTUALIZAR AL CAMBIAR]

#### Configuración Centralizada

**CONFIG CENTRAL:** `config/landing.json`
- **Ruta oficial:** `config/landing.json`
- **Contiene:** Teléfonos, WhatsApp, email, coordenadas, rutas de imágenes, IDs de tracking

**Todos los valores DEBEN leerse de este config, NO hardcodear.**

#### Hash de Validación

**Critical CSS Hash (MD5):** `53ef5e7f`
**Versión mínima requerida:** v2.0.0

**Comando para calcular hash:**
```bash
# Hash actual del Critical CSS compartido
md5 -q assets/css/critical.css | head -c 8
# Resultado: 53ef5e7f
```

---

### 📦 CRITICAL CSS COMPARTIDO

**⚠️ IMPORTANTE:** El Critical CSS NO se duplica en cada landing. Se sirve desde un archivo centralizado.

#### Estructura de Archivos

```
proyecto/
├── assets/
│   └── css/
│       └── critical.css          ← Critical CSS compartido (FUENTE ÚNICA)
├── config/
│   └── landing.json              ← Config centralizado
├── index.html                     ← Plantilla maestra
└── servicios/
    └── [slug]/
        └── index.html             ← Landing (USA critical.css)
```

#### Qué va INLINE vs Archivo Compartido

**✅ INLINE en cada landing (solo lo mínimo para LCP):**
```html
<head>
    <!-- Preload critical fonts -->
    <link rel="preload" href="../../assets/fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin fetchpriority="high">
    <link rel="preload" href="../../assets/fonts/montserrat-800.woff2" as="font" type="font/woff2" crossorigin fetchpriority="high">

    <!-- Preload hero image -->
    <link rel="preload" as="image" href="../../assets/images/optimizadas/emergencia-electrica-culiacan-1200w.webp" fetchpriority="high">

    <!-- Critical CSS compartido -->
    <link rel="stylesheet" href="../../assets/css/critical.css" fetchpriority="high">
</head>
```

**✅ EN assets/css/critical.css (95 líneas de index.html):**
- 5 fuentes web (@font-face)
- Variables CSS (:root)
- Base styles (*, body, container, h1/h2/h3)
- Nav styles
- Hero styles (desktop + mobile)
- Button styles
- Floating buttons
- Mobile media queries

**❌ NO DUPLICAR:** El bloque `<style>` completo ya NO va inline en cada landing.

#### Ventajas del Critical CSS Compartido

- ✅ **1 fuente de verdad** - Cambio en 1 archivo = actualiza todas las landings
- ✅ **Cacheable** - Navegador cachea critical.css, mejora performance
- ✅ **Menos duplicación** - Archivos HTML más pequeños
- ✅ **Más fácil mantener** - Actualizar estilos en 1 solo lugar
- ✅ **Validación centralizada** - Hash de critical.css valida todas las landings

#### Migración de Landings Existentes

**Antes (inline):**
```html
<head>
    <style>
        @font-face{...}  <!-- 95 líneas aquí -->
        :root{...}
        ...
    </style>
</head>
```

**Después (compartido):**
```html
<head>
    <link rel="stylesheet" href="../../assets/css/critical.css" fetchpriority="high">
</head>
```

**Comando para migrar:**
```bash
# 1. Extraer Critical CSS de index.html a archivo (95 líneas)
sed -n '78,172p' index.html > assets/css/critical.css

# 2. Actualizar landings para usar critical.css
find servicios/ -name "index.html" -exec sed -i '' 's|<style>.*</style>|<link rel="stylesheet" href="../../assets/css/critical.css" fetchpriority="high">|' {} \;
```

---

### 🗂️ CONFIGURACIÓN CENTRALIZADA

**config/landing.json** - Archivo de configuración central para TODAS las landings

#### Crear config/landing.json

```json
{
  "version": "v2.0.0",
  "lastUpdate": "2025-01-28T00:00:00Z",
  "contact": {
    "phone": "+526673922273",
    "phoneDisplay": "667 392 2273",
    "whatsapp": "526673922273",
    "email": "contacto@electricistaculiacanpro.mx"
  },
  "location": {
    "city": "Culiacán",
    "state": "Sinaloa",
    "country": "MX",
    "coordinates": {
      "latitude": 24.7903,
      "longitude": -107.3878
    }
  },
  "tracking": {
    "googleAnalyticsId": "G-7CML8QYBGQ",
    "googleTagManagerId": "GTM-5Z2QRZ5Q"
  },
  "images": {
    "heroDefault": {
      "800w": "assets/images/optimizadas/emergencia-electrica-culiacan-800w.webp",
      "1200w": "assets/images/optimizadas/emergencia-electrica-culiacan-1200w.webp",
      "alt": "Electricista profesional en Culiacán atendiendo emergencia 24 horas"
    },
    "logo": {
      "main": "logo-electricista-culiacan-pro.webp",
      "navDimensions": { "width": 140, "height": 140 },
      "footerDimensions": { "width": 200, "height": 76 }
    }
  },
  "business": {
    "name": "Electricista Culiacán Pro",
    "url": "https://electricistaculiacanpro.mx/",
    "rating": {
      "value": 4.8,
      "count": 50
    },
    "openingHours": "Mo,Tu,We,Th,Fr,Sa,Su 00:00-23:59",
    "priceRange": "$$"
  },
  "styles": {
    "criticalCssFile": "assets/css/critical.css",
    "criticalCssHash": "53ef5e7f",
    "mainCssFile": "styles.css",
    "themeColor": "#0066cc"
  }
}
```

#### Usar config en las Landings

**❌ ANTES (hardcoded):**
```html
<a href="https://wa.me/526673922273">WhatsApp</a>
<a href="tel:+526673922273">Llamar</a>
```

**✅ DESPUÉS (desde config):**
```javascript
// Cargar config
fetch('../../config/landing.json')
  .then(r => r.json())
  .then(config => {
    // Usar valores del config
    document.querySelector('#cta-whatsapp').href =
      `https://wa.me/${config.contact.whatsapp}`;
    document.querySelector('#cta-llamar').href =
      `tel:${config.contact.phone}`;
  });
```

**O mejor, usar template variables:**
```html
<!-- En el generador de landings, leer config primero -->
<a href="https://wa.me/{{config.contact.whatsapp}}">WhatsApp: {{config.contact.phoneDisplay}}</a>
```

#### Comando para Crear Config

```bash
cat > config/landing.json <<'EOF'
{
  "version": "v2.0.0",
  ...
}
EOF
```

---

### ✅ VALIDACIÓN AUTOMÁTICA DE VERSIONES

#### Script de Validación

**validate-landing.sh** - Valida que la landing use la versión correcta

```bash
#!/bin/bash

# Validador de Landing Pages v2.0.0
# Valida que la landing page use la plantilla vigente

LANDING_PATH="$1"
CONFIG_PATH="config/landing.json"
CRITICAL_CSS_PATH="assets/css/critical.css"

echo "🔍 Validando: $LANDING_PATH"

# 1. Verificar que existe el config
if [ ! -f "$CONFIG_PATH" ]; then
    echo "❌ FALLA: config/landing.json no existe"
    exit 1
fi

# 2. Leer versión vigente del config
VERSION_VIGENTE=$(jq -r '.version' "$CONFIG_PATH")
echo "✅ Versión vigente: $VERSION_VIGENTE"

# 3. Leer hash vigente del Critical CSS
CRITICAL_CSS_HASH_VIGENTE=$(jq -r '.styles.criticalCssHash' "$CONFIG_PATH")
echo "✅ Hash vigente Critical CSS: $CRITICAL_CSS_HASH_VIGENTE"

# 4. Calcular hash real del critical.css
CRITICAL_CSS_HASH_REAL=$(md5 -q "$CRITICAL_CSS_PATH" | head -c 8)

if [ "$CRITICAL_CSS_HASH_VIGENTE" != "$CRITICAL_CSS_HASH_REAL" ]; then
    echo "❌ FALLA: Hash de critical.css NO coincide"
    echo "   Vigente: $CRITICAL_CSS_HASH_VIGENTE"
    echo "   Real:    $CRITICAL_CSS_HASH_REAL"
    exit 1
fi

# 5. Verificar que la landing usa critical.css compartido
if ! grep -q "href=\".*critical.css\"" "$LANDING_PATH"; then
    echo "❌ FALLA: Landing NO usa critical.css compartido"
    exit 1
fi

# 6. Verificar versión de la landing (meta tag)
if grep -q "data-template-version=\"$VERSION_VIGENTE\"" "$LANDING_PATH"; then
    echo "✅ Landing usa versión vigente: $VERSION_VIGENTE"
else
    echo "❌ FALLA: Landing NO tiene versión vigente"
    echo "   Agregar: <meta name=\"template-version\" content=\"$VERSION_VIGENTE\" data-template-version=\"$VERSION_VIGENTE\">"
    exit 1
fi

# 7. Verificar teléfonos del config
CONFIG_PHONE=$(jq -r '.contact.whatsapp' "$CONFIG_PATH")
if ! grep -q "$CONFIG_PHONE" "$LANDING_PATH"; then
    echo "❌ FALLA: Landing NO usa teléfono del config"
    echo "   Config: $CONFIG_PHONE"
    exit 1
fi

# 8. Verificar GTM ID del config
CONFIG_GTM=$(jq -r '.tracking.googleTagManagerId' "$CONFIG_PATH")
if ! grep -q "$CONFIG_GTM" "$LANDING_PATH"; then
    echo "❌ FALLA: Landing NO usa GTM ID del config"
    echo "   Config: $CONFIG_GTM"
    exit 1
fi

echo ""
echo "✅ ✅ ✅ VALIDACIÓN EXITOSA"
echo "Landing $LANDING_PATH pasa todas las validaciones"
exit 0
```

#### Uso del Validador

```bash
# Validar una landing específica
./validate-landing.sh servicios/reparacion-cortos-circuitos/index.html

# Validar todas las landings
find servicios/ -name "index.html" | while read landing; do
    ./validate-landing.sh "$landing" || exit 1
done
```

#### Meta Tag de Versión (OBLIGATORIO)

Cada landing DEBE incluir este meta tag en `<head>`:

```html
<meta name="template-version" content="v2.0.0" data-template-version="v2.0.0">
```

Esto permite la validación automática.

---

### 🔄 FLUJO DE ACTUALIZACIÓN DE PLANTILLA

**Cuando cambie index.html o styles.css:**

#### Paso 1: Actualizar Fuente de Verdad

```bash
# 1. Hacer cambios en index.html
vim index.html

# 2. Extraer nuevo Critical CSS (95 líneas)
sed -n '78,172p' index.html > assets/css/critical.css

# 3. Calcular nuevo hash
NEW_HASH=$(md5 -q assets/css/critical.css | head -c 8)
echo "Nuevo hash: $NEW_HASH"

# 4. Actualizar config/landing.json
jq ".styles.criticalCssHash = \"$NEW_HASH\"" config/landing.json > config/landing.json.tmp
mv config/landing.json.tmp config/landing.json

# 5. Incrementar versión
jq '.version = "v2.1.0"' config/landing.json > config/landing.json.tmp
mv config/landing.json.tmp config/landing.json

# 6. Actualizar fecha
jq ".lastUpdate = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"" config/landing.json > config/landing.json.tmp
mv config/landing.json.tmp config/landing.json
```

#### Paso 2: Actualizar Sección "Fuente de Verdad" en landing-creator.md

```bash
# Editar .claude/commands/landing-creator.md
# Actualizar:
# - Última actualización: [nueva fecha]
# - Versión de plantilla: [nueva versión]
# - Commit/Hash: [nuevo hash del commit]
# - Critical CSS: [verificar líneas exactas]
```

#### Paso 3: Recalcular Hashes

```bash
# Recalcular hash del Critical CSS
md5 -q assets/css/critical.css | head -c 8

# Recalcular hash de styles.css (si cambió)
md5 -q styles.css
```

#### Paso 4: Regenerar Landings Afectadas

**Opción A: Regenerar todas las landings**
```bash
# Listar todas las landings
find servicios/ -name "index.html" > landings.txt

# Regenerar cada una (usar landing-creator)
# Este comando debe ejecutarse manualmente para cada landing
```

**Opción B: Solo actualizar meta tag de versión**
```bash
# Si solo cambió versión, actualizar meta tag
find servicios/ -name "index.html" -exec sed -i '' 's/data-template-version="v2.0.0"/data-template-version="v2.1.0"/' {} \;
```

#### Paso 5: Validar Todas las Landings

```bash
# Ejecutar validador en todas las landings
find servicios/ -name "index.html" | while read landing; do
    echo "Validando: $landing"
    ./validate-landing.sh "$landing" || echo "❌ FALLA: $landing"
done
```

#### Paso 6: Commit de Actualización

```bash
git add index.html assets/css/critical.css config/landing.json .claude/commands/landing-creator.md
git commit -m "chore(plantilla): actualizar a v2.1.0

- Actualizado Critical CSS con [descripción de cambios]
- Nuevo hash: $NEW_HASH
- Regeneradas [N] landings afectadas

✅ Todas las landings validadas contra nueva versión"
```

---

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
**Nota:** `theme-color` solo para meta; NO usar #0066cc en botones/textos. La paleta UI permitida es la naranja definida arriba.

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

### ❌ FALLA AUTOMÁTICA - ESTRUCTURA HTML OBLIGATORIA (v2.0.0)

**🚨 REGLA CRÍTICA: Toda landing v2.0.0 DEBE tener navegación + breadcrumbs**

Esta regla previene el error de remover accidentalmente la navegación o breadcrumbs pensando que no son necesarios.

**ESTRUCTURA OBLIGATORIA (en orden exacto):**

```html
<body>
    <!-- 1. GTM noscript -->
    <noscript>
      <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5Z2QRZ5Q" ...></iframe>
    </noscript>

    <!-- 2. NAVEGACIÓN (OBLIGATORIA) -->
    <nav class="nav">
        <div class="container">
            <div class="nav-wrapper">
                <a href="/" class="logo">
                    <img src="../../logo-electricista-culiacan-pro.webp"
                         alt="Electricista Culiacán Pro"
                         width="140" height="140">
                </a>
                <button class="mobile-menu-btn" aria-label="Menú">...</button>
                <ul class="nav-menu">...</ul>
            </div>
        </div>
    </nav>

    <!-- 3. BREADCRUMBS (OBLIGATORIOS) -->
    <div class="breadcrumb-wrapper">
        <div class="container">
            <nav aria-label="Breadcrumb" itemscope itemtype="https://schema.org/BreadcrumbList">
                <ol class="breadcrumb">...</ol>
            </nav>
        </div>
    </div>

    <!-- 4. Hero y resto del contenido -->
    <header id="inicio" class="hero">...</header>
```

**✅ REFERENCIA:**
- **Archivo:** `servicios/reparacion-cortos-circuitos/index.html`
- **Navegación:** Líneas 255-278
- **Breadcrumbs:** Líneas 280-302

**❌ PROHIBIDO:**
- ❌ Landings SIN navegación - FALLA INMEDIATA
- ❌ Landings SIN breadcrumbs - FALLA INMEDIATA
- ❌ Hero que empieza directamente después de GTM - FALLA
- ❌ Breadcrumbs solo en JSON-LD sin HTML visible - FALLA

**✅ VALIDACIÓN AUTOMÁTICA:**
El script `validate-landing.sh` verifica automáticamente:
```bash
# Verifica que existe <nav class="nav">
# Verifica que existe class="breadcrumb-wrapper"
```

**⚠️ POR QUÉ ESTA REGLA:**
En una sesión anterior se removió accidentalmente la navegación pensando que no era necesaria. Esta regla previene ese error garantizando que TODA landing v2.0.0 tenga estructura completa.

**CHECKLIST PRE-MODIFICACIÓN:**
Antes de hacer cambios estructurales a una landing:
1. ✅ Abrir `servicios/reparacion-cortos-circuitos/index.html` (referencia v2.0.0)
2. ✅ Comparar estructura completa (nav → breadcrumbs → hero)
3. ✅ Ejecutar `./validate-landing.sh` ANTES de modificar
4. ✅ Ejecutar `./validate-landing.sh` DESPUÉS de modificar

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

**Imagen hero por defecto (desde config):**
- USAR: `config.images.heroDefault["800w"]` y `config.images.heroDefault["1200w"]` (igual que index.html)
- NO USAR: hero-electrical-*.webp u otras imágenes obsoletas a menos que el usuario las especifique

**⚠️ REGLA #0.2 - BOTONES FLOTANTES (CRÍTICO):**

Los botones flotantes (WhatsApp + Llamar) DEBEN usar EXACTAMENTE esta estructura (index.html línea 3862-3876):

```html
<a href="https://wa.me/{{config.contact.whatsapp}}?text=Hola%2C%20necesito%20informaci%C3%B3n%20sobre%20servicios%20de%20electricidad%20en%20Culiac%C3%A1n"
   id="cta-whatsapp"
   class="floating-btn floating-whatsapp"
   target="_blank"
   rel="noopener noreferrer"
   aria-label="Contactar por WhatsApp - Respuesta inmediata">
    <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    <span class="online-badge" aria-label="En línea"></span>
</a>

<a href="tel:{{config.contact.phone}}"
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
- ❌ NO hardcodear teléfonos - Siempre desde `config.contact.*`

**⚠️ REGLA #0.3 - CRITICAL CSS COMPLETO (CRÍTICO):**

Cada página DEBE cargar `assets/css/critical.css` (fuente única). NO se permite duplicar el bloque `<style>` inline (salvo preloads mínimos).

**Referencia del contenido de critical.css:** ver sección “Critical CSS compartido”. Si algo falta o sobra respecto a index.html, actualizar `assets/css/critical.css` y recalcular hash.

**Consecuencias de Critical CSS incompleto o inline desactualizado:**
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

**⚠️ REGLA #0.6 - ABRIR PÁGINAS PARA VERIFICACIÓN (CRÍTICO):**

🚨 **NUNCA abrir archivos HTML con `file://` - Safari bloquea CSS por seguridad CORS**

**❌ MAL (CSS NO carga):**
```bash
open -a Safari "/ruta/al/proyecto/servicios/[slug]/index.html"
# Resultado: Sin estilos, imágenes rotas, navegación sin formato
```

**✅ BIEN (usar servidor HTTP local):**
```bash
# 1. Iniciar servidor HTTP en raíz del proyecto
cd "/ruta/al/proyecto"
python3 -m http.server 8080 &

# 2. Abrir página vía localhost
open -a Safari "http://localhost:8080/servicios/[slug]/index.html"
```

**Problema:** Safari (y otros navegadores) bloquean la carga de archivos CSS, fuentes, e imágenes cuando se abre un archivo HTML local con el protocolo `file://` por razones de seguridad CORS (Cross-Origin Resource Sharing).

**Solución:** Servir los archivos a través de un servidor HTTP local usando `python3 -m http.server` en la raíz del proyecto.

**✅ VERIFICACIÓN CORRECTA:**
1. Servidor HTTP iniciado en background (`&`)
2. Página abierta con `http://localhost:8080/...`
3. Todos los estilos cargan correctamente
4. Todas las imágenes se muestran
5. Logo visible
6. Navegación con formato correcto

**⚠️ IMPORTANTE:** Siempre verificar que el servidor HTTP esté corriendo antes de abrir la página. Si ya hay un servidor corriendo en el puerto 8080, usar otro puerto (8081, 8082, etc.).

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

**Teléfonos oficiales:** leer siempre de `config/landing.json` (`contact.whatsapp`, `contact.phone`)

**Imágenes hero por defecto:** usar `config.images.heroDefault`

**Theme color:** #0066cc (solo meta, no UI)

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

### 📋 0. VERSIÓN Y CONFIG (NUEVO - OBLIGATORIO)

- [ ] **Versión de plantilla vigente** - Meta tag presente:
  ```html
  <meta name="template-version" content="v2.0.0" data-template-version="v2.0.0">
  ```
- [ ] **Uso de CSS compartido** - Landing usa `critical.css` compartido:
  ```html
  <link rel="stylesheet" href="../../assets/css/critical.css" fetchpriority="high">
  ```
- [ ] **Hash/fecha coincide** - Validado con `./validate-landing.sh [ruta]` (hash actual `53ef5e7f`)
- [ ] **Valores del config central** - Teléfonos, GTM/GA IDs, email, coordenadas, hero, logos tomados de `config/landing.json`
- [ ] **Config existe** - Archivo `config/landing.json` presente en raíz del proyecto
- [ ] **Critical.css existe** - Archivo `assets/css/critical.css` presente y actualizado
- [ ] **Rutas relativas** - Sin rutas absolutas locales
- [ ] **Accesibilidad mínima** - `alt` descriptivo (hero, servicios), `aria-current="page"` en breadcrumb, foco visible (usa estilos existentes)

**✅ VALIDAR CON:**
```bash
./validate-landing.sh servicios/[slug]/index.html
```

**❌ SI FALTA VERSIÓN O CONFIG → Landing NO es válida**

---

### 📋 1. Critical CSS Compartido (OBLIGATORIO)

- [ ] **Critical CSS NO inline** - Bloque `<style>` eliminado del `<head>`
- [ ] **Link a critical.css** - `<link rel="stylesheet" href="../../assets/css/critical.css" fetchpriority="high">`
- [ ] **Preloads presentes** - Fuentes críticas y hero image preloaded
- [ ] **Hash coincide** - Hash de `critical.css` coincide con `config/landing.json`:
  ```bash
  md5 -q assets/css/critical.css | head -c 8
  ```

**✅ CONTENIDO DE critical.css (95 líneas de index.html):**
- 5 fuentes web @font-face - Inter (400, 500, 600) + Montserrat (700, 800)
- Variables CSS :root - Todas las variables (--brand, --brand-light, --text, etc.)
- Base styles - *, body, .container, h1/h2/h3
- Nav styles - .nav, .nav-wrapper, .logo, .logo img
- Hero styles - .hero, .hero-background, .hero-content, .hero::after, media queries móvil
- Button styles - .btn-primary con gradientes y transiciones
- Floating buttons - .floating-btn, .floating-call, .floating-whatsapp

**❌ SI USA CSS INLINE O NO USA critical.css → Landing FALLA validación**

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
- [ ] **Meta description:** 120-155 caracteres (óptimo), máximo 160 (revisar ancho en píxeles en SERP)
- [ ] **Canonical URL:** `<link rel="canonical" href="https://..." />`
- [ ] **Canonical/OG por slug** - Construidos según la URL final de la landing
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
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-7CML8QYBGQ"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-7CML8QYBGQ');
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
      script.src = 'https://www.googletagmanager.com/gtm.js?id=GTM-5Z2QRZ5Q';
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
    <iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5Z2QRZ5Q"
            height="0" width="0" style="display:none;visibility:hidden"></iframe>
  </noscript>
  ```

**❌ SI FALTA GTM → Deployment FALLA en SEO audit**

**Nota de tracking:** Usar GA vía gtag o vía GTM. Si se cargan ambos, asegurar que GA no esté duplicado en GTM para evitar doble conteo.

### 📋 8. Teléfonos y Datos del Config (OBLIGATORIO)

- [ ] **Teléfonos del config** - Leer de `config/landing.json` → `contact.phone` y `contact.whatsapp`
- [ ] **WhatsApp correcto:** `https://wa.me/{{config.contact.whatsapp}}`
- [ ] **Tel correcto:** `tel:{{config.contact.phone}}`
- [ ] **Email del config:** `{{config.contact.email}}`
- [ ] **Coordenadas del config:** `{{config.location.coordinates.latitude}}`, `{{config.location.coordinates.longitude}}`
- [ ] **GTM ID del config:** `{{config.tracking.googleTagManagerId}}`
- [ ] **GA ID del config:** `{{config.tracking.googleAnalyticsId}}`

**✅ VERIFICAR:**
```bash
# Teléfonos coinciden con config
jq -r '.contact.phone' config/landing.json  # Debe ser +526673922273
jq -r '.contact.whatsapp' config/landing.json  # Debe ser 526673922273
```

**❌ SI HAY TELÉFONOS HARDCODED → Cliente recibe datos desactualizados**

### 📋 9. Imágenes Hero Correctas (OBLIGATORIO)

- [ ] **Usar valores del config** `config.images.heroDefault` (800w y 1200w)
- [ ] **NO usar** hero-electricista-culiacan-*.webp (obsoletas)
- [ ] **Rutas correctas** según profundidad:
  - Servicios: `../../assets/images/optimizadas/`
  - Colonias: `../../assets/images/optimizadas/`

**❌ SI USA IMÁGENES OBSOLETAS O FUERA DE CONFIG → Inconsistencia visual**

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

## 🛠️ Procedimiento de Corrección (Top-Down)

Cuando se corrija una landing existente, seguir este flujo exacto y añadir la evidencia en la respuesta:

1. Auditar de arriba hacia abajo: abrir `servicios/[slug]/index.html` y recorrer el HTML en orden. Enumerar cada error encontrado (con línea/archivo) sin corregir aún.
2. Citar la regla del documento que incumple cada error.
3. Aplicar las correcciones en el mismo orden enumerado.
4. Forzar que todos los datos (teléfono, WhatsApp, email, IDs, coordenadas, hero, logos) provengan de `config/landing.json`.
5. Verificar que usa `assets/css/critical.css` (sin bloque `<style>` inline), meta de versión vigente, hash vigente, rutas relativas, accesibilidad mínima (`alt`, `aria-current` en breadcrumb), canonical/OG por slug, theme-color solo en meta.
6. Ejecutar `./validate-landing.sh servicios/[slug]/index.html`. Si falla, corregir y revalidar hasta que pase.
7. Entregar: lista de errores inicial (enumerados), cambios aplicados por regla, resultado del validador.

Prompt sugerido para Claude al corregir:
```
Audita y corrige top-down esta landing: servicios/[slug]/index.html.
1) Recorre el HTML de arriba hacia abajo. Enumera cada error que halles (con línea/archivo). No corrijas aún.
2) Cita la regla de .claude/commands/landing-creator.md que se incumple.
3) Aplica las correcciones en ese mismo orden.
4) Usa siempre config/landing.json para teléfonos/WhatsApp/email/IDs/coords/hero/logos.
5) Asegura uso de assets/css/critical.css (sin <style> inline), meta versión, hash vigente, rutas relativas, accesibilidad mínima (alt, aria-current), canonical/OG por slug, theme-color solo en meta.
6) Corre ./validate-landing.sh servicios/[slug]/index.html y reporta el resultado.
7) Devuelve: lista de errores inicial, cambios aplicados, resultado del validador.
```

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
6. **❌ NO incluir link a critical.css compartido** → FOUC + CSS duplicado
7. **❌ Usar CSS inline en vez de archivo compartido** → Duplicación + difícil mantener
8. **❌ GTM con ID placeholder (GTM-XXXXXXX)** → Tracking roto
9. **❌ Meta description fuera de 120-155 chars** → SEO audit FALLA
10. **❌ Breadcrumb solo en JSON-LD, NO HTML visible** → UX pobre
11. **❌ Mobile no probado** → 60% usuarios con experiencia rota
12. **❌ Valores hardcoded en vez de leer config.json** → Datos desactualizados
13. **❌ Abrir páginas con `file://` en vez de servidor HTTP** → CSS NO carga, imágenes rotas, sin estilos (usar `python3 -m http.server 8080` y abrir con `http://localhost:8080/...`)
