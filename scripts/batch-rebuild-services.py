#!/usr/bin/env python3
"""
Batch Rebuild Service Pages - Subagentes Reconstructores
Applies 9 critical fixes to make service pages consistent with homepage style.
"""
import re
import sys
import os

# ============================================================
# BLOCK 1: Critical CSS from homepage (lines 12-56), paths adjusted for ../../
# ============================================================
CRITICAL_CSS = """    <style>
        @font-face{font-family:'Inter';font-style:normal;font-weight:400;font-display:swap;src:url('../../assets/fonts/inter-400.woff2') format('woff2');size-adjust:107%;ascent-override:90%;descent-override:22%;line-gap-override:0%}
        @font-face{font-family:'Inter';font-style:normal;font-weight:600;font-display:swap;src:url('../../assets/fonts/inter-600.woff2') format('woff2');size-adjust:107%;ascent-override:90%;descent-override:22%;line-gap-override:0%}
        @font-face{font-family:'Montserrat';font-style:normal;font-weight:800;font-display:swap;src:url('../../assets/fonts/montserrat-800.woff2') format('woff2');size-adjust:113%;ascent-override:89%;descent-override:24%;line-gap-override:0%}
        :root{--brand:#E36414;--brand-light:#F97316;--text:#0F172A;--text-light:#475569;--bg:#FFFFFF;--bg-soft:#F8FAFC;--border:#E2E8F0;--shadow:rgba(15,23,42,0.1);--gradient-brand:linear-gradient(135deg,#F97316 0%,#E36414 100%);--container-max-width:1200px;--container-gutter:24px;--nav-h:74px}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;font-size:16px;line-height:1.7;color:var(--text);background-color:var(--bg-soft);padding-top:80px}
        .container{max-width:var(--container-max-width);margin:0 auto;padding:0 var(--container-gutter)}
        h1,h2,h3{font-family:'Montserrat',sans-serif;font-weight:800;color:var(--text);letter-spacing:-0.025em;line-height:1.2}
        h1{font-size:clamp(2.5rem,5vw,4rem);margin-bottom:1.5rem}
        .nav{position:fixed;top:0;left:0;right:0;z-index:50;background:transparent;border-bottom:none;padding:16px 0}
        .nav-wrapper{display:flex;align-items:center;justify-content:space-between}
        .logo{display:block;text-decoration:none;transition:opacity .2s ease;contain:layout}
        .logo img{height:86px;width:auto;display:block;max-height:100px;mix-blend-mode:multiply}
        .logo:hover{opacity:0.9}
        @media (max-width:768px){.logo img{height:62px;max-height:72px}}
        .nav-menu{display:flex;list-style:none;gap:2rem}
        .nav-link{color:#f97316;font-weight:500;text-decoration:none;transition:color .2s ease;text-shadow:0 2px 4px rgba(0,0,0,0.3)}
        .nav-link:hover{color:#ea580c;text-shadow:0 2px 6px rgba(0,0,0,0.15)}
        .hero{min-height:85vh;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:flex-start;align-items:center;text-align:center;padding:140px 16px 2.5rem 16px}
        .hero-background{position:absolute;inset:0;z-index:0;display:block}
        .hero-background img{width:100%;height:100%;object-fit:cover;object-position:50% 30%;content-visibility:visible}
        @media (max-width:768px){.hero-background img{object-position:55% 35%}}
        .hero::after{content:"";position:absolute;top:0;left:0;right:0;height:180px;z-index:1;background:linear-gradient(180deg,rgba(0,0,0,0.35) 0%,transparent 100%);pointer-events:none}
        .hero-content{position:relative;z-index:2;width:95%;max-width:550px;margin:0 auto 2rem;background:rgba(0,0,0,0.35);border-radius:24px;padding:2rem 1.5rem;border:1px solid rgba(255,255,255,0.15)}
        .hero-subtitle{font-size:clamp(1rem,2vw,1.25rem);color:#F1F5F9;margin-bottom:1.5rem;line-height:1.5}
        .hero-rating{display:inline-flex;align-items:center;gap:0.5rem;margin:1rem 0;padding:0.75rem 1.25rem;background:rgba(255,255,255,0.98);border-radius:50px;font-size:0.9rem}
        .hero-eta-badge{display:flex;align-items:center;gap:0.5rem;background:rgba(255,255,255,0.14);border:1px solid rgba(255,255,255,0.3);border-radius:999px;padding:0.5rem 1rem;margin-bottom:0.75rem;font-size:0.85rem;color:#fff}
        .hero-features{display:flex;justify-content:center;gap:1.5rem;margin:1.5rem 0;flex-wrap:wrap}.feature-item{display:flex;align-items:center;gap:0.5rem;color:#fff;font-size:0.9rem}.feature-icon{width:20px;height:20px}
        .rating-stars{color:#FBBF24}.rating-score{font-weight:600}.rating-count{color:#64748B;font-size:0.85rem}.eta-dot{width:8px;height:8px;background:#22c55e;border-radius:50%}
        .btn-primary{display:inline-block;background:linear-gradient(135deg,#fba336 0%,#f97316 45%,#e36414 100%);color:#fff;border:none;border-radius:14px;padding:17px 34px;font-weight:700;font-size:1rem;text-decoration:none;cursor:pointer;box-shadow:0 10px 24px rgba(227,100,20,0.28);min-height:48px;min-width:48px}
        .mobile-menu-btn{display:none;flex-direction:column;justify-content:space-between;width:28px;height:20px;cursor:pointer;background:none;border:none;padding:0;gap:0}
        .mobile-menu-btn span{display:block;height:3px;width:100%;background:#F97316;border-radius:2px;margin:0;box-shadow:0 1px 2px rgba(0,0,0,0.2)}
        @media (max-width:768px){
            .mobile-menu-btn{display:flex}
            .nav-menu{position:fixed;top:65px;left:-100%;width:100%;height:calc(100vh - 65px);background:rgba(255,255,255,0.98);flex-direction:column;padding:3rem 2rem;gap:2rem}
            .nav-menu.active{left:0}
            .hero{min-height:70vh;height:auto;display:flex;flex-direction:column;justify-content:flex-start;align-items:center;padding:calc(var(--nav-h) + 48px) 16px 60px}
            #inicio{scroll-margin-top:calc(var(--nav-h) + 48px)}
            .hero h1,.hero-subtitle,.hero .btn-primary,.hero-content,.hero-rating,.hero-features,.fade-in{animation:none!important;opacity:1!important;transform:none!important}
            .hero-content{backdrop-filter:none!important;-webkit-backdrop-filter:none!important;box-shadow:0 2px 8px rgba(0,0,0,0.15)!important}
        }
        @media (max-width:480px){.hero h1,.hero-subtitle,.hero .btn-primary,.fade-in{animation:none!important;opacity:1!important;transform:none!important}}
        .floating-btn{position:fixed;right:max(18px,env(safe-area-inset-right,18px));width:54px;height:54px;border-radius:50%;display:grid;place-items:center;color:#fff;font-size:1.1rem;box-shadow:0 10px 28px rgba(0,0,0,0.16);transition:transform .12s ease,box-shadow .12s ease,filter .12s ease,opacity .2s ease;z-index:90;text-decoration:none}.floating-btn:hover{transform:translateY(-2px);box-shadow:0 14px 34px rgba(0,0,0,0.2);filter:brightness(1.05)}.floating-btn:focus-visible{outline:3px solid #fff;outline-offset:3px;box-shadow:0 0 0 6px rgba(249,115,22,0.5)}.floating-call{background:#0f4fa8;bottom:max(18px,env(safe-area-inset-bottom,18px))}.floating-whatsapp{background:#22c55e;bottom:calc(max(18px,env(safe-area-inset-bottom,18px)) + 60px)}body.menu-open .floating-btn{opacity:0;pointer-events:none}
    </style>"""

