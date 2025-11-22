#!/bin/bash

# Script para importar y optimizar imágenes de Downloads
# Electricista Culiacán Pro

echo "🖼️  IMPORTADOR Y OPTIMIZADOR DE IMÁGENES"
echo "=========================================="
echo ""

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Directorios
DOWNLOADS_DIR="$HOME/Downloads"
PROJECT_DIR="/Users/hectorpc/Documents/Hector Palazuelos/Google My Business/electricista culiacan pro"
ORIGINALES_DIR="$PROJECT_DIR/assets/images/originales"
OPTIMIZADAS_DIR="$PROJECT_DIR/assets/images/optimizadas"

# Crear directorios si no existen
mkdir -p "$ORIGINALES_DIR"
mkdir -p "$OPTIMIZADAS_DIR"

echo -e "${BLUE}📂 Buscando imágenes de hoy en Downloads...${NC}"
echo ""

# Buscar imágenes descargadas hoy
images=($(find "$DOWNLOADS_DIR" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" \) -mtime -1 | sort))

if [ ${#images[@]} -eq 0 ]; then
    echo -e "${RED}❌ No se encontraron imágenes descargadas hoy${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Encontradas ${#images[@]} imágenes${NC}"
echo ""

# Mostrar imágenes encontradas
echo -e "${YELLOW}Imágenes a procesar:${NC}"
for i in "${!images[@]}"; do
    filename=$(basename "${images[$i]}")
    echo "  $((i+1)). $filename"
done
echo ""

# Menú interactivo para renombrar
echo -e "${BLUE}🏷️  Asignar nombres a las imágenes${NC}"
echo ""
echo "Tipos de imagen sugeridos:"
echo "  1) hero - Imagen principal del sitio"
echo "  2) instalacion-electrica - Servicio de instalación"
echo "  3) reparacion-cortocircuitos - Servicio de reparación"
echo "  4) instalacion-contactos - Instalación de contactos/apagadores"
echo "  5) iluminacion-led - Instalación de lámparas/iluminación"
echo "  6) tableros-electricos - Mantenimiento de tableros"
echo "  7) emergencia-electrica - Servicio de emergencia"
echo "  8) electricista-trabajo - Electricista trabajando (genérico)"
echo "  9) equipo-herramientas - Herramientas y equipo"
echo "  10) personalizado - Escribir nombre custom"
echo ""

declare -A image_names

for i in "${!images[@]}"; do
    img="${images[$i]}"
    filename=$(basename "$img")

    echo -e "${YELLOW}────────────────────────────────────────${NC}"
    echo -e "Imagen $((i+1)) de ${#images[@]}: ${BLUE}$filename${NC}"
    echo ""
    read -p "Tipo de imagen (1-10) [Enter para saltar]: " tipo

    case $tipo in
        1) name="hero-electricista-culiacan" ;;
        2) name="instalacion-electrica-culiacan" ;;
        3) name="reparacion-cortocircuitos-culiacan" ;;
        4) name="instalacion-contactos-culiacan" ;;
        5) name="iluminacion-led-culiacan" ;;
        6) name="tableros-electricos-culiacan" ;;
        7) name="emergencia-electrica-culiacan" ;;
        8) name="electricista-trabajo-culiacan" ;;
        9) name="equipo-herramientas-electricista" ;;
        10)
            read -p "Nombre personalizado: " custom_name
            name="${custom_name}-culiacan"
            ;;
        *)
            echo -e "${YELLOW}⊘ Imagen saltada${NC}"
            continue
            ;;
    esac

    # Si ya existe el nombre, agregar número
    if [[ -n "${image_names[$name]}" ]]; then
        counter=2
        while [[ -n "${image_names[${name}-${counter}]}" ]]; do
            ((counter++))
        done
        name="${name}-${counter}"
    fi

    image_names[$name]="$img"
    echo -e "${GREEN}✓ Asignado: $name${NC}"
    echo ""
done

echo ""
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo -e "${GREEN}📋 RESUMEN DE IMÁGENES A PROCESAR${NC}"
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo ""

if [ ${#image_names[@]} -eq 0 ]; then
    echo -e "${RED}❌ No se seleccionaron imágenes${NC}"
    exit 0
fi

for name in "${!image_names[@]}"; do
    echo -e "  ${GREEN}✓${NC} $name"
done

echo ""
read -p "¿Proceder con la optimización? (s/n): " confirm

if [[ $confirm != "s" && $confirm != "S" ]]; then
    echo "❌ Cancelado"
    exit 0
fi

echo ""
echo -e "${BLUE}🚀 Iniciando proceso de optimización...${NC}"
echo ""

# Procesar cada imagen
count=0
for name in "${!image_names[@]}"; do
    img="${image_names[$name]}"
    ext="${img##*.}"

    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Procesando: $name${NC}"
    echo ""

    # 1. Copiar original
    cp "$img" "$ORIGINALES_DIR/${name}.${ext}"
    echo -e "  ${GREEN}✓${NC} Copiado a originales/"

    # 2. Determinar si es hero o servicio
    if [[ $name == *"hero"* ]]; then
        sizes=(1200 800 420)
        qualities=(85 85 80)
        echo "  → Tipo: HERO (3 tamaños)"
    else
        sizes=(800 420)
        qualities=(85 80)
        echo "  → Tipo: SERVICIO (2 tamaños)"
    fi

    # 3. Optimizar a WebP en diferentes tamaños
    for i in "${!sizes[@]}"; do
        size=${sizes[$i]}
        quality=${qualities[$i]}
        output="$OPTIMIZADAS_DIR/${name}-${size}w.webp"

        cwebp -q $quality -resize $size 0 "$img" -o "$output" 2>/dev/null

        if [ $? -eq 0 ]; then
            filesize=$(du -h "$output" | cut -f1)
            echo -e "  ${GREEN}✓${NC} ${size}w.webp (${filesize}) - calidad ${quality}%"
        else
            echo -e "  ${RED}✗${NC} Error generando ${size}w"
        fi
    done

    echo ""
    ((count++))
done

echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo -e "${GREEN}✅ ¡OPTIMIZACIÓN COMPLETADA!${NC}"
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo ""

echo "📊 Estadísticas:"
echo "  • Imágenes procesadas: $count"
echo "  • Originales guardadas en: assets/images/originales/"
echo "  • Optimizadas guardadas en: assets/images/optimizadas/"
echo ""

# Tamaños
original_size=$(du -sh "$ORIGINALES_DIR" | cut -f1)
optimized_size=$(du -sh "$OPTIMIZADAS_DIR" | cut -f1)

echo "💾 Tamaños:"
echo "  • Originales: $original_size"
echo "  • Optimizadas: $optimized_size"
echo ""

echo -e "${BLUE}📄 Archivos generados:${NC}"
ls -lh "$OPTIMIZADAS_DIR/" | grep -v "^total" | tail -20 | awk '{printf "  %s  %s\n", $5, $9}'

echo ""
echo -e "${GREEN}🎉 ¡Listo para usar en el sitio web!${NC}"
echo ""
echo "💡 Próximo paso: Actualizar el HTML para usar estas imágenes"
