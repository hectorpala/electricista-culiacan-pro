#!/usr/bin/env python3
"""
Script para redimensionar imágenes de service cards a 420x235px
Autor: Electricista Culiacán Pro
Fecha: 2026-02-08

Este script redimensiona las imágenes de service cards que no tienen
las dimensiones correctas (420x235px). Usa Pillow para mantener calidad.

Uso:
    python resize-service-cards.py

Imágenes a procesar:
    1. reparacion-cortocircuitos-culiacan-420w.webp (420x160 → 420x235)
    2. instalacion-contactos-culiacan-420w.webp (420x230 → 420x235)
    3. instalacion-electrica-culiacan-420w.webp (420x230 → 420x235)
"""

from PIL import Image
import os
from pathlib import Path

# Configuración
IMG_DIR = Path("assets/images/optimizadas")
TARGET_WIDTH = 420
TARGET_HEIGHT = 235
QUALITY = 85  # Calidad para webp (0-100)

# Imágenes a redimensionar con sus dimensiones actuales
IMAGES_TO_RESIZE = {
    "reparacion-cortocircuitos-culiacan-420w.webp": (420, 160),
    "instalacion-contactos-culiacan-420w.webp": (420, 230),
    "instalacion-electrica-culiacan-420w.webp": (420, 230),
}


def resize_image(image_path: Path, target_size: tuple) -> bool:
    """
    Redimensiona una imagen a las dimensiones objetivo.

    Args:
        image_path: Ruta a la imagen
        target_size: Tupla (ancho, alto) objetivo

    Returns:
        True si se redimensionó correctamente, False en caso contrario
    """
    try:
        # Abrir imagen
        img = Image.open(image_path)
        current_size = img.size

        print(f"\n📸 Procesando: {image_path.name}")
        print(f"   Tamaño actual: {current_size[0]}x{current_size[1]}")
        print(f"   Tamaño objetivo: {target_size[0]}x{target_size[1]}")

        # Redimensionar
        # LANCZOS es el mejor algoritmo para reducir tamaño manteniendo calidad
        img_resized = img.resize(target_size, Image.Resampling.LANCZOS)

        # Crear backup del original
        backup_path = image_path.with_suffix('.webp.backup')
        if not backup_path.exists():
            img.save(backup_path, 'WEBP', quality=QUALITY)
            print(f"   ✅ Backup creado: {backup_path.name}")

        # Guardar imagen redimensionada
        img_resized.save(image_path, 'WEBP', quality=QUALITY)

        # Verificar resultado
        img_check = Image.open(image_path)
        final_size = img_check.size
        img_check.close()

        if final_size == target_size:
            print(f"   ✅ Redimensionada correctamente a {final_size[0]}x{final_size[1]}")
            return True
        else:
            print(f"   ❌ Error: tamaño final {final_size[0]}x{final_size[1]} no coincide")
            return False

    except Exception as e:
        print(f"   ❌ Error al procesar {image_path.name}: {str(e)}")
        return False
    finally:
        if 'img' in locals():
            img.close()


def main():
    """Función principal"""
    print("=" * 70)
    print("🔧 REDIMENSIONADOR DE SERVICE CARDS - ELECTRICISTA CULIACÁN PRO")
    print("=" * 70)
    print(f"\nDirectorio de imágenes: {IMG_DIR}")
    print(f"Dimensión objetivo: {TARGET_WIDTH}x{TARGET_HEIGHT}px")
    print(f"Calidad WebP: {QUALITY}%")
    print(f"\nImágenes a procesar: {len(IMAGES_TO_RESIZE)}")

    # Verificar que el directorio existe
    if not IMG_DIR.exists():
        print(f"\n❌ ERROR: El directorio {IMG_DIR} no existe")
        return

    # Verificar que Pillow está instalado
    try:
        from PIL import __version__
        print(f"\n✅ Pillow version: {__version__}")
    except ImportError:
        print("\n❌ ERROR: Pillow no está instalado")
        print("   Instala con: pip install Pillow")
        return

    # Procesar cada imagen
    success_count = 0
    error_count = 0

    for filename, current_size in IMAGES_TO_RESIZE.items():
        image_path = IMG_DIR / filename

        if not image_path.exists():
            print(f"\n⚠️  Imagen no encontrada: {filename}")
            error_count += 1
            continue

        if resize_image(image_path, (TARGET_WIDTH, TARGET_HEIGHT)):
            success_count += 1
        else:
            error_count += 1

    # Resumen final
    print("\n" + "=" * 70)
    print("📊 RESUMEN")
    print("=" * 70)
    print(f"✅ Exitosas: {success_count}")
    print(f"❌ Errores: {error_count}")
    print(f"📁 Total procesadas: {success_count + error_count}")

    if success_count > 0:
        print("\n💡 SIGUIENTE PASO:")
        print("   1. Verifica visualmente las imágenes redimensionadas")
        print("   2. Prueba el homepage en navegador")
        print("   3. Si todo se ve bien, haz commit de los cambios")
        print("   4. Los backups (.webp.backup) se pueden eliminar después")

    if error_count > 0:
        print("\n⚠️  ATENCIÓN: Hubo errores. Revisa los mensajes arriba.")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
