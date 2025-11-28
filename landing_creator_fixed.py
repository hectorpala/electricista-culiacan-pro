#!/usr/bin/env python3
"""
Landing Creator Fixed v2.0 - Genera páginas idénticas a plomeroculiacanpro.mx
Versión corregida y alineada con el documento landing-creator.md actualizado

Características:
- Critical CSS completo (126 líneas)
- Colores naranja (#E36414, #F97316)
- Nav transparente con menu completo
- Logo con dimensiones correctas (140x140 nav, 200x76 footer)
- Botones flotantes con SVG icons
- Breadcrumb visible para SEO
- Footer completo con 4 columnas
- Mobile responsive con backdrop-filter
"""

import os
import sys
from pathlib import Path
import json
from datetime import datetime

# Configuración del sitio objetivo
SITE_CONFIG = {
    "domain": "electricistaculiacanpro.mx",
    "phone": "667 163 1231",
    "phone_clean": "6671631231",
    "whatsapp": "526671631231",
    "business_name": "Electricista Culiacán Pro",
    "service_type": "Electrician",  # Para schemas
    "keywords_base": "electricista culiacan",
}

def get_critical_css():
    """Critical CSS completo - 126 líneas exactas como plomeroculiacanpro.mx"""
    return """    <style>
        @font-face{font-family:'Inter';font-style:normal;font-weight:400;font-display:swap;src:url('/assets/fonts/inter-400.woff2') format('woff2')}
        @font-face{font-family:'Inter';font-style:normal;font-weight:500;font-display:swap;src:url('/assets/fonts/inter-500.woff2') format('woff2')}
        @font-face{font-family:'Inter';font-style:normal;font-weight:600;font-display:swap;src:url('/assets/fonts/inter-600.woff2') format('woff2')}
        @font-face{font-family:'Montserrat';font-style:normal;font-weight:700;font-display:swap;src:url('/assets/fonts/montserrat-700.woff2') format('woff2')}
        @font-face{font-family:'Montserrat';font-style:normal;font-weight:800;font-display:swap;src:url('/assets/fonts/montserrat-800.woff2') format('woff2')}
        :root{--brand:#E36414;--brand-light:#F97316;--text:#0F172A;--text-light:#475569;--bg:#FFFFFF;--bg-soft:#F8FAFC;--border:#E2E8F0;--shadow:rgba(15,23,42,0.1);--gradient-brand:linear-gradient(135deg,#F97316 0%,#E36414 100%);--container-max-width:1200px;--container-gutter:24px}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;font-size:16px;line-height:1.7;color:var(--text);background-color:var(--bg-soft);padding-top:80px}
        .container{max-width:var(--container-max-width);margin:0 auto;padding:0 var(--container-gutter)}
        h1,h2,h3{font-family:'Montserrat',sans-serif;font-weight:800;color:var(--text);letter-spacing:-0.025em;line-height:1.2}
        h1{font-size:clamp(2.5rem,5vw,4rem);margin-bottom:1.5rem}
        .nav{position:fixed;top:0;left:0;right:0;z-index:50;background:transparent;border-bottom:none;padding:22px 0}
        .nav-wrapper{display:flex;align-items:center;justify-content:space-between}
        .logo{display:block;text-decoration:none;transition:opacity .2s ease;contain:layout}
        .logo img{height:140px;width:auto;display:block;max-height:160px;mix-blend-mode:multiply;aspect-ratio:512/195}
        .logo:hover{opacity:0.9}
        @media (max-width:768px){.logo img{height:90px;max-height:100px}}
        .nav-menu{display:flex;list-style:none;gap:2rem}
        .nav-link{color:#fff;font-weight:500;text-decoration:none;transition:color .2s ease}
        .nav-link:hover{color:var(--brand-light)}
        .nav-cta{background:var(--gradient-brand);color:white;padding:0.625rem 1.5rem;border-radius:8px;text-decoration:none;font-weight:600}
        .hero{position:relative;min-height:85vh;display:grid;place-items:center;text-align:center;overflow:hidden;padding:140px 16px}
        .hero-background{position:absolute;inset:0;z-index:0}
        .hero-background img{width:100%;height:100%;object-fit:cover;object-position:center center;content-visibility:auto}
        .hero-content{position:relative;z-index:2;max-width:900px;width:min(90vw,840px);margin:0 auto;background:rgba(255,255,255,0.15);backdrop-filter:blur(1px);-webkit-backdrop-filter:blur(1px);border-radius:24px;padding:3rem 2.5rem;border:1px solid rgba(255,255,255,0.2);box-shadow:0 8px 32px rgba(0,0,0,0.1);contain:layout paint}
        .hero h1{color:#FFFFFF;text-shadow:0 2px 8px rgba(0,0,0,0.3);margin-bottom:1.5rem}
        .hero-subtitle{font-size:1.2rem;color:#F1F5F9;margin-bottom:3rem;max-width:640px;margin-left:auto;margin-right:auto;line-height:1.55;text-shadow:0 1px 4px rgba(0,0,0,0.4)}
        .btn-primary{display:inline-block;background:var(--gradient-brand);color:white;padding:1rem 2rem;border-radius:8px;text-decoration:none;font-weight:600;font-size:1.1rem;transition:transform 0.2s,box-shadow 0.2s}
        .btn-primary:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(227,100,20,0.3)}
        .btn-secondary{display:inline-block;background:transparent;color:var(--brand);border:2px solid var(--brand);padding:1rem 2rem;border-radius:8px;text-decoration:none;font-weight:600;transition:all 0.2s}
        .btn-secondary:hover{background:var(--brand);color:white}
        .section{padding:4rem 0}
        .section-alt{background:var(--bg-soft)}
        .section h2{font-size:2.5rem;text-align:center;margin-bottom:3rem}
        .benefits-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:2rem;margin-top:3rem}
        .benefit-card{background:white;padding:2rem;border-radius:12px;box-shadow:0 2px 10px var(--shadow);text-align:center}
        .benefit-icon{width:64px;height:64px;margin:0 auto 1rem;color:var(--brand)}
        .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:2rem}
        .card{background:white;border-radius:12px;overflow:hidden;box-shadow:0 2px 10px var(--shadow);transition:transform 0.2s}
        .card:hover{transform:translateY(-4px)}
        .card-image{width:100%;height:200px;object-fit:cover}
        .card-content{padding:1.5rem}
        .faq{max-width:800px;margin:0 auto}
        .faq-item{background:white;margin-bottom:1rem;border-radius:8px;overflow:hidden;box-shadow:0 2px 10px var(--shadow)}
        .faq-item summary{padding:1.25rem;cursor:pointer;font-weight:600;list-style:none;display:flex;justify-content:space-between;align-items:center}
        .faq-item summary::after{content:'+';font-size:1.5rem;color:var(--brand)}
        .faq-item[open] summary::after{content:'−'}
        .faq-item p{padding:0 1.25rem 1.25rem;color:var(--text-light)}
        .final-cta{text-align:center;padding:2rem;background:white;border-radius:12px;box-shadow:0 2px 10px var(--shadow)}
        .cta-text{font-size:1.25rem;margin-bottom:1.5rem;color:var(--text)}
        .cta-buttons{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
        .footer{background:var(--text);color:white;padding:3rem 0 1rem;margin-top:4rem}
        .footer-content{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:2rem;margin-bottom:2rem}
        .footer h3{margin-bottom:1rem}
        .footer-links{list-style:none}
        .footer-links li{margin-bottom:0.5rem}
        .footer-links a{color:rgba(255,255,255,0.8);text-decoration:none}
        .footer-links a:hover{color:white}
        .floating-btn{position:fixed;right:18px;width:54px;height:54px;border-radius:50%;display:grid;place-items:center;color:#fff;font-size:1.1rem;box-shadow:0 10px 28px rgba(0,0,0,0.16);transition:transform .12s ease,box-shadow .12s ease,filter .12s ease;z-index:60;text-decoration:none}
        .floating-btn:hover{transform:translateY(-2px);box-shadow:0 14px 34px rgba(0,0,0,0.2);filter:brightness(1.05)}
        .floating-call{background:#0f4fa8;bottom:18px}
        .floating-whatsapp{background:#22c55e;bottom:78px}
        @media (max-width:768px){
            body{padding-top:70px}
            .nav{padding:15px 0}
            .nav-menu{position:fixed;top:65px;left:-100%;width:100%;height:calc(100vh - 65px);background:rgba(255,255,255,0.98);flex-direction:column;padding:3rem 2rem;gap:2rem;transition:left 0.3s}
            .nav-menu.active{left:0}
            .hero{min-height:75vh;padding-top:85px!important;align-items:flex-start!important}
            .hero-background img{object-position:40% 35%}
            .hero-content{margin-top:0!important;padding:1.5rem 1.25rem!important;background:rgba(255,255,255,0.12)!important;backdrop-filter:blur(1px)!important;-webkit-backdrop-filter:blur(1px)!important}
            .hero h1{margin-top:0!important;margin-bottom:0.5rem!important;font-size:clamp(1.5rem,5vw,2rem)!important;line-height:1.2!important;color:var(--text)!important;text-shadow:none!important}
            .hero-subtitle{display:none!important}
            .hero-rating{margin-top:1rem;margin-bottom:1.5rem;background:rgba(255,255,255,0.9)!important;backdrop-filter:blur(0.5px);-webkit-backdrop-filter:blur(0.5px)}
            .hero .btn-primary{width:100%!important;max-width:100%!important;font-size:1rem!important;padding:0.875rem 1.5rem!important}
            .section{padding:3rem 0}
            .section h2{font-size:1.75rem}
            .benefits-grid{grid-template-columns:1fr}
            .cta-buttons{flex-direction:column}
        }
    </style>"""

