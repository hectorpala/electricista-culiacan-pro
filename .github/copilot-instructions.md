# Copilot Instructions - Electricista Culiacán Pro

## Project Overview
**Electricista Culiacán Pro** is an SEO-optimized local service website for an electrical contractor in Culiacán, Mexico. This is a **static site** deployed on GitHub Pages with no backend—all optimization targets client-side performance, crawlability, and conversion.

**Key Goals**: Rank for local electrical services, drive WhatsApp/phone conversions, maintain excellent Core Web Vitals.

---

## Architecture & Key Patterns

### Static Site Structure
- **Root**: `index.html` (main landing page, ~1200 lines)
- **Services Pages**: `/servicios/{service-type}/index.html` (~17 service variations)
- **Blog**: `/blog/{topic}/index.html` (~6 posts for SEO content)
- **Location Pages**: `/servicios/electricista-colonias-culiacan/` (geographic targeting)
- **Utility Pages**: `/contacto/`, `/gracias/` (conversion funnels)

**Pattern**: Each HTML file is self-contained with inline critical CSS + deferred main JS. No build pipeline needed.

### Color Palette & Typography
- **Brand Colors**: Primary orange `#F97316`, accent `#E36414`, secondary orange `#FBA336`
- **WhatsApp**: `#25D366` (for floating buttons)
- **Typography**: Inter (body) + Montserrat (headings) — self-hosted WebP2 fonts in `/assets/fonts/`
- **CSS Variables** defined in `:root` of `styles.css` — always use these instead of hardcoding colors

### Performance-Critical Conventions
1. **LCP Image Preloading**: Hero images use `rel="preload"` + responsive `imagesrcset` in `<head>`
2. **Service Worker Caching** (`sw.js`): Precaches critical assets, implements cache-first strategy, cleans old versions on activation
3. **CSS Optimization**: `styles.min.css` generated via `npm run build:css` (removes comments, minifies to ~4KB)
4. **Script Deferral**: `main.js` and `analytics-events.js` loaded with `defer` attribute — never `async`
5. **Reduced Motion**: Mobile animations disabled in stylesheet with `animation: none !important` to prevent CLS

---

## Critical Developer Workflows

### Build & Optimization
```bash
npm run build:css           # Minify styles.css → styles.min.css
npm run validate:sitemap    # Check sitemap validity (xmllint)
npm run validate:schemas    # Validate JSON-LD schemas via Python script
npm run build              # Full build: CSS + sitemap + schemas validation
npm run test:all           # Run all validations
```

### Image Optimization
- Images must be WebP/AVIF format in `/assets/images/optimizadas/`
- Use responsive `srcset` with `imagesizes` attribute (e.g., `500w`, `800w`, `1200w`)
- Command: `npm run optimize:images` (requires cwebp installed via `brew install webp`)

### Local Development
```bash
python3 -m http.server 8000    # Quick Python server
# or
npm run dev                     # If live-reload configured
```
Visit `http://localhost:8000` and test mobile responsiveness + Core Web Vitals locally.

### Search Console & SEO
- `robots.txt` configured at root
- `sitemap.xml` + `sitemap_index.xml` at root — update via `npm run generate:sitemap`
- `sitemap-images.xml` for image SEO
- Schema.org JSON-LD embedded in `<head>` of all pages (Electrician, LocalBusiness, Organization)

---

## Tracking & Analytics Integration

### Google Analytics 4 (GA4) + Google Tag Manager (GTM)
- **GTM Container ID**: Imported from `gtm-config-import-v2.json` (see [INSTRUCCIONES_FINALES.md](INSTRUCCIONES_FINALES.md))
- **Event Tracking** in `analytics-events.js`:
  - `contact_whatsapp`: WhatsApp CTA clicks (floating button + exit popup)
  - `contact_phone`: Phone call button clicks
  - `click_seo_card`: Service card clicks (for conversion funnel tracking)
  - `scroll_depth`: Scroll tracking at 25%, 50%, 75%, 100%

**When modifying tracking**: Update both GTM import file AND `analytics-events.js` to stay in sync. Event names are case-sensitive.

### Custom Events Pattern
```javascript
gtag('event', 'event_name', {
  'event_category': 'Category',
  'event_label': 'Specific Label',
  'value': 1
});
```

---

## Content & Localization

