// Main JavaScript - Electricista Culiacán Pro
// Loaded with defer for optimal performance
// Last updated: 2026-02-16

// Mobile menu toggle with scroll position preservation
(function() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.nav-menu');
    if (!mobileMenuBtn || !navMenu) return;

    let scrollY = 0;

    function openMenu() {
        scrollY = window.scrollY;
        document.body.style.top = '-' + scrollY + 'px';
        document.body.classList.add('menu-open');
        navMenu.classList.add('active');
        mobileMenuBtn.classList.add('active');
        mobileMenuBtn.setAttribute('aria-expanded', 'true');
        mobileMenuBtn.setAttribute('aria-label', 'Cerrar menú de navegación');
    }

    function closeMenu() {
        const savedScrollY = scrollY;
        document.body.classList.remove('menu-open');
        document.body.style.top = '';
        navMenu.classList.remove('active');
        mobileMenuBtn.classList.remove('active');
        mobileMenuBtn.setAttribute('aria-expanded', 'false');
        mobileMenuBtn.setAttribute('aria-label', 'Abrir menú de navegación');
        window.scrollTo(0, savedScrollY);
    }

    mobileMenuBtn.addEventListener('click', () => {
        if (document.body.classList.contains('menu-open')) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    // Close mobile menu when clicking a link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', closeMenu);
    });
})();

// Nav scroll – fondo solido al hacer scroll
(function() {
    var nav = document.querySelector('.nav');
    if (!nav) return;

    var ticking = false;

    function updateNav() {
        if (window.scrollY > 50) {
            nav.classList.add('nav-scrolled');
        } else {
            nav.classList.remove('nav-scrolled');
        }
        ticking = false;
    }

    window.addEventListener('scroll', function() {
        if (!ticking) {
            requestAnimationFrame(updateNav);
            ticking = true;
        }
    }, { passive: true });

    updateNav();
})();

// Urgency indicator - mensaje dinamico segun hora del dia
(function() {
    var el = document.getElementById('urgency-text');
    if (!el) return;

    var h = new Date().getHours();
    if (h >= 7 && h < 22) {
        el.textContent = 'Disponible ahora – respuesta en ~5 min';
    } else {
        el.textContent = 'Servicio nocturno activo';
    }
})();