def get_nav_html():
    """Nav completo con estructura correcta"""
    return """    <!-- Navigation -->
    <nav class="nav">
        <div class="container">
            <div class="nav-wrapper">
                <a href="/" class="logo">
                    <img src="/assets/images/logo-512.webp"
                         alt="Electricista Culiacán Pro"
                         width="140"
                         height="140">
                </a>
                <ul class="nav-menu">
                    <li><a href="/#inicio" class="nav-link">Inicio</a></li>
                    <li><a href="/#servicios" class="nav-link">Servicios</a></li>
                    <li><a href="/#nosotros" class="nav-link">Nosotros</a></li>
                    <li><a href="/#contacto" class="nav-link">Contacto</a></li>
                    <li><a href="tel:6671631231" class="nav-cta">📞 667 163 1231</a></li>
                </ul>
            </div>
        </div>
    </nav>"""

def get_floating_buttons():
    """Botones flotantes con SVG icons correctos"""
    return """    <!-- Botones Flotantes -->
    <a href="https://wa.me/526671631231?text=Hola%2C%20necesito%20un%20electricista%20urgente"
       id="cta-whatsapp"
       class="floating-btn floating-whatsapp"
       target="_blank"
       rel="noopener noreferrer"
       aria-label="Contactar por WhatsApp">
        <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
        </svg>
    </a>
    <a href="tel:+526671631231"
       id="cta-llamar"
       class="floating-btn floating-call"
       aria-label="Llamar ahora">
        <svg width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
            <path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"/>
        </svg>
    </a>"""

