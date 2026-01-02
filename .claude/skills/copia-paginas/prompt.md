---
name: copia-paginas
description: Clone a reference page's HTML/CSS/JS structure exactly while changing only approved content fields; verify with structural diffs and report any deviations.
metadata:
  short-description: Copy page structure exactly; content-only changes
  version: 2.0.0
  triggers:
    - /copia-paginas
    - /copiar-pagina
    - /sync-pages
    - /clone-page
---

# Page Structure Clone (exact match)

## Objetivo
Copiar la página A como plantilla exacta para la página B.  
Solo puede cambiar contenido. Todo lo demás debe quedar idéntico.

## Entradas requeridas
- `source_path`: ruta de la página fuente (A).
- `target_path`: ruta de la página destino (B).
- `content_allowlist`: lista estricta de campos que pueden cambiar.
- `tracking_allowlist` (opcional): IDs permitidos (GTM/GA/Clarity).
- `ignore_blocks` (opcional): selectores o bloques completos que pueden excluirse.

---

## Definición de "contenido" (lo único que puede cambiar)

```
✅ PERMITIDO CAMBIAR:
- Texto visible (nodos de texto)
- Valores de href, src, srcset (solo la URL, no atributos asociados)
- alt, title
- Teléfonos, emails, nombres de marca
- IDs de tracking SOLO si están en tracking_allowlist
- Contenido de JSON-LD (schema) - solo datos, no estructura
```

---

## Todo lo demás es ESTRUCTURAL y debe quedar IDÉNTICO

```
🔒 PROHIBIDO CAMBIAR:
- Árbol de tags y orden exacto de nodos
- Clases, IDs, roles
- aria-*, data-* y cualquier atributo no permitido
- width, height, sizes, loading, decoding, fetchpriority
- Comentarios HTML
- Orden y ubicación de scripts y estilos
- Orden de secciones y bloques (popup, CTA flotantes, footer, etc)
- Variables CSS (:root)
- Selectores CSS y sus propiedades
- Media queries y breakpoints
- Orden de reglas CSS
```

---

## Flujo obligatorio

### Paso 1: Lectura
```bash
# Abrir ambas páginas
read source_path  # Página A (plantilla)
read target_path  # Página B (destino)
```

### Paso 2: Copia base
```
# Copiar estructura de A como base en B
- HTML completo
- CSS (inline y externos)
- JS (orden y atributos)
- Assets referenciados (verificar existencia)
```

### Paso 3: Reemplazo de contenido
```
# Reemplazar SOLO contenido permitido:
FOR each element in content_allowlist:
  - Localizar elemento en B
  - Preservar estructura/atributos
  - Cambiar solo el valor de contenido
  - Verificar que no se alteró estructura
```

### Paso 4: Validación estructural
```
# Validar con diff estructural
- Comparar HTML normalizado
- Comparar CSS regla por regla
- Comparar orden de scripts
- Generar reporte de diferencias
```

### Paso 5: Reporte
```
# Reportar resultado
IF diferencias == 0:
  return PASS
ELSE:
  return FAIL + lista_diferencias
```

---

## Validación mínima obligatoria

### 1) HTML (estructura)

```python
# Proceso de validación HTML:
1. Normalizar HTML de A y B
2. Reemplazar valores permitidos por placeholder <content>
3. Extraer secuencia de tags + atributos (sin texto visible)
4. Comparar línea por línea
5. Debe coincidir 1:1
```

**Elementos a validar:**
- [ ] Orden de tags
- [ ] Nombres de clases (exactos)
- [ ] IDs (exactos)
- [ ] Atributos aria-* (todos)
- [ ] Atributos data-* (todos)
- [ ] width, height en imágenes
- [ ] sizes, srcset pattern (no URLs)
- [ ] loading, fetchpriority, decoding
- [ ] Estructura de SVG inline
- [ ] Comentarios HTML

### 2) CSS

```python
# Proceso de validación CSS:
1. Extraer todas las reglas de A
2. Extraer todas las reglas de B
3. Comparar selector por selector
4. Comparar propiedad por propiedad
5. Comparar valor por valor
```

**Archivos a validar:**
- [ ] CSS inline (`<style>` en head)
- [ ] critical.css / critical.min.css
- [ ] styles.css / styles.min.css
- [ ] Cualquier otro CSS referenciado