// Real-time form validation
(function() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    // Tomamos el control de la validación (mensajes accesibles propios)
    // en vez del bocadillo nativo del navegador.
    form.noValidate = true;

    const nombreField = document.getElementById('nombre');
    const telefonoField = document.getElementById('telefono');
    const emailField = document.getElementById('email');
    const mensajeField = document.getElementById('mensaje');

    const validators = {
        nombre: (value) => value.trim().length >= 2,
        telefono: (value) => /^[0-9]{10}$/.test(value.replace(/\s/g, '')),
        email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
        mensaje: (value) => value.trim().length >= 10
    };

    const errorMessages = {
        nombre: 'Escribe tu nombre completo (mínimo 2 caracteres).',
        telefono: 'El teléfono debe tener 10 dígitos.',
        email: 'Escribe un email válido.',
        mensaje: 'Describe tu problema o servicio (mínimo 10 caracteres).'
    };

    const fieldsByKey = {
        nombre: nombreField,
        telefono: telefonoField,
        email: emailField,
        mensaje: mensajeField
    };

    // Estilos mínimos de accesibilidad, inyectados una sola vez desde JS
    // (no se toca ninguna hoja CSS).
    if (!document.getElementById('form-a11y-css')) {
        const a11yStyle = document.createElement('style');
        a11yStyle.id = 'form-a11y-css';
        a11yStyle.textContent =
            '.field-error{color:#C2410C;font-size:0.9rem;margin-top:0.25rem;display:block;}' +
            '.field-error:empty{display:none;}' +
            '.form-errors{color:#C2410C;font-size:0.9rem;margin:0 0 1rem;}' +
            '.form-errors:empty{display:none;}';
        document.head.appendChild(a11yStyle);
    }

    // Un <span class="field-error"> por campo, dentro de su contenedor.
    const errorElsByKey = {};
    Object.keys(fieldsByKey).forEach(function(key) {
        const field = fieldsByKey[key];
        const wrapper = field.closest('.form-field') || field.parentNode;
        const errorId = key + '-error';
        let errorEl = document.getElementById(errorId);
        if (!errorEl) {
            errorEl = document.createElement('span');
            errorEl.className = 'field-error';
            errorEl.id = errorId;
            wrapper.appendChild(errorEl);
        }
        field.setAttribute('aria-describedby', errorId);
        errorElsByKey[key] = errorEl;
    });

    // Región resumen de errores al inicio del formulario.
    let formErrors = form.querySelector('.form-errors');
    if (!formErrors) {
        formErrors = document.createElement('div');
        formErrors.className = 'form-errors';
        formErrors.setAttribute('role', 'alert');
        formErrors.setAttribute('aria-live', 'polite');
        form.insertBefore(formErrors, form.firstChild);
    }

    let submitAttempted = false;

    function validateField(field, validatorKey) {
        const value = field.value;
        const fieldWrapper = field.closest('.form-field');
        const isValid = validators[validatorKey](value);
        const errorEl = errorElsByKey[validatorKey];

        if (value.length === 0 && !submitAttempted) {
            fieldWrapper.classList.remove('valid', 'invalid');
            field.removeAttribute('aria-invalid');
            errorEl.textContent = '';
        } else if (isValid) {
            fieldWrapper.classList.remove('invalid');
            fieldWrapper.classList.add('valid');
            field.setAttribute('aria-invalid', 'false');
            errorEl.textContent = '';
        } else {
            fieldWrapper.classList.remove('valid');
            fieldWrapper.classList.add('invalid');
            field.setAttribute('aria-invalid', 'true');
            errorEl.textContent = errorMessages[validatorKey];
        }

        return isValid;
    }

    // Tras un intento de envío fallido, si el usuario corrige todos los
    // campos sin volver a enviar, el resumen accesible también se limpia.
    function refreshFormErrorsSummary() {
        if (!submitAttempted) return;
        const stillInvalid = Object.keys(fieldsByKey).some(function(key) {
            return !validators[key](fieldsByKey[key].value);
        });
        if (!stillInvalid) {
            formErrors.textContent = '';
        }
    }

    nombreField.addEventListener('input', () => { validateField(nombreField, 'nombre'); refreshFormErrorsSummary(); });
    nombreField.addEventListener('blur', () => { validateField(nombreField, 'nombre'); refreshFormErrorsSummary(); });

    telefonoField.addEventListener('input', () => {
        telefonoField.value = telefonoField.value.replace(/\D/g, '');
        validateField(telefonoField, 'telefono');
        refreshFormErrorsSummary();
    });
    telefonoField.addEventListener('blur', () => { validateField(telefonoField, 'telefono'); refreshFormErrorsSummary(); });

    emailField.addEventListener('input', () => { validateField(emailField, 'email'); refreshFormErrorsSummary(); });
    emailField.addEventListener('blur', () => { validateField(emailField, 'email'); refreshFormErrorsSummary(); });

    mensajeField.addEventListener('input', () => { validateField(mensajeField, 'mensaje'); refreshFormErrorsSummary(); });
    mensajeField.addEventListener('blur', () => { validateField(mensajeField, 'mensaje'); refreshFormErrorsSummary(); });

    // Al enviar: si algo es inválido, bloquea el envío, muestra el resumen
    // accesible y mueve el foco al primer campo con error. Si todo es
    // válido, deja pasar el envío tal como hoy (lo maneja el otro listener).
    form.addEventListener('submit', function(e) {
        submitAttempted = true;

        const results = {
            nombre: validateField(nombreField, 'nombre'),
            telefono: validateField(telefonoField, 'telefono'),
            email: validateField(emailField, 'email'),
            mensaje: validateField(mensajeField, 'mensaje')
        };

        const allValid = results.nombre && results.telefono && results.email && results.mensaje;

        if (!allValid) {
            e.preventDefault();
            if (typeof e.stopImmediatePropagation === 'function') {
                e.stopImmediatePropagation();
            }
            formErrors.textContent = 'Hay campos con errores: corrige la información marcada antes de enviar.';
            const firstInvalidKey = Object.keys(results).filter(function(key) {
                return !results[key];
            })[0];
            if (firstInvalidKey) {
                fieldsByKey[firstInvalidKey].focus();
            }
            return false;
        }

        formErrors.textContent = '';
    });
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
                const whatsappMessage = `Hola! Solicito cotización de servicios eléctricos:\n\n` +
                                      `Nombre: ${nombre}\n` +
                                      `Teléfono: ${telefono}\n` +
                                      `Email: ${email}\n` +
                                      `Mensaje: ${mensaje}`;
                const whatsappURL = `https://wa.me/526673922273?text=${encodeURIComponent(whatsappMessage)}`;
                window.open(whatsappURL, '_blank');
                window.location.href = '/gracias/';
            } else {
                throw new Error('Netlify form submission failed');
            }
        } catch (error) {
            alert('No pudimos enviar el formulario. Te llevamos a WhatsApp para atenderte de inmediato.');
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

// CTA fijo con tracking
(function(){
  var PATH = location.pathname;
  var wa = document.getElementById("cta-whatsapp");
  var tl = document.getElementById("cta-llamar");

  window.dataLayer = window.dataLayer || [];
  function pushEvt(type, label) {
    try {
      window.dataLayer.push({
        event: "cta_click",
        cta_type: type,
        cta_label: label,
        page: PATH
      });
    } catch(e) {}
  }

  if (wa) {
    wa.addEventListener("click", function() {
      pushEvt("whatsapp", "cta_floating");
    });
  }
  if (tl) {
    tl.addEventListener("click", function() {
      pushEvt("llamar", "cta_floating");
    });
  }
})();

// Mini footer nav tracking
(function(){
  window.dataLayer=window.dataLayer||[];
  document.querySelectorAll(".site-mini-nav a").forEach(function(a){
    if(a.dataset.navBound==="1") return; a.dataset.navBound="1";
    a.addEventListener("click", function(){
      try{ dataLayer.push({event:"nav_click", nav_label:a.textContent.trim(), nav_href:a.getAttribute("href"), page:location.pathname}); }catch(e){}
    });
  });
})();

// Tracking de tarjetas SEO - diferido con requestIdleCallback
(typeof requestIdleCallback === 'function' ? requestIdleCallback : setTimeout)(function() {
  document.querySelectorAll('.seo-card[data-event="click_seo_card"]').forEach(function(card) {
    card.addEventListener('click', function(e) {
      var cardName = this.getAttribute('data-card-name');
      var cardPosition = this.getAttribute('data-card-position');
      var cardHref = this.getAttribute('href');

      try {
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({
          'event': 'click_seo_card',
          'card_name': cardName,
          'card_position': cardPosition,
          'card_url': cardHref,
          'page_location': window.location.pathname
        });
      } catch(e) {}
    });
  });

  var scrollDepths = [25, 50, 75, 90];
  var scrollTracked = {};
  var scrollTicking = false;
  var cachedScrollableHeight = document.documentElement.scrollHeight - window.innerHeight;

  window.addEventListener('resize', function() {
    cachedScrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
  }, { passive: true });

  window.addEventListener('scroll', function() {
    if (scrollTicking) return;
    scrollTicking = true;
    requestAnimationFrame(function() {
      var scrollPercent = Math.round((window.scrollY / cachedScrollableHeight) * 100);
      for (var i = 0; i < scrollDepths.length; i++) {
        var depth = scrollDepths[i];
        if (scrollPercent >= depth && !scrollTracked[depth]) {
          scrollTracked[depth] = true;
          try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
              'event': 'scroll_depth',
              'scroll_percentage': depth,
              'page_location': window.location.pathname
            });
          } catch(e) {}
        }
      }
      scrollTicking = false;
    });
  }, { passive: true });
})();

