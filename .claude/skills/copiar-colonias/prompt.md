---
name: copiar-colonias
description: Copia la estructura de paginas de colonias de plomero a electricista, cambiando solo contenido
metadata:
  short-description: Copiar paginas de colonias plomero->electricista
  version: 1.0.0
  triggers:
    - /copiar-colonias
    - /copiarcolonias
    - /copy-colonies
---

# Copiar Colonias (plomero -> electricista)

## Objetivo
Crear paginas de colonias para electricista usando la estructura EXACTA de plomero.
Solo cambia el contenido (textos, telefonos, URLs). Estructura HTML/CSS identica.

## Rutas base

PLOMERO (fuente):
/Users/hectorpc/Documents/Hector Palazuelos/Google My Business/plomero culiacan pro/servicios/plomero-colonias-culiacan/{colonia}/index.html

ELECTRICISTA (destino):
/Users/hectorpc/Documents/Hector Palazuelos/Google My Business/electricista culiacan pro/servicios/electricista-colonias-culiacan/{colonia}/index.html

## CSS correcto

<!-- USAR SIEMPRE (archivo en raiz, copiado de plomero) -->
<link rel="stylesheet" href="../../../styles.min.css">

## Contenido a cambiar

REEMPLAZOS OBLIGATORIOS:
  # Marca
  - "Plomero" -> "Electricista"
  - "plomero" -> "electricista"
  - "plomeria" -> "electricidad"
  - "Plomeria" -> "Electricidad"

  # Telefono
  - "667 120 5864" -> "667 392 2273"
  - "6671205864" -> "6673922273"
  - "526671205864" -> "526673922273"

  # Dominio
  - "plomeroculiacanpro.mx" -> "electricistaculiacanpro.mx"

  # GTM (si difiere)
  - GTM-XXXXXX -> GTM-W75CRTX5

  # Logo
  - "plomero-culiacan-pro-logo" -> "electricista-culiacan-pro-logo"

  # Servicios principales (caja naranja hero)
  PLOMERO: Emergencias 24/7, reparacion de fugas, destape de drenajes, instalacion de tinacos
  ELECTRICISTA: Emergencias 24/7, reparacion de cortocircuitos, instalacion de contactos, tableros electricos

  # URLs servicios
  - "/servicios/emergencias-plomeria/" -> "/servicios/emergencia-24-7/"
  - "/servicios/reparacion-fugas/" -> "/servicios/reparacion-cortos-circuitos/"
  - "/servicios/destape-drenajes/" -> "/servicios/instalacion-contactos/"
  - "/servicios/instalacion-tinacos/" -> "/servicios/mantenimiento-tableros/"

## Estructura de benefits (emojis)

<div class="benefits-grid">
  <div class="benefit"><div class="benefit-icon">🏠</div><h3>Conocemos la Zona</h3><p>Experiencia en el fraccionamiento</p></div>
  <div class="benefit"><div class="benefit-icon">⚡</div><h3>Llegada Rapida</h3><p>Respuesta en 20-30 min</p></div>
  <div class="benefit"><div class="benefit-icon">💰</div><h3>Precios Justos</h3><p>Sin sorpresas</p></div>
  <div class="benefit"><div class="benefit-icon">🔧</div><h3>Trabajo Garantizado</h3><p>Garantia 6 meses</p></div>
  <div class="benefit"><div class="benefit-icon">✅</div><h3>Profesionales</h3><p>Electricistas certificados</p></div>
</div>

Nota: Para zona comercial (Centro), usar 🏢 en vez de 🏠

## Servicios de electricista (cards)

<div class="grid">
  <div class="card"><h3>Instalacion Electrica</h3><p>Instalaciones completas para casas y negocios. Cableado y tierra fisica.</p></div>
  <div class="card"><h3>Reparacion de Cortocircuitos</h3><p>Deteccion y reparacion de cortocircuitos, fallas y apagones.</p></div>
  <div class="card"><h3>Contactos y Apagadores</h3><p>Instalacion de contactos polarizados, apagadores y dimmers.</p></div>
  <div class="card"><h3>Tableros Electricos</h3><p>Revision, actualizacion y cambio de breakers.</p></div>
  <div class="card"><h3>Iluminacion</h3><p>Instalacion de lamparas, spots LED y sistemas de iluminacion.</p></div>
  <div class="card"><h3>Emergencias 24/7</h3><p>Atencion inmediata para emergencias electricas.</p></div>