# ============================================================
# BLOCK 2: Breadcrumb CSS (replaces inline style block in service pages)
# ============================================================
BREADCRUMB_CSS = """    <style>
        .breadcrumb-wrapper {
            background: #f8fafc;
            border-bottom: 1px solid #e2e8f0;
            padding: 0.75rem 0;
            margin-top: 80px;
            position: relative;
            z-index: 10;
        }
        .breadcrumb {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 0.5rem;
            list-style: none;
            font-size: 0.875rem;
            line-height: 1.4;
            color: #64748b;
        }
        .breadcrumb li {
            display: flex;
            align-items: center;
            gap: 0.35rem;
        }
        .breadcrumb-link {
            color: #E36414;
            text-decoration: none;
            transition: color 0.2s;
        }
        .breadcrumb-link:hover {
            color: #ea580c;
            text-decoration: underline;
        }
        .breadcrumb-separator {
            color: #cbd5e0;
            user-select: none;
        }
        .breadcrumb-current {
            color: #475569;
            font-weight: 500;
        }
    </style>"""

# ============================================================
# BLOCK 3: GTM optimized loading (from homepage)
# ============================================================
GTM_BLOCK = """<script>
window.dataLayer = window.dataLayer || [];
(function() {
  var gtmLoaded = false;
  var clarityLoaded = false;

  var loadGTM = function() {
    if (gtmLoaded) return;
    gtmLoaded = true;
    var script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtm.js?id=GTM-W75CRTX5';
    document.head.appendChild(script);
  };

  var loadClarity = function() {
    if (clarityLoaded) return;
    clarityLoaded = true;
    (function(c,l,a,r,i,t,y){
      c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
      t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
      y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "ukonwm7t1p");
  };

  var interactionEvents = ['scroll', 'click', 'touchstart', 'keydown'];
  var onInteraction = function() {
    loadGTM();
    interactionEvents.forEach(function(e) {
      window.removeEventListener(e, onInteraction, {passive: true, capture: true});
    });
  };
  interactionEvents.forEach(function(e) {
    window.addEventListener(e, onInteraction, {passive: true, capture: true});
  });

  setTimeout(loadGTM, 12000);

  window.addEventListener('load', function() {
    setTimeout(loadClarity, 7000);
  });
})();
</script>"""