**Reglas clave que DEBEN coincidir:**
```css
/* Variables */
:root { }

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
.hero-features { }
.btn-primary { }

/* Flotantes */
.floating-btn { }
.floating-call { }
.floating-whatsapp { }

/* Media Queries */
@media (max-width: 768px) { /* todas las reglas */ }
@media (max-width: 480px) { /* todas las reglas */ }
```

### 3) Scripts

```python
# Proceso de validación Scripts:
1. Extraer todos los <script> de A
2. Extraer todos los <script> de B
3. Comparar orden exacto
4. Comparar atributos (async, defer, type, src)
5. No agregar ni quitar scripts fuera del allowlist
```

---

## Output requerido

### PASS (estructura idéntica)
```markdown
## Resultado: ✅ PASS

### Resumen
- Fuente: {source_path}
- Destino: {target_path}
- Diferencias estructurales: 0
- Cambios de contenido: {N}

### Contenido actualizado
| Elemento | Valor anterior | Valor nuevo |
|----------|---------------|-------------|
| title | "Plomero..." | "Electricista..." |
| h1 | "Plomero..." | "Electricista..." |
| tel: | 6672... | 6671... |

### Verificación
- [x] HTML estructura idéntica
- [x] CSS idéntico
- [x] Scripts idénticos
- [x] Contenido preservado
```

### FAIL (hay diferencias)
```markdown
## Resultado: ❌ FAIL

### Diferencias encontradas: {N}

| Archivo | Línea | Tipo | Esperado (A) | Encontrado (B) |
|---------|-------|------|--------------|----------------|
| index.html | 45 | attr | aria-label="Abrir menú" | (ausente) |
| critical.css | 23 | value | padding:16px 0 | padding:22px 0 |
| critical.css | 26 | value | height:86px | height:140px |

### Acciones requeridas
1. Agregar aria-label en button (línea 45)
2. Cambiar padding en .nav (línea 23)
3. Cambiar height en .logo img (línea 26)
```

---

## Reglas estrictas

### ❌ PROHIBIDO
- No afirmar "listo" sin validación completa
- No asumir que algo está correcto sin verificar
- No cambiar estructura "porque parece mejor"
- No omitir archivos CSS (si hay .min.css, validar ambos)
- No ignorar diferencias "menores"

### ✅ OBLIGATORIO
- Validar CADA selector CSS
- Validar CADA atributo HTML
- Reportar TODAS las diferencias
- Si no puedes validar algo, decirlo explícitamente
- Si hay dudas, preguntar ANTES de cambiar estructura

---

## Ejemplo de content_allowlist

```yaml
content_allowlist:
  # Textos
  - title
  - meta[name="description"]
  - h1, h2, h3, p (texto interno)
  - .hero-subtitle (texto)
  - .benefit-content p (texto)
  
  # URLs
  - link[rel="canonical"] href
  - meta[property="og:url"] content
  - a.logo href (si cambia dominio)
  - img src, srcset (URLs, no pattern)
  
  # Contacto
  - tel: enlaces
  - wa.me/ enlaces
  - mailto: enlaces
  
  # Schema
  - script[type="application/ld+json"] (contenido JSON)
  
  # Tracking (solo si en tracking_allowlist)
  - GTM-XXXXXX
  - G-XXXXXX
  - clarity project id

tracking_allowlist:
  - GTM-ABCD123
  - G-XYZ789

ignore_blocks:
  - <!-- Google Tag Manager -->
  - <!-- End Google Tag Manager -->
```

---

## Comandos de validación

```bash
# Comparar estructura HTML (sin contenido)
diff <(grep -oE '<[^>]+>' A.html | sort) <(grep -oE '<[^>]+>' B.html | sort)

# Comparar CSS selector por selector
echo "=== A ===" && curl -s "url-A/css" | grep -oE "\.selector\{[^}]+\}"
echo "=== B ===" && curl -s "url-B/css" | grep -oE "\.selector\{[^}]+\}"

# Verificar atributos específicos
grep -n "aria-label\|aria-expanded\|aria-controls\|srcset\|sizes" archivo.html

# Comparar archivos CSS completos
diff <(cat A/critical.min.css) <(cat B/critical.min.css)
```

---

## Regla de oro

> **Si hay CUALQUIER diferencia estructural entre A y B, es un FAIL.**
> 
> El agente NO puede reportar PASS hasta que la validación muestre 
> CERO diferencias en estructura, CSS, y orden de elementos.
> 
> "Casi igual" NO es igual. 
> "Solo un atributo" ES una diferencia.
> "Es menor" NO es excusa.
