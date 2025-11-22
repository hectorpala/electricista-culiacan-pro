/**
 * GTM Auto-Configuration Script
 * Electricista Culiacán Pro
 *
 * Este script configura automáticamente Google Tag Manager con los eventos
 * necesarios para tracking de conversiones y comportamiento del usuario.
 */

(function() {
    'use strict';

    // Configuración
    const GTM_ID = 'GTM-XXXXXXX'; // Reemplazar con el ID real
    const GA4_ID = 'G-XXXXXXXXXX'; // Reemplazar con el ID real

    /**
     * Inicializar dataLayer
     */
    window.dataLayer = window.dataLayer || [];

    /**
     * Track click en tarjetas SEO
     */
    function trackSEOCards() {
        document.querySelectorAll('.seo-card').forEach(card => {
            card.addEventListener('click', function(e) {
                const cardName = this.dataset.cardName || this.querySelector('h3')?.textContent || 'Unknown';
                const cardPosition = this.dataset.cardPosition || '0';
                const cardURL = this.href || window.location.href;

                window.dataLayer.push({
                    event: 'click_seo_card',
                    cardName: cardName,
                    cardPosition: cardPosition,
                    cardURL: cardURL
                });

                console.log('[GTM] SEO Card clicked:', {cardName, cardPosition, cardURL});
            });
        });
    }

    /**
     * Track scroll depth
     */
    function trackScrollDepth() {
        const thresholds = [25, 50, 75, 100];
        const triggered = new Set();

        window.addEventListener('scroll', function() {
            const scrollPercent = Math.round(
                (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100
            );

            thresholds.forEach(threshold => {
                if (scrollPercent >= threshold && !triggered.has(threshold)) {
                    triggered.add(threshold);

                    window.dataLayer.push({
                        event: 'scroll_depth',
                        scrollDepth: threshold
                    });

                    console.log('[GTM] Scroll depth:', threshold + '%');
                }
            });
        });
    }

    /**
     * Track clicks en WhatsApp
     */
    function trackWhatsAppClicks() {
        document.querySelectorAll('a[href*="wa.me"]').forEach(link => {
            link.addEventListener('click', function(e) {
                const buttonLocation = this.closest('[data-location]')?.dataset.location ||
                                     this.className ||
                                     'unknown';

                window.dataLayer.push({
                    event: 'click_whatsapp',
                    buttonLocation: buttonLocation
                });

                console.log('[GTM] WhatsApp clicked:', buttonLocation);
            });
        });
    }

    /**
     * Track clicks en teléfono
     */
    function trackPhoneClicks() {
        document.querySelectorAll('a[href^="tel:"]').forEach(link => {
            link.addEventListener('click', function(e) {
                const buttonLocation = this.closest('[data-location]')?.dataset.location ||
                                     this.className ||
                                     'unknown';

                window.dataLayer.push({
                    event: 'click_phone',
                    buttonLocation: buttonLocation
                });

                console.log('[GTM] Phone clicked:', buttonLocation);
            });
        });
    }

    /**
     * Track envío de formulario
     */
    function trackFormSubmit() {
        const form = document.getElementById('contact-form');
        if (!form) return;

        form.addEventListener('submit', function(e) {
            window.dataLayer.push({
                event: 'form_submit',
                formId: 'contact-form',
                formLocation: window.location.pathname
            });

            console.log('[GTM] Form submitted');
        });
    }

    /**
     * Track clicks en servicios
     */
    function trackServiceClicks() {
        document.querySelectorAll('a[href*="/servicios/"]').forEach(link => {
            link.addEventListener('click', function(e) {
                const serviceName = this.querySelector('h3')?.textContent ||
                                  this.dataset.service ||
                                  'unknown';

                window.dataLayer.push({
                    event: 'click_service',
                    serviceName: serviceName,
                    serviceURL: this.href
                });

                console.log('[GTM] Service clicked:', serviceName);
            });
        });
    }

    /**
     * Inicializar todos los trackers
     */
    function init() {
        console.log('[GTM] Initializing auto-tracking...');

        // Esperar a que el DOM esté listo
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', function() {
                setupTracking();
            });
        } else {
            setupTracking();
        }
    }

    function setupTracking() {
        trackSEOCards();
        trackScrollDepth();
        trackWhatsAppClicks();
        trackPhoneClicks();
        trackFormSubmit();
        trackServiceClicks();

        console.log('[GTM] All trackers initialized ✓');
    }

    // Iniciar
    init();

})();
