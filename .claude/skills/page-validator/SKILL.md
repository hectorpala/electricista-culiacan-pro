---
name: page-validator
description: Valida automáticamente páginas nuevas contra index.html de referencia para detectar errores ANTES de commit. Verifica hero, botones flotantes, CSS crítico, imágenes. Use after creating or editing HTML pages.
allowed-tools: Read(*), Grep(*), Glob(**)
---

# Page Validator

## Cuándo activarme

Actívame automáticamente:
- **DESPUÉS** de crear nueva página HTML
- **DESPUÉS** de editar archivos en `servicios/` o `colonias/`
- **ANTES** de hacer git commit
- Cuando usuario pregunta "¿está bien esta página?"

## Mi trabajo

Valido páginas nuevas contra `index.html` (referencia) para detectar errores comunes.

## Validaciones Críticas

### 1. Hero Section (CRÍTICO)

**Estructura correcta:**
```html
<header class="hero">
  <picture class="hero-background">
    <source type="image/webp"
            srcset="hero-800w.webp 800w, hero-1200w.webp 1200w"
            sizes="100vw">
    <img src="hero-1200w.webp"
         alt="..."
         decoding="async"
         fetchpriority="high">
  </picture>
</header>
```

**❌ Errores comunes:**
- Usar `<div class="hero-background">` en vez de `<picture>`
- Falta `<source type="image/webp">`
- Falta `srcset` attribute
- Falta `decoding="async"`
- Falta `fetchpriority="high"`
- Usar imagen obsoleta `hero-electrical-*.webp`

**✅ DEBE TENER:**
- `<picture class="hero-background">`
- `<source type="image/webp">` con srcset
- `<img>` con decoding="async" y fetchpriority="high"
- Imagen correcta: `hero-electricista-trabajo-{size}.webp`

---

### 2. Botones Flotantes (CRÍTICO)

**Estructura correcta:**
```html
<!-- WhatsApp -->
<a href="https://wa.me/526671234567"
   class="floating-btn floating-whatsapp"
   aria-label="Contactar por WhatsApp">
  <svg width="24" height="24" viewBox="0 0 24 24">
    <path d="M17.472..."/>
  </svg>
</a>

<!-- Teléfono -->
<a href="tel:+526671234567"
   class="floating-btn floating-call"
   aria-label="Llamar ahora">
  <svg width="24" height="24" viewBox="0 0 24 24">
    <path d="M20.01..."/>
  </svg>
</a>
```

**❌ Errores comunes:**
- Usar clase `cta-btn` en vez de `floating-btn`
- Usar emojis 💬 📞 en vez de SVG
- Falta `aria-label`
- Colores incorrectos en CSS

**✅ DEBE TENER:**
- Clase `floating-btn floating-whatsapp` (WhatsApp)
- Clase `floating-btn floating-call` (Teléfono)
- `<svg>` con `<path>` (NO emojis)
- WhatsApp: `background:#22c55e` en CSS
- Teléfono: `background:#0f4fa8` en CSS

---

### 3. Critical CSS (CRÍTICO)

**Debe incluir en `<style>` inline:**
- Reset CSS básico
- Variables CSS (`:root`)
- Estilos de `.hero`, `.nav`, `.container`
- Estilos de botones flotantes
- Media queries mobile

**❌ Errores comunes:**
- Falta Critical CSS inline
- CSS solo en archivo externo
- Variables CSS no definidas

**✅ DEBE TENER:**
```html
<style>
  :root {
    --primary-color: #0f4fa8;
    --secondary-color: #f97316;
    /* ... */
  }

  * { margin:0; padding:0; box-sizing:border-box; }

  .hero { /* ... */ }
  .nav { /* ... */ }
  /* ... */
</style>
```

---

### 4. Imágenes WebP (IMPORTANTE)

**Verificar:**
- Todas las imágenes en formato WebP
- NO usar JPG/PNG (excepto fallback)
- Atributo `loading="lazy"` (excepto hero)
- Atributo `alt` descriptivo

**❌ Errores comunes:**
- Imágenes JPG/PNG sin WebP
- Falta `alt` text
- Hero con `loading="lazy"` (debe ser eager)

---

### 5. Schema JSON-LD (IMPORTANTE)

**Verificar:**
- JSON válido (sin comas extra)
- `@context: "https://schema.org"`
- `@type` correcto
- Campos obligatorios completos

**Mínimo requerido:**
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "...",
  "address": { "addressLocality": "Culiacán" },
  "telephone": "..."
}
```

---

### 6. Meta Tags Básicos (IMPORTANTE)

**Verificar:**
- `<title>` presente (50-60 chars)
- `<meta name="description">` (120-155 chars)
- `<link rel="canonical">` con URL correcta
- Open Graph básico (og:title, og:description)

---

## Formato del Reporte

```
✅ VALIDACIÓN DE PÁGINA
Archivo: servicios/instalacion-minisplit/index.html
Referencia: index.html