GTM_NOSCRIPT = """<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-W75CRTX5"
     height="0" width="0" style="display:none;visibility:hidden"></iframe>
</noscript>"""

# ============================================================
# BLOCK 4: Logo with srcset (homepage pattern)
# ============================================================
LOGO_BLOCK = """<a href="/" class="logo"><img src="/assets/images/optimizadas/logo-256w.webp"
            srcset="/assets/images/optimizadas/logo-128w.webp 128w, /assets/images/optimizadas/logo-256w.webp 256w"
            sizes="(max-width:768px) 96px, 140px"
            alt="Electricista Culiacan Pro - Logo"
            width="140"
            height="140"></a>"""

# ============================================================
# BLOCK 5: Hero ETA badge
# ============================================================
HERO_ETA_BADGE = """<div class="hero-eta-badge fade-in"><span class="eta-dot"></span><span class="eta-text">Tiempo real: llegamos en 35 min en tu zona</span></div>"""

# ============================================================
# BLOCK 6: Exit intent popup
# ============================================================
EXIT_POPUP = """<div id="exit-intent-popup" role="dialog" aria-modal="true" aria-labelledby="exit-popup-title" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.3);z-index:9999;align-items:center;justify-content:center;"><div class="exit-popup-content" style="background:#fff;border-radius:16px;padding:2rem;max-width:400px;margin:1rem;position:relative;box-shadow:0 20px 60px rgba(0,0,0,0.3);"><button class="exit-popup-close" style="position:absolute;top:1rem;right:1rem;background:none;border:none;font-size:1.5rem;cursor:pointer;color:#666;line-height:1;padding:0.25rem 0.5rem;" aria-label="Cerrar popup">&times;</button><h3 id="exit-popup-title" style="color:#0F172A;margin-bottom:1rem;font-size:1.5rem;">Espera!</h3><p style="color:#475569;margin-bottom:1.5rem;line-height:1.6;">Tienes una emergencia de electricidad? Contactanos ahora y llegamos en 30-60 minutos.</p><div style="display:flex;flex-direction:column;gap:0.75rem;"><a href="https://wa.me/526673922273?text=Hola%2C%20necesito%20un%20electricista%20urgente" id="exit-popup-whatsapp" target="_blank" rel="noopener noreferrer" style="background:#22c55e;color:#fff;padding:0.875rem 1.5rem;border-radius:8px;text-decoration:none;font-weight:600;text-align:center;display:flex;align-items:center;justify-content:center;gap:0.5rem;"><svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>WhatsApp</a><a href="tel:+526673922273" id="exit-popup-phone" style="background:#0f4fa8;color:#fff;padding:0.875rem 1.5rem;border-radius:8px;text-decoration:none;font-weight:600;text-align:center;display:flex;align-items:center;justify-content:center;gap:0.5rem;"><svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24"><path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"/></svg>Llamar Ahora</a></div></div></div>"""

