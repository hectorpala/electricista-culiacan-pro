#!/usr/bin/env python3
"""
Optimize images automatically (PNG -> WebP conversion)
Electricista Culiacán Pro - Image Optimizer
"""

import os
import subprocess
from pathlib import Path
from typing import List, Tuple


def find_images(extensions: List[str] = None) -> List[Path]:
    """Find all images in the project"""
    if extensions is None:
        extensions = [".png", ".jpg", ".jpeg"]

    images = []
    for ext in extensions:
        images.extend(Path(".").rglob(f"*{ext}"))

    # Filter out hidden directories and common excludes
    images = [img for img in images if not any(
        part.startswith(".") for part in img.parts
    ) and "node_modules" not in img.parts]

    return sorted(images)


def get_file_size(file_path: Path) -> int:
    """Get file size in bytes"""
    return file_path.stat().st_size


def format_size(size_bytes: int) -> str:
    """Format size in human-readable format"""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def convert_to_webp(input_path: Path, output_path: Path = None, quality: int = 85) -> Tuple[bool, str]:
    """Convert image to WebP format using cwebp"""
    if output_path is None:
        output_path = input_path.with_suffix(".webp")

    try:
        # Check if cwebp is available
        result = subprocess.run(
            ["cwebp", "-version"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return False, "cwebp not installed. Install with: brew install webp"

        # Convert image
        subprocess.run(
            ["cwebp", "-q", str(quality), str(input_path), "-o", str(output_path)],
            check=True,
            capture_output=True
        )

        return True, f"Converted to {output_path}"

    except subprocess.CalledProcessError as e:
        return False, f"Conversion failed: {e}"
    except FileNotFoundError:
        return False, "cwebp not found. Install with: brew install webp"


def main():
    """Main execution"""
    print("🖼️  Optimizing images for Electricista Culiacán Pro...\n")

    # Find all images
    images = find_images([".png", ".jpg", ".jpeg"])
    print(f"📄 Found {len(images)} images\n")

    if not images:
        print("No images to optimize")
        return

    total_before = 0
    total_after = 0
    converted_count = 0
    errors = []

    for img_path in images:
        # Skip if already optimized (in optimizadas folder)
        if "optimizadas" in str(img_path):
            print(f"⏭️  Skipping (already optimized): {img_path}")
            continue

        # Get original size
        original_size = get_file_size(img_path)
        total_before += original_size

        # Determine output path
        if "originales" in str(img_path):
            output_path = Path(str(img_path).replace("originales", "optimizadas")).with_suffix(".webp")
        else:
            output_path = img_path.with_suffix(".webp")

        # Create output directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Convert to WebP
        print(f"🔄 Converting: {img_path}")
        success, message = convert_to_webp(img_path, output_path, quality=85)

        if success:
            new_size = get_file_size(output_path)
            total_after += new_size
            converted_count += 1

            reduction = ((original_size - new_size) / original_size) * 100
            print(f"   ✅ {format_size(original_size)} → {format_size(new_size)} ({reduction:.1f}% reduction)")
        else:
            errors.append(f"{img_path}: {message}")
            print(f"   ❌ {message}")

    # Summary
    print("\n" + "=" * 60)
    print("📊 Optimization Summary")
    print("=" * 60)
    print(f"Images processed: {len(images)}")
    print(f"✅ Converted: {converted_count}")
    print(f"❌ Errors: {len(errors)}")

    if converted_count > 0:
        total_reduction = ((total_before - total_after) / total_before) * 100
        print(f"\n💾 Total size before: {format_size(total_before)}")
        print(f"💾 Total size after: {format_size(total_after)}")
        print(f"📉 Total reduction: {total_reduction:.1f}%")

    if errors:
        print("\n⚠️  Errors:")
        for error in errors:
            print(f"   {error}")

    print("=" * 60)

    if errors:
        print("\n⚠️  Some images failed to convert")
        print("Install webp tools with: brew install webp")
    else:
        print("\n🎉 All images optimized successfully!")


if __name__ == "__main__":
    main()
