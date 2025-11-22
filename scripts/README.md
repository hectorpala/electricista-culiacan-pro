# Scripts de Automatización - Electricista Culiacán Pro

Colección de scripts Python para automatizar tareas comunes de mantenimiento del sitio.

## 📋 Scripts Disponibles

### 1. `generate_sitemap.py`
Genera automáticamente sitemap.xml desde todos los archivos HTML del proyecto.

```bash
python3 scripts/generate_sitemap.py
```

**Funcionalidad:**
- Escanea todos los archivos `index.html` en el proyecto
- Genera URLs con prioridades apropiadas por sección
- Actualiza fechas de modificación
- Crea sitemap.xml válido según schema oficial

**Salida:**
- `sitemap.xml` - Sitemap principal con todas las URLs

---

### 2. `validate_schemas.py`
Valida todos los esquemas JSON-LD en archivos HTML.

```bash
python3 scripts/validate_schemas.py
```

**Validaciones:**
- ✅ Sintaxis JSON válida
- ✅ Campos requeridos (@context, @type)
- ✅ Estructura de @graph
- ✅ Campos específicos por tipo de schema (Electrician, Service, FAQPage)

**Códigos de salida:**
- `0` - Todos los schemas válidos
- `1` - Errores encontrados

---

### 3. `optimize_images.py`
Convierte imágenes PNG/JPG a WebP para optimización.

```bash
python3 scripts/optimize_images.py
```

**Requisitos:**
```bash
brew install webp
```

**Funcionalidad:**
- Busca imágenes PNG, JPG, JPEG
- Convierte a WebP con calidad 85
- Soporta estructura originales/ → optimizadas/
- Calcula reducción de tamaño

**Salida:**
- Archivos `.webp` optimizados
- Reporte de reducción de tamaño

---

### 4. `check_links.py`
Verifica enlaces internos rotos en archivos HTML.

```bash
python3 scripts/check_links.py
```

**Validaciones:**
- 🔗 Enlaces internos (rutas relativas y absolutas)
- 📧 Enlaces de email (mailto:)
- 📱 Enlaces telefónicos (tel:)
- 🌐 Enlaces externos (reportados, no validados)

**Códigos de salida:**
- `0` - Todos los enlaces válidos
- `1` - Enlaces rotos encontrados

---

### 5. `update_lastmod.py`
Actualiza fechas `<lastmod>` en sitemap.xml basándose en modificación de archivos.

```bash
python3 scripts/update_lastmod.py
```

**Funcionalidad:**
- Lee sitemap.xml existente
- Obtiene fecha de modificación real de cada archivo
- Actualiza tags `<lastmod>`
- Mantiene formato XML válido

---

### 6. `deploy.py`
Script de despliegue automatizado con validaciones pre-deploy.

```bash
python3 scripts/deploy.py
```

**Validaciones pre-deploy:**
- ✅ Git status (sin cambios sin commitear)
- ✅ Sitemap válido
- ✅ CNAME correcto

**Acciones:**
- Push a GitHub (rama main)
- Verificación de accesibilidad del sitio

---

## 🔄 Flujo de Trabajo Recomendado

### Desarrollo Diario
```bash
# 1. Verificar schemas
python3 scripts/validate_schemas.py

# 2. Verificar links
python3 scripts/check_links.py

# 3. Actualizar sitemap
python3 scripts/generate_sitemap.py
python3 scripts/update_lastmod.py
```

### Antes de Deploy
```bash
# Validación completa
python3 scripts/validate_schemas.py && \
python3 scripts/check_links.py && \
python3 scripts/deploy.py
```

### Optimización de Imágenes
```bash
# Solo cuando agregues nuevas imágenes
python3 scripts/optimize_images.py
```

---

## 🛠️ Requisitos

### Python 3.7+
Todos los scripts requieren Python 3.7 o superior.

```bash
python3 --version
```

### Dependencias del Sistema

**xmllint** (para validación XML):
```bash
# macOS (usualmente pre-instalado)
# Viene con Xcode Command Line Tools

# Linux
sudo apt-get install libxml2-utils
```

**cwebp** (para optimización de imágenes):
```bash
# macOS
brew install webp

# Linux
sudo apt-get install webp
```

---

## 📊 Integración con CI/CD

Estos scripts se usan en los workflows de GitHub Actions:

- `.github/workflows/validate-site.yml` - Usa `validate_schemas.py`, `check_links.py`
- `.github/workflows/seo-check.yml` - Validaciones SEO semanales
- `.github/workflows/deploy.yml` - Deploy automatizado

---

## 🐛 Troubleshooting

### Error: "cwebp not found"
```bash
brew install webp
```

### Error: "xmllint not found"
```bash
xcode-select --install
```

### Error: "Permission denied"
```bash
chmod +x scripts/*.py
```

### Sitemap no se genera
Verifica que estés en la raíz del proyecto:
```bash
cd /path/to/electricista-culiacan-pro
python3 scripts/generate_sitemap.py
```

---

## 📝 Notas

- Todos los scripts están diseñados para ejecutarse desde la **raíz del proyecto**
- Los scripts son **idempotentes**: pueden ejecutarse múltiples veces sin efectos secundarios
- Los archivos en carpetas ocultas (`.git`, `.github`) son ignorados automáticamente
- Las validaciones siguen las reglas de `formatoparacrearurlelectricidad.md`

---

## 🤝 Contribuir

Para mejorar estos scripts:

1. Mantén compatibilidad con Python 3.7+
2. Usa type hints cuando sea posible
3. Incluye manejo de errores robusto
4. Actualiza este README con cambios

---

**Última actualización:** 2025-11-22
**Proyecto:** Electricista Culiacán Pro
**Sitio:** https://electricistaculiacanpro.mx