# ============================================================
# FLOATING BUTTONS (homepage exact)
# ============================================================
FLOATING_BUTTONS = """<!-- Floating CTA Buttons -->
<a href="https://wa.me/526673922273?text=Hola%2C%20necesito%20ayuda%20con%20un%20problema%20de%20electricidad" target="_blank" rel="noopener" class="floating-btn floating-whatsapp" aria-label="WhatsApp"><svg width="26" height="26" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg></a>
<a href="tel:+526673922273" class="floating-btn floating-call" aria-label="Llamar"><svg width="26" height="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg></a>"""


def fix_page(filepath):
    """Apply all 9 remaining fixes to a service page."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    fixes = []
    
    # FIX 1: Replace entire <style> block with critical CSS + breadcrumb CSS
    # Find the existing style block(s) and replace
    old_style = re.search(r'(<style>.*?</style>)', content, re.DOTALL)
    if old_style:
        # Check if it's a breadcrumb style
        if 'breadcrumb' in old_style.group(1):
            # Replace breadcrumb style with our fixed version
            content = content.replace(old_style.group(1), BREADCRUMB_CSS.strip())
            fixes.append("FIX1a: Breadcrumb CSS replaced (color #E36414)")
        
    # FIX 2: Remove critical.css link and add inline critical CSS
    # Remove <link rel="stylesheet" href="../../assets/css/critical.css"...>
    if 'critical.css' in content:
        content = re.sub(r'\s*<link[^>]*critical\.css[^>]*>', '', content)
        fixes.append("FIX2a: Removed critical.css link")
    
    # FIX 3: Replace styles.min.css with styles.7f293647.css (and remove duplicates)
    # Remove ALL styles.min.css links
    count_min = content.count('styles.min.css')
    if count_min > 0:
        content = re.sub(r'\s*<link[^>]*styles\.min\.css[^>]*>', '', content)
        fixes.append(f"FIX3: Removed {count_min}x styles.min.css")
    
    # FIX 4: Insert critical CSS + stylesheet link after </script> in head (before OG meta)
    # Find the right insertion point - after preload links, before OG meta
    if ':root{--brand' not in content:
        # Insert after the last preload link
        preload_pattern = r'(<link[^>]*(?:preload|fetchpriority)[^>]*>)\s*\n'
        matches = list(re.finditer(preload_pattern, content))
        if matches:
            insert_pos = matches[-1].end()
        else:
            # Fallback: insert before </head> minus some space
            insert_pos = content.find('<!-- Breadcrumb') 
            if insert_pos == -1:
                insert_pos = content.find('<!-- Open Graph')
            if insert_pos == -1:
                insert_pos = content.find('</head>')
        
        css_insert = CRITICAL_CSS + '\n    <link rel="stylesheet" href="../../styles.7f293647.css">\n'
        content = content[:insert_pos] + css_insert + content[insert_pos:]
        fixes.append("FIX4: Inserted critical CSS inline + styles.7f293647.css")
    
    # FIX 5: Remove direct gtag.js script (Google Analytics loaded directly)
    gtag_pattern = r'\s*<!-- Google tag \(gtag\.js\) -->.*?</script>\s*'
    if re.search(gtag_pattern, content, re.DOTALL):
        content = re.sub(gtag_pattern, '\n', content, flags=re.DOTALL)
        fixes.append("FIX5: Removed direct gtag.js script")
    
    # Also remove standalone gtag async script without comment
    content = re.sub(r'\s*<script async src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]*"></script>', '', content)
    content = re.sub(r'\s*<script>\s*window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|\s*\[\];\s*function gtag\(\)\{dataLayer\.push\(arguments\);\}\s*gtag\(\'js\'.*?</script>', '', content, flags=re.DOTALL)
    
    # FIX 6: Replace GTM loading pattern
    # Find existing GTM block and replace with optimized version
    old_gtm_patterns = [
        r'<script>\s*window\.dataLayer\s*=\s*window\.dataLayer\s*\|\|\s*\[\];\s*\(function\(\)\s*\{.*?var loadGTM.*?\}\);\s*\}\)\(\);\s*</script>',
        r'<!-- Google Tag Manager -->\s*<script>.*?loadGTM.*?</script>',
    ]
    gtm_replaced = False
    for pattern in old_gtm_patterns:
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, GTM_BLOCK, content, flags=re.DOTALL)
            gtm_replaced = True
            fixes.append("FIX6: Replaced GTM with optimized loading")
            break
    
    if not gtm_replaced and 'interactionEvents' not in content:
        # Insert GTM block after <body>
        body_pos = content.find('<body>')
        if body_pos != -1:
            body_end = body_pos + len('<body>')
            content = content[:body_end] + GTM_BLOCK + '\n' + content[body_end:]
            fixes.append("FIX6: Inserted optimized GTM block after <body>")
    
    # Ensure GTM noscript is present
    if 'ns.html?id=GTM-W75CRTX5' not in content:
        # Insert after GTM script
        gtm_end = content.find('</script>', content.find('interactionEvents'))
        if gtm_end != -1:
            content = content[:gtm_end+9] + GTM_NOSCRIPT + '\n' + content[gtm_end+9:]
            fixes.append("FIX6b: Added GTM noscript")

    # FIX 7: Fix logo to use srcset
    logo_pattern = r'<a[^>]*class="logo"[^>]*>.*?</a>'
    old_logo = re.search(logo_pattern, content, re.DOTALL)
    if old_logo and 'logo-128w' not in old_logo.group(0):
        content = content.replace(old_logo.group(0), LOGO_BLOCK)
        fixes.append("FIX7: Logo updated with srcset")
    
    # FIX 8: Fix breadcrumb color #0066cc -> #E36414
    if '#0066cc' in content:
        content = content.replace('#0066cc', '#E36414')
        fixes.append("FIX8: Breadcrumb color fixed to #E36414")
    
    # FIX 9: Add hero-eta-badge if missing
    if 'hero-eta-badge' not in content:
        # Insert before h1 inside hero-content
        hero_h1 = re.search(r'(<div class="hero-content">.*?)(<h1)', content, re.DOTALL)
        if hero_h1:
            content = content[:hero_h1.end(1)] + HERO_ETA_BADGE + content[hero_h1.end(1):]
            fixes.append("FIX9: Added hero-eta-badge")
    
    # FIX 10: Add exit-intent popup if missing  
    if 'exit-intent-popup' not in content:
        # Insert before floating buttons or before </body>
        float_pos = content.find('<!-- Floating CTA')
        if float_pos == -1:
            float_pos = content.find('class="floating-btn')
            if float_pos != -1:
                # Go back to the start of the <a tag
                float_pos = content.rfind('<a', 0, float_pos)
        if float_pos != -1:
            content = content[:float_pos] + '\n' + EXIT_POPUP + '\n\n' + content[float_pos:]
        else:
            # Insert before </body>
            body_end = content.rfind('</body>')
            if body_end != -1:
                content = content[:body_end] + '\n' + EXIT_POPUP + '\n\n' + FLOATING_BUTTONS + '\n\n' + content[body_end:]
        fixes.append("FIX10: Added exit-intent popup")
    
    # FIX 11: Remove inter-500.woff2 preload (not in homepage)
    if 'inter-500.woff2' in content:
        content = re.sub(r'\s*<link[^>]*inter-500\.woff2[^>]*>', '', content)
        fixes.append("FIX11: Removed inter-500 preload")
    
    # Write back
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n{'='*60}")
        print(f"FIXED: {filepath}")
        print(f"{'='*60}")
        for fix in fixes:
            print(f"  [OK] {fix}")
        print(f"  Total: {len(fixes)} fixes applied")
        return len(fixes)
    else:
        print(f"\n  [SKIP] {filepath} - no changes needed")
        return 0


if __name__ == '__main__':
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Target pages
    pages = [
        'servicios/electricista/index.html',
        'servicios/emergencia-24-7/index.html',
        'servicios/instalacion-electrica/index.html',
    ]
    
    # If args provided, use those instead
    if len(sys.argv) > 1:
        pages = sys.argv[1:]
    
    total_fixes = 0
    for page in pages:
        path = os.path.join(base, page) if not os.path.isabs(page) else page
        if os.path.exists(path):
            total_fixes += fix_page(path)
        else:
            print(f"  [ERROR] File not found: {path}")
    
    print(f"\n{'='*60}")
    print(f"BATCH COMPLETE: {total_fixes} total fixes across {len(pages)} pages")
    print(f"{'='*60}")
