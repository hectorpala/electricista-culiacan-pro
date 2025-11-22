#!/usr/bin/env python3
"""
Update lastmod dates in sitemap.xml based on file modification times
Electricista Culiacán Pro - Sitemap Date Updater
"""

import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from xml.dom import minidom


def get_file_mtime(url_path: str) -> str:
    """Get file modification time"""
    # Convert URL path to file path
    if url_path == "/":
        file_path = Path("index.html")
    else:
        file_path = Path(url_path.lstrip("/")) / "index.html"

    if file_path.exists():
        mtime = file_path.stat().st_mtime
        return datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    else:
        # Return today's date if file not found
        return datetime.now().strftime("%Y-%m-%d")


def update_sitemap():
    """Update lastmod dates in sitemap.xml"""
    sitemap_path = Path("sitemap.xml")

    if not sitemap_path.exists():
        print("❌ sitemap.xml not found")
        return False

    # Parse sitemap
    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    # Define namespace
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    updated_count = 0

    # Update each URL
    for url in root.findall("sm:url", ns):
        loc = url.find("sm:loc", ns)
        lastmod = url.find("sm:lastmod", ns)

        if loc is not None:
            url_path = loc.text.replace("https://electricistaculiacanpro.mx", "")
            new_date = get_file_mtime(url_path)

            if lastmod is not None:
                old_date = lastmod.text
                if old_date != new_date:
                    lastmod.text = new_date
                    updated_count += 1
                    print(f"📅 Updated {url_path}: {old_date} → {new_date}")
            else:
                # Add lastmod if missing
                lastmod = ET.SubElement(url, "lastmod")
                lastmod.text = new_date
                updated_count += 1
                print(f"➕ Added lastmod to {url_path}: {new_date}")

    # Save updated sitemap with pretty formatting
    xml_str = ET.tostring(root, encoding='utf-8')
    dom = minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="    ", encoding='UTF-8').decode('utf-8')

    # Fix XML declaration
    pretty_xml = pretty_xml.replace('<?xml version="1.0" ?>\n',
                                    '<?xml version="1.0" encoding="UTF-8"?>\n')

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

    return updated_count


def main():
    """Main execution"""
    print("📅 Updating lastmod dates in sitemap.xml...\n")

    updated_count = update_sitemap()

    if updated_count is False:
        print("\n❌ Failed to update sitemap")
        exit(1)

    print("\n" + "=" * 60)
    print("📊 Update Summary")
    print("=" * 60)
    print(f"URLs updated: {updated_count}")
    print("=" * 60)

    if updated_count > 0:
        print(f"\n✅ Updated {updated_count} lastmod dates")
    else:
        print("\n✅ All dates are up to date")


if __name__ == "__main__":
    main()
