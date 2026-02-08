#!/usr/bin/env python3
"""
Batch fix: aplica fixes HTML+SEO a homepage, contacto, blogs y servicios.
Similar a batch-fix-colonias.py pero para las paginas principales del sitio.

Uso:
  python3 scripts/batch-fix-pages.py --dry-run   # Ver que se cambiaria
  python3 scripts/batch-fix-pages.py              # Aplicar fixes
"""
import os, re, sys

PROJECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES = [
    'index.html',
    'contacto/index.html',
    'blog/ahorro-energia-iluminacion-led/index.html',
    'blog/como-prevenir-cortocircuitos-casa/index.html',
    'blog/cuando-llamar-electricista-emergencia/index.html',
    'blog/mantenimiento-tablero-electrico-preventivo/index.html',
    'blog/seguridad-electrica-temporada-lluvias/index.html',
    'blog/senales-instalacion-electrica-obsoleta/index.html',
    'servicios/cambio-cableado-electrico/index.html',
    'servicios/electricista-a-domicilio/index.html',
    'servicios/electricista-cerca-de-mi/index.html',
    'servicios/electricista-precios/index.html',
    'servicios/electricista/index.html',
    'servicios/emergencia-24-7/index.html',
    'servicios/iluminacion-led/index.html',
    'servicios/instalacion-centro-carga/index.html',
    'servicios/instalacion-contactos/index.html',
    'servicios/instalacion-electrica/index.html',
    'servicios/instalacion-minisplit/index.html',
    'servicios/instalacion-ventiladores-techo/index.html',
]

# Target nav HTML (5 links with id)
NAV_TARGET = '<ul class="nav-menu" id="nav-menu"><li><a href="/" class="nav-link">Inicio</a></li><li><a href="/#servicios" class="nav-link">Servicios</a></li><li><a href="/#sobre-nosotros" class="nav-link">Sobre Nosotros</a></li><li><a href="/blog/" class="nav-link">Blog</a></li><li><a href="/#contacto" class="nav-link">Contacto</a></li></ul>'

# aria target
ARIA_TARGET = 'aria-label="Abrir menu de navegacion" aria-expanded="false" aria-controls="nav-menu"'


def fix_page(filepath, dry_run=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    fixes = []

    # FIX 1: rel="noopener" on all target="_blank" links that don't have it
    # Match target="_blank" NOT followed by rel="noopener"
    old_count = content.count('target="_blank"')
    noopener_count = content.count('rel="noopener"')
    if old_count > noopener_count:
        # Add rel="noopener" where missing
        content = re.sub(
            r'target="_blank"(?!\s*rel="noopener")',
            'target="_blank" rel="noopener"',
            content
        )
        new_noopener = content.count('rel="noopener"')
        if new_noopener > noopener_count:
            fixes.append('noopener: added %d' % (new_noopener - noopener_count))

    # FIX 2: tel:+52 format
    if 'tel:6673922273' in content:
        content = content.replace('tel:6673922273', 'tel:+526673922273')
        fixes.append('tel:+52 format')

    # FIX 3: z-index 50->90, 60->90 for floating buttons
    # Be careful: only change z-index in floating button styles, not nav
    # Replace z-index:60 -> z-index:90
    if 'z-index:60' in content:
        content = content.replace('z-index:60', 'z-index:90')
        fixes.append('z-index 60->90')

    # FIX 4: Nav - replace various nav patterns with standard 5-link nav
    # Pattern: <ul class="nav-menu"> ... </ul> (various contents)
    if 'id="nav-menu"' not in content:
        # Replace the nav-menu ul with standard version
        content = re.sub(
            r'<ul class="nav-menu">\s*.*?</ul>',
            NAV_TARGET,
            content,
            flags=re.DOTALL
        )
        if 'id="nav-menu"' in content:
            fixes.append('nav: 5 links + id')

    # FIX 5: aria-label on mobile menu button
    # Various patterns: aria-label="Menú", aria-label="Menu", etc.
    if 'aria-controls="nav-menu"' not in content:
        content = re.sub(
            r'aria-label="Men[uú]"',
            ARIA_TARGET,
            content
        )
        if 'aria-controls="nav-menu"' in content:
            fixes.append('aria-label improved')

    # FIX 6: Footer year 2024->2026, 2025->2026
    if '&copy; 2024' in content or '&copy; 2025' in content:
        content = content.replace('&copy; 2024', '&copy; 2026')
        content = content.replace('&copy; 2025', '&copy; 2026')
        fixes.append('footer year->2026')

    # Also fix © in JSON-LD schemas
    if '"© 2024' in content:
        content = content.replace('"© 2024', '"© 2026')
        fixes.append('schema year->2026')

    # FIX 7: Add /terminos/ link to footer if missing
    if '/terminos/' not in content:
        # Try to add terms link to footer
        content = re.sub(
            r'(<p>&copy; 2026 Electricista Culiac[aá]n Pro\.)(\s*Todos los derechos reservados\.)(</p>)',
            r'\1\2 | <a href="/terminos/" style="color:inherit;text-decoration:underline">Términos</a>\3',
            content
        )
        if '/terminos/' in content:
            fixes.append('footer: +terminos link')

    if content == original:
        return 'NO_CHANGE', fixes

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return 'FIXED', fixes


def main():
    dry_run = '--dry-run' in sys.argv
    fixed = 0
    no_change = 0
    results = []

    for page in PAGES:
        filepath = os.path.join(PROJECT, page)
        if not os.path.isfile(filepath):
            results.append('  MISSING: %s' % page)
            continue

        status, fixes = fix_page(filepath, dry_run)
        if status == 'FIXED':
            fixed += 1
            results.append('  FIXED: %s (%s)' % (page, ', '.join(fixes)))
        else:
            no_change += 1
            results.append('  OK: %s (no changes needed)' % page)

    mode = 'DRY RUN' if dry_run else 'APPLIED'
    print('\n=== BATCH FIX PAGES (%s) ===' % mode)
    print('Fixed:      %d' % fixed)
    print('No change:  %d' % no_change)
    print('Total:      %d' % len(PAGES))
    print('\nDetails:')
    for r in results:
        print(r)


if __name__ == '__main__':
    main()
