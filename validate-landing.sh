#!/bin/bash
# validate-landing.sh - Valida que una landing page de servicios
# cumpla con la estructura del template v2.0.0 (referencia: ventiladores-techo)
# Uso: ./validate-landing.sh servicios/[slug]/index.html

FILE="$1"
ERRORS=0
WARNINGS=0

if [ -z "$FILE" ]; then
    echo "Uso: ./validate-landing.sh <ruta-a-index.html>"
    exit 1
fi

if [ ! -f "$FILE" ]; then
    echo "ERROR: Archivo no encontrado: $FILE"
    exit 1
fi

CONTENT=$(cat "$FILE")

pass() {
    echo "  OK  $1"
}

fail() {
    echo "  FAIL  $1"
    ERRORS=$((ERRORS + 1))
}

warn() {
    echo "  WARN  $1"
    WARNINGS=$((WARNINGS + 1))
}

echo "Validando: $FILE"
echo "-------------------------------------------"

# 1. Security Headers
if echo "$CONTENT" | grep -q 'X-Content-Type-Options' && \
   echo "$CONTENT" | grep -q 'X-Frame-Options' && \
   echo "$CONTENT" | grep -q 'X-XSS-Protection'; then
    pass "Security headers (X-Content-Type, X-Frame, X-XSS)"
else
    fail "Faltan security headers (X-Content-Type-Options, X-Frame-Options, X-XSS-Protection)"
fi

# 2. Robots meta
if echo "$CONTENT" | grep -q '<meta name="robots"'; then
    pass "Meta robots presente"
else
    fail "Falta <meta name=\"robots\">"
fi

# 3. Template version
if echo "$CONTENT" | grep -q 'template-version.*v2.0.0'; then
    pass "Template version v2.0.0"
else
    fail "Falta meta template-version v2.0.0"
fi

# 4. NO hero-eta-badge HTML element (CSS class is OK)
if echo "$CONTENT" | grep -q 'class="hero-eta-badge"'; then
    fail "Tiene hero-eta-badge HTML element (debe eliminarse)"
else
    pass "Sin hero-eta-badge HTML element"
fi

# 5. Footer logo pro
if echo "$CONTENT" | grep -q 'electricista-culiacan-pro-logo.webp'; then
    pass "Footer logo pro (electricista-culiacan-pro-logo.webp)"
else
    fail "Footer logo incorrecto (debe ser electricista-culiacan-pro-logo.webp)"
fi

# 6. NO CSS preload for external styles file
if echo "$CONTENT" | grep -q 'rel="preload".*styles\.' || \
   echo "$CONTENT" | grep -q 'preload.*as="style".*styles\.'; then
    fail "Tiene preload de styles externo (debe eliminarse)"
else
    pass "Sin preload de styles externo"
fi

# 7. NO meta author
if echo "$CONTENT" | grep -q '<meta name="author"'; then
    warn "Tiene meta author (no critico pero referencia no lo tiene)"
else
    pass "Sin meta author"
fi

# 8. Inline critical CSS (@font-face)
if echo "$CONTENT" | grep -q '@font-face'; then
    pass "Inline critical CSS con @font-face"
else
    fail "Falta inline critical CSS (@font-face declarations)"
fi

# 9. Montserrat 800
if echo "$CONTENT" | grep -q 'Montserrat'; then
    if echo "$CONTENT" | grep -q '800'; then
        pass "Montserrat 800 declarado"
    else
        fail "Falta font-weight 800 para Montserrat"
    fi
else
    fail "Falta Montserrat en @font-face"
fi

# 10. Hero content section
if echo "$CONTENT" | grep -q 'hero-content'; then
    pass "Hero content presente"
else
    fail "Falta .hero-content"
fi

# 11. Breadcrumb
if echo "$CONTENT" | grep -q 'BreadcrumbList' || echo "$CONTENT" | grep -q 'breadcrumb'; then
    pass "Breadcrumb presente"
else
    fail "Falta breadcrumb (schema o HTML)"
fi

# 12. Floating buttons (WhatsApp + Call)
if echo "$CONTENT" | grep -q 'floating-whatsapp' && \
   echo "$CONTENT" | grep -q 'floating-call'; then
    pass "Botones flotantes (WhatsApp + Llamar)"
else
    fail "Faltan botones flotantes (.floating-whatsapp y/o .floating-call)"
fi

# 13. Exit intent popup
if echo "$CONTENT" | grep -q 'exit-intent-popup'; then
    pass "Exit intent popup presente"
else
    fail "Falta exit-intent-popup"
fi

# 14. Deferred GTM loading
if echo "$CONTENT" | grep -q 'GTM-W75CRTX5' || echo "$CONTENT" | grep -q 'googletagmanager'; then
    pass "GTM configurado"
else
    warn "No se encontro GTM (puede estar en main.min.js)"
fi

# 15. main.min.js
if echo "$CONTENT" | grep -q 'main\.min\.js'; then
    pass "main.min.js presente"
else
    fail "Falta <script src=\"/main.min.js\" defer>"
fi

# 16. Schema JSON-LD
if echo "$CONTENT" | grep -q 'application/ld+json'; then
    pass "Schema JSON-LD presente"
else
    fail "Falta schema JSON-LD"
fi

# 17. Canonical URL
if echo "$CONTENT" | grep -q 'rel="canonical"'; then
    pass "Canonical URL presente"
else
    fail "Falta canonical URL"
fi

# 18. Open Graph tags
if echo "$CONTENT" | grep -q 'og:title' && echo "$CONTENT" | grep -q 'og:description'; then
    pass "Open Graph tags presentes"
else
    warn "Faltan Open Graph tags (og:title, og:description)"
fi

echo "-------------------------------------------"

if [ $ERRORS -gt 0 ]; then
    echo "RESULTADO: FALLO - $ERRORS errores, $WARNINGS advertencias"
    exit 1
else
    if [ $WARNINGS -gt 0 ]; then
        echo "RESULTADO: PASO con $WARNINGS advertencias"
    else
        echo "RESULTADO: PASO - Todas las validaciones OK"
    fi
    exit 0
fi
