# Copiar Landing (Método Rápido)

Crea landing pages copiando una landing de referencia validada v2.0.0 y solo cambiando textos.

## 🚀 Por qué usar este método

- ✅ **10x más rápido** - Copias código validado, solo cambias contenido
- ✅ **0 errores** - Estructura ya validada, imposible fallar
- ✅ **Simple** - Solo 3 pasos: copiar, editar textos, validar

## 📋 Landings de Referencia Disponibles

Usa cualquiera de estas como base (todas v2.0.0 validadas):

1. **servicios/reparacion-cortos-circuitos/** - Landing de servicios completa
2. **servicios/electricista-colonias-culiacan/** - Landing de zonas/colonias
3. **servicios/electricista-cerca-de-mi/** - Landing de ubicación

## 🎯 Proceso (3 pasos)

### Paso 1: Copiar landing de referencia

```bash
# Copiar la landing completa
cp -r servicios/[landing-referencia] servicios/[nuevo-slug]

# Ejemplo:
cp -r servicios/reparacion-cortos-circuitos servicios/electricista-emergencias
```

### Paso 2: Editar solo los textos

Abre `servicios/[nuevo-slug]/index.html` y cambia **SOLO** estos valores:

**En `<head>`:**
```html
<title>[Nuevo título 50-60 chars] | Electricista Culiacán Pro</title>
<meta name="description" content="[Nueva descripción 120-155 chars]">
<link rel="canonical" href="https://electricistaculiacanpro.mx/servicios/[nuevo-slug]/" />
```

**En breadcrumbs:**
```html
<span class="breadcrumb-current" itemprop="name">[Nuevo nombre visible]</span>
```

**En hero:**
```html
<h1>[Nuevo H1 - keyword principal]</h1>
<p class="hero-subtitle">[Nueva descripción corta]</p>
```

**En benefits (4-5 cards):**
```html
<h3>[Nuevo título benefit]</h3>
<p>[Nueva descripción benefit]</p>
```

**En FAQ (si tiene):**
```html
<h3>[Nueva pregunta]</h3>
<p>[Nueva respuesta]</p>
```

**En JSON-LD schemas (al final):**
- Actualizar `name`, `description`, `url` en Service schema
- Actualizar breadcrumb names
- Actualizar FAQs si las cambiaste

**❌ NO CAMBIES:**
- Estructura HTML
- Clases CSS
- Colores
- SVG icons
- Teléfonos (vienen del config)
- GTM/GA IDs
- Navegación
- Footer

### Paso 3: Validar

```bash
# Ejecutar validador
./validate-landing.sh servicios/[nuevo-slug]/index.html

# Abrir en navegador (con servidor HTTP)
python3 -m http.server 8080 &
open -a Safari "http://localhost:8080/servicios/[nuevo-slug]/index.html"
```

## ✅ Checklist Final

Antes de hacer commit, verificar:

- [ ] Title: 50-60 caracteres
- [ ] Meta description: 120-155 caracteres
- [ ] Canonical URL actualizado con nuevo slug
- [ ] Breadcrumb con nuevo nombre
- [ ] H1 actualizado
- [ ] Benefits actualizados (4-5 cards)
- [ ] FAQs actualizadas (si las tiene)
- [ ] JSON-LD schemas actualizados
- [ ] **Validador pasa:** `./validate-landing.sh` → ✅
- [ ] **Se ve bien en desktop** (1440px)
- [ ] **Se ve bien en mobile** (375px)

## 💡 Ejemplo Completo

```bash
# 1. Copiar referencia
cp -r servicios/reparacion-cortos-circuitos servicios/electricista-emergencias-24h

# 2. Editar textos en index.html
# - Title: "Electricista Emergencias 24h Culiacán | Respuesta Inmediata"
# - Description: "Electricista de emergencias 24 horas en Culiacán. Atendemos apagones, cortocircuitos y fallas eléctricas. Servicio urgente con llegada en 30 minutos."
# - H1: "Electricista de Emergencias 24 Horas en Culiacán"
# - Benefits: actualizar los 5 benefits
# - FAQs: actualizar 4-6 preguntas

# 3. Validar
./validate-landing.sh servicios/electricista-emergencias-24h/index.html

# 4. Abrir y revisar
python3 -m http.server 8080 &
open -a Safari "http://localhost:8080/servicios/electricista-emergencias-24h/index.html"
```

## 🚨 Errores Comunes a Evitar

1. **❌ NO cambiar estructura HTML** - Solo textos
2. **❌ NO cambiar colores** - Ya están correctos
3. **❌ NO cambiar clases CSS** - Ya están validadas
4. **❌ NO hardcodear teléfonos** - Vienen del config automáticamente
5. **❌ NO olvidar actualizar canonical URL** - Debe tener el nuevo slug
6. **❌ NO olvidar actualizar schemas JSON-LD** - Deben reflejar el nuevo contenido

## 📝 Prompt para Claude

Si quieres que Claude haga el trabajo:

```
Copia la landing servicios/[landing-referencia] a servicios/[nuevo-slug] y actualiza solo los textos:

- Title: [nuevo title 50-60 chars]
- Meta description: [nueva descripción 120-155 chars]
- H1: [nuevo H1]
- Hero subtitle: [nuevo subtitle]
- Benefits (5 cards):
  1. [título] - [descripción]
  2. [título] - [descripción]
  3. [título] - [descripción]
  4. [título] - [descripción]
  5. [título] - [descripción]
- FAQs (4-6 preguntas):
  1. [pregunta] - [respuesta]
  2. [pregunta] - [respuesta]
  ...

NO cambies estructura, colores, clases ni estilos.
Solo actualiza textos y schemas JSON-LD.
Valida con ./validate-landing.sh al final.
```

## ⚡ Tiempo Estimado

- Copiar landing: **10 segundos**
- Editar textos: **5-10 minutos**
- Validar: **30 segundos**

**Total: 10-15 minutos** vs 1+ hora con landing-creator desde cero.

---

**¿Listo para empezar?**

Dame:
1. Landing de referencia (reparacion-cortos-circuitos, electricista-colonias-culiacan, electricista-cerca-de-mi)
2. Nuevo slug
3. Textos (title, description, H1, benefits, FAQs)

Y tendrás tu landing en 10 minutos.
