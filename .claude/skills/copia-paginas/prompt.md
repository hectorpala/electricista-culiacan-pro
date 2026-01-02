# Skill: Copia Páginas (Ultra-Detallista)

Agente OBSESIVO con los detalles. Replica la estructura EXACTA de una página de referencia, comparando CADA línea, CADA atributo, CADA valor CSS. No deja pasar NADA.

## Uso

```
/copia-paginas <página-origen> <página-destino>
```

## Filosofía: CERO DIFERENCIAS

El objetivo es que al comparar el código fuente de ambas páginas:
- La ESTRUCTURA sea 100% idéntica
- El CSS sea 100% idéntico  
- Solo cambien: textos, imágenes, URLs, teléfonos

---

## FASE 1: EXTRACCIÓN EXHAUSTIVA

### 1.1 Leer Página Origen Completa
```
Lee TODA la página origen línea por línea.
Extrae CADA elemento en orden:
```

### 1.2 Análisis del `<head>`
Extraer en orden exacto:
- [ ] `<meta charset>`
- [ ] `<meta viewport>` - valor exacto
- [ ] `<title>` - estructura
- [ ] `<meta name="description">` - atributos
- [ ] `<meta name="robots">`
- [ ] `<link rel="canonical">` 
- [ ] `<meta property="og:*">` - cada uno
- [ ] `<meta name="twitter:*">` - cada uno
- [ ] `<link rel="preconnect">` - orden y atributos
- [ ] `<link rel="preload">` - cada uno con as, type, fetchpriority
- [ ] `<link rel="stylesheet">` - orden y atributos
- [ ] `<style>` inline - CONTENIDO COMPLETO
- [ ] `<script type="application/ld+json">` - estructura (no contenido)

### 1.3 Análisis del `<nav>`
Extraer CADA detalle:
- [ ] `.nav` - todas las clases
- [ ] `.nav-wrapper` - estructura
- [ ] `.logo` - tag `<a>` con TODOS los atributos
- [ ] `.logo img`:
  - src exacto pattern
  - srcset con TODOS los breakpoints
  - sizes con TODOS los valores
  - alt pattern
  - width, height
  - loading (presente o ausente)
  - fetchpriority
  - decoding
- [ ] `.nav-menu`:
  - id (ej: "nav-menu")
  - estructura `<ul>/<li>/<a>`
- [ ] `.nav-link` - cada uno
- [ ] `.mobile-menu-btn`:
  - aria-label valor exacto
  - aria-expanded valor
  - aria-controls valor
  - estructura de `<span>` hijos

### 1.4 Análisis del Hero
- [ ] `.hero` section - id, clases
- [ ] `<picture class="hero-background">`:
  - `<source type="image/avif">`:
    - srcset con TODOS los tamaños (500w, 800w, 1200w, etc.)
    - sizes exactos
  - `<source type="image/webp">`:
    - srcset completo
    - sizes exactos
  - `<img>`:
    - src
    - alt
    - width, height
    - loading
    - fetchpriority
    - decoding
- [ ] `.hero-content`:
  - clases adicionales
  - estructura interna
- [ ] `.hero-eta-badge` - estructura
- [ ] `.hero h1` - solo estructura
- [ ] `.hero-subtitle` - solo estructura
- [ ] `.hero-rating`:
  - estructura completa
  - clases de hijos
- [ ] `.hero-features`:
  - estructura de `.feature-item`
  - estructura de `.feature-icon` (SVG inline?)
- [ ] `.btn-primary` - atributos, clases

### 1.5 Análisis de Secciones
Para CADA sección principal:
- [ ] ID de sección
- [ ] Clases de sección
- [ ] Estructura de contenedor
- [ ] Estructura de grid/flex
- [ ] Estructura de cards/items
- [ ] Orden de elementos

### 1.6 Análisis de Botones Flotantes
- [ ] `.floating-btn` estructura
- [ ] `.floating-call`:
  - href pattern
  - aria-label
  - SVG interno