</div>

## Imagenes hero (rutas relativas)

<picture class="hero-background">
  <source type="image/webp" srcset="../../../assets/images/optimizadas/electricista-culiacan-hero-500w.webp 500w,../../../assets/images/optimizadas/electricista-culiacan-hero-800w.webp 800w,../../../assets/images/optimizadas/electricista-culiacan-hero-1200w.webp 1200w" sizes="100vw">
  <img src="../../../assets/images/optimizadas/electricista-culiacan-hero-800w.webp" alt="Electricista profesional en Culiacan" width="800" height="533" loading="eager">
</picture>

## Flujo de ejecucion

### Paso 1: Recibir nombre de colonia
Usuario: /copiar-colonias las-quintas
         /copiar-colonias centro
         /copiar-colonias tres-rios

### Paso 2: Verificar que existe en plomero
ls "/Users/hectorpc/Documents/Hector Palazuelos/Google My Business/plomero culiacan pro/servicios/plomero-colonias-culiacan/{colonia}/index.html"

### Paso 3: Crear directorio en electricista
mkdir -p "/Users/hectorpc/Documents/Hector Palazuelos/Google My Business/electricista culiacan pro/servicios/electricista-colonias-culiacan/{colonia}"

### Paso 4: Leer pagina de plomero
cat "/plomero culiacan pro/servicios/plomero-colonias-culiacan/{colonia}/index.html"

### Paso 5: Crear pagina de electricista
- Copiar estructura HTML exacta
- Aplicar todos los reemplazos de contenido
- Usar CSS: href="../../../styles.min.css"
- Usar imagenes hero con rutas relativas
- Guardar en electricista

### Paso 6: Verificar
# Abrir en navegador
open "/electricista culiacan pro/servicios/electricista-colonias-culiacan/{colonia}/index.html"

## Validacion obligatoria

- [ ] CSS apunta a ../../../styles.min.css
- [ ] Hero srcset usa rutas relativas ../../../assets/images/...
- [ ] Telefono es 667 392 2273
- [ ] Dominio es electricistaculiacanpro.mx
- [ ] Logo es electricista-culiacan-pro-logo
- [ ] Servicios son de electricista (no plomeria)
- [ ] Benefits usan emojis correctos
- [ ] Canonical URL es correcta

## Ejemplo de uso

Usuario: /copiar-colonias guadalupe

Claude:
1. Verifico que existe /plomero/servicios/plomero-colonias-culiacan/guadalupe/
2. Creo /electricista/servicios/electricista-colonias-culiacan/guadalupe/
3. Copio estructura, aplico reemplazos
4. Verifico CSS y rutas
5. Abro en navegador para confirmar

Resultado: Pagina creada en /servicios/electricista-colonias-culiacan/guadalupe/

## Modo batch (multiples colonias)

Usuario: /copiar-colonias las-quintas,centro,tres-rios

Claude: Proceso las 3 colonias en secuencia

## Errores comunes a evitar

1. NO usar /assets/css/styles.min.css - usar ../../../styles.min.css
2. NO usar rutas absolutas en srcset - usar rutas relativas
3. NO olvidar cambiar telefono
4. NO dejar texto de plomeria
5. NO olvidar canonical URL

---

# CHECKLIST FINAL

Antes de reportar completado:

- [ ] Archivo existe en electricista
- [ ] Se abre correctamente en navegador
- [ ] Estilos se cargan (no se ve feo)
- [ ] Telefono correcto (667 392 2273)
- [ ] Sin menciones a plomero/plomeria
- [ ] Servicios son de electricista
- [ ] Hero image visible
- [ ] Botones flotantes funcionan
