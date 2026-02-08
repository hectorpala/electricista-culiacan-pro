#!/usr/bin/env python3
"""
Genera landing pages de colonias usando 10-de-abril como template base.
Las paginas se crean ya optimizadas con los 17 fixes HTML+SEO.

Uso:
  python3 scripts/generar-colonias-v2.py --dry-run   # Ver cuantas se crearian
  python3 scripts/generar-colonias-v2.py              # Crear todas
  python3 scripts/generar-colonias-v2.py 50           # Crear solo 50
"""
import os, json, sys, urllib.parse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
BASE = os.path.join(PROJECT_DIR, 'servicios', 'electricista-colonias-culiacan')
FALTANTES = os.path.join(PROJECT_DIR, 'colonias-faltantes.json')
TEMPLATE_DIR = os.path.join(BASE, '10-de-abril')

TEMPLATE_NAME = '10 de Abril'
TEMPLATE_SLUG = '10-de-abril'
TEMPLATE_ENCODED = '10%20de%20Abril'

POPULAR = [
    ('chapultepec', 'Chapultepec'),
    ('centro', 'Centro'),
    ('las-quintas', 'Las Quintas'),
    ('lomas-del-boulevard', 'Lomas del Boulevard'),
    ('villa-universidad', 'Villa Universidad'),
    ('bosques-del-humaya', 'Bosques del Humaya'),
    ('real-del-valle', 'Real del Valle'),
    ('country-tres-rios', 'Country Tres Rios'),
    ('guadalupe', 'Guadalupe'),
    ('la-primavera', 'La Primavera'),
]


def get_nearby(current_slug):
    result = []
    for slug, name in POPULAR:
        if slug != current_slug and len(result) < 4:
            result.append((slug, name))
    return result


def generate_page(template, nombre, slug):
    encoded = urllib.parse.quote(nombre)
    content = template

    # Replace colony name (all occurrences)
    content = content.replace(TEMPLATE_NAME, nombre)

    # Replace slug (all occurrences)
    content = content.replace(TEMPLATE_SLUG, slug)

    # Replace URL-encoded name
    content = content.replace(TEMPLATE_ENCODED, encoded)

    # Update interlinking: rebuild nearby colonies for this specific colony
    nearby = get_nearby(slug)
    old_links = (
        '<li><a href="/servicios/electricista-colonias-culiacan/chapultepec/">Chapultepec</a></li>'
        '<li><a href="/servicios/electricista-colonias-culiacan/centro/">Centro</a></li>'
        '<li><a href="/servicios/electricista-colonias-culiacan/las-quintas/">Las Quintas</a></li>'
        '<li><a href="/servicios/electricista-colonias-culiacan/lomas-del-boulevard/">Lomas del Boulevard</a></li>'
    )
    new_links = ''.join(
        '<li><a href="/servicios/electricista-colonias-culiacan/%s/">%s</a></li>' % (s, n)
        for s, n in nearby
    )
    content = content.replace(old_links, new_links)

    return content


def main():
    dry_run = '--dry-run' in sys.argv
    limit = 0
    for arg in sys.argv[1:]:
        if arg != '--dry-run' and arg.isdigit():
            limit = int(arg)

    # Read template
    template_path = os.path.join(TEMPLATE_DIR, 'index.html')
    if not os.path.exists(template_path):
        print('ERROR: Template not found: %s' % template_path)
        return

    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Read colonias faltantes
    with open(FALTANTES, 'r', encoding='utf-8') as f:
        data = json.load(f)

    colonias = data['colonias']
    created = 0
    skipped_exists = 0

    for col in colonias:
        nombre = col['nombre']
        slug = col['slug']
        dir_path = os.path.join(BASE, slug)
        file_path = os.path.join(dir_path, 'index.html')

        if os.path.exists(file_path):
            skipped_exists += 1
            continue

        if limit and created >= limit:
            break

        if not dry_run:
            os.makedirs(dir_path, exist_ok=True)
            html = generate_page(template, nombre, slug)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html)

        created += 1

    mode = 'DRY RUN' if dry_run else 'CREATED'
    print('\n=== GENERAR COLONIAS V2 (%s) ===' % mode)
    print('Created:        %d' % created)
    print('Already exist:  %d' % skipped_exists)
    print('Total in JSON:  %d' % len(colonias))


if __name__ == '__main__':
    main()
