# 🛠️ Comandos Útiles - Electricista Culiacán Pro

## 🔍 Búsqueda y Reemplazo

### Actualizar todos los números de teléfono

```bash
# Buscar todas las ocurrencias del número placeholder
grep -r "667 000 0000" .

# Reemplazar en todos los archivos HTML (macOS)
find . -name "*.html" -exec sed -i '' 's/667 000 0000/TU_NUMERO_AQUI/g' {} +

# Reemplazar en todos los archivos (Linux)
find . -name "*.html" -exec sed -i 's/667 000 0000/TU_NUMERO_AQUI/g' {} +

# Reemplazar formato internacional
find . -name "*.html" -exec sed -i '' 's/+526670000000/+52667TUNUMERO/g' {} +
```

### Actualizar emails

```bash
# Buscar emails
grep -r "contacto@electricistaculiacanpro.mx" .

# Reemplazar email
find . -name "*.html" -exec sed -i '' 's/contacto@electricistaculiacanpro.mx/TU_EMAIL@DOMINIO.com/g' {} +
```

### Actualizar dominio

```bash
# Reemplazar dominio en todos los archivos
find . -type f \( -name "*.html" -o -name "*.xml" -o -name "*.json" \) \
  -exec sed -i '' 's/electricistaculiacanpro.mx/TU-DOMINIO.com/g' {} +
```

---

## 📦 Copiar Assets desde Plomero

### Copiar fuentes

```bash
# Desde la carpeta del proyecto electricista, ejecutar:
cp "../plomero culiacan pro/assets/fonts/"*.woff2 assets/fonts/

# Verificar que se copiaron
ls -lh assets/fonts/
```

### Copiar estructura de iconos (si existen)

```bash
# Copiar iconos PWA
cp -r "../plomero culiacan pro/assets/icons/" assets/icons/

# Verificar
ls -lh assets/icons/
```

---

## 🖼️ Optimización de Imágenes

### Convertir JPG/PNG a WebP

```bash
# Instalar cwebp (macOS)
brew install webp

# Convertir una imagen
cwebp -q 85 input.jpg -o output.webp

# Convertir todas las imágenes JPG de una carpeta
for file in assets/images/*.jpg; do
  cwebp -q 85 "$file" -o "${file%.jpg}.webp"
done

# Convertir todas las PNG
for file in assets/images/*.png; do
  cwebp -q 85 "$file" -o "${file%.png}.webp"
done
```

### Optimizar WebP existentes

```bash
# Re-optimizar WebP para reducir tamaño
for file in assets/images/*.webp; do
  cwebp -q 80 "$file" -o "${file%.webp}-optimized.webp"
done
```

### Redimensionar imágenes (ImageMagick)

```bash
# Instalar ImageMagick
brew install imagemagick

# Redimensionar manteniendo aspect ratio
convert input.jpg -resize 800x600 output.jpg

# Redimensionar todas las imágenes grandes
for file in assets/images/*.jpg; do
  convert "$file" -resize 1200x1200\> "$file"
done
```

---

## 🚀 Servidor Local

### Python (simple)

```bash
# Python 3
python3 -m http.server 8000

# Abrir en navegador
open http://localhost:8000
```

### Node.js (con live reload)

```bash
# Instalar http-server globalmente
npm install -g http-server

# Ejecutar
http-server -p 8000 -o

# Con live reload (instalar live-server)
npm install -g live-server
live-server --port=8000
```

### PHP

```bash
php -S localhost:8000
```

---

## 📊 Análisis de Código

### Contar líneas de código

```bash
# Total de líneas en HTML
find . -name "*.html" | xargs wc -l

# Total de líneas en CSS
find . -name "*.css" | xargs wc -l

# Total de líneas en JS
find . -name "*.js" | xargs wc -l

# Resumen completo
echo "HTML:" && find . -name "*.html" | xargs wc -l | tail -1
echo "CSS:" && find . -name "*.css" | xargs wc -l | tail -1
echo "JS:" && find . -name "*.js" | xargs wc -l | tail -1
```

