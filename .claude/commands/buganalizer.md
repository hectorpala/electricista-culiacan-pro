# buganalizer

Audita una página completa de forma top‑down y reporta todos los errores antes de corregir.

## Flujo

1) Lee estos archivos antes de auditar:
   - `.claude/commands/landing-creator.md`
   - `creadordecontenidoseo.md`
   - `config/landing.json`
2) Recorre el HTML de arriba hacia abajo (ej.: `servicios/[slug]/index.html`). Enumera cada error en orden de aparición, con línea/archivo y regla incumplida.
3) Chequeos clave:
   - Datos desde `config/landing.json`: teléfono/WhatsApp/email/IDs/coords/hero/logos (sin hardcodes).
   - CSS crítico: cargar `assets/css/critical.css`, sin bloque `<style>` inline; meta de versión vigente; hash esperado `53ef5e7f`.
   - Rutas relativas; canonical/OG por slug; `og:image` existente en assets; `theme-color` solo en meta.
   - Hero y botones flotantes con estructura y SVG correctos.
   - Accesibilidad: `alt` contextual en imágenes, `aria-current` en breadcrumb, foco visible por estilos base.
   - SEO: H1 único; jerarquía H1>H2>H3; metas en rango (px, no solo caracteres); schemas correctos por tipo (Service/LocalBusiness/FAQ/Article) y válidos en schema.org.
   - Enlaces internos: anchors descriptivos; cluster a servicios/colonias/blog; CTAs visibles con datos del config.
4) Lista de errores: severidad, regla violada, línea/archivo, arreglo propuesto.
5) Si se pide corrección: aplicar en el mismo orden enumerado y revalidar.
6) Ejecutar `./validate-landing.sh [ruta]`; si falla, corregir y repetir.
7) Entregar: lista inicial de errores, cambios aplicados (si hubo), resultado del validador.

## Prompt sugerido

```
Audita y corrige top-down esta landing: servicios/[slug]/index.html.
1) Recorre el HTML de arriba hacia abajo. Enumera cada error que halles (línea/archivo). No corrijas aún.
2) Cita la regla de .claude/commands/landing-creator.md o creadordecontenidoseo.md que se incumple.
3) Aplica las correcciones en el mismo orden enumerado.
4) Usa siempre config/landing.json para teléfonos/WhatsApp/email/IDs/coords/hero/logos.
5) Asegura: assets/css/critical.css (sin <style> inline), meta versión, hash 53ef5e7f, rutas relativas, accesibilidad mínima (alt, aria-current), canonical/OG por slug, theme-color solo en meta.
6) Corre ./validate-landing.sh servicios/[slug]/index.html y reporta el resultado.
7) Devuelve: lista de errores inicial, cambios aplicados, resultado del validador.
```
