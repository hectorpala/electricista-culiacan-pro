// Main JavaScript - Electricista Culiacán Pro
// Loaded with defer for optimal performance
// Last updated: 2025-12-14

// Helper to defer non-critical code until idle
const deferIdle = (fn, delay = 1500) => {
    if ('requestIdleCallback' in window) {
        requestIdleCallback(fn, { timeout: 3000 });
    } else {
        setTimeout(fn, delay);
    }
};

// ==========================================
// CRITICAL PATH - Menu & Form Validation
// ==========================================

// Mobile menu toggle
(function() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.nav-menu');

    if (!mobileMenuBtn || !navMenu) return;

    mobileMenuBtn.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        mobileMenuBtn.classList.toggle('active');
        document.body.classList.toggle('menu-open');
    });

    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            mobileMenuBtn.classList.remove('active');
            document.body.classList.remove('menu-open');
        });
    });
})();

// Real-time form validation (critical for UX)
(function() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    const nombreField = document.getElementById('nombre');
    const telefonoField = document.getElementById('telefono');
    const emailField = document.getElementById('email');
    const mensajeField = document.getElementById('mensaje');
    const submitBtn = form.querySelector('button[type="submit"]');

    const validators = {
        nombre: (value) => value.trim().length >= 2,
        telefono: (value) => /^[0-9]{10}$/.test(value.replace(/\s/g, '')),
        email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
        mensaje: (value) => value.trim().length >= 10
    };

    function validateField(field, validatorKey) {
        const value = field.value;
        const fieldWrapper = field.closest('.form-field');
        const isValid = validators[validatorKey](value);

        if (value.length === 0) {
            fieldWrapper.classList.remove('valid', 'invalid');
        } else if (isValid) {
            fieldWrapper.classList.remove('invalid');
            fieldWrapper.classList.add('valid');
        } else {
            fieldWrapper.classList.remove('valid');
            fieldWrapper.classList.add('invalid');
        }

        updateSubmitButton();
        return isValid;
    }

    function isFormValid() {
        return validators.nombre(nombreField.value) &&
               validators.telefono(telefonoField.value) &&
               validators.email(emailField.value) &&
               validators.mensaje(mensajeField.value);
    }

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

    nombreField.addEventListener('input', () => validateField(nombreField, 'nombre'));
    nombreField.addEventListener('blur', () => validateField(nombreField, 'nombre'));

    telefonoField.addEventListener('input', () => {
        telefonoField.value = telefonoField.value.replace(/\D/g, '');
        validateField(telefonoField, 'telefono');
    });
    telefonoField.addEventListener('blur', () => validateField(telefonoField, 'telefono'));

    emailField.addEventListener('input', () => validateField(emailField, 'email'));
    emailField.addEventListener('blur', () => validateField(emailField, 'email'));

    mensajeField.addEventListener('input', () => validateField(mensajeField, 'mensaje'));
    mensajeField.addEventListener('blur', () => validateField(mensajeField, 'mensaje'));

    updateSubmitButton();
})();

// Form submission (critical for conversion)
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
            nombre, telefono, email, mensaje,
            source: 'homepage_form',
            url: window.location.href
        };

        if (window.dataLayer) {
            window.dataLayer.push({
                'event': 'generate_lead',
                'form_name': 'contact_form_homepage',
                'method': 'netlify_forms',
                'value': 1,
                'currency': 'MXN'
            });
        }

        try {
            const leads = JSON.parse(localStorage.getItem('electricista_leads') || '[]');
            leads.push(leadData);
            localStorage.setItem('electricista_leads', JSON.stringify(leads));
        } catch (e) {}

        try {
            const response = await fetch('/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: new URLSearchParams(formData).toString()
            });

            if (response.ok) {
                const whatsappMessage = `Hola! Solicito cotización:\n\nNombre: ${nombre}\nTel: ${telefono}\nEmail: ${email}\nMensaje: ${mensaje}`;
                window.open(`https://wa.me/526673922273?text=${encodeURIComponent(whatsappMessage)}`, '_blank');
                window.location.href = '/gracias';
            } else {
                throw new Error('Failed');
            }
        } catch (error) {
            alert('Formulario enviado. Te redirigiremos a WhatsApp.');
            const whatsappMessage = `Hola! Solicito cotización:\n\nNombre: ${nombre}\nTel: ${telefono}\nEmail: ${email}\nMensaje: ${mensaje}`;
            window.location.href = `https://wa.me/526673922273?text=${encodeURIComponent(whatsappMessage)}`;
        }
    });
})();

// ==========================================
// DEFERRED - Non-critical tracking & features
// ==========================================

deferIdle(() => {
    // WhatsApp tracking
    document.querySelectorAll('a[href^="https://wa.me"]').forEach(link => {
        link.addEventListener('click', function() {
            if (window.dataLayer) {
                window.dataLayer.push({
                    'event': 'whatsapp_click',
                    'location': this.closest('section')?.id || 'unknown',
                    'page_location': window.location.pathname
                });
            }
        });
    });

    // Phone call tracking
    document.querySelectorAll('a[href^="tel:"]').forEach(link => {
        link.addEventListener('click', function() {
            if (window.dataLayer) {
                window.dataLayer.push({
                    'event': 'phone_click',
                    'location': this.closest('section')?.id || 'unknown',
                    'page_location': window.location.pathname
                });
            }
        });
    });

    // Scroll depth tracking
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

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                window.scrollTo({ top: target.offsetTop - 80, behavior: 'smooth' });
            }
        });
    });

    // Fade-in animation on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    document.querySelectorAll('.card, .section').forEach(el => observer.observe(el));

    // Service Worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/sw.js').catch(() => {});
    }

    // DataLayer page view
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({
        'event': 'page_view',
        'page_title': document.title,
        'page_location': window.location.href,
        'page_path': window.location.pathname
    });
});

// Exit Intent Popup (deferred further)
deferIdle(() => {
    const popup = document.getElementById('exit-intent-popup');
    if (!popup) return;

    let popupShown = false;
    const POPUP_DELAY = 30000;
    const SESSION_KEY = 'exitPopupShown';

    if (sessionStorage.getItem(SESSION_KEY)) return;

    function showPopup() {
        if (popupShown) return;
        popupShown = true;
        sessionStorage.setItem(SESSION_KEY, 'true');
        popup.style.display = 'flex';
        document.body.style.overflow = 'hidden';
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

    const closeBtn = popup.querySelector('.exit-popup-close');
    if (closeBtn) closeBtn.addEventListener('click', hidePopup);
    popup.addEventListener('click', function(e) { if (e.target === popup) hidePopup(); });
    document.addEventListener('keydown', function(e) { if (e.key === 'Escape') hidePopup(); });

    if (!isMobile()) {
        document.addEventListener('mouseleave', function(e) { if (e.clientY < 10) showPopup(); });
    }

    if (isMobile()) {
        setTimeout(showPopup, POPUP_DELAY);
        history.pushState(null, '', location.href);
        window.addEventListener('popstate', function() {
            if (!popupShown) {
                showPopup();
                history.pushState(null, '', location.href);
            }
        });
    }
}, 2500);
