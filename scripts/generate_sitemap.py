#!/usr/bin/env python3
"""
Generate sitemap.xml automatically from HTML files
Electricista Culiacán Pro - Sitemap Generator
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from xml.dom import minidom

# Configuration
BASE_URL = "https://electricistaculiacanpro.mx"
TODAY = datetime.now().strftime("%Y-%m-%d")

# Priority mapping
PRIORITIES = {
    "/": 1.0,
    "/contacto/": 0.8,
    "/colonias/": 0.9,
    "/servicios/": 0.9,
}

# Change frequency mapping
CHANGEFREQ = {
    "/": "weekly",
    "/colonias/": "weekly",
    "/servicios/": "monthly",
    "/contacto/": "monthly",
}


def find_html_files():
    """Find all index.html files in the project"""
    html_files = []
    for root, dirs, files in os.walk("."):
        # Skip hidden directories and common excludes
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ["node_modules", "dist", "build"]]

        if "index.html" in files:
            # Convert path to URL format
            path = root.replace("./", "/").replace("\\", "/")
            if path == "/":
                url_path = "/"
            else:
                url_path = path + "/" if not path.endswith("/") else path
            html_files.append(url_path)

    return sorted(html_files)


def get_priority(url_path):
    """Get priority for a URL path"""
    if url_path in PRIORITIES:
        return PRIORITIES[url_path]

    # Default priorities by section
    if url_path.startswith("/servicios/"):
        return 0.9
    elif url_path.startswith("/colonias/"):
        return 0.7 if url_path != "/colonias/" else 0.9
    else:
        return 0.5


def get_changefreq(url_path):
    """Get change frequency for a URL path"""
    if url_path in CHANGEFREQ:
        return CHANGEFREQ[url_path]

    # Default change frequency
    return "monthly"


def create_sitemap(html_files):
    """Create sitemap XML from HTML files"""
    # Create root element with namespaces
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    urlset.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    urlset.set("xsi:schemaLocation",
               "http://www.sitemaps.org/schemas/sitemap/0.9 "
               "http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd")

    # Add comment
    comment = ET.Comment(" Generated automatically by generate_sitemap.py ")
    urlset.append(comment)

    for path in html_files:
        url = ET.SubElement(urlset, "url")

        loc = ET.SubElement(url, "loc")
        loc.text = BASE_URL + path

        lastmod = ET.SubElement(url, "lastmod")
        lastmod.text = TODAY

        changefreq = ET.SubElement(url, "changefreq")
        changefreq.text = get_changefreq(path)

        priority = ET.SubElement(url, "priority")
        priority.text = str(get_priority(path))

    return urlset


def prettify_xml(elem):
    """Return a pretty-printed XML string"""
    rough_string = ET.tostring(elem, encoding='utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ", encoding='UTF-8').decode('utf-8')


def main():
    """Main execution"""
    print("🗺️  Generating sitemap.xml for Electricista Culiacán Pro...")

    # Find all HTML files
    html_files = find_html_files()
    print(f"📄 Found {len(html_files)} HTML pages")

    # Create sitemap
    sitemap = create_sitemap(html_files)

    # Generate pretty XML
    xml_content = prettify_xml(sitemap)

    # Fix XML declaration (minidom adds extra line)
    xml_content = xml_content.replace('<?xml version="1.0" ?>\n',
                                      '<?xml version="1.0" encoding="UTF-8"?>\n')

    # Write to file
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)

    print(f"✅ sitemap.xml generated with {len(html_files)} URLs")
    print(f"📅 Last modified: {TODAY}")

    # Show summary by section
    sections = {}
    for path in html_files:
        section = path.split('/')[1] if len(path.split('/')) > 1 and path != "/" else "root"
        sections[section] = sections.get(section, 0) + 1

    print("\n📊 URLs by section:")
    for section, count in sorted(sections.items()):
        print(f"   {section}: {count}")


if __name__ == "__main__":
    main()