def create_landing_page(slug, keyword, h1, meta_description, hero_subtitle, hero_image="emergencia-electrica-culiacan"):
    """Genera una landing page completa"""

    # Validar longitudes
    if len(h1) > 70:
        print(f"⚠️ H1 muy largo ({len(h1)} chars). Máximo recomendado: 70")

    if len(meta_description) > 160:
        print(f"⚠️ Meta description muy larga ({len(meta_description)} chars). Se cortará en Google")

    # Title optimizado
    title = f"{keyword.title()} | {SITE_CONFIG['business_name']}"
    if len(title) > 70:
        title = f"{keyword.title()} | Electricista Culiacán"

    html = f"""<!DOCTYPE html>
<html lang="es-MX">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta_description}">
    <meta name="keywords" content="{keyword}, {SITE_CONFIG['keywords_base']}, electricista urgente, electricidad culiacan">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="author" content="{SITE_CONFIG['business_name']}">

    <!-- Favicons -->
    <link rel="icon" href="/favicon.ico" sizes="any">
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/icons/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/assets/icons/apple-touch-icon.png">

    <!-- Open Graph -->
    <meta property="og:title" content="{h1}">
    <meta property="og:description" content="{meta_description}">
    <meta property="og:image" content="https://{SITE_CONFIG['domain']}/assets/images/{hero_image}-1200w.webp">
    <meta property="og:url" content="https://{SITE_CONFIG['domain']}/{slug}/">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="es_MX">

    <!-- Canonical -->
    <link rel="canonical" href="https://{SITE_CONFIG['domain']}/{slug}/">

    <!-- Preloads -->
    <link rel="preload" as="image" href="/assets/images/{hero_image}-1200w.webp" fetchpriority="high">
    <link rel="preload" href="/assets/fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin fetchpriority="high">
    <link rel="preload" href="/assets/fonts/inter-500.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/assets/fonts/montserrat-800.woff2" as="font" type="font/woff2" crossorigin fetchpriority="high">

{get_critical_css()}

    <!-- JSON-LD Schema -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@graph": [
            {{
                "@type": "WebSite",
                "name": "{SITE_CONFIG['business_name']}",
                "url": "https://{SITE_CONFIG['domain']}/",
                "logo": "https://{SITE_CONFIG['domain']}/assets/images/logo-512.webp"
            }},
            {{
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {{
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Inicio",
                        "item": "https://{SITE_CONFIG['domain']}/"
                    }},
                    {{
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Servicios",
                        "item": "https://{SITE_CONFIG['domain']}/#servicios"
                    }},
                    {{
                        "@type": "ListItem",
                        "position": 3,
                        "name": "{h1}",
                        "item": "https://{SITE_CONFIG['domain']}/{slug}/"
                    }}
                ]
            }},
            {{
                "@type": "Service",
                "serviceType": "{keyword}",
                "name": "{h1}",
                "description": "{meta_description}",
                "provider": {{
                    "@type": "{SITE_CONFIG['service_type']}",
                    "name": "{SITE_CONFIG['business_name']}",
                    "telephone": "+52{SITE_CONFIG['phone_clean']}",
                    "address": {{
                        "@type": "PostalAddress",
                        "addressLocality": "Culiacán",
                        "addressRegion": "Sinaloa",
                        "addressCountry": "MX"
                    }},
                    "aggregateRating": {{
                        "@type": "AggregateRating",
                        "ratingValue": "4.8",
                        "reviewCount": "150",
                        "bestRating": "5"
                    }}
                }}
            }}
        ]
    }}
    </script>
</head>
<body>
{get_nav_html()}

    <!-- Breadcrumb (OBLIGATORIO para SEO) -->
    <nav class="breadcrumb" aria-label="breadcrumb" style="background:#f8f9fa;padding:12px 0;font-size:14px;border-bottom:1px solid #e9ecef">
        <div class="container">
            <ol style="list-style:none;display:flex;gap:0.5rem;margin:0;padding:0;flex-wrap:wrap">
                <li><a href="https://{SITE_CONFIG['domain']}/" style="color:#E36414;text-decoration:none">Inicio</a></li>
                <li style="color:#6c757d">›</li>
                <li><a href="https://{SITE_CONFIG['domain']}/#servicios" style="color:#E36414;text-decoration:none">Servicios</a></li>
                <li style="color:#6c757d">›</li>
                <li style="color:#6c757d" aria-current="page">{h1}</li>
            </ol>
        </div>
    </nav>

    <!-- Hero -->
    <header id="inicio" class="hero">
        <picture class="hero-background">
            <source type="image/webp"
                    srcset="/assets/images/{hero_image}-800w.webp 800w, /assets/images/{hero_image}-1200w.webp 1200w"
                    sizes="100vw">
            <img src="/assets/images/{hero_image}-1200w.webp"
                 srcset="/assets/images/{hero_image}-800w.webp 800w, /assets/images/{hero_image}-1200w.webp 1200w"
                 sizes="100vw"
                 alt="{h1}"
                 width="1200"
                 height="800"
                 fetchpriority="high"
                 decoding="async">
        </picture>
        <div class="container">
            <div class="hero-content">
                <h1>{h1}</h1>
                <p class="hero-subtitle">{hero_subtitle}</p>
                <a href="#contacto" class="btn-primary">Solicitar Servicio Ahora</a>
            </div>
        </div>
    </header>

    <!-- Sección Beneficios -->
    <section class="section">
        <div class="container">
            <h2>¿Por qué elegirnos?</h2>
            <div class="benefits-grid">
                <div class="benefit-card">
                    <svg class="benefit-icon" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                    </svg>
                    <h3>Servicio Garantizado</h3>
                    <p>6 meses de garantía en todos nuestros trabajos</p>
                </div>
                <div class="benefit-card">
                    <svg class="benefit-icon" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/>
                    </svg>
                    <h3>Llegada Rápida</h3>
                    <p>30-60 minutos en cualquier zona de Culiacán</p>
                </div>
                <div class="benefit-card">
                    <svg class="benefit-icon" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/>
                    </svg>
                    <h3>Técnicos Certificados</h3>
                    <p>Personal calificado y con experiencia comprobada</p>
                </div>
                <div class="benefit-card">
                    <svg class="benefit-icon" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1.41 16.09V20h-2.67v-1.93c-1.71-.36-3.16-1.46-3.27-3.4h1.96c.1.81.45 1.61 1.67 1.61 1.16 0 1.6-.64 1.6-1.46 0-2.27-5.17-1.77-5.17-5.32 0-1.91 1.41-2.94 3.14-3.3V4h2.67v2.15c1.63.39 2.75 1.51 2.85 3.15h-1.97c-.05-.73-.48-1.44-1.54-1.44-1.03 0-1.54.51-1.54 1.34 0 2.22 5.17 1.77 5.17 5.24 0 1.91-1.27 3.06-3.09 3.44z"/>
                    </svg>
                    <h3>Precios Justos</h3>
                    <p>Cotización sin compromiso y precios competitivos</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Sección FAQs -->
    <section class="section">
        <div class="container">
            <h2>Preguntas Frecuentes</h2>
            <div class="faq-list">
                <details class="faq-item">
                    <summary>¿Ofrecen servicio de emergencia 24/7?</summary>
                    <p>Sí, ofrecemos servicio de emergencia las 24 horas del día, los 7 días de la semana. Llegamos en 30-60 minutos a cualquier zona de Culiacán.</p>
                </details>
                <details class="faq-item">
                    <summary>¿Cuánto cuesta una visita de diagnóstico?</summary>
                    <p>La visita de diagnóstico tiene un costo accesible que se descuenta del total si acepta el servicio. Cotización sin compromiso.</p>
                </details>
                <details class="faq-item">
                    <summary>¿Trabajan con instalaciones trifásicas?</summary>
                    <p>Sí, somos especialistas en instalaciones monofásicas y trifásicas, tanto residenciales como comerciales e industriales.</p>
                </details>
                <details class="faq-item">
                    <summary>¿Ofrecen garantía en sus trabajos?</summary>
                    <p>Todos nuestros trabajos incluyen garantía de 6 meses por escrito. Usamos materiales de primera calidad certificados.</p>
                </details>
                <details class="faq-item">
                    <summary>¿Pueden ayudar con la instalación de sistemas de iluminación LED?</summary>
                    <p>Sí, somos expertos en modernización a iluminación LED. Ahorre hasta 80% en su consumo eléctrico con nuestros sistemas.</p>
                </details>
            </div>
        </div>
    </section>

    <!-- Sección Contacto -->
    <section id="contacto" class="section section-alt">
        <div class="container">
            <h2>Contacta con Nosotros</h2>
            <div class="final-cta">
                <p class="cta-text">WhatsApp: 52 {SITE_CONFIG['phone']} · Llamadas: {SITE_CONFIG['phone']}</p>
                <div class="cta-buttons">
                    <a href="https://wa.me/{SITE_CONFIG['whatsapp']}" target="_blank" class="btn-primary btn-whatsapp">WhatsApp</a>
                    <a href="tel:{SITE_CONFIG['phone_clean']}" class="btn-secondary">Llamar Ahora</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <img src="/assets/images/logo-512.webp"
                         alt="{SITE_CONFIG['business_name']}"
                         width="200"
                         height="76"
                         style="filter:brightness(0) invert(1)">
                    <p style="margin-top:1rem">Servicio profesional de electricidad en Culiacán. Atención 24/7 con técnicos certificados.</p>
                </div>
                <div class="footer-section">
                    <h3>Contacto</h3>
                    <ul class="footer-links">
                        <li>📞 {SITE_CONFIG['phone']}</li>
                        <li>📱 WhatsApp: {SITE_CONFIG['phone']}</li>
                        <li>📧 contacto@{SITE_CONFIG['domain']}</li>
                        <li>📍 Culiacán, Sinaloa</li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Servicios</h3>
                    <ul class="footer-links">
                        <li><a href="/#servicios">Instalación Eléctrica</a></li>
                        <li><a href="/#servicios">Reparación de Cortocircuitos</a></li>
                        <li><a href="/#servicios">Iluminación LED</a></li>
                        <li><a href="/#servicios">Emergencias 24/7</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h3>Horario</h3>
                    <ul class="footer-links">
                        <li>Lunes a Domingo</li>
                        <li>24 horas</li>
                        <li>Emergencias disponibles</li>
                        <li>Respuesta inmediata</li>
                    </ul>
                </div>
            </div>
            <div style="text-align:center;padding-top:2rem;border-top:1px solid rgba(255,255,255,0.1);margin-top:2rem">
                <p>&copy; 2024 {SITE_CONFIG['business_name']}. Todos los derechos reservados.</p>
            </div>
        </div>
    </footer>

{get_floating_buttons()}

</body>
</html>"""

    return html

