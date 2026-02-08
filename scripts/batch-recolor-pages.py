#!/usr/bin/env python3
"""batch-recolor-pages.py - Recolor blue design to match homepage orange (#E36414)"""
import os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# All pages with blue color references (from grep audit)
PAGES = [
    'contacto/index.html',
    'gracias/index.html',
    'blog/ahorro-energia-iluminacion-led/index.html',
    'blog/cuando-llamar-electricista-emergencia/index.html',
    'blog/mantenimiento-tablero-electrico-preventivo/index.html',
    'blog/como-prevenir-cortocircuitos-casa/index.html',
    'blog/seguridad-electrica-temporada-lluvias/index.html',
    'blog/senales-instalacion-electrica-obsoleta/index.html',
    'servicios/reparacion-cortocircuitos/index.html',
    'servicios/emergencia-24-7/index.html',
    'servicios/mantenimiento-tableros/index.html',
    'servicios/instalacion-electrica/index.html',
    'servicios/instalacion-tierra-fisica/index.html',
]

DRY_RUN = '--dry-run' in sys.argv

def recolor(html):
    changes = []

    # ===== PHASE 1: Global hex color replacements =====
    hex_map = [
        ('#1E40AF', '#E36414', 'brand'),
        ('#1e40af', '#E36414', 'brand-lc'),
        ('#3B82F6', '#F97316', 'brand-light'),
        ('#3b82f6', '#F97316', 'brand-light-lc'),
        ('#1E3A8A', '#C2410C', 'brand-dark'),
        ('#1e3a8a', '#C2410C', 'brand-dark-lc'),
        ('#F0F9FF', '#FFF7ED', 'bg-soft-blue->warm'),
        ('#f0f9ff', '#FFF7ED', 'bg-soft-lc'),
    ]
    for old, new, label in hex_map:
        count = html.count(old)
        if count > 0:
            html = html.replace(old, new)
            changes.append(f"  {old} -> {new} [{label}] ({count}x)")

    # ===== PHASE 2: Nav background (inline <style> blocks) =====
    nav_bg_full = 'background:rgba(30,64,175,0.98);backdrop-filter:blur(10px);border-bottom:none;padding:16px 0;box-shadow:0 2px 12px rgba(0,0,0,0.15)'
    nav_bg_new  = 'background:transparent;border-bottom:none;padding:16px 0'
    if nav_bg_full in html:
        html = html.replace(nav_bg_full, nav_bg_new)
        changes.append("  Nav bg: solid blue -> transparent")

    # Remaining rgba(30,64,175,0.98) = mobile nav/menu -> white bg
    rgba_blue_98 = 'rgba(30,64,175,0.98)'
    count = html.count(rgba_blue_98)
    if count > 0:
        html = html.replace(rgba_blue_98, 'rgba(255,255,255,0.98)')
        changes.append(f"  rgba(30,64,175,0.98) -> white ({count}x)")

    # ===== PHASE 2b: ALL remaining rgba(30,64,175,...) patterns =====
    # Catch any box-shadow or other rgba with this blue
    rgba_blue_04 = 'rgba(30,64,175,0.4)'
    count = html.count(rgba_blue_04)
    if count > 0:
        html = html.replace(rgba_blue_04, 'rgba(227,100,20,0.28)')
        changes.append(f"  rgba(30,64,175,0.4) -> orange ({count}x)")

    rgba_blue_05 = 'rgba(30,64,175,0.5)'
    count = html.count(rgba_blue_05)
    if count > 0:
        html = html.replace(rgba_blue_05, 'rgba(227,100,20,0.35)')
        changes.append(f"  rgba(30,64,175,0.5) -> orange ({count}x)")

    # ===== PHASE 3: Nav link styles =====
    nl_old = '.nav-link{color:#fff;font-weight:500;text-decoration:none;transition:color .2s ease;padding:0.5rem 1rem;border-radius:6px}'
    nl_new = '.nav-link{color:#f97316;font-weight:500;text-decoration:none;transition:color .2s ease;text-shadow:0 2px 4px rgba(0,0,0,0.3)}'
    if nl_old in html:
        html = html.replace(nl_old, nl_new)
        changes.append("  Nav links: white -> orange + text-shadow")

    nlh_old = '.nav-link:hover{color:var(--accent);background:rgba(255,255,255,0.1)}'
    nlh_new = '.nav-link:hover{color:#ea580c;text-shadow:0 2px 6px rgba(0,0,0,0.15)}'
    if nlh_old in html:
        html = html.replace(nlh_old, nlh_new)
        changes.append("  Nav hover: accent -> orange")

    # ===== PHASE 4: Mobile menu button bars =====
    mb_old = '.mobile-menu-btn span{display:block;height:3px;width:100%;background:#fff;border-radius:2px}'
    mb_new = '.mobile-menu-btn span{display:block;height:3px;width:100%;background:#F97316;border-radius:2px;box-shadow:0 1px 2px rgba(0,0,0,0.2)}'
    if mb_old in html:
        html = html.replace(mb_old, mb_new)
        changes.append("  Menu btn bars: white -> orange")

    # ===== PHASE 5: Logo sizing to match homepage =====
    logo_old = '.logo img{height:60px;width:auto;display:block;max-height:70px}'
    logo_new = '.logo img{height:86px;width:auto;display:block;max-height:100px;mix-blend-mode:multiply}'
    if logo_old in html:
        html = html.replace(logo_old, logo_new)
        changes.append("  Logo: 60px -> 86px + mix-blend-mode")

    logo_m_old = '.logo img{height:50px;max-height:60px}'
    logo_m_new = '.logo img{height:62px;max-height:72px}'
    if logo_m_old in html:
        html = html.replace(logo_m_old, logo_m_new)
        changes.append("  Logo mobile: 50px -> 62px")

    return html, changes


# ===== MAIN =====
total = 0
for page in PAGES:
    path = os.path.join(BASE, page)
    if not os.path.exists(path):
        print(f"WARNING  NOT FOUND: {page}")
        continue

    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    new_html, changes = recolor(html)

    if changes:
        if not DRY_RUN:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_html)
        tag = "DRY" if DRY_RUN else "OK"
        print(f"[{tag}] {page} -- {len(changes)} fix(es):")
        for c in changes:
            print(c)
        total += len(changes)
    else:
        print(f"[OK ] {page} -- already orange")

print(f"\n{'[DRY RUN] ' if DRY_RUN else ''}Total: {total} fixes across {len(PAGES)} pages")