- [ ] `.floating-whatsapp`:
  - href pattern  
  - aria-label
  - SVG interno

### 1.7 Análisis del Footer
- [ ] Estructura completa
- [ ] Links y su orden
- [ ] Copyright estructura

---

## FASE 2: EXTRACCIÓN DE CSS

### 2.1 CSS Inline (`<style>` en head)
Extraer CADA regla en orden:
```css
/* Para cada selector, extraer: */
- Selector exacto
- Cada propiedad y valor
- Orden de propiedades
```

### 2.2 Archivos CSS Externos
Para cada archivo referenciado:
- Leer contenido completo
- Extraer cada regla
- Notar orden de reglas

### 2.3 Lista de Selectores a Comparar
```
/* Críticos - deben ser IDÉNTICOS */
:root { /* todas las variables */ }
* { }
body { }
.container { }
h1, h2, h3 { }
h1 { }

/* Nav */
.nav { }
.nav-wrapper { }
.logo { }
.logo img { }
.logo:hover { }
.nav-menu { }
.nav-link { }
.nav-link:hover { }
.mobile-menu-btn { }
.mobile-menu-btn span { }

/* Hero */
.hero { }
.hero-background { }
.hero-background img { }
.hero::after { }
.hero-content { }
.hero h1 { }
.hero-subtitle { }
.hero-rating { }
.hero-eta-badge { }
.hero-features { }
.feature-item { }
.feature-icon { }
.rating-stars { }
.rating-score { }
.rating-count { }
.eta-dot { }
.btn-primary { }
.btn-primary:hover { } /* si existe */

/* Flotantes */
.floating-btn { }
.floating-btn:hover { }
.floating-btn:focus-visible { }
.floating-call { }
.floating-whatsapp { }

/* Media Queries - ORDEN EXACTO */
@media (max-width: 768px) {
  /* cada regla dentro */
}
@media (max-width: 480px) {
  /* cada regla dentro */
}
```

---

## FASE 3: COMPARACIÓN LÍNEA POR LÍNEA

### 3.1 Crear Tabla de Diferencias
```markdown
| Ubicación | Elemento | Origen | Destino | Acción |
|-----------|----------|--------|---------|--------|
| head:15 | meta viewport | content="..." | content="..." | IGUALAR |
| nav:3 | button aria-label | "Abrir menú" | ausente | AGREGAR |
| css:23 | .nav padding | 16px 0 | 22px 0 | CAMBIAR |
```

### 3.2 Tipos de Diferencias a Detectar

**HTML:**
- Tag diferente
- Atributo ausente
- Atributo con valor diferente
- Orden de atributos diferente
- Elemento hijo faltante
- Elemento hijo extra
- Orden de hijos diferente

**CSS:**
- Selector ausente
- Selector extra
- Propiedad ausente
- Propiedad extra
- Valor diferente
- Orden de propiedades diferente
- Media query ausente
- Media query con contenido diferente

---

## FASE 4: APLICAR CAMBIOS (SIN PERDER CONTENIDO)

### 4.1 Contenido a PRESERVAR (no tocar)
```
- Texto dentro de <title>
- Texto dentro de <meta description>
- Texto dentro de <h1>, <h2>, <p>, etc.
- URLs de imágenes del sitio destino
- Números de teléfono
- Enlaces de WhatsApp
- Contenido de JSON-LD (schema)
- URLs en href (excepto estructura)
```

### 4.2 Estructura a COPIAR EXACTAMENTE
```
- Orden de tags
- Nombres de clases
- IDs
- Atributos aria-*
- Atributos data-*
- srcset patterns (reemplazando nombre de imagen)
- sizes valores
- width/height valores
- Estructura de SVG inline
- Orden de CSS rules
- Valores CSS
- Media queries completos
```

### 4.3 Proceso de Edición

