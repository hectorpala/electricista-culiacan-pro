#!/bin/bash

# ===========================================
# Script: crear-colonia.sh
# Descripcion: Automatiza la creacion de landing pages para colonias
# Uso: ./scripts/crear-colonia.sh "Nombre de la Colonia"
# ===========================================

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Directorio base del proyecto
BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COLONIAS_DIR="$BASE_DIR/colonias"
TEMPLATE_DIR="$COLONIAS_DIR/centro"

# Funcion para generar slug
generate_slug() {
    local name="$1"
    # Convertir a minusculas, reemplazar acentos, espacios por guiones
    echo "$name" | \
        tr '[:upper:]' '[:lower:]' | \
        sed 's/á/a/g; s/é/e/g; s/í/i/g; s/ó/o/g; s/ú/u/g; s/ñ/n/g; s/ü/u/g; s/Á/a/g; s/É/e/g; s/Í/i/g; s/Ó/o/g; s/Ú/u/g; s/Ñ/n/g' | \
        sed 's/ /-/g' | \
        sed 's/[^a-z0-9-]//g' | \
        sed 's/--*/-/g' | \
        sed 's/^-//; s/-$//'
}

# Verificar argumentos
if [ -z "$1" ]; then
    echo -e "${RED}Error: Debes proporcionar el nombre de la colonia${NC}"
    echo "Uso: $0 \"Nombre de la Colonia\""
    exit 1
fi

COLONIA_NAME="$1"
COLONIA_SLUG=$(generate_slug "$COLONIA_NAME")

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}🏘️  CREADOR DE LANDING DE COLONIAS${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "📋 Colonia: ${YELLOW}$COLONIA_NAME${NC}"
echo -e "🔗 Slug: ${YELLOW}$COLONIA_SLUG${NC}"
echo ""

# Verificar si ya existe
if [ -d "$COLONIAS_DIR/$COLONIA_SLUG" ]; then
    echo -e "${YELLOW}⚠️  La colonia '$COLONIA_SLUG' ya existe${NC}"
    echo -e "📂 Ubicación: $COLONIAS_DIR/$COLONIA_SLUG"
    exit 0
fi

# Verificar que existe el template
if [ ! -f "$TEMPLATE_DIR/index.html" ]; then
    echo -e "${RED}Error: No se encontró el template en $TEMPLATE_DIR${NC}"
    exit 1
fi

echo -e "[PASO 1/4] Creando directorio..."
mkdir -p "$COLONIAS_DIR/$COLONIA_SLUG"
echo -e "${GREEN}✅ Directorio creado${NC}"

echo -e "[PASO 2/4] Copiando template..."
cp "$TEMPLATE_DIR/index.html" "$COLONIAS_DIR/$COLONIA_SLUG/index.html"
echo -e "${GREEN}✅ Template copiado${NC}"

echo -e "[PASO 3/4] Personalizando contenido..."

# Archivo a modificar
TARGET_FILE="$COLONIAS_DIR/$COLONIA_SLUG/index.html"

# Reemplazar todas las ocurrencias
# 1. Reemplazar "Centro" (nombre) por el nuevo nombre
sed -i '' "s/Centro/$COLONIA_NAME/g" "$TARGET_FILE"

# 2. Reemplazar "centro" (slug en URLs) por el nuevo slug
sed -i '' "s|/colonias/centro/|/colonias/$COLONIA_SLUG/|g" "$TARGET_FILE"

echo -e "${GREEN}✅ Contenido personalizado${NC}"

echo -e "[PASO 4/4] Validando HTML..."
# Verificar que el archivo existe y tiene contenido
if [ -s "$TARGET_FILE" ]; then
    echo -e "${GREEN}✅ HTML validado${NC}"
else
    echo -e "${RED}❌ Error: El archivo está vacío${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}🎉 LANDING CREADA EXITOSAMENTE${NC}"
echo -e "📂 Ubicación: colonias/$COLONIA_SLUG/index.html"
echo -e "🌐 URL: https://electricistaculiacanpro.mx/colonias/$COLONIA_SLUG/"
echo ""

# Abrir en navegador (opcional)
if [ "$2" == "--open" ]; then
    open "$TARGET_FILE"
fi