### Tamaño de archivos

```bash
# Ver tamaño de archivos principales
du -h index.html styles.css main.js

# Ver tamaño total del proyecto
du -sh .

# Ver tamaño por carpeta
du -sh */
```

---

## 🔧 Git (Control de Versiones)

### Inicializar repositorio

```bash
# Crear .gitignore
cat > .gitignore << EOF
.DS_Store
*.log
node_modules/
.env
.vscode/
*.swp
*.swo
EOF

# Inicializar git
git init

# Primer commit
git add .
git commit -m "Initial commit: Electricista Culiacán Pro website"

# Conectar con GitHub
git remote add origin https://github.com/TU_USUARIO/electricista-culiacan-pro.git
git branch -M main
git push -u origin main
```

### Comandos útiles de Git

```bash
# Ver estado
git status

# Agregar cambios
git add .

# Commit
git commit -m "Descripción de los cambios"

# Subir cambios
git push

# Ver historial
git log --oneline

# Crear rama
git checkout -b nueva-funcionalidad

# Cambiar de rama
git checkout main
```

---

## 🌐 Deployment

### GitHub Pages

```bash
# Asegurarse de estar en main
git checkout main

# Crear rama gh-pages
git checkout -b gh-pages

# Subir a GitHub
git push origin gh-pages

# El sitio estará en:
# https://TU_USUARIO.github.io/electricista-culiacan-pro/
```

### Netlify CLI

```bash
# Instalar Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
netlify deploy

# Deploy a producción
netlify deploy --prod
```

### Vercel

```bash
# Instalar Vercel CLI
npm install -g vercel

# Deploy
vercel

# Deploy a producción
vercel --prod
```

---

## 🧪 Testing y Validación

### Validar HTML

```bash
# Usar validador online desde CLI
curl -H "Content-Type: text/html; charset=utf-8" \
  --data-binary @index.html \
  https://validator.w3.org/nu/?out=gnu
```

### Validar CSS

```bash
# Validar CSS
curl -H "Content-Type: text/css; charset=utf-8" \
  --data-binary @styles.css \
  https://jigsaw.w3.org/css-validator/validator
```

### Lighthouse CLI

```bash
# Instalar Lighthouse
npm install -g lighthouse

# Ejecutar audit
lighthouse http://localhost:8000 --view

# Solo performance
lighthouse http://localhost:8000 --only-categories=performance --view

# Guardar reporte
lighthouse http://localhost:8000 --output=html --output-path=./lighthouse-report.html
```

---

## 🔍 SEO Tools

### Generar sitemap automáticamente

```bash
# Usando find para listar todas las páginas HTML
find . -name "*.html" -not -path "*/\.*" | while read file; do
  url=$(echo "$file" | sed 's|^\./||' | sed 's|/index\.html$|/|')
  echo "<url><loc>https://electricistaculiacanpro.mx/$url</loc></url>"
done
```

### Validar Schema.org

```bash
# Extraer JSON-LD del HTML
grep -A 100 'application/ld+json' index.html > schema.json

# Validar en línea
curl -X POST \
  -H "Content-Type: application/json" \
  -d @schema.json \
  https://validator.schema.org/
```

---

## 📱 PWA Tools

### Generar iconos PWA desde una imagen

```bash
# Instalar pwa-asset-generator
npm install -g pwa-asset-generator

# Generar todos los iconos
pwa-asset-generator logo.png assets/icons/ \
  --background "#1E40AF" \
  --manifest manifest.json

# Solo iconos, sin splash screens
pwa-asset-generator logo.png assets/icons/ \
  --icon-only \
  --background "#1E40AF"
```

---

## 🔒 Seguridad

### Verificar enlaces rotos

```bash
# Instalar broken-link-checker
npm install -g broken-link-checker

# Verificar sitio local
blc http://localhost:8000 -ro

# Verificar sitio en producción
blc https://electricistaculiacanpro.mx -ro
```

### Analizar headers de seguridad

