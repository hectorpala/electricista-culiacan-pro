#!/usr/bin/env python3
"""
Batch fix: aplica los 17 fixes HTML+SEO a todas las paginas de colonias.
Mismo resultado que los subagentes Bug Hunter + SEO Auditor + Fixer HTML + Fixer SEO.
"""
import os, re, json, sys

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    'servicios', 'electricista-colonias-culiacan')

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

def extract_colony_name(content):
    m = re.search(r'<title>Electricista en ([^,<]+),\s*Culiac', content)
    return m.group(1).strip() if m else None

def is_already_fixed(content):
    return 'application/ld+json' in content

def get_nearby(current_slug):
    result = []
    for slug, name in POPULAR:
        if slug != current_slug and len(result) < 4:
            result.append((slug, name))
    return result

def fix_file(filepath, slug, dry_run=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    colony = extract_colony_name(content)
    if not colony:
        return 'SKIP_NO_NAME', slug, None

    if is_already_fixed(content):
        return 'SKIP_DONE', slug, colony

    original = content

    # HTML FIX 1: rel="noopener" en WhatsApp CTA
    content = content.replace(
        'target="_blank">WhatsApp</a>',
        'target="_blank" rel="noopener">WhatsApp</a>')

    # HTML FIX 2: rel="noopener" en WhatsApp flotante
    content = content.replace(
        'floating-whatsapp" target="_blank"',
        'floating-whatsapp" target="_blank" rel="noopener"')

    # HTML FIX 3: tel:+52
    content = content.replace(
        'href="tel:6673922273" class="btn-secondary"',
        'href="tel:+526673922273" class="btn-secondary"')

    # HTML FIX 4: main.min.js
    if 'main.min.js' not in content:
        content = content.replace('</body>',
            '<script src="../../../main.min.js" defer></script></body>')

    # HTML FIX 5: Nav 3->5 links + id
    content = content.replace(
        '<ul class="nav-menu"><li><a href="/" class="nav-link">Inicio</a></li><li><a href="/#servicios" class="nav-link">Servicios</a></li><li><a href="/#contacto" class="nav-link">Contacto</a></li></ul>',
        '<ul class="nav-menu" id="nav-menu"><li><a href="/" class="nav-link">Inicio</a></li><li><a href="/#servicios" class="nav-link">Servicios</a></li><li><a href="/#sobre-nosotros" class="nav-link">Sobre Nosotros</a></li><li><a href="/blog/" class="nav-link">Blog</a></li><li><a href="/#contacto" class="nav-link">Contacto</a></li></ul>')

    # HTML FIX 6: z-index 60->90
    content = content.replace('z-index:60', 'z-index:90')

    # HTML FIX 7: aria mejorado
    content = content.replace(
        'aria-label="Menu"',
        'aria-label="Abrir menu de navegacion" aria-expanded="false" aria-controls="nav-menu"')

    # SEO FIX 1: Title con telefono
    content = content.replace(
        '<title>Electricista en %s, Culiac\u00e1n | 24/7</title>' % colony,
        '<title>Electricista en %s, Culiac\u00e1n | 24/7 | 667 392 2273</title>' % colony)

    # SEO FIX 2: Meta description con CTA
    old_desc = 'Electricista profesional en %s, Culiac\u00e1n \u00b7 Emergencia 24/7 \u00b7 Llegada 20-30 min \u00b7 Cotizaci\u00f3n gratis WhatsApp \u00b7 4.8\u2605' % colony
    new_desc = 'Electricista profesional en %s, Culiac\u00e1n. Emergencias 24/7 con llegada en 20-30 min. Cotizaci\u00f3n gratis por WhatsApp. Llama al 667 392 2273. \u26054.8 en rese\u00f1as.' % colony
    content = content.replace(old_desc, new_desc)

    # SEO FIX 3: og:url + og:image
    content = content.replace(
        'og:locale" content="es_MX">',
        'og:locale" content="es_MX"><meta property="og:url" content="https://electricistaculiacanpro.mx/servicios/electricista-colonias-culiacan/%s/"><meta property="og:image" content="https://electricistaculiacanpro.mx/assets/images/optimizadas/hero-electricista-culiacan-800w.webp">' % slug)

    # SEO FIX 4: Schema JSON-LD
    schema = json.dumps({"@context":"https://schema.org","@graph":[
        {"@type":"Electrician",
         "name":"Electricista Culiac\u00e1n Pro - %s" % colony,
         "url":"https://electricistaculiacanpro.mx/servicios/electricista-colonias-culiacan/%s/" % slug,
         "telephone":"+526673922273",
         "address":{"@type":"PostalAddress","addressLocality":"Culiac\u00e1n","addressRegion":"Sinaloa","addressCountry":"MX"},
         "areaServed":{"@type":"Place","name":"%s, Culiac\u00e1n" % colony},
         "openingHoursSpecification":{"@type":"OpeningHoursSpecification",
            "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            "opens":"00:00","closes":"23:59"},
         "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"150"}},
        {"@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":"Inicio","item":"https://electricistaculiacanpro.mx/"},
            {"@type":"ListItem","position":2,"name":"Colonias","item":"https://electricistaculiacanpro.mx/servicios/electricista-colonias-culiacan/"},
            {"@type":"ListItem","position":3,"name":colony}]}
    ]}, ensure_ascii=False)
    content = content.replace('</head>', '<script type="application/ld+json">%s</script>\n</head>' % schema)

    # SEO FIX 5: H2 Cobertura
    content = content.replace('<h2>Cobertura</h2>', '<h2>Cobertura en %s, Culiac\u00e1n</h2>' % colony)

    # SEO FIX 6: H2 Testimonios
    content = content.replace('<h2>Testimonios</h2>', '<h2>Testimonios de Clientes en %s</h2>' % colony)

    # SEO FIX 7: H2 CTA
    content = content.replace('<h2>\u00bfNecesitas Electricista?</h2>', '<h2>\u00bfNecesitas Electricista en %s?</h2>' % colony)

    # SEO FIX 8: Alt text
    content = content.replace(
        'alt="Electricista en %s"' % colony,
        'alt="Electricista profesional en %s, Culiac\u00e1n - servicio de emergencia 24/7"' % colony)

    # SEO FIX 9: Interlinking
    nearby = get_nearby(slug)
    links_html = ''.join('<li><a href="/servicios/electricista-colonias-culiacan/%s/">%s</a></li>' % (s, n) for s, n in nearby)
    interlink = (
        '<section class="section"><div class="container">'
        '<h2>Servicios El\u00e9ctricos en %s</h2>' % colony +
        '<div class="services-grid">'
        '<div class="service-card"><h3>Instalaci\u00f3n El\u00e9ctrica</h3><p><a href="/servicios/instalacion-electrica/">Instalaci\u00f3n el\u00e9ctrica profesional</a> en %s.</p></div>' % colony +
        '<div class="service-card"><h3>Reparaci\u00f3n de Cortocircuitos</h3><p><a href="/servicios/reparacion-cortocircuitos/">Reparaci\u00f3n de cortocircuitos</a> con diagn\u00f3stico gratuito.</p></div>'
        '<div class="service-card"><h3>Electricista a Domicilio</h3><p><a href="/servicios/electricista-a-domicilio/">Electricista a domicilio</a> en tu colonia.</p></div>'
        '</div>'
        '<h2>Colonias Cercanas a %s</h2>' % colony +
        '<ul class="colonias-links">%s</ul>' % links_html +
        '</div></section></main>')
    content = content.replace('</main>', interlink)

    # SEO FIX 10: Footer
    content = content.replace(
        '<footer class="footer"><div class="container"><p>\u00a9 2025 Electricista Culiac\u00e1n Pro</p></div></footer>',
        '<footer class="footer"><div class="container"><p>&copy; 2026 Electricista Culiac\u00e1n Pro. Todos los derechos reservados. | <a href="/terminos/" style="color:inherit;text-decoration:underline">T\u00e9rminos</a></p></div></footer>')

    if content == original:
        return 'SKIP_NO_CHANGE', slug, colony

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return 'FIXED', slug, colony


def main():
    dry_run = '--dry-run' in sys.argv
    limit = None
    for arg in sys.argv[1:]:
        if arg.isdigit():
            limit = int(arg)

    fixed, skipped_done, skipped_other = 0, 0, 0
    results = []

    dirs = sorted(os.listdir(BASE))
    for d in dirs:
        filepath = os.path.join(BASE, d, 'index.html')
        if not os.path.isfile(filepath):
            continue

        if limit and fixed >= limit:
            break

        status, slug, colony = fix_file(filepath, d, dry_run)

        if status == 'FIXED':
            fixed += 1
            results.append('  FIXED: %s (%s)' % (slug, colony))
        elif status == 'SKIP_DONE':
            skipped_done += 1
        elif status == 'SKIP_NO_NAME':
            skipped_other += 1
            results.append('  SKIP: %s (no colony name found)' % slug)
        elif status == 'SKIP_NO_CHANGE':
            skipped_other += 1
            results.append('  SKIP: %s (no patterns matched)' % slug)

    mode = 'DRY RUN' if dry_run else 'APPLIED'
    print('\n=== BATCH FIX COLONIAS (%s) ===' % mode)
    print('Fixed:          %d' % fixed)
    print('Already done:   %d' % skipped_done)
    print('Skipped/other:  %d' % skipped_other)
    print('Total scanned:  %d' % (fixed + skipped_done + skipped_other))
    if results:
        print('\nDetails:')
        for r in results:
            print(r)


if __name__ == '__main__':
    main()