// Exit-Intent Popup - versión simplificada (móvil: back button)
(typeof requestIdleCallback === 'function' ? requestIdleCallback : setTimeout)(function() {
    var popup = document.getElementById('exit-intent-popup');
    if (!popup) return;

    var closeBtn = document.querySelector('.exit-popup-close');
    var whatsappBtn = document.getElementById('exit-popup-whatsapp');
    var phoneBtn = document.getElementById('exit-popup-phone');
    var popupShown = false;
    var SESSION_KEY = 'exitPopupShown';

    // Ya se mostró en esta sesión? Salir
    if (sessionStorage.getItem(SESSION_KEY)) return;

    function isMobile() {
        return window.innerWidth <= 768 || 'ontouchstart' in window;
    }

    function showPopup() {
        if (popupShown) return;
        popupShown = true;
        sessionStorage.setItem(SESSION_KEY, 'true');
        popup.style.display = 'flex';
        document.body.style.overflow = 'hidden';

        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'exit_intent_shown',
                'page_location': window.location.pathname,
                'trigger': isMobile() ? 'mobile_back' : 'desktop_mouseleave'
            });
        } catch(e) {}
    }

    function hidePopup() {
        popup.style.display = 'none';
        document.body.style.overflow = '';

        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'exit_intent_closed',
                'page_location': window.location.pathname
            });
        } catch(e) {}
    }

    // DESKTOP: Mouse leave detection
    if (!isMobile()) {
        document.addEventListener('mouseleave', function(e) {
            if (e.clientY < 10) showPopup();
        });
    }

    // MOBILE: Detectar botón back (sin timer de 30s)
    if (isMobile()) {
        history.pushState(null, '', location.href);
        window.addEventListener('popstate', function() {
            if (!popupShown) {
                showPopup();
                history.pushState(null, '', location.href);
            }
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener('click', function(e) {
            e.preventDefault();
            hidePopup();
        });
    }

    popup.addEventListener('click', function(e) {
        if (e.target === popup) hidePopup();
    });

    document.addEventListener('keydown', function(e) {
        if (popup.style.display === 'flex' && e.key === 'Escape') hidePopup();
    });

    if (whatsappBtn) {
        whatsappBtn.addEventListener('click', function() {
            try {
                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'exit_intent_whatsapp_click',
                    'page_location': window.location.pathname
                });
            } catch(e) {}
        });
    }

    if (phoneBtn) {
        phoneBtn.addEventListener('click', function() {
            try {
                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'exit_intent_phone_click',
                    'page_location': window.location.pathname
                });
            } catch(e) {}
        });
    }
}, 2500);