═══════════════════════════════════════

🎯 HERO SECTION

✅ Estructura <picture> correcta
✅ <source type="image/webp"> presente
✅ srcset configurado: 800w, 1200w
✅ decoding="async" presente
✅ fetchpriority="high" presente
✅ Imagen correcta: hero-electricista-trabajo-1200w.webp

───────────────────────────────────────

🔘 BOTONES FLOTANTES

✅ WhatsApp: Clase "floating-btn floating-whatsapp"
✅ Teléfono: Clase "floating-btn floating-call"
✅ Ambos usan SVG (no emojis)
✅ aria-label presente en ambos
✅ Colores CSS correctos:
   - WhatsApp: #22c55e ✅
   - Teléfono: #0f4fa8 ✅

───────────────────────────────────────

🎨 CRITICAL CSS

✅ <style> inline presente (2.8 KB)
✅ Variables CSS definidas (12 variables)
✅ Reset CSS incluido
✅ Media queries mobile presentes

───────────────────────────────────────

🖼️ IMÁGENES

✅ 6/6 imágenes en WebP
✅ Todas tienen alt text
✅ loading="lazy" en imágenes no-hero
✅ Hero sin lazy loading ✅

───────────────────────────────────────

📋 SCHEMA JSON-LD

✅ JSON válido (sin errores sintaxis)
✅ @context correcto
✅ LocalBusiness completo
⚠️  aggregateRating: FALTA (opcional pero recomendado)

───────────────────────────────────────

🏷️ META TAGS

✅ Title: 58 caracteres ✅
✅ Description: 142 caracteres ✅
✅ Canonical URL correcto
✅ Open Graph completo (4/4)

═══════════════════════════════════════

🎉 RESULTADO: APROBADA

✅ 0 errores críticos
⚠️  1 advertencia (aggregateRating)

La página está lista para commit.

🔧 Mejora opcional:
- Agregar aggregateRating al Schema (+10% CTR)
```

**Ejemplo con errores:**

```
❌ VALIDACIÓN DE PÁGINA
Archivo: servicios/instalacion-minisplit/index.html

═══════════════════════════════════════

❌ ERRORES CRÍTICOS ENCONTRADOS

1. 🔴 [CRÍTICO] Hero Section - Línea 45
   Problema: Usa <div class="hero-background"> en vez de <picture>

   ❌ Encontrado:
   <div class="hero-background">
     <img src="hero.jpg" alt="...">
   </div>

   ✅ Debe ser:
   <picture class="hero-background">
     <source type="image/webp" srcset="...">
     <img src="..." decoding="async" fetchpriority="high">
   </picture>

2. 🔴 [CRÍTICO] Botones Flotantes - Línea 320
   Problema: Usa emojis 💬 en vez de SVG

   ❌ Encontrado:
   <a class="cta-btn">💬 WhatsApp</a>

   ✅ Debe ser:
   <a class="floating-btn floating-whatsapp">
     <svg>...</svg>
   </a>

3. 🟠 [IMPORTANTE] Critical CSS
   Problema: NO hay <style> inline, solo link a CSS externo

   ❌ Solo tiene: <link rel="stylesheet" href="styles.css">
   ✅ Debe tener: <style>...Critical CSS...</style>

═══════════════════════════════════════

🚫 RESULTADO: NO APROBADA

❌ 3 errores críticos deben corregirse antes de commit
⚠️  2 advertencias opcionales

NO hacer commit hasta corregir errores críticos.
```

## Instrucciones de Ejecución

1. **Leer archivos en paralelo:**
   - `index.html` (referencia)
   - Página a validar

2. **Validar cada sección** contra criterios

3. **Reportar errores** con:
   - Nivel: CRÍTICO / IMPORTANTE / ADVERTENCIA
   - Ubicación: Línea exacta
   - Problema: Qué está mal
   - Código encontrado vs código esperado

4. **Dar veredicto final:**
   - ✅ APROBADA: Lista para commit
   - ❌ NO APROBADA: Corregir errores primero

## Niveles de Severidad

- 🔴 **CRÍTICO**: Bloquea commit, debe corregirse
- 🟠 **IMPORTANTE**: Afecta funcionalidad/SEO
- 🟡 **ADVERTENCIA**: Mejora recomendada

## NO hacer

- NO editar archivos automáticamente
- NO aprobar páginas con errores críticos
- Solo validar y reportar

## Referencias

Basado en: `.claude/commands/validar.md`
