#!/bin/bash

# Script de optimización de imágenes para Electricista Culiacán Pro
# Convierte PNG/JPG a WebP optimizado en múltiples tamaños

echo "🖼️  OPTIMIZADOR DE IMÁGENES - Electricista Culiacán Pro"
echo "======================================================"
echo ""

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Directorios
INPUT_DIR="assets/images"
OUTPUT_DIR="assets/images/optimizadas"

# Crear directorio de salida si no existe
mkdir -p "$OUTPUT_DIR"

# Contador
count=0

echo -e "${BLUE}📁 Buscando imágenes en: $INPUT_DIR${NC}"
echo ""

# Función para optimizar imagen
optimize_image() {
    local input_file="$1"
    local filename=$(basename "$input_file")
    local name="${filename%.*}"

    echo -e "${YELLOW}🔧 Procesando: $filename${NC}"

    # Hero images (1200w, 800w, 420w)
    if [[ $name == *"hero"* ]]; then
        echo "  → Detectado como HERO - generando 3 tamaños"

        # 1200w - Alta resolución
        cwebp -q 85 -resize 1200 0 "$input_file" -o "$OUTPUT_DIR/${name}-1200w.webp" 2>/dev/null
        if [ $? -eq 0 ]; then
            size=$(du -h "$OUTPUT_DIR/${name}-1200w.webp" | cut -f1)
            echo -e "  ${GREEN}✓${NC} 1200w.webp ($size)"
        fi

        # 800w - Resolución media
        cwebp -q 85 -resize 800 0 "$input_file" -o "$OUTPUT_DIR/${name}-800w.webp" 2>/dev/null
        if [ $? -eq 0 ]; then
            size=$(du -h "$OUTPUT_DIR/${name}-800w.webp" | cut -f1)
            echo -e "  ${GREEN}✓${NC} 800w.webp ($size)"
        fi

        # 420w - Móvil
        cwebp -q 80 -resize 420 0 "$input_file" -o "$OUTPUT_DIR/${name}-420w.webp" 2>/dev/null
        if [ $? -eq 0 ]; then
            size=$(du -h "$OUTPUT_DIR/${name}-420w.webp" | cut -f1)
            echo -e "  ${GREEN}✓${NC} 420w.webp ($size)"
        fi

    # Service images (800w, 420w)
    else
        echo "  → Detectado como SERVICIO - generando 2 tamaños"

        # 800w - Escritorio
        cwebp -q 85 -resize 800 0 "$input_file" -o "$OUTPUT_DIR/${name}-800w.webp" 2>/dev/null
        if [ $? -eq 0 ]; then
            size=$(du -h "$OUTPUT_DIR/${name}-800w.webp" | cut -f1)
            echo -e "  ${GREEN}✓${NC} 800w.webp ($size)"
        fi

        # 420w - Móvil
        cwebp -q 80 -resize 420 0 "$input_file" -o "$OUTPUT_DIR/${name}-420w.webp" 2>/dev/null
        if [ $? -eq 0 ]; then
            size=$(du -h "$OUTPUT_DIR/${name}-420w.webp" | cut -f1)
            echo -e "  ${GREEN}✓${NC} 420w.webp ($size)"
        fi
    fi

    echo ""
    ((count++))
}

# Procesar todas las imágenes PNG y JPG
for img in "$INPUT_DIR"/*.{png,PNG,jpg,JPG,jpeg,JPEG} 2>/dev/null; do
    if [ -f "$img" ]; then
        # Saltar si está en carpeta optimizadas
        if [[ "$img" != *"/optimizadas/"* ]]; then
            optimize_image "$img"
        fi
    fi
done

echo "======================================================"
echo -e "${GREEN}✅ Optimización completada!${NC}"
echo ""
echo "📊 Estadísticas:"
echo "  • Imágenes procesadas: $count"
echo "  • Ubicación: $OUTPUT_DIR/"
echo ""
echo "🔍 Ver resultados:"
echo "  ls -lh $OUTPUT_DIR/"
echo ""
echo "📦 Tamaños generados:"
echo "  • Hero: 1200w, 800w, 420w"
echo "  • Servicios: 800w, 420w"
echo ""

# Mostrar tamaño total
total_size=$(du -sh "$OUTPUT_DIR" | cut -f1)
echo "💾 Tamaño total optimizado: $total_size"
echo ""

# Listar archivos generados
echo -e "${BLUE}📄 Archivos generados:${NC}"
ls -lh "$OUTPUT_DIR/" | grep -v "^total" | awk '{printf "  %s  %s\n", $5, $9}'