// Service Worker Registration
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {})
            .catch(err => {});
    });
}

// Bottom Sheet Cotización Móvil
(typeof requestIdleCallback === 'function' ? requestIdleCallback : setTimeout)(function() {
    var trigger = document.getElementById('quote-trigger');
    var overlay = document.getElementById('quote-overlay');
    var sheet = document.getElementById('quote-sheet');
    var closeBtn = document.querySelector('.quote-sheet-close');
    var form = document.getElementById('quote-form');
    var chips = document.querySelectorAll('.quote-chip');

    if (!trigger || !sheet) return;

    var selectedService = '';
    var scrollY = 0;

    var focusableElements = sheet.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    var firstFocusable = focusableElements[0];
    var lastFocusable = focusableElements[focusableElements.length - 1];

    function openSheet() {
        scrollY = window.scrollY;
        document.body.classList.add('quote-sheet-open');
        overlay.classList.add('active');
        sheet.classList.add('active');
        sheet.setAttribute('aria-hidden', 'false');
        overlay.setAttribute('aria-hidden', 'false');

        var firstInput = sheet.querySelector('input');
        if (firstInput) {
            setTimeout(function() { firstInput.focus(); }, 100);
        }

        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'quote_sheet_open',
                'page_location': window.location.pathname
            });
        } catch(e) {}
    }

    function closeSheet() {
        document.body.classList.remove('quote-sheet-open');
        overlay.classList.remove('active');
        sheet.classList.remove('active');
        sheet.setAttribute('aria-hidden', 'true');
        overlay.setAttribute('aria-hidden', 'true');
        window.scrollTo(0, scrollY);
        trigger.focus();
    }

    trigger.addEventListener('click', openSheet);
    overlay.addEventListener('click', closeSheet);

    if (closeBtn) {
        closeBtn.addEventListener('click', closeSheet);
    }

    var touchStartY = 0;
    var touchCurrentY = 0;
    var handle = sheet.querySelector('.quote-sheet-handle');

    if (handle) {
        handle.addEventListener('touchstart', function(e) {
            touchStartY = e.touches[0].clientY;
        }, { passive: true });

        handle.addEventListener('touchmove', function(e) {
            touchCurrentY = e.touches[0].clientY;
            var deltaY = touchCurrentY - touchStartY;
            if (deltaY > 0) {
                sheet.style.transform = 'translateY(' + deltaY + 'px)';
            }
        }, { passive: true });

        handle.addEventListener('touchend', function() {
            var deltaY = touchCurrentY - touchStartY;
            if (deltaY > 100) closeSheet();
            sheet.style.transform = '';
            touchStartY = 0;
            touchCurrentY = 0;
        });
    }

    document.addEventListener('keydown', function(e) {
        if (!sheet.classList.contains('active')) return;

        if (e.key === 'Escape') {
            closeSheet();
            return;
        }

        if (e.key === 'Tab') {
            if (e.shiftKey) {
                if (document.activeElement === firstFocusable) {
                    e.preventDefault();
                    lastFocusable.focus();
                }
            } else {
                if (document.activeElement === lastFocusable) {
                    e.preventDefault();
                    firstFocusable.focus();
                }
            }
        }
    });

    chips.forEach(function(chip) {
        chip.addEventListener('click', function() {
            chips.forEach(function(c) { c.classList.remove('selected'); });
            this.classList.add('selected');
            selectedService = this.getAttribute('data-service');
        });
    });

    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            var nombre = document.getElementById('quote-nombre').value.trim();
            var whatsapp = document.getElementById('quote-whatsapp').value.trim();
            var mensaje = document.getElementById('quote-mensaje').value.trim();

            if (!nombre || !whatsapp) {
                alert('Por favor completa los campos obligatorios.');
                return;
            }

            var msg = '¡Hola! Solicito cotización:\n\n';
            msg += 'Nombre: ' + nombre + '\n';
            msg += 'WhatsApp: ' + whatsapp + '\n';
            if (selectedService) msg += 'Servicio: ' + selectedService + '\n';
            if (mensaje) msg += 'Detalle: ' + mensaje + '\n';

            var whatsappURL = 'https://wa.me/526673922273?text=' + encodeURIComponent(msg);

            try {
                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'generate_lead',
                    'form_name': 'quote_sheet_mobile',
                    'method': 'whatsapp',
                    'service': selectedService || 'no_especificado',
                    'value': 1,
                    'currency': 'MXN'
                });
            } catch(e) {}

            try {
                var leads = JSON.parse(localStorage.getItem('electricista_leads') || '[]');
                leads.push({
                    timestamp: new Date().toISOString(),
                    nombre: nombre,
                    whatsapp: whatsapp,
                    servicio: selectedService,
                    mensaje: mensaje,
                    source: 'quote_sheet_mobile',
                    url: window.location.href
                });
                localStorage.setItem('electricista_leads', JSON.stringify(leads));
            } catch(e) {}

            window.open(whatsappURL, '_blank');
            closeSheet();
            form.reset();
            chips.forEach(function(c) { c.classList.remove('selected'); });
            selectedService = '';
        });
    }

    var whatsappInput = document.getElementById('quote-whatsapp');
    if (whatsappInput) {
        whatsappInput.addEventListener('input', function() {
            this.value = this.value.replace(/\D/g, '');
        });
    }
})();