Para cada diferencia:
1. Leer archivo destino
2. Localizar línea/sección exacta
3. Aplicar cambio mínimo necesario
4. Verificar que no se rompió nada
5. Si hay .min.css, actualizar AMBOS

---

## FASE 5: VERIFICACIÓN EXHAUSTIVA

### 5.1 Comparación Post-Cambio
```bash
# Comparar CSS
diff <(curl -s origen/css) <(curl -s destino/css)

# Comparar estructura HTML (sin contenido)
# Extraer solo tags y atributos
```

### 5.2 Checklist de Verificación

**Nav:**
- [ ] .nav padding idéntico
- [ ] .logo clases idénticas
- [ ] .logo img height desktop idéntico
- [ ] .logo img height mobile idéntico
- [ ] .logo img srcset pattern idéntico
- [ ] .logo img sizes idéntico
- [ ] .logo:hover idéntico
- [ ] button aria-label presente
- [ ] button aria-expanded presente
- [ ] button aria-controls presente
- [ ] ul#nav-menu presente
- [ ] .nav-link transition idéntico
- [ ] .nav-link:hover idéntico
- [ ] .mobile-menu-btn estructura idéntica
- [ ] .mobile-menu-btn span idéntico

**Hero:**
- [ ] .hero clases idénticas
- [ ] picture.hero-background presente
- [ ] source[type="image/avif"] presente
- [ ] source srcset tiene 500w, 800w, 1200w
- [ ] source sizes idéntico
- [ ] source[type="image/webp"] presente
- [ ] img atributos idénticos
- [ ] .hero-content estructura idéntica
- [ ] .hero::after CSS idéntico

**CSS General:**
- [ ] :root variables idénticas
- [ ] Todos los selectores presentes
- [ ] Todos los valores idénticos
- [ ] Media queries idénticos
- [ ] Orden de reglas idéntico

---

## FASE 6: REPORTE FINAL

```markdown
# Reporte de Sincronización de Páginas

## Resumen
- **Origen:** {ruta completa}
- **Destino:** {ruta completa}
- **Diferencias encontradas:** {número}
- **Cambios aplicados:** {número}
- **Errores:** {número o "ninguno"}

## Cambios Detallados

### HTML Changes
| Línea | Antes | Después | Razón |
|-------|-------|---------|-------|
| 45 | `<button>` | `<button aria-label="...">` | Agregar accesibilidad |

### CSS Changes  
| Archivo | Selector | Propiedad | Antes | Después |
|---------|----------|-----------|-------|---------|
| critical.css | .nav | padding | 22px 0 | 16px 0 |
| critical.css | .logo img | height | 140px | 86px |

### Archivos Modificados
1. `index.html` - {N} cambios
2. `assets/css/critical.css` - {N} cambios
3. `assets/css/critical.min.css` - {N} cambios

### Verificación
| Check | Estado |
|-------|--------|
| CSS idéntico | ✅ |
| Nav structure | ✅ |
| Hero structure | ✅ |
| Contenido preservado | ✅ |

### Imágenes Creadas (si aplica)
- hero-{nombre}-500w.avif
- hero-{nombre}-500w.webp
- hero-{nombre}-1200w.avif
```

---

## COMANDOS ÚTILES

```bash
# Comparar CSS en producción
echo "=== ORIGEN ===" && curl -s "{url-origen}/css" | grep -oE "selector\{[^}]+\}"
echo "=== DESTINO ===" && curl -s "{url-destino}/css" | grep -oE "selector\{[^}]+\}"

# Comparar estructura HTML
diff <(grep -oE '<[^>]+>' origen.html) <(grep -oE '<[^>]+>' destino.html)

# Verificar atributos específicos
grep -n "aria-label\|aria-expanded\|aria-controls" archivo.html
```

---

## REGLA DE ORO

> Si hay CUALQUIER diferencia entre origen y destino (excepto contenido de texto/imágenes), 
> ES UN ERROR que debe corregirse antes de terminar.

El agente NO termina hasta que la comparación muestre CERO diferencias estructurales.