```bash
# Ver headers del sitio
curl -I https://electricistaculiacanpro.mx

# Análisis completo
curl -s -I https://electricistaculiacanpro.mx | grep -E "X-|Content-Security"
```

---

## 🎨 Generar Paleta de Colores

### Extraer colores del CSS

```bash
# Extraer todos los colores hex
grep -Eo '#[0-9A-Fa-f]{6}' styles.css | sort -u

# Contar uso de cada color
grep -Eo '#[0-9A-Fa-f]{6}' styles.css | sort | uniq -c | sort -rn
```

---

## 📋 Backup y Limpieza

### Crear backup

```bash
# Backup comprimido con fecha
tar -czf "backup-electricista-$(date +%Y%m%d).tar.gz" \
  --exclude='.git' \
  --exclude='node_modules' \
  --exclude='.DS_Store' \
  .

# Verificar
ls -lh backup-electricista-*.tar.gz
```

### Limpiar archivos temporales

```bash
# Eliminar .DS_Store
find . -name ".DS_Store" -delete

# Eliminar archivos de respaldo de editores
find . -name "*~" -delete
find . -name "*.swp" -delete

# Ver espacio liberado
du -sh .
```

---

## 🔄 Actualización Masiva

### Actualizar copyright año

```bash
# Actualizar año en todos los archivos
find . -name "*.html" -exec sed -i '' 's/© 2024/© 2025/g' {} +
find . -name "*.html" -exec sed -i '' 's/©2024/©2025/g' {} +
```

### Cambiar versión del sitio

```bash
# Actualizar versión en manifest.json y SW
sed -i '' 's/v1.0.0/v1.1.0/g' manifest.json sw.js
```

---

## 🎯 Comandos de Producción

### Minificar CSS

```bash
# Usar csso
npm install -g csso-cli
csso styles.css -o styles.min.css

# Ver reducción de tamaño
ls -lh styles.css styles.min.css
```

### Minificar JavaScript

```bash
# Usar terser
npm install -g terser
terser main.js -c -m -o main.min.js

# Ver reducción
ls -lh main.js main.min.js
```

### Minificar HTML

```bash
# Usar html-minifier
npm install -g html-minifier
html-minifier index.html \
  --collapse-whitespace \
  --remove-comments \
  --minify-css true \
  --minify-js true \
  -o index.min.html
```

---

## 📊 Analytics de Archivos

### Ver archivos más grandes

```bash
# Top 10 archivos más grandes
find . -type f -exec du -h {} + | sort -rh | head -10

# Solo imágenes
find assets/images -type f -exec du -h {} + | sort -rh
```

### Estadísticas del proyecto

```bash
# Crear reporte completo
cat > stats.txt << EOF
=== ESTADÍSTICAS DEL PROYECTO ===
Fecha: $(date)

Archivos HTML: $(find . -name "*.html" | wc -l)
Archivos CSS: $(find . -name "*.css" | wc -l)
Archivos JS: $(find . -name "*.js" | wc -l)
Archivos JSON: $(find . -name "*.json" | wc -l)

Líneas de HTML: $(find . -name "*.html" | xargs cat | wc -l)
Líneas de CSS: $(find . -name "*.css" | xargs cat | wc -l)
Líneas de JS: $(find . -name "*.js" | xargs cat | wc -l)

Tamaño total: $(du -sh . | cut -f1)
EOF

cat stats.txt
```

---

## 💡 Tips Rápidos

```bash
# Ver sitio en tu IP local (para probar en móvil)
python3 -m http.server 8000
# Luego accede desde tu móvil a: http://TU_IP_LOCAL:8000

# Encontrar texto en todos los archivos
grep -r "texto a buscar" .

# Reemplazar texto en todos los HTML
find . -name "*.html" -exec sed -i '' 's/buscar/reemplazar/g' {} +

# Ver estructura de carpetas
ls -R

# Crear múltiples carpetas a la vez
mkdir -p servicios/{instalacion,reparacion,emergencia}
```

---

**Guarda este archivo para referencia rápida durante el desarrollo!**