// Hide floating buttons in critical sections
(typeof requestIdleCallback === 'function' ? requestIdleCallback : setTimeout)(function() {
    var floatingBtns = document.querySelectorAll('.floating-btn');
    var quoteTrigger = document.getElementById('quote-trigger');
    if (!floatingBtns.length) return;

    var criticalSections = document.querySelectorAll('#contacto, .footer, .contact-form, .map-embed');
    if (!criticalSections.length) return;

    var isHidden = false;
    var menuOpen = false;
    var sheetOpen = false;

    var bodyObserver = new MutationObserver(function(mutations) {
        menuOpen = document.body.classList.contains('menu-open');
        sheetOpen = document.body.classList.contains('quote-sheet-open');
    });
    bodyObserver.observe(document.body, { attributes: true, attributeFilter: ['class'] });

    function updateVisibility(shouldHide) {
        if (shouldHide === isHidden) return;
        isHidden = shouldHide;
        var opacity = shouldHide ? '0' : '1';
        var pointer = shouldHide ? 'none' : 'auto';
        for (var i = 0; i < floatingBtns.length; i++) {
            floatingBtns[i].style.cssText = 'opacity:' + opacity + ';pointer-events:' + pointer;
        }
        if (quoteTrigger && !sheetOpen) {
            quoteTrigger.style.cssText = 'opacity:' + opacity + ';pointer-events:' + pointer;
        }
    }

    var observer = new IntersectionObserver(function(entries) {
        var anyVisible = false;
        for (var i = 0; i < entries.length; i++) {
            if (entries[i].isIntersecting && entries[i].intersectionRatio > 0.3) {
                anyVisible = true;
                break;
            }
        }
        if (!menuOpen) updateVisibility(anyVisible);
    }, {
        threshold: [0, 0.3, 0.5],
        rootMargin: '0px 0px -100px 0px'
    });

    criticalSections.forEach(function(section) {
        observer.observe(section);
    });
})();

