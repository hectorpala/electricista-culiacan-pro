/**
 * Script de Verificación de Tracking
 * Electricista Culiacán Pro
 *
 * Verifica que todos los eventos de tracking estén configurados correctamente
 * y funcionando en el sitio.
 */

(function() {
    'use strict';

    const results = {
        gtm: { status: 'unknown', details: [] },
        ga4: { status: 'unknown', details: [] },
        dataLayer: { status: 'unknown', details: [] },
        events: { status: 'unknown', details: [] },
        elements: { status: 'unknown', details: [] }
    };

    /**
     * Verificar Google Tag Manager
     */
    function checkGTM() {
        console.log('\n🔍 Verificando Google Tag Manager...');

        if (typeof google_tag_manager !== 'undefined') {
            results.gtm.status = 'success';
            results.gtm.details.push('✅ GTM está cargado');

            const gtmContainers = Object.keys(google_tag_manager);
            results.gtm.details.push(`✅ Containers encontrados: ${gtmContainers.length}`);
            gtmContainers.forEach(container => {
                results.gtm.details.push(`   - ${container}`);
            });
        } else {
            results.gtm.status = 'error';
            results.gtm.details.push('❌ GTM no está cargado');
        }
    }

    /**
     * Verificar Google Analytics 4
     */
    function checkGA4() {
        console.log('\n🔍 Verificando Google Analytics 4...');

        if (typeof gtag !== 'undefined') {
            results.ga4.status = 'success';
            results.ga4.details.push('✅ GA4 (gtag.js) está cargado');
        } else if (typeof ga !== 'undefined') {
            results.ga4.status = 'warning';
            results.ga4.details.push('⚠️  Universal Analytics detectado (legacy)');
        } else {
            results.ga4.status = 'error';
            results.ga4.details.push('❌ GA4 no está cargado');
        }
    }

    /**
     * Verificar dataLayer
     */
    function checkDataLayer() {
        console.log('\n🔍 Verificando dataLayer...');

        if (typeof window.dataLayer !== 'undefined' && Array.isArray(window.dataLayer)) {
            results.dataLayer.status = 'success';
            results.dataLayer.details.push(`✅ dataLayer existe (${window.dataLayer.length} eventos)`);

            // Mostrar eventos en dataLayer
            const eventTypes = new Set();
            window.dataLayer.forEach(item => {
                if (item.event) {
                    eventTypes.add(item.event);
                }
            });

            if (eventTypes.size > 0) {
                results.dataLayer.details.push(`✅ Tipos de eventos: ${eventTypes.size}`);
                eventTypes.forEach(event => {
                    results.dataLayer.details.push(`   - ${event}`);
                });
            }
        } else {
            results.dataLayer.status = 'error';
            results.dataLayer.details.push('❌ dataLayer no existe o no es un array');
        }
    }

    /**
     * Verificar elementos rastreables
     */
    function checkTrackableElements() {
        console.log('\n🔍 Verificando elementos rastreables...');

        const checks = [
            {
                selector: '.seo-card',
                name: 'Tarjetas SEO',
                requiredData: ['data-card-name', 'data-card-position']
            },
            {
                selector: 'a[href*="wa.me"]',
                name: 'Enlaces WhatsApp',
                requiredData: []
            },
            {
                selector: 'a[href^="tel:"]',
                name: 'Enlaces Teléfono',
                requiredData: []
            },
            {
                selector: '#contact-form',
                name: 'Formulario de Contacto',
                requiredData: []
            },
            {
                selector: 'a[href*="/servicios/"]',
                name: 'Enlaces a Servicios',
                requiredData: []
            }
        ];

        let allGood = true;

        checks.forEach(check => {
            const elements = document.querySelectorAll(check.selector);

            if (elements.length > 0) {
                results.elements.details.push(`✅ ${check.name}: ${elements.length} encontrado(s)`);

                // Verificar atributos data requeridos
                if (check.requiredData.length > 0) {
                    let missingData = 0;
                    elements.forEach(el => {
                        check.requiredData.forEach(attr => {
                            if (!el.hasAttribute(attr)) {
                                missingData++;
                            }
                        });
                    });

                    if (missingData > 0) {
                        results.elements.details.push(`   ⚠️  ${missingData} elemento(s) sin atributos data`);
                        allGood = false;
                    }
                }
            } else {
                results.elements.details.push(`❌ ${check.name}: no encontrado`);
                allGood = false;
            }
        });

        results.elements.status = allGood ? 'success' : 'warning';
    }

    /**
     * Simular eventos para verificar tracking
     */
    function testEventTracking() {
        console.log('\n🔍 Verificando configuración de eventos...');

        const eventsToCheck = [
            'click_seo_card',
            'scroll_depth',
            'click_whatsapp',
            'click_phone',
            'form_submit'
        ];

        let foundEvents = 0;

        // Buscar en el código si los eventos están configurados
        const scripts = Array.from(document.querySelectorAll('script'));
        const scriptContent = scripts.map(s => s.textContent).join(' ');

        eventsToCheck.forEach(eventName => {
            if (scriptContent.includes(eventName)) {
                results.events.details.push(`✅ Evento configurado: ${eventName}`);
                foundEvents++;
            } else {
                results.events.details.push(`❌ Evento no encontrado: ${eventName}`);
            }
        });

        results.events.status = foundEvents === eventsToCheck.length ? 'success' : 'warning';
    }

    /**
     * Generar reporte
     */
    function generateReport() {
        console.log('\n' + '='.repeat(60));
        console.log('📊 REPORTE DE VERIFICACIÓN DE TRACKING');
        console.log('Electricista Culiacán Pro');
        console.log('='.repeat(60));

        Object.keys(results).forEach(category => {
            const categoryName = category.toUpperCase();
            const status = results[category].status;
            const icon = status === 'success' ? '✅' :
                        status === 'warning' ? '⚠️' :
                        status === 'error' ? '❌' : '❓';

            console.log(`\n${icon} ${categoryName}`);
            results[category].details.forEach(detail => {
                console.log(`  ${detail}`);
            });
        });

        console.log('\n' + '='.repeat(60));

        // Resumen final
        const totalChecks = Object.keys(results).length;
        const successCount = Object.values(results).filter(r => r.status === 'success').length;
        const warningCount = Object.values(results).filter(r => r.status === 'warning').length;
        const errorCount = Object.values(results).filter(r => r.status === 'error').length;

        console.log('RESUMEN:');
        console.log(`  Total de categorías: ${totalChecks}`);
        console.log(`  ✅ Exitosas: ${successCount}`);
        console.log(`  ⚠️  Advertencias: ${warningCount}`);
        console.log(`  ❌ Errores: ${errorCount}`);
        console.log('='.repeat(60));

        // Recomendaciones
        if (errorCount > 0 || warningCount > 0) {
            console.log('\n💡 RECOMENDACIONES:');
            if (results.gtm.status === 'error') {
                console.log('  - Verificar que GTM esté instalado correctamente en el <head>');
            }
            if (results.ga4.status === 'error') {
                console.log('  - Instalar GA4 o configurarlo via GTM');
            }
            if (results.dataLayer.status === 'error') {
                console.log('  - Inicializar dataLayer antes de GTM');
            }
            if (results.events.status !== 'success') {
                console.log('  - Verificar que script-gtm-auto.js esté cargado');
            }
            if (results.elements.status !== 'success') {
                console.log('  - Agregar atributos data a elementos rastreables');
            }
        } else {
            console.log('\n✅ Todo está configurado correctamente!');
        }

        return results;
    }

    /**
     * Iniciar verificación
     */
    function init() {
        console.log('🚀 Iniciando verificación de tracking...');

        // Esperar a que el DOM esté listo
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', runChecks);
        } else {
            runChecks();
        }
    }

    function runChecks() {
        checkGTM();
        checkGA4();
        checkDataLayer();
        checkTrackableElements();
        testEventTracking();

        // Esperar un poco para que GTM se inicialice
        setTimeout(() => {
            const report = generateReport();

            // Hacer el reporte disponible globalmente
            window.trackingVerification = report;

            console.log('\n💾 Reporte guardado en: window.trackingVerification');
            console.log('📋 Para ver el reporte: console.table(window.trackingVerification)');
        }, 2000);
    }

    // Hacer el script ejecutable desde consola
    window.verificarTracking = init;

    // Auto-ejecutar al cargar
    init();

})();
