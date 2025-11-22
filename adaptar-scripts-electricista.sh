#!/bin/bash

# Script para adaptar todos los scripts de plomero a electricista
# Reemplaza terminología y URLs

echo "🔧 ADAPTADOR DE SCRIPTS: Plomero → Electricista"
echo "================================================"
echo ""

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

count=0

echo -e "${BLUE}📝 Adaptando scripts Python...${NC}"
echo ""

# Adaptar scripts Python
for script in scripts/automation/*.py; do
    if [ -f "$script" ]; then
        filename=$(basename "$script")
        echo -e "  Procesando: ${YELLOW}$filename${NC}"

        # Reemplazos de terminología
        sed -i '' 's/plomero/electricista/g' "$script"
        sed -i '' 's/Plomero/Electricista/g' "$script"
        sed -i '' 's/PLOMERO/ELECTRICISTA/g' "$script"
        sed -i '' 's/plomería/electricidad/g' "$script"
        sed -i '' 's/Plomería/Electricidad/g' "$script"

        # Reemplazos de URLs
        sed -i '' 's/plomeroculiacanpro\.mx/electricistaculiacanpro.mx/g' "$script"

        # Reemplazos de servicios específicos
        sed -i '' 's/destape de drenajes/instalación eléctrica/g' "$script"
        sed -i '' 's/Destape de Drenajes/Instalación Eléctrica/g' "$script"
        sed -i '' 's/reparación de fugas/reparación de cortocircuitos/g' "$script"
        sed -i '' 's/Reparación de Fugas/Reparación de Cortocircuitos/g' "$script"
        sed -i '' 's/detección de fugas/detección de fallas eléctricas/g' "$script"
        sed -i '' 's/Detección de Fugas/Detección de Fallas Eléctricas/g' "$script"
        sed -i '' 's/instalación de sanitarios/instalación de contactos/g' "$script"
        sed -i '' 's/Instalación de Sanitarios/Instalación de Contactos/g' "$script"
        sed -i '' 's/mantenimiento de boiler/mantenimiento de tableros/g' "$script"
        sed -i '' 's/Mantenimiento de Boiler/Mantenimiento de Tableros/g' "$script"

        # Schema.org type
        sed -i '' 's/Plumber/Electrician/g' "$script"
        sed -i '' 's/"@type": "HomeAndConstructionBusiness"/"@type": "Electrician"/g' "$script"

        echo -e "  ${GREEN}✓${NC} Adaptado"
        ((count++))
    fi
done

echo ""
echo -e "${BLUE}📜 Adaptando scripts Bash...${NC}"
echo ""

# Adaptar scripts Bash
for script in *.sh; do
    # Saltar el script actual
    if [[ "$script" == "adaptar-scripts-electricista.sh" ]]; then
        continue
    fi

    # Saltar scripts de optimización de imágenes
    if [[ "$script" == *"optimizar"* ]]; then
        continue
    fi

    if [ -f "$script" ]; then
        filename=$(basename "$script")
        echo -e "  Procesando: ${YELLOW}$filename${NC}"

        # Reemplazos de terminología
        sed -i '' 's/plomero/electricista/g' "$script"
        sed -i '' 's/Plomero/Electricista/g' "$script"
        sed -i '' 's/PLOMERO/ELECTRICISTA/g' "$script"
        sed -i '' 's/plomería/electricidad/g' "$script"
        sed -i '' 's/Plomería/Electricidad/g' "$script"

        # Reemplazos de URLs
        sed -i '' 's/plomeroculiacanpro\.mx/electricistaculiacanpro.mx/g' "$script"

        echo -e "  ${GREEN}✓${NC} Adaptado"
        ((count++))
    fi
done

echo ""
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo -e "${GREEN}✅ ADAPTACIÓN COMPLETADA${NC}"
echo -e "${BLUE}═══════════════════════════════════════${NC}"
echo ""
echo "📊 Estadísticas:"
echo -e "  • Scripts adaptados: ${GREEN}$count${NC}"
echo ""
echo "🔍 Cambios realizados:"
echo "  ✓ plomero → electricista"
echo "  ✓ plomería → electricidad"
echo "  ✓ URLs actualizadas"
echo "  ✓ Schema.org: Plumber → Electrician"
echo "  ✓ Servicios específicos adaptados"
echo ""
echo -e "${GREEN}🎉 Scripts listos para usar!${NC}"
echo ""
echo "💡 Próximo paso:"
echo "   Crear template de página de colonia y generar las 17 páginas"
