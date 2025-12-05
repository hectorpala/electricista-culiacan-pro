# Auditar Landing Page - SEO y UX

Analiza una landing page y genera un reporte detallado con calificación numérica en SEO, Performance, UX y Contenido.

## 📝 Uso

```
/auditar-landing servicios/{slug}/
```

**Ejemplos:**
- `/auditar-landing servicios/instalacion-minisplit/`
- `/auditar-landing servicios/reparacion-cortos-circuitos/`
- `/auditar-landing servicios/iluminacion-led/`

---

## 🎯 Criterios de Evaluación

### **1. SEO Técnico (40 puntos)**

#### Meta Tags Básicos (10 pts)
- [ ] **Title tag** (3 pts)
  - ✅ Existe y es único
  - ✅ Entre 50-60 caracteres
  - ✅ Incluye "Culiacán" y keyword principal
  - ⚠️ -1 pt si <50 o >60 chars
  - ❌ -3 pts si falta o es genérico

- [ ] **Meta description** (3 pts)
  - ✅ Existe y es única
  - ✅ Entre 120-155 caracteres
  - ✅ Incluye llamada a la acción
  - ⚠️ -1 pt si <120 o >155 chars
  - ❌ -3 pts si falta

- [ ] **Meta keywords** (2 pts)
  - ✅ 6-8 keywords separadas por coma
  - ✅ Incluye variaciones del servicio
  - ⚠️ -1 pt si tiene menos de 6 o más de 8

- [ ] **Canonical URL** (2 pts)
  - ✅ Tag `<link rel="canonical">` presente
  - ✅ URL correcta: `https://electricistaculiacanpro.mx/servicios/{slug}/`
  - ❌ -2 pts si falta o es incorrecta

#### Open Graph y Social (8 pts)
- [ ] **Open Graph básico** (4 pts)
  - ✅ `og:title` - 1 pt
  - ✅ `og:description` - 1 pt
  - ✅ `og:image` - 1 pt (debe ser imagen hero 800w)
  - ✅ `og:url` - 1 pt

- [ ] **Twitter Card** (2 pts)
  - ✅ `twitter:card` = "summary_large_image"
  - ✅ `twitter:title` y `twitter:description`

- [ ] **Tema y mobile** (2 pts)
  - ✅ `theme-color` = #0066cc
  - ✅ `viewport` configurado correctamente

#### Schema.org Structured Data (12 pts)
- [ ] **BreadcrumbList Schema** (4 pts)
  - ✅ JSON-LD presente
  - ✅ 3 niveles: Inicio → Servicios → Servicio actual
  - ✅ URLs correctas
  - ✅ Nombres correctos (no genéricos)

- [ ] **Service Schema** (4 pts)
  - ✅ `@type: "Service"`
  - ✅ `serviceType` específico del servicio
  - ✅ `description` única (40-60 palabras)
  - ✅ `areaServed` con colonias de Culiacán

- [ ] **Electrician Schema** (4 pts)
  - ✅ `@type: "Electrician"`
  - ✅ Nombre, teléfono, dirección
  - ✅ Rating (4.8) y review count
  - ✅ `priceRange` presente

#### Estructura de Contenido (10 pts)
- [ ] **H1 único y optimizado** (3 pts)
  - ✅ Solo 1 H1 en toda la página
  - ✅ Incluye servicio + "Culiacán"
  - ✅ Entre 8-15 palabras
  - ❌ -3 pts si hay múltiples H1

- [ ] **Jerarquía de headings** (3 pts)
  - ✅ H2 para secciones principales
  - ✅ No se salta niveles (H1→H3)
  - ✅ Headings descriptivos (no "Sección 1")

- [ ] **Breadcrumbs HTML** (2 pts)
  - ✅ Visible en la página
  - ✅ Con estructura `<nav aria-label="breadcrumb">`
  - ✅ Último elemento con clase `.breadcrumb-current`

- [ ] **Alt text en imágenes** (2 pts)
  - ✅ Imagen hero tiene alt descriptivo
  - ✅ Alt incluye keyword del servicio
  - ⚠️ -1 pt si alt es genérico

---

### **2. Performance (20 puntos)**

#### Imágenes Optimizadas (10 pts)
- [ ] **Formato WebP** (3 pts)
  - ✅ Todas las imágenes en .webp
  - ⚠️ -1 pt por cada imagen en .jpg/.png

- [ ] **Responsive images** (4 pts)
  - ✅ Hero con `srcset` para 800w y 1200w
  - ✅ Atributo `sizes` configurado
  - ✅ Imágenes existen en ambos tamaños
  - ❌ -2 pts si falta algún tamaño

- [ ] **Lazy loading** (3 pts)
  - ✅ Imágenes con `loading="lazy"` (excepto hero)
  - ✅ Hero sin lazy loading (prioritaria)

#### CSS y Scripts (6 pts)
- [ ] **Critical CSS inline** (3 pts)
  - ✅ Existe `<link rel="stylesheet" href="../../assets/css/critical.css">`
  - ✅ Archivo critical.css existe y es pequeño (<10KB)
  - ❌ -3 pts si falta

