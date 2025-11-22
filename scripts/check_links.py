#!/usr/bin/env python3
"""
Check for broken links in HTML files
Electricista Culiacán Pro - Link Checker
"""

import re
from pathlib import Path
from typing import Dict, List, Set
from urllib.parse import urlparse


def find_html_files() -> List[Path]:
    """Find all HTML files"""
    html_files = list(Path(".").rglob("*.html"))
    html_files = [f for f in html_files if not any(
        part.startswith(".") for part in f.parts
    ) and "node_modules" not in f.parts]
    return sorted(html_files)


def extract_links(html_content: str, file_path: Path) -> Dict[str, List[str]]:
    """Extract all links from HTML content"""
    links = {
        "internal": [],
        "external": [],
        "anchors": [],
        "email": [],
        "tel": []
    }

    # Extract href attributes
    href_pattern = r'href=["\']([^"\']+)["\']'
    hrefs = re.findall(href_pattern, html_content)

    for href in hrefs:
        # Skip empty links
        if not href or href == "#":
            continue

        # Email links
        if href.startswith("mailto:"):
            links["email"].append(href)
        # Tel links
        elif href.startswith("tel:"):
            links["tel"].append(href)
        # Anchors
        elif href.startswith("#"):
            links["anchors"].append(href)
        # External links
        elif href.startswith("http://") or href.startswith("https://"):
            links["external"].append(href)
        # Internal links
        else:
            links["internal"].append(href)

    return links


def resolve_internal_path(link: str, from_file: Path) -> Path:
    """Resolve internal link to file path"""
    # Remove query string and anchor
    link = link.split("?")[0].split("#")[0]

    # Handle absolute paths from root
    if link.startswith("/"):
        # Remove leading slash for Path resolution
        link = link.lstrip("/")
        if link.endswith("/"):
            return Path(link) / "index.html"
        elif not link:
            return Path("index.html")
        elif not link.endswith(".html"):
            return Path(link) / "index.html"
        return Path(link)

    # Handle relative paths
    base_dir = from_file.parent
    target = base_dir / link

    if target.is_dir():
        return target / "index.html"
    elif not str(target).endswith(".html"):
        return Path(str(target) + "/index.html")

    return target


def check_internal_link(link: str, from_file: Path) -> bool:
    """Check if internal link target exists"""
    target_path = resolve_internal_path(link, from_file)
    return target_path.exists()


def main():
    """Main execution"""
    print("🔗 Checking links in HTML files...\n")

    # Find all HTML files
    html_files = find_html_files()
    print(f"📄 Found {len(html_files)} HTML files\n")

    all_broken_links = []
    all_stats = {
        "internal": 0,
        "external": 0,
        "broken": 0,
        "email": 0,
        "tel": 0
    }

    for file_path in html_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            links = extract_links(content, file_path)

            # Check internal links
            broken = []
            for link in links["internal"]:
                all_stats["internal"] += 1
                if not check_internal_link(link, file_path):
                    broken.append(link)
                    all_stats["broken"] += 1

            all_stats["external"] += len(links["external"])
            all_stats["email"] += len(links["email"])
            all_stats["tel"] += len(links["tel"])

            if broken:
                all_broken_links.append({
                    "file": file_path,
                    "broken": broken
                })
                print(f"❌ {file_path}")
                for link in broken:
                    print(f"   ⚠️  Broken link: {link}")
            else:
                print(f"✅ {file_path}")

        except Exception as e:
            print(f"⚠️  Error processing {file_path}: {e}")

    # Summary
    print("\n" + "=" * 60)
    print("📊 Link Check Summary")
    print("=" * 60)
    print(f"HTML files checked: {len(html_files)}")
    print(f"🔗 Internal links: {all_stats['internal']}")
    print(f"🌐 External links: {all_stats['external']}")
    print(f"📧 Email links: {all_stats['email']}")
    print(f"📱 Tel links: {all_stats['tel']}")
    print(f"❌ Broken links: {all_stats['broken']}")
    print("=" * 60)

    if all_broken_links:
        print("\n⚠️  Files with broken links:")
        for item in all_broken_links:
            print(f"\n{item['file']}:")
            for link in item['broken']:
                target = resolve_internal_path(link, item['file'])
                print(f"   {link} → {target} (NOT FOUND)")

        print("\n❌ Link check failed!")
        exit(1)
    else:
        print("\n🎉 All internal links are valid!")


if __name__ == "__main__":
    main()
