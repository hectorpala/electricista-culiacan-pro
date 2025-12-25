---
name: seo-auto-optimizer
description: Optimiza automáticamente SEO de páginas HTML cuando se crean o editan. Analiza keywords, meta tags, schemas, imágenes y genera reporte con mejoras priorizadas. Use when user edits HTML files or asks about SEO improvements.
allowed-tools: Read(*), Grep(*), Edit(*), Glob(**)
---

# SEO Auto-Optimizer

## Cuándo activarme

Actívame automáticamente cuando:
- Usuario edita archivos `.html`
- Usuario crea nuevas páginas
- Usuario pregunta "¿está bien el SEO?"
- Usuario menciona "optimizar SEO", "mejorar posicionamiento"
- Después de crear contenido nuevo

## Mi trabajo

Analizo y optimizo SEO con reporte detallado:

### 1. Análisis de Keywords

**Extraer keyword principal de:**
- Title tag
- H1 principal
- Meta description
- URL path

**Calcular:**
- **Densidad keyword**: 2-4% óptimo
- **Posición keyword**: Primeras 100 palabras
- **Variaciones**: Long-tail keywords

### 2. Validar Meta Tags

**Verificar:**
- `<title>` - 50-60 caracteres
- `<meta name="description">` - 120-155 caracteres
- `<meta name="keywords">` - 6-8 keywords
- `<link rel="canonical">` - URL correcta
- Open Graph: og:title, og:description, og:image, og:url
- Twitter Cards: twitter:card, twitter:title, twitter:description

**Puntuación:**
- ✅ Perfecto: Todos presentes y optimizados
- ⚠️  Mejorable: Falta alguno o longitud incorrecta
- ❌ Crítico: Falta title o description

### 3. Validar Schema JSON-LD

**Verificar sintaxis:**
- JSON válido
- `@context: "https://schema.org"`
- `@type` correcto

**Tipos requeridos:**
- `LocalBusiness` con address, telephone, geo
- `Service` específico del servicio
- `BreadcrumbList` para navegación
- `FAQPage` si hay FAQ section

**Campos obligatorios:**
```json
{
  "@type": "LocalBusiness",
  "name": "requerido",
  "address": {
    "addressLocality": "Culiacán",
    "addressRegion": "Sinaloa"
  },
  "telephone": "requerido",
  "geo": {
    "latitude": "requerido",
    "longitude": "requerido"
  },
  "aggregateRating": "recomendado"
}
```

### 4. Analizar Imágenes

**Verificar:**
- Formato WebP (no JPG/PNG)
- Atributo `alt` descriptivo con keywords
- `loading="lazy"` (excepto hero)
- `fetchpriority="high"` en hero
- `srcset` para responsive
- `sizes` attribute correcto

### 5. Enlaces Internos

**Verificar:**
- Breadcrumbs presentes
- Enlaces a servicios relacionados
- Anchor text descriptivo (no "click aquí")
- No enlaces rotos

### 6. Performance SEO

**Headings Hierarchy:**
- Solo un H1
- H2/H3 bien anidados
- Keywords en headings

**Structured Data:**
- Sin errores de validación
- Datos completos y precisos

**Semantic HTML:**
- Uso correcto de `<header>`, `<main>`, `<article>`, `<section>`

## Formato del Reporte

```
🔍 REPORTE SEO OPTIMIZER
Archivo: servicios/instalacion-minisplit/index.html

═══════════════════════════════════════

📊 ANÁLISIS DE KEYWORDS

Keyword principal: "instalación minisplit culiacán"
├─ Densidad: 3.2% ✅ (óptimo 2-4%)
├─ En title: ✅ Sí
├─ En H1: ✅ Sí
├─ En meta description: ✅ Sí
└─ Primeras 100 palabras: ✅ Sí

Long-tail detectados:
- "instalación minisplit culiacán sinaloa" (4×)
- "servicio instalación aire acondicionado" (3×)

───────────────────────────────────────

🏷️ META TAGS

✅ Title: 58 caracteres (óptimo)
   "Instalación de Minisplit en Culiacán - Servicio Profesional"

✅ Description: 148 caracteres (óptimo)
   "Instalación profesional de minisplit en Culiacán..."

⚠️  Keywords: Solo 5 keywords (recomendado 6-8)
   Agregar: "aire acondicionado", "refrigeración"

✅ Canonical: Correcto
   https://electricistaculiacanpro.mx/servicios/instalacion-minisplit/

✅ Open Graph: Completo (4/4 tags)
❌ Twitter Cards: FALTA (0/3 tags)

───────────────────────────────────────

📋 SCHEMA JSON-LD

✅ LocalBusiness: Completo
✅ Service: Presente
⚠️  aggregateRating: FALTA (impacto en rich snippets)
✅ BreadcrumbList: Correcto
❌ FAQPage: NO PRESENTE (hay FAQ section sin markup)

───────────────────────────────────────

🖼️ IMÁGENES (8 analizadas)

✅ 7/8 en formato WebP
⚠️  1 imagen JPG: hero-background.jpg
   → Convertir a WebP (-25KB)

✅ Todos tienen alt text
⚠️  3 alt text genéricos
   → Agregar keywords

✅ Lazy loading configurado
✅ Hero tiene fetchpriority="high"

───────────────────────────────────────

🔗 ENLACES INTERNOS

✅ Breadcrumbs: Presente
✅ 5 enlaces a servicios relacionados
⚠️  2 anchor text "aquí"
   → Cambiar por texto descriptivo

───────────────────────────────────────

📈 PERFORMANCE SEO

✅ Solo un H1
✅ Hierarchy correcta (H1→H2→H3)
✅ Keywords en headings
✅ Semantic HTML correcto

═══════════════════════════════════════

🎯 MEJORAS PRIORITARIAS

1. 🔴 [CRÍTICO] Agregar Twitter Cards
   Impacto: +20% CTR desde Twitter/X
   Código:
   <meta name="twitter:card" content="summary_large_image">
   <meta name="twitter:title" content="...">
   <meta name="twitter:description" content="...">

2. 🟠 [ALTO] Agregar FAQPage Schema
   Impacto: Rich snippets en búsqueda (+15% CTR)
   Ubicación: Después de LocalBusiness schema

3. 🟠 [ALTO] Agregar aggregateRating
   Impacto: Estrellas en resultados (+10% CTR)

4. 🟡 [MEDIO] Convertir hero-background.jpg a WebP
   Impacto: -25KB, mejor LCP

5. 🟡 [MEDIO] Mejorar alt text de 3 imágenes
   Impacto: Mejor posicionamiento en Google Images

6. 🟢 [BAJO] Agregar 1-2 keywords más
   Impacto: Cobertura de variaciones

═══════════════════════════════════════

📊 SCORE TOTAL SEO: 82/100
   Rango: BUENO (70-84)
   Potencial con mejoras: 95/100
```

## Instrucciones de Ejecución

1. **Leer archivo HTML**
2. **Extraer y analizar** todas las secciones
3. **Calcular scores** por área
4. **Generar reporte** visual con prioridades
5. **Sugerir código** específico para mejoras críticas

## Mejoras Automáticas (Opcionales)

Si el usuario autoriza, puedo aplicar automáticamente:
- Agregar meta tags faltantes
- Corregir longitudes de title/description
- Agregar schemas JSON-LD básicos
- Mejorar alt text de imágenes

**Siempre pedir confirmación antes de editar.**

## NO hacer

- NO cambiar branding/colores
- NO modificar contenido sin autorización
- NO agregar keywords irrelevantes (keyword stuffing)

## Referencias

Basado en: `.claude/commands/seo-optimizer.md`