### Language & Regional Context
- **Language**: Spanish (Mexico) — meta tags set to `es-MX`
- **Geo-tags**: Culiacán coordinates embedded (`24.7903, -107.3878`)
- **All copy** is Spanish; validate spelling against Mexican conventions

### Content Types
1. **Service Pages**: Product-focused landing pages with schema markup (Electrician/LocalService)
2. **Blog Posts**: SEO keyword-targeted (topics like "cómo detectar fallas eléctricas", "problemas comunes de electricidad")
3. **Colony Pages**: Local SEO targeting specific neighborhoods in Culiacán (data in `colonias-completas-culiacan.json`)

### JSON Schemas
- Located in `<head>` as `<script type="application/ld+json">`
- Types used: `LocalBusiness`, `Electrician`, `FAQPage`, `BreadcrumbList`, `Product`, `BlogPosting`
- Validate with [schema.org validator](https://validator.schema.org/) before deploying
- Command: `npm run validate:schemas`

---

## PWA & Offline Capability

### Manifest & Service Worker
- **PWA Manifest**: `manifest.json` — defines app name, icons, theme colors, display mode
- **Service Worker**: `sw.js` — precaches critical assets, implements network-first fallback for API calls
- **Cache Strategy**: Cache-first for images/fonts, network-first for HTML pages
- **Version Management**: `CACHE_VERSION = 'v6'` in `sw.js` — increment when updating precached assets

### When to Update Cache
1. Modify `PRECACHE_ASSETS` array in `sw.js` for new critical files
2. Increment `CACHE_VERSION` (e.g., `v6` → `v7`)
3. Old caches auto-cleanup on activate event

---

## Common Tasks & File Locations

| Task | Key Files | Command |
|------|-----------|---------|
| Update contact info (phone/email) | `index.html`, `/contacto/`, analytics-events.js | `sed -i '' 's/667392XXXX/[new]/g' $(find . -name '*.html' -o -name '*.js')` |
| Add new service landing page | `/servicios/{new-service}/index.html` | Copy template, update schema + links |
| Write blog post | `/blog/{topic}/index.html` | Include schema, add to sitemap manually |
| Modify colors | `styles.css` (`:root` section) | Update CSS variables, rebuild with `npm run build:css` |
| Add PWA icon | `/assets/icons/` | Multiple sizes (48x48 → 512x512) in manifest.json |
| Adjust image responsive breakpoints | Image `srcset` attributes in HTML | Update `imagesizes` media queries per page |

---

## Git Workflow & Deployment

- **Repository**: GitHub Pages enabled (`CNAME` file points to custom domain)
- **Deployment**: Any push to main branch auto-deploys
- **Branching**: Feature branches for large changes, PR review before merge
- **.gitignore**: Excludes DS_Store, logs, node_modules, .env

---

## Common Mistakes to Avoid

1. **Hardcoding Colors**: Never use `#F97316` directly—always use CSS variables (`var(--brand)`)
2. **Breaking Schema**: Ensure JSON-LD is valid JSON with no trailing commas or unescaped characters
3. **Forgetting Image Optimization**: Images must be WebP/AVIF—never upload raw JPG/PNG
4. **Modifying Minified Files**: Edit `styles.css` (source), then run `npm run build:css`; never edit `styles.min.css` directly
5. **Sidebar Cache Issues**: If cached version persists, increment `CACHE_VERSION` in `sw.js`
6. **SEO Metadata Out of Sync**: Update meta tags + schema.org JSON-LD together for consistency

---

## Testing & Validation Checklist

Before deploying changes:
- [ ] Run `npm run build` (validates CSS + sitemaps + schemas)
- [ ] Test on mobile (320px + 768px breakpoints)
- [ ] Verify Core Web Vitals locally (Lighthouse in DevTools)
- [ ] Check GA4 events fire (DevTools Network tab for gtag calls)
- [ ] Validate new pages in [schema.org validator](https://validator.schema.org/)
- [ ] Verify images load in correct format (WebP in Chrome, AVIF if available)

---

## Key Documentation Files

- [DOCUMENTACION_TECNICA_RESUMEN.md](DOCUMENTACION_TECNICA_RESUMEN.md): Full tech stack breakdown
- [RESUMEN_PROYECTO.md](RESUMEN_PROYECTO.md): Project completion status
- [COMANDOS_UTILES.md](COMANDOS_UTILES.md): Utility commands (search/replace, image optimization, Git workflows)
- [README.md](README.md): Quick start guide + feature overview
