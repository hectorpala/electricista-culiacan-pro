#!/bin/bash

# Script automático para optimizar todas las imágenes de Downloads
# Electricista Culiacán Pro

echo "🖼️  OPTIMIZADOR AUTOMÁTICO DE IMÁGENES"
echo "======================================"
echo ""

# Directorios
DOWNLOADS_DIR="$HOME/Downloads"
PROJECT_DIR="/Users/hectorpc/Documents/Hector Palazuelos/Google My Business/electricista culiacan pro"
ORIGINALES_DIR="$PROJECT_DIR/assets/images/originales"
OPTIMIZADAS_DIR="$PROJECT_DIR/assets/images/optimizadas"

# Crear directorios
mkdir -p "$ORIGINALES_DIR"
mkdir -p "$OPTIMIZADAS_DIR"

echo "📂 Buscando imágenes Gemini en Downloads..."
echo ""

# Contador
count=0
total=0

# Procesar cada imagen Gemini
for img in "$DOWNLOADS_DIR"/Gemini_Generated_Image_*.png; do
    if [ ! -f "$img" ]; then
        continue
    fi

    ((total++))
    filename=$(basename "$img")

    # Generar nombre descriptivo automático
    if [ $count -eq 0 ]; then
        name="hero-electricista-culiacan"
    elif [ $count -eq 1 ]; then
        name="instalacion-electrica-culiacan"
    elif [ $count -eq 2 ]; then
        name="reparacion-cortocircuitos-culiacan"
    elif [ $count -eq 3 ]; then
        name="instalacion-contactos-culiacan"
    elif [ $count -eq 4 ]; then
        name="iluminacion-led-culiacan"
    elif [ $count -eq 5 ]; then
        name="tableros-electricos-culiacan"
    elif [ $count -eq 6 ]; then
        name="emergencia-electrica-culiacan"
    else
        name="electricista-servicio-$count-culiacan"
    fi

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Procesando $((count+1)): $name"
    echo ""

    # Copiar original
    cp "$img" "$ORIGINALES_DIR/${name}.png"
    echo "  ✓ Original guardado"

    # Determinar tamaños según tipo
    if [ $count -eq 0 ]; then
        # Hero - 3 tamaños
        sizes="1200 800 420"
        echo "  → Tipo: HERO (3 tamaños)"
    else
        # Servicio - 2 tamaños
        sizes="800 420"
        echo "  → Tipo: SERVICIO (2 tamaños)"
    fi

    # Generar WebP optimizados
    for size in $sizes; do
        if [ $size -eq 420 ]; then
            quality=80
        else
            quality=85
        fi

        output="$OPTIMIZADAS_DIR/${name}-${size}w.webp"
        cwebp -q $quality -resize $size 0 "$img" -o "$output" 2>/dev/null

        if [ $? -eq 0 ]; then
            filesize=$(du -h "$output" | cut -f1)
            echo "  ✓ ${size}w.webp ($filesize) - calidad ${quality}%"
        fi
    done

    echo ""
    ((count++))

    # Límite de 10 imágenes para no saturar
    if [ $count -ge 10 ]; then
        break
    fi
done

echo "======================================"
echo "✅ OPTIMIZACIÓN COMPLETADA"
echo "======================================"
echo ""
echo "📊 Estadísticas:"
echo "  • Imágenes encontradas: $total"
echo "  • Imágenes procesadas: $count"
echo ""

# Tamaños
if [ $count -gt 0 ]; then
    original_size=$(du -sh "$ORIGINALES_DIR" 2>/dev/null | cut -f1)
    optimized_size=$(du -sh "$OPTIMIZADAS_DIR" 2>/dev/null | cut -f1)

    echo "💾 Espacio:"
    echo "  • Originales: ${original_size:-0}"
    echo "  • Optimizadas: ${optimized_size:-0}"
    echo ""

    echo "📄 Archivos generados:"
    ls -lh "$OPTIMIZADAS_DIR/" 2>/dev/null | grep -v "^total" | tail -20 | awk '{printf "  %s  %s\n", $5, $9}'
    echo ""
fi

echo "🎉 ¡Listo!"
echo ""
echo "📁 Ubicaciones:"
echo "  • Originales: assets/images/originales/"
echo "  • Optimizadas: assets/images/optimizadas/"
