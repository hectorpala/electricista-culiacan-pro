#!/bin/bash

# Validador de Landing Pages v2.0.0
# Valida que la landing page use la plantilla vigente

LANDING_PATH="$1"
CONFIG_PATH="config/landing.json"
CRITICAL_CSS_PATH="assets/css/critical.css"

if [ -z "$LANDING_PATH" ]; then
    echo "❌ ERROR: Especifica la ruta de la landing"
    echo "Uso: ./validate-landing.sh servicios/[slug]/index.html"
    exit 1
fi

if [ ! -f "$LANDING_PATH" ]; then
    echo "❌ ERROR: Landing no existe: $LANDING_PATH"
    exit 1
fi

echo "🔍 Validando: $LANDING_PATH"
echo ""

# 1. Verificar que existe el config
if [ ! -f "$CONFIG_PATH" ]; then
    echo "❌ FALLA: config/landing.json no existe"
    exit 1
fi
echo "✅ Config existe: $CONFIG_PATH"

# 2. Leer versión vigente del config
VERSION_VIGENTE=$(jq -r '.version' "$CONFIG_PATH")
echo "✅ Versión vigente: $VERSION_VIGENTE"

# 3. Leer hash vigente del Critical CSS
CRITICAL_CSS_HASH_VIGENTE=$(jq -r '.styles.criticalCssHash' "$CONFIG_PATH")
echo "✅ Hash vigente Critical CSS: $CRITICAL_CSS_HASH_VIGENTE"

# 4. Calcular hash real del critical.css
if [ ! -f "$CRITICAL_CSS_PATH" ]; then
    echo "❌ FALLA: critical.css no existe"
    exit 1
fi

CRITICAL_CSS_HASH_REAL=$(md5 -q "$CRITICAL_CSS_PATH" | head -c 8)

if [ "$CRITICAL_CSS_HASH_VIGENTE" != "$CRITICAL_CSS_HASH_REAL" ]; then
    echo "❌ FALLA: Hash de critical.css NO coincide"
    echo "   Vigente: $CRITICAL_CSS_HASH_VIGENTE"
    echo "   Real:    $CRITICAL_CSS_HASH_REAL"
    exit 1
fi
echo "✅ Hash de critical.css coincide: $CRITICAL_CSS_HASH_REAL"

# 5. Verificar estructura HTML obligatoria (nav + breadcrumbs)
if ! grep -q '<nav class="nav">' "$LANDING_PATH"; then
    echo "❌ FALLA: Landing NO tiene navegación <nav class=\"nav\">"
    echo "   Toda landing v2.0.0 DEBE tener navegación completa"
    echo "   Referencia: servicios/reparacion-cortos-circuitos/index.html líneas 255-278"
    exit 1
fi
echo "✅ Navegación presente"

if ! grep -q 'class="breadcrumb-wrapper"' "$LANDING_PATH"; then
    echo "❌ FALLA: Landing NO tiene breadcrumbs"
    echo "   Toda landing v2.0.0 DEBE tener breadcrumbs HTML visibles"
    echo "   Referencia: servicios/reparacion-cortos-circuitos/index.html líneas 280-302"
    exit 1
fi
echo "✅ Breadcrumbs presentes"

# 6. Verificar que la landing usa critical.css compartido
if ! grep -q "href=\".*critical.css\"" "$LANDING_PATH"; then
    echo "❌ FALLA: Landing NO usa critical.css compartido"
    echo "   Agregar: <link rel=\"stylesheet\" href=\"../../assets/css/critical.css\" fetchpriority=\"high\">"
    exit 1
fi
echo "✅ Landing usa critical.css compartido"

# 7. Verificar versión de la landing (meta tag)
if grep -q "data-template-version=\"$VERSION_VIGENTE\"" "$LANDING_PATH"; then
    echo "✅ Landing usa versión vigente: $VERSION_VIGENTE"
else
    echo "❌ FALLA: Landing NO tiene versión vigente"
    echo "   Agregar: <meta name=\"template-version\" content=\"$VERSION_VIGENTE\" data-template-version=\"$VERSION_VIGENTE\">"
    exit 1
fi

# 8. Verificar teléfonos del config
CONFIG_PHONE=$(jq -r '.contact.whatsapp' "$CONFIG_PATH")
if ! grep -q "$CONFIG_PHONE" "$LANDING_PATH"; then
    echo "❌ FALLA: Landing NO usa teléfono del config"
    echo "   Config: $CONFIG_PHONE"
    exit 1
fi
echo "✅ Teléfono correcto: $CONFIG_PHONE"

# 9. Verificar GTM ID del config
CONFIG_GTM=$(jq -r '.tracking.googleTagManagerId' "$CONFIG_PATH")
if ! grep -q "$CONFIG_GTM" "$LANDING_PATH"; then
    echo "❌ FALLA: Landing NO usa GTM ID del config"
    echo "   Config: $CONFIG_GTM"
    exit 1
fi
echo "✅ GTM ID correcto: $CONFIG_GTM"

# 10. Verificar GA ID del config
CONFIG_GA=$(jq -r '.tracking.googleAnalyticsId' "$CONFIG_PATH")
if ! grep -q "$CONFIG_GA" "$LANDING_PATH"; then
    echo "❌ FALLA: Landing NO usa GA ID del config"
    echo "   Config: $CONFIG_GA"
    exit 1
fi
echo "✅ GA ID correcto: $CONFIG_GA"

echo ""
echo "✅ ✅ ✅ VALIDACIÓN EXITOSA"
echo "Landing $LANDING_PATH pasa todas las validaciones"
exit 0