// Contact link click tracking
(function() {
    document.addEventListener('click', function(e) {
        var link = e.target.closest('a[href^="tel:"], a[href*="wa.me"]');
        if (!link) return;
        var href = link.getAttribute('href');
        var tipo = href.startsWith('tel:') ? 'phone' : 'whatsapp';
        var numero = href.replace(/[^\d]/g, '');
        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'contact_link_click',
                'contact_type': tipo,
                'phone_number': numero,
                'page_location': window.location.pathname,
                'link_text': link.textContent.trim().substring(0, 50),
                'link_location': link.getBoundingClientRect().y > window.innerHeight/2 ? 'below_fold' : 'above_fold'
            });
        } catch(e) {}
    }, true);
})();

// Time-on-page milestone tracking
(function() {
    var timeOnPageSegments = [30, 60, 120, 300];
    var timeTracked = {};
    var startTime = Date.now();
    setInterval(function() {
        var currentTime = Math.floor((Date.now() - startTime) / 1000);
        for (var i = 0; i < timeOnPageSegments.length; i++) {
            var segment = timeOnPageSegments[i];
            if (currentTime >= segment && !timeTracked[segment]) {
                timeTracked[segment] = true;
                try {
                    window.dataLayer = window.dataLayer || [];
                    window.dataLayer.push({
                        'event': 'page_time_milestone',
                        'time_seconds': segment,
                        'page_location': window.location.pathname
                    });
                } catch(e) {}
            }
        }
    }, 1000);
})();

// Internal link click tracking
(function() {
    var mainNavLinks = document.querySelectorAll('a[href^="/servicios/"], a[href^="/blog/"], a[href^="/electricista-colonias/"]');
    mainNavLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            var href = this.getAttribute('href');
            var text = this.textContent.trim().substring(0, 100);
            var pageType = 'internal_link';
            if (href.includes('/servicios/')) pageType = 'service_page';
            if (href.includes('/blog/')) pageType = 'blog_page';
            if (href.includes('/electricista-colonias/')) pageType = 'colony_page';
            try {
                window.dataLayer = window.dataLayer || [];
                window.dataLayer.push({
                    'event': 'internal_link_click',
                    'link_text': text,
                    'link_url': href,
                    'page_type': pageType,
                    'page_location': window.location.pathname
                });
            } catch(e) {}
        });
    });
})();

// Page view type tracking
(function() {
    var pathname = window.location.pathname;
    if (pathname.includes('/servicios/')) {
        var serviceMatch = pathname.match(/servicios\/([^\/]+)/);
        var serviceName = serviceMatch ? serviceMatch[1].replace(/-/g, ' ') : 'unknown';
        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'view_service_page',
                'service_name': serviceName,
                'page_location': pathname
            });
        } catch(e) {}
    }
    if (pathname.includes('/electricista-colonias-culiacan/')) {
        var colonyMatch = pathname.match(/electricista-colonias-culiacan\/([^\/]+)/);
        var colonyName = colonyMatch ? colonyMatch[1].replace(/-/g, ' ') : 'unknown';
        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'view_colony_page',
                'colony_name': colonyName,
                'page_location': pathname
            });
        } catch(e) {}
    }
    if (pathname.includes('/blog/')) {
        var postMatch = pathname.match(/blog\/([^\/]+)/);
        var postTitle = postMatch ? postMatch[1].replace(/-/g, ' ') : 'unknown';
        try {
            window.dataLayer = window.dataLayer || [];
            window.dataLayer.push({
                'event': 'view_blog_post',
                'post_title': postTitle,
                'page_location': pathname
            });
        } catch(e) {}
    }
})();
