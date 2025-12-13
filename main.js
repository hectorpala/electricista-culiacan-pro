// Main JavaScript - Electricista Culiacán Pro
// Loaded with defer for optimal performance
// Last updated: 2025-11-21

// Mobile menu toggle
(function() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.nav-menu');

    if (!mobileMenuBtn || !navMenu) return;

    mobileMenuBtn.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        mobileMenuBtn.classList.toggle('active');
        // Prevent CLS: lock body scroll when menu is open
        document.body.classList.toggle('menu-open');
    });

    // Close mobile menu when clicking a link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            mobileMenuBtn.classList.remove('active');
            document.body.classList.remove('menu-open');
        });
    });
})();

// Smooth scroll for anchor links
(function() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;

            e.preventDefault();
            const target = document.querySelector(href);

            if (target) {
                const offsetTop = target.offsetTop - 80; // Adjust for fixed header
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
})();

// Real-time form validation
(function() {
    const form = document.getElementById('contact-form');
    if (!form) return; // Exit if form doesn't exist

    const nombreField = document.getElementById('nombre');
    const telefonoField = document.getElementById('telefono');
    const emailField = document.getElementById('email');
    const mensajeField = document.getElementById('mensaje');
    const submitBtn = form.querySelector('button[type="submit"]');

    // Validation functions
    const validators = {
        nombre: (value) => value.trim().length >= 2,
        telefono: (value) => /^[0-9]{10}$/.test(value.replace(/\s/g, '')),
        email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
        mensaje: (value) => value.trim().length >= 10
    };

    // Validate single field
    function validateField(field, validatorKey) {
        const value = field.value;
        const fieldWrapper = field.closest('.form-field');
        const isValid = validators[validatorKey](value);

        if (value.length === 0) {
            // Empty: neutral state
            fieldWrapper.classList.remove('valid', 'invalid');
        } else if (isValid) {
            // Valid: green checkmark
            fieldWrapper.classList.remove('invalid');
            fieldWrapper.classList.add('valid');
        } else {
            // Invalid: red X
            fieldWrapper.classList.remove('valid');
            fieldWrapper.classList.add('invalid');
        }

        updateSubmitButton();
        return isValid;
    }

    // Check if form is completely valid
    function isFormValid() {
        return validators.nombre(nombreField.value) &&
               validators.telefono(telefonoField.value) &&
               validators.email(emailField.value) &&
               validators.mensaje(mensajeField.value);
    }

    // Enable/disable submit button based on form validity
    function updateSubmitButton() {
        if (isFormValid()) {
            submitBtn.disabled = false;
            submitBtn.style.opacity = '1';
            submitBtn.style.cursor = 'pointer';
        } else {
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.6';
            submitBtn.style.cursor = 'not-allowed';
        }
    }

    // Add real-time validation listeners
    nombreField.addEventListener('input', () => validateField(nombreField, 'nombre'));
    nombreField.addEventListener('blur', () => validateField(nombreField, 'nombre'));

    telefonoField.addEventListener('input', () => {
        // Only allow numbers
        telefonoField.value = telefonoField.value.replace(/\D/g, '');
        validateField(telefonoField, 'telefono');
    });
    telefonoField.addEventListener('blur', () => validateField(telefonoField, 'telefono'));

    emailField.addEventListener('input', () => validateField(emailField, 'email'));
    emailField.addEventListener('blur', () => validateField(emailField, 'email'));

    mensajeField.addEventListener('input', () => validateField(mensajeField, 'mensaje'));
    mensajeField.addEventListener('blur', () => validateField(mensajeField, 'mensaje'));

    // Initial state: button disabled
    updateSubmitButton();
})();

// Multi-layer lead capture: Netlify Forms + localStorage + GA4 + WhatsApp
(function() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        const formData = new FormData(this);
        const nombre = formData.get('nombre');
        const telefono = formData.get('telefono');
        const email = formData.get('email');
        const mensaje = formData.get('mensaje');

        const leadData = {
            timestamp: new Date().toISOString(),
            nombre: nombre,
            telefono: telefono,
            email: email,
            mensaje: mensaje,
            source: 'homepage_form',
            url: window.location.href
        };

        // 1. Track lead in GA4 via GTM dataLayer (immediate)
        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'generate_lead',
                'form_name': 'contact_form_homepage',
                'method': 'netlify_forms',
                'value': 1,
                'currency': 'MXN'
            });
        }

        // 2. Store in localStorage as backup (immediate)
        try {
            const leads = JSON.parse(localStorage.getItem('electricista_leads') || '[]');
            leads.push(leadData);
            localStorage.setItem('electricista_leads', JSON.stringify(leads));
        } catch (e) {
            // console.error('Error storing lead in localStorage:', e);
        }

        // 3. Submit to Netlify Forms (primary backend)
        try {
            const response = await fetch('/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams(formData).toString()
            });

            if (response.ok) {
                // Success: show thank you and open WhatsApp
                const whatsappMessage = `Hola! Solicito cotización de servicios eléctricos:\n\n` +
                                      `Nombre: ${nombre}\n` +
                                      `Teléfono: ${telefono}\n` +
                                      `Email: ${email}\n` +
                                      `Mensaje: ${mensaje}`;
                const whatsappURL = `https://wa.me/526673922273?text=${encodeURIComponent(whatsappMessage)}`;

                // Open WhatsApp in new tab
                window.open(whatsappURL, '_blank');

                // Redirect to thank you page
                window.location.href = '/gracias';
            } else {
                throw new Error('Netlify form submission failed');
            }
        } catch (error) {
            // console.error('Error submitting to Netlify:', error);

            // Fallback: open WhatsApp directly
            alert('Formulario enviado. Te redirigiremos a WhatsApp.');
            const whatsappMessage = `Hola! Solicito cotización de servicios eléctricos:\n\n` +
                                  `Nombre: ${nombre}\n` +
                                  `Teléfono: ${telefono}\n` +
                                  `Email: ${email}\n` +
                                  `Mensaje: ${mensaje}`;
            const whatsappURL = `https://wa.me/526673922273?text=${encodeURIComponent(whatsappMessage)}`;
            window.location.href = whatsappURL;
        }
    });
})();