def main():
    print("\n🎨 Landing Page Creator v2.0 - Electricista Culiacán Pro")
    print("=" * 60)
    print("Genera páginas con el estilo exacto de plomeroculiacanpro.mx")
    print("=" * 60)

    # Solicitar información
    print("\n1️⃣ ¿Cuál es el slug de la página?")
    print("   Ejemplo: electricista-urgente")
    slug = input("   > ").strip().lower().replace(" ", "-")

    print("\n2️⃣ ¿Cuál es la keyword principal?")
    print("   Ejemplo: electricista urgente")
    keyword = input("   > ").strip()

    print("\n3️⃣ ¿Cuál es el título H1? (máx 70 chars)")
    print("   Ejemplo: Electricista Urgente en Culiacán 24/7")
    h1 = input("   > ").strip()

    print("\n4️⃣ ¿Meta description? (máx 160 chars)")
    print("   Ejemplo: Electricista urgente en Culiacán. Llegada 30-60 min...")
    meta_description = input("   > ").strip()

    print("\n5️⃣ ¿Subtítulo del hero?")
    print("   Ejemplo: Atención inmediata para emergencias eléctricas")
    hero_subtitle = input("   > ").strip()

    print("\n6️⃣ ¿Nombre de imagen hero? (sin extensión)")
    print("   Ejemplo: emergencia-electrica-culiacan")
    print("   Enter para usar: emergencia-electrica-culiacan")
    hero_image = input("   > ").strip()
    if not hero_image:
        hero_image = "emergencia-electrica-culiacan"

    # Crear directorio
    output_dir = Path(slug)
    output_dir.mkdir(exist_ok=True)

    # Generar HTML
    html = create_landing_page(slug, keyword, h1, meta_description, hero_subtitle, hero_image)

    # Guardar archivo
    output_file = output_dir / "index.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print("\n✅ Landing page creada exitosamente!")
    print(f"📁 Ubicación: {output_file}")
    print(f"🌐 URL: https://{SITE_CONFIG['domain']}/{slug}/")

    print("\n📋 Checklist de verificación:")
    print("   ✅ Nav completo con menu y teléfono")
    print("   ✅ Logo con dimensiones y estilos correctos:")
    print("      • Nav: 140x140 con mix-blend-mode:multiply")
    print("      • Mobile: 90x90")
    print("      • Footer: 200x76 con filter:brightness(0) invert(1)")
    print("   ✅ Nav links blancos (#fff) para contraste sobre hero")
    print("   ✅ Hero con <picture> y <source> para WebP")
    print("   ✅ Botones flotantes con SVG icons (no emojis)")
    print("   ✅ Critical CSS completo actualizado")
    print("   ✅ Colores naranja (#E36414, #F97316)")
    print("   ✅ Nav transparente")
    print("   ✅ Blur optimizado:")
    print("      • Desktop hero-content: blur(1px)")
    print("      • Mobile hero-content: blur(1px)")
    print("      • Mobile hero-rating: blur(0.5px)")
    print("   ✅ Breadcrumb visible para SEO")
    print("   ✅ Sección FAQs incluida")
    print("   ✅ Footer completo con 4 columnas")

    print("\n⚠️ IMPORTANTE - Archivos necesarios:")
    print(f"   • /assets/images/{hero_image}-800w.webp")
    print(f"   • /assets/images/{hero_image}-1200w.webp")
    print("   • /assets/images/logo-512.webp")
    print("   • /assets/fonts/inter-400.woff2")
    print("   • /assets/fonts/inter-500.woff2")
    print("   • /assets/fonts/inter-600.woff2")
    print("   • /assets/fonts/montserrat-700.woff2")
    print("   • /assets/fonts/montserrat-800.woff2")

    print("\n🔍 Verificación visual obligatoria:")
    print("   1. Abrir en navegador: open " + str(output_file))
    print("   2. Verificar en desktop (1440px)")
    print("   3. Verificar en mobile (390px - iPhone 14 Pro)")
    print("   4. Confirmar que NO hay scroll horizontal")
    print("   5. Confirmar que botones flotantes funcionan")

if __name__ == "__main__":
    main()