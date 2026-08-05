# 🔌 Electricista Culiacán Pro - Instrucciones de Implementación

## ✅ Archivos Creados Exitosamente

### Archivos Principales
- ✅ `index.html` - Página principal con hero, servicios, testimonios, FAQ
- ✅ `styles.css` - Estilos con paleta azul eléctrico + amarillo
- ✅ `main.js` - JavaScript con menú móvil, tracking, animaciones
- ✅ `manifest.json` - PWA configuration
- ✅ `sw.js` - Service Worker para funcionalidad offline
- ✅ `robots.txt` - SEO crawling rules
- ✅ `sitemap.xml` - Sitemap base

### Páginas Adicionales
- ✅ `contacto/index.html` - Página de contacto
- ✅ `gracias/index.html` - Página de agradecimiento post-conversión

### Carpetas
- ✅ `/assets/` - Para imágenes, fonts, iconos
- ✅ `/blog/` - Para artículos
- ✅ `/servicios/` - Para páginas de servicios
- ✅ `/sitemaps/` - Para sitemaps adicionales

---

## 🚨 TAREAS CRÍTICAS PENDIENTES

### 1. Actualizar Números de Teléfono ⚠️

**Reemplazar en TODOS los archivos:**

Buscar: `667 000 0000` o `+526670000000`

Reemplazar con el número real del electricista.

**Archivos a actualizar:**
- `index.html` (3 lugares)
- `contacto/index.html` (3 lugares)
- `gracias/index.html` (2 lugares)

```bash
# Comando para buscar todos los números:
grep -r "667 000 0000" .
```

### 2. Crear/Copiar Assets 📦

#### A. Logo Principal
Crear o adaptar logo:
- **Archivo**: `logo-electricista-culiacan-pro.webp`
- **Ubicación**: Raíz del proyecto
- **Dimensiones**: 400x120px aprox
- **Formato**: WebP optimizado

#### B. Fuentes (Copiar del proyecto plomero)
Copiar estos archivos a `assets/fonts/`:
```
assets/fonts/inter-400.woff2
assets/fonts/montserrat-800.woff2
```
(Nota 2026-08-04: inter-500/600 y montserrat-700 eran duplicados byte-a-byte de inter-400/
montserrat-800 y ya no existen en el repo — usar solo estos 2 archivos, con font-weight
distinto en el @font-face pero la misma URL.)

**Comando para copiar:**
```bash
cp "../plomero culiacan pro/assets/fonts/"*.woff2 assets/fonts/
```

#### C. Iconos PWA
Crear iconos en `assets/icons/`:
- `favicon.ico` (32x32)
- `favicon.png` (192x192)
- `icon-72x72.png`
- `icon-96x96.png`
- `icon-128x128.png`
- `icon-144x144.png`
- `icon-152x152.png`
- `icon-192x192.png`
- `icon-384x384.png`
- `icon-512x512.png`

**Herramienta recomendada**: https://realfavicongenerator.net/

#### D. Imágenes de Servicios
Agregar imágenes en `assets/images/`:
- Instalaciones eléctricas
- Reparación de cortocircuitos
- Tableros eléctricos
- Iluminación
- Equipo de trabajo

---

## 🔧 Personalización

### Cambiar Colores (si es necesario)

Editar `styles.css`, líneas 34-45:

```css
:root {
  --brand: #1E40AF;        /* Azul principal */
  --brand-light: #3B82F6;  /* Azul claro */
  --brand-dark: #1E3A8A;   /* Azul oscuro */
  --accent: #FCD34D;       /* Amarillo energía */
  --whatsapp: #25D366;     /* WhatsApp verde */
}
```

### Actualizar Información de Contacto

En `index.html` y otras páginas, actualizar:
- Email: `contacto@electricistaculiacanpro.mx`
- Dirección física (si aplica)
- Horarios de atención

### Modificar Servicios

En `index.html`, sección de servicios (línea ~140):
- Agregar/quitar servicios según necesidad
- Actualizar descripciones
- Agregar precios (opcional)

---

## 📊 Configuración de Analytics

### Google Tag Manager (GTM)

1. Crear cuenta en https://tagmanager.google.com
2. Obtener el código GTM (ej: GTM-XXXXXXX)
3. Agregar en `index.html` después de `<head>`:

```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
<!-- End Google Tag Manager -->
```

4. Agregar después de `<body>`:

```html
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```

### Google Analytics 4 (GA4)

Configurar desde GTM o directamente en el código.

---

## 🌐 Configuración de Dominio

### Opción 1: GitHub Pages (Gratis)

1. Crear repositorio en GitHub
2. Subir todos los archivos
3. Ir a Settings → Pages
4. Seleccionar branch `main`
5. Configurar dominio personalizado: `electricistaculiacanpro.mx`

### Opción 2: Netlify (Gratis)

1. Crear cuenta en https://netlify.com
2. Arrastrar carpeta del proyecto
3. Configurar dominio personalizado
4. HTTPS automático

### Opción 3: Hosting tradicional

Subir archivos via FTP al servidor.

---

## 📝 Contenido Pendiente

### Testimonios
Agregar testimonios reales en `index.html` (línea ~240)

### FAQ
Expandir preguntas frecuentes según dudas comunes

### Blog Posts
Crear artículos en `/blog/` sobre:
- "¿Cómo prevenir cortocircuitos en casa?"
- "Señales de que necesitas actualizar tu instalación eléctrica"
- "Guía de mantenimiento eléctrico preventivo"

### Páginas de Servicios Individuales
Crear en `/servicios/`:
- `instalacion-electrica/index.html`
- `reparacion-cortocircuitos/index.html`
- `emergencia-24-7/index.html`
- `mantenimiento-tableros/index.html`

### Páginas por Colonias (SEO Local)
Crear en `/servicios/electricista-colonias-culiacan/`:
- `las-quintas/index.html`
- `tres-rios/index.html`
- `centro/index.html`
- etc.

---

## 🚀 Lanzamiento

### Checklist Pre-Launch

- [ ] Números de teléfono actualizados
- [ ] Logo creado y optimizado
- [ ] Fuentes copiadas
- [ ] Iconos PWA generados
- [ ] Imágenes de servicios agregadas
- [ ] GTM/GA4 configurado
- [ ] Dominio configurado
- [ ] HTTPS habilitado
- [ ] Probar en móvil
- [ ] Probar formularios
- [ ] Verificar enlaces WhatsApp
- [ ] Probar llamadas telefónicas
- [ ] Revisar SEO (meta tags, schema)
- [ ] Enviar sitemap a Google Search Console

### Herramientas de Testing

- **PageSpeed Insights**: https://pagespeed.web.dev/
- **Mobile-Friendly Test**: https://search.google.com/test/mobile-friendly
- **Schema Validator**: https://validator.schema.org/
- **GTM Preview**: Modo preview en Tag Manager

---

## 📞 Soporte

Para dudas o asistencia con la implementación:
- Revisar README.md
- Consultar documentación de cada tecnología
- Probar en navegador local primero

---

**Última actualización**: 21 de noviembre, 2025

✅ **Proyecto base completado y listo para personalización**
