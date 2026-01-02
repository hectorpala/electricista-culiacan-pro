---
name: service-card-validator
description: Valida que todas las service cards del sitio tengan estructura correcta, dimensiones 420x235 y service-cta
allowed-tools: Read(*), Grep(*), Glob(**), Edit(*)
---

# Service Card Validator

## Cuándo activarme

Actívame cuando:
- Usuario dice "valida las service cards"
- Usuario dice "revisa las tarjetas de servicios"
- Usuario menciona "service-cta" o "service cards"

## Qué valido

### 1. Estructura HTML Correcta

```html
<a href="..." class="card card--img">
    <div class="service-card">
        <figure class="media-box">
            <picture>
                <source type="image/webp" srcset="...420w.webp 420w, ...800w.webp 800w">
                <img src="...420w.webp" width="420" height="235" loading="lazy">
            </picture>
        </figure>
    </div>
    <h3>Título Sin Emojis</h3>
    <p>Descripción...</p>
    <span class="service-cta">Más Información →</span>
</a>
```

### 2. Errores Comunes

❌ **Dimensiones incorrectas:**
```html
<img width="800" height="600">  <!-- Debe ser 420x235 -->
```

❌ **Emojis en H3:**
```html
<h3>⚡ Instalación</h3>  <!-- NO emojis -->
```

❌ **Falta service-cta:**
```html
</a>  <!-- Sin <span class="service-cta"> antes del cierre -->
```

❌ **Estructura plana:**
```html
<a class="card">
    <img src="...">  <!-- Falta service-card > media-box > picture -->
    <h3>Título</h3>
</a>
```

## Proceso de Validación

1. **Buscar archivos:** Uso Glob para encontrar todos los HTML en `servicios/` y `colonias/`
2. **Leer contenido:** Leo cada archivo
3. **Validar 5 áreas:**
   - Estructura: `service-card > media-box > picture`
   - Dimensiones: `width="420" height="235"`
   - Sin emojis en H3
   - Tiene `<span class="service-cta">`
   - Clases correctas: `card card--img`

4. **Reportar:** Lista de errores por archivo

## Formato de Reporte

```markdown
## Service Cards Validation Report

### ✅ APROBADAS (12 archivos)
- colonias/tres-rios/index.html
- servicios/instalacion-electrica/index.html
...

### ❌ ERRORES (3 archivos)

**colonias/centro/index.html**
- Línea 480: Dimensiones incorrectas (800x600 → debe ser 420x235)
- Línea 485: Falta service-cta
- Línea 477: Estructura incorrecta (falta media-box)

**servicios/emergencia-24-7/index.html**
- Línea 120: Emoji en H3: "⚡ Emergencias"
```

## Ejemplo de Uso

<example>
Usuario: "valida las service cards"

Yo:
1. Busco todos los archivos HTML en servicios/ y colonias/
2. Valido cada service card contra los 5 criterios
3. Genero reporte con errores específicos
4. Pregunto: "¿Quieres que corrija automáticamente? (s/n)"
</example>

## Reglas

- SIEMPRE reportar línea exacta del error
- NUNCA modificar sin autorización del usuario
- Si usuario dice "s" o "corrige": aplicar correcciones con Edit tool
- Validar TODAS las páginas del sitio, no solo una