- [ ] **Scripts optimizados** (3 pts)
  - ✅ Scripts con `defer` o al final del body
  - ✅ No hay scripts bloqueantes en `<head>`

#### Tamaño de Página (4 pts)
- [ ] **HTML minificado o limpio** (2 pts)
  - ✅ Sin comentarios HTML innecesarios
  - ✅ Sin espacios en blanco excesivos
  - ⚠️ -1 pt si tiene >100 líneas de comentarios

- [ ] **Recursos externos mínimos** (2 pts)
  - ✅ Fuentes locales (no Google Fonts CDN)
  - ✅ No más de 3 archivos CSS externos

---

### **3. UX/Conversión (25 puntos)**

#### CTAs y Conversión (10 pts)
- [ ] **Cantidad de CTAs** (4 pts)
  - ✅ Mínimo 4 CTAs de WhatsApp
    - Nav superior: 1 pt
    - Hero section: 1 pt
    - Benefits box: 1 pt
    - Floating button: 1 pt
  - ❌ -1 pt por cada CTA faltante

- [ ] **Calidad de CTAs** (3 pts)
  - ✅ Texto específico del servicio (no genérico "Contactar")
  - ✅ Incluye número de teléfono visible
  - ✅ Color de botón destacado (naranja #E36414)

- [ ] **WhatsApp links correctos** (3 pts)
  - ✅ Formato: `https://wa.me/526673922273?text={mensaje}`
  - ✅ Mensaje pre-rellenado con nombre del servicio
  - ✅ Número correcto (667 392 2273)

#### Navegación y Usabilidad (8 pts)
- [ ] **Breadcrumbs funcionales** (2 pts)
  - ✅ Links clicables que funcionan
  - ✅ Estilo visual claro (azul para links, gris para actual)

- [ ] **Header sticky** (2 pts)
  - ✅ Navegación fija al hacer scroll
  - ✅ CTA visible siempre en nav

- [ ] **Floating CTA button** (2 pts)
  - ✅ Botón flotante de WhatsApp visible
  - ✅ Con icono de WhatsApp
  - ✅ Posición fija en mobile

- [ ] **Mobile-friendly** (2 pts)
  - ✅ Viewport configurado
  - ✅ Textos legibles sin zoom
  - ✅ Botones de tamaño táctil (>44px)

#### Propuesta de Valor (7 pts)
- [ ] **Hero section efectivo** (4 pts)
  - ✅ H1 claro con beneficio principal
  - ✅ Subtitle de 30-50 palabras con detalles
  - ✅ Imagen hero relevante al servicio
  - ✅ CTA visible "above the fold"

- [ ] **Social proof** (3 pts)
  - ✅ Menciona "150+ clientes satisfechos"
  - ✅ Rating 4.8★ visible
  - ✅ Garantía mencionada ("por escrito", "6 meses", etc.)

---

### **4. Contenido (15 puntos)**

#### Benefits Section (8 pts)
- [ ] **4 benefits únicos** (4 pts)
  - ✅ 4 cards de benefits
  - ✅ Cada benefit es específico del servicio (no genérico)
  - ⚠️ -1 pt por cada benefit genérico
  - ❌ -1 pt si tiene menos de 4 benefits

- [ ] **Descripciones detalladas** (4 pts)
  - ✅ Cada descripción: 40-60 palabras
  - ✅ Incluye datos técnicos o números específicos
  - ✅ No usa frases cliché ("mejor servicio", "calidad garantizada")
  - ⚠️ -1 pt por cada descripción <40 palabras

#### Textos de Marketing (4 pts)
- [ ] **Intro de benefits** (2 pts)
  - ✅ Pregunta específica relacionada al servicio
  - ✅ Menciona zona geográfica (Culiacán, colonias)
  - ✅ Incluye social proof (150 clientes, rating)

- [ ] **CTA box en benefits** (2 pts)
  - ✅ Título persuasivo
  - ✅ Descripción específica del servicio
  - ✅ Urgencia o beneficio claro

#### Consistencia de Template (3 pts)
- [ ] **Template version** (1 pt)
  - ✅ Tiene `data-template-version="v2.0.0"`

- [ ] **Sección "Nuestros Servicios" intacta** (2 pts)
  - ✅ No modificada del template original
  - ✅ Todos los 6 servicios presentes
  - ✅ Links correctos a otros servicios

---

## 📊 Sistema de Calificación

### Escala de Puntuación Total (100 puntos)

| Puntos | Calificación | Estado |
|--------|--------------|--------|
| 90-100 | **A+ Excelente** | 🟢 Listo para producción |
| 80-89  | **A Muy bueno** | 🟢 Listo para producción |
| 70-79  | **B Bueno** | 🟡 Mejoras menores recomendadas |
| 60-69  | **C Aceptable** | 🟡 Necesita mejoras |
| 50-59  | **D Deficiente** | 🔴 Requiere trabajo |
| <50    | **F Reprobado** | 🔴 NO publicar |

### Desglose por Categoría

- **SEO Técnico**: 40 puntos
- **Performance**: 20 puntos
- **UX/Conversión**: 25 puntos
- **Contenido**: 15 puntos

---

## 📝 Formato de Reporte

El reporte debe seguir este formato:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 AUDITORÍA SEO/UX - {nombre del servicio}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 Landing: servicios/{slug}/index.html
📅 Fecha: {fecha actual}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 CALIFICACIÓN POR CATEGORÍA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. SEO Técnico:       XX/40 (XX%)  [✅/⚠️/❌]
2. Performance:       XX/20 (XX%)  [✅/⚠️/❌]
3. UX/Conversión:     XX/25 (XX%)  [✅/⚠️/❌]
4. Contenido:         XX/15 (XX%)  [✅/⚠️/❌]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 CALIFICACIÓN TOTAL: XX/100 (X)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Estado: [🟢 Listo / 🟡 Mejoras recomendadas / 🔴 Requiere trabajo]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 DETALLES POR SECCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## 1. SEO Técnico (XX/40)

### Meta Tags Básicos (X/10)
✅ Title: "..." (XX chars) - Correcto
❌ Description: Falta meta description
⚠️  Keywords: Solo 4 keywords (recomendado: 6-8)
✅ Canonical: URL correcta

### Open Graph (X/8)
✅ og:title presente
✅ og:description presente
...

### Schema.org (X/12)
...

### Estructura (X/10)
...

## 2. Performance (XX/20)
...

## 3. UX/Conversión (XX/25)
...

## 4. Contenido (XX/15)
...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 RECOMENDACIONES PRIORITARIAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 CRÍTICO (bloquea publicación):
1. [Descripción del problema crítico]
2. [Otro problema crítico]

🟡 IMPORTANTE (mejora significativa):
1. [Mejora importante]
2. [Otra mejora importante]

🟢 OPCIONAL (optimización adicional):
1. [Optimización sugerida]
2. [Otra optimización]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ ASPECTOS DESTACADOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

- [Aspecto positivo 1]
- [Aspecto positivo 2]
- [Aspecto positivo 3]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🔧 Proceso de Auditoría

Cuando recibas el comando `/auditar-landing servicios/{slug}/`, debes:

1. **Leer el archivo HTML**
   ```
   servicios/{slug}/index.html
   ```

2. **Verificar archivos relacionados**
   ```
   servicios/{slug}/config.json (si existe)
   assets/images/optimizadas/{slug}-culiacan-800w.webp
   assets/images/optimizadas/{slug}-culiacan-1200w.webp
   assets/css/critical.css
   ```

3. **Evaluar cada sección según los criterios**
   - Asignar puntos a cada subsección
   - Anotar problemas encontrados
   - Identificar aspectos positivos

4. **Calcular puntuación total**
   - Sumar puntos de las 4 categorías
   - Determinar calificación (A+, A, B, C, D, F)
   - Definir estado (🟢/🟡/🔴)

5. **Generar reporte completo**
   - Usar el formato especificado
   - Incluir detalles específicos de cada problema
   - Priorizar recomendaciones (crítico/importante/opcional)
   - Destacar aspectos positivos

6. **Recomendaciones accionables**
   - Ser específico: indicar líneas de código, textos exactos
   - Proporcionar ejemplos de cómo corregir
   - Priorizar por impacto en conversión y SEO

---

## ⚠️ Notas Importantes

- **Sé estricto**: No dar puntos completos si algo no cumple 100%
- **Sé específico**: Mencionar líneas de código, textos exactos
- **Sé constructivo**: Ofrecer soluciones, no solo críticas
- **Prioriza conversión**: UX y CTAs son tan importantes como SEO técnico
- **Compara con template v2.0.0**: Verificar que sigue las mejores prácticas establecidas

---

## 💡 Ejemplos de Evaluación

### Ejemplo 1: Title Tag
```html
<title>Instalación Minisplit Culiacán | Ahorra hasta 40%</title>
```
- ✅ 3/3 puntos
- Razón: 56 caracteres (dentro de 50-60), incluye "Culiacán", keyword "Instalación Minisplit", beneficio claro

### Ejemplo 2: Benefit Genérico (MAL)
```html
<h3>Mejor Servicio</h3>
<p>Ofrecemos el mejor servicio de calidad.</p>
```
- ❌ 0/1 punto
- Razón: Genérico, sin detalles técnicos, cliché, <40 palabras

### Ejemplo 3: Benefit Específico (BIEN)
```html
<h3>Instalación certificada en 3 horas promedio</h3>
<p>Instalamos tu minisplit en 3 horas promedio con electricistas certificados.
Incluye pruebas de presión, soldadura con nitrógeno y verificación de carga de
gas refrigerante. Cumplimos normas NOM-ENER. Garantía por escrito de 6 meses.</p>
```
- ✅ 1/1 punto benefit único + 1/1 descripción detallada
- Razón: 52 palabras, datos técnicos específicos, números concretos, garantía mencionada
