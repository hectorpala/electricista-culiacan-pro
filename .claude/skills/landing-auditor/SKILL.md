---
name: landing-auditor
description: Audita automáticamente landing pages de servicios/colonias con calificación SEO, Performance y UX. Use when user creates, edits, or asks to review landing pages.
allowed-tools: Read(*), Grep(*), Glob(**)
---

# Landing Page Auditor

## Cuándo activarme

Actívame automáticamente cuando detectes:
- Usuario crea nueva landing page
- Usuario edita archivo `index.html` en `servicios/` o `colonias/`
- Usuario pregunta "¿está bien esta landing?"
- Usuario menciona "auditar", "revisar", "validar landing"

## Mi trabajo

Genero un reporte detallado con calificación numérica en 4 áreas:

### 1. SEO Técnico (40 puntos)

**Meta Tags Básicos (10 pts)**
- Title tag (50-60 chars, incluye "Culiacán" + keyword)
- Meta description (120-155 chars, con CTA)
- Meta keywords (6-8 keywords)
- Canonical URL correcto

**Open Graph y Social (8 pts)**
- og:title, og:description, og:image, og:url
- Twitter cards

**Schema JSON-LD (12 pts)**
- LocalBusiness con datos completos
- Servicio específico
- Breadcrumbs
- FAQPage

**Headings y Keywords (10 pts)**
- H1 único con keyword principal
- H2/H3 bien estructurados
- Densidad keyword 2-4%

### 2. Performance (25 puntos)

**Imágenes (10 pts)**
- WebP format
- Lazy loading (excepto hero)
- srcset y sizes correctos
- fetchpriority="high" en hero

**CSS/JS (8 pts)**
- Critical CSS inline
- CSS minificado
- Sin JS bloqueante

**HTML (7 pts)**
- Sin recursos externos bloqueantes
- Preconnect a Google Fonts

### 3. UX y Conversión (20 puntos)

**Llamadas a Acción (8 pts)**
- Botones flotantes WhatsApp + Teléfono
- CTAs en hero y footer
- Textos accionables

**Contenido (12 pts)**
- Título claro y persuasivo
- Beneficios visibles
- Testimonios/reseñas
- FAQ section

### 4. Contenido y Localización (15 puntos)

**Localización Culiacán (8 pts)**
- Menciones a "Culiacán" en contenido
- Colonias/zonas específicas
- Referencias locales

**Calidad Contenido (7 pts)**
- Longitud adecuada (800+ palabras)
- Sin duplicados
- Ortografía correcta

## Formato del Reporte

```
📊 AUDITORÍA LANDING PAGE
Página: servicios/{slug}/

═══════════════════════════════════════

🔍 SEO TÉCNICO: 35/40
✅ Meta tags completos
⚠️  Schema JSON-LD: falta aggregateRating (-2)
✅ Headings bien estructurados

⚡ PERFORMANCE: 22/25
✅ Imágenes WebP optimizadas
⚠️  CSS no minificado (-3)

🎯 UX Y CONVERSIÓN: 18/20
✅ CTAs visibles y accionables
⚠️  Falta sección testimonios (-2)

📍 CONTENIDO LOCAL: 14/15
✅ Excelente localización Culiacán

───────────────────────────────────────
📈 CALIFICACIÓN TOTAL: 89/100
   Rango: EXCELENTE (85-100)

═══════════════════════════════════════

🔧 MEJORAS PRIORITARIAS:

1. [ALTO] Agregar aggregateRating en Schema
   Impacto SEO: +5% CTR en búsqueda

2. [MEDIO] Minificar CSS
   Impacto: Reducir ~15KB, mejor LCP

3. [BAJO] Agregar testimonios
   Impacto: +10% conversión estimada
```

## Instrucciones de Ejecución

1. **Leer archivo HTML** de la landing page
2. **Analizar cada sección** contra criterios
3. **Calcular puntaje** por área
4. **Generar reporte** con formato visual
5. **Priorizar mejoras** por impacto

## NO hacer

- NO modificar archivos automáticamente
- NO hacer suposiciones sobre branding/colores
- Solo reportar, no cambiar

## Referencias

Basado en: `.claude/commands/auditar-landing.md`