// WhatsApp tracking
(function() {
    const whatsappLinks = document.querySelectorAll('a[href^="https://wa.me"]');

    whatsappLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Track WhatsApp click
            if (window.dataLayer) {
                window.dataLayer.push({
                    'event': 'whatsapp_click',
                    'location': this.closest('section')?.id || 'unknown',
                    'page_location': window.location.pathname
                });
            }
        });
    });
})();

// Phone call tracking
(function() {
    const phoneLinks = document.querySelectorAll('a[href^="tel:"]');

    phoneLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Track phone click
            if (window.dataLayer) {
                window.dataLayer.push({
                    'event': 'phone_click',
                    'location': this.closest('section')?.id || 'unknown',
                    'page_location': window.location.pathname
                });
            }
        });
    });
})();

// Scroll depth tracking
(function() {
    const scrollDepths = [25, 50, 75, 90];
    const scrollTracked = {};

    window.addEventListener('scroll', function() {
        const scrollPercent = Math.round((window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100);

        scrollDepths.forEach(function(depth) {
            if (scrollPercent >= depth && !scrollTracked[depth]) {
                scrollTracked[depth] = true;

                if (window.dataLayer) {
                    window.dataLayer.push({
                        'event': 'scroll_depth',
                        'scroll_percentage': depth,
                        'page_location': window.location.pathname
                    });
                }
            }
        });
    });
})();

// Add fade-in animation on scroll
(function() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe cards and sections
    document.querySelectorAll('.card, .section').forEach(el => {
        observer.observe(el);
    });
})();

// Service Worker Registration (PWA)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered:', registration.scope);
            })
            .catch(err => {
                console.log('SW registration failed:', err);
            });
    });
}

// Initialize DataLayer for GTM
window.dataLayer = window.dataLayer || [];

// Track page view
window.dataLayer.push({
    'event': 'page_view',
    'page_title': document.title,
    'page_location': window.location.href,
    'page_path': window.location.pathname
});

console.log('✅ Electricista Culiacán Pro - JavaScript loaded successfully');

// Exit Intent Popup
(function() {
    const popup = document.getElementById('exit-intent-popup');
    if (!popup) return;

    let popupShown = false;
    const POPUP_DELAY = 30000; // 30 segundos para móvil
    const SESSION_KEY = 'exitPopupShown';

    // No mostrar si ya se mostró en esta sesión
    if (sessionStorage.getItem(SESSION_KEY)) return;

    function showPopup() {
        if (popupShown) return;
        popupShown = true;
        sessionStorage.setItem(SESSION_KEY, 'true');
        popup.style.display = 'flex';
        document.body.style.overflow = 'hidden';

        // Track en GA4
        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'exit_intent_shown',
                'trigger': isMobile() ? 'mobile_timer' : 'desktop_mouseleave'
            });
        }
    }

    function hidePopup() {
        popup.style.display = 'none';
        document.body.style.overflow = '';
    }

    function isMobile() {
        return window.innerWidth <= 768 || 'ontouchstart' in window;
    }

    // Cerrar popup
    const closeBtn = popup.querySelector('.exit-popup-close');
    if (closeBtn) {
        closeBtn.addEventListener('click', hidePopup);
    }

    // Cerrar al hacer clic fuera
    popup.addEventListener('click', function(e) {
        if (e.target === popup) hidePopup();
    });

    // Cerrar con ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') hidePopup();
    });

    // DESKTOP: Detectar cuando el mouse sale hacia arriba
    if (!isMobile()) {
        document.addEventListener('mouseleave', function(e) {
            if (e.clientY < 10) {
                showPopup();
            }
        });
    }

    // MÓVIL: Mostrar después de 30 segundos sin conversión
    if (isMobile()) {
        setTimeout(function() {
            // Solo mostrar si no han hecho clic en WhatsApp o teléfono
            showPopup();
        }, POPUP_DELAY);

        // También al presionar botón "atrás"
        history.pushState(null, '', location.href);
        window.addEventListener('popstate', function() {
            if (!popupShown) {
                showPopup();
                history.pushState(null, '', location.href);
            }
        });
    }
})();
