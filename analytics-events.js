// Google Analytics 4 - Custom Event Tracking
// Electricista Culiacán Pro

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', function() {

  // Track WhatsApp clicks (Main floating button)
  const whatsappBtn = document.getElementById('cta-whatsapp');
  if (whatsappBtn) {
    whatsappBtn.addEventListener('click', function() {
      gtag('event', 'contact_whatsapp', {
        'event_category': 'Conversion',
        'event_label': 'WhatsApp Floating Button',
        'value': 1
      });
    });
  }

  // Track WhatsApp clicks (Exit popup)
  const exitWhatsappBtn = document.getElementById('exit-popup-whatsapp');
  if (exitWhatsappBtn) {
    exitWhatsappBtn.addEventListener('click', function() {
      gtag('event', 'contact_whatsapp', {
        'event_category': 'Conversion',
        'event_label': 'WhatsApp Exit Popup',
        'value': 1
      });
    });
  }

  // Track phone calls (Main floating button)
  const phoneBtn = document.getElementById('cta-llamar');
  if (phoneBtn) {
    phoneBtn.addEventListener('click', function() {
      gtag('event', 'contact_phone', {
        'event_category': 'Conversion',
        'event_label': 'Phone Floating Button',
        'value': 1
      });
    });
  }

  // Track phone calls (Exit popup)
  const exitPhoneBtn = document.getElementById('exit-popup-phone');
  if (exitPhoneBtn) {
    exitPhoneBtn.addEventListener('click', function() {
      gtag('event', 'contact_phone', {
        'event_category': 'Conversion',
        'event_label': 'Phone Exit Popup',
        'value': 1
      });
    });
  }

  // Track all WhatsApp links (hero, services, etc)
  const allWhatsappLinks = document.querySelectorAll('a[href*="wa.me"]');
  allWhatsappLinks.forEach(function(link) {
    if (!link.id || (link.id !== 'cta-whatsapp' && link.id !== 'exit-popup-whatsapp')) {
      link.addEventListener('click', function() {
        const linkText = this.textContent.trim().substring(0, 50);
        gtag('event', 'contact_whatsapp', {
          'event_category': 'Conversion',
          'event_label': 'WhatsApp Link - ' + linkText,
          'value': 1
        });
      });
    }
  });

  // Track all phone links
  const allPhoneLinks = document.querySelectorAll('a[href^="tel:"]');
  allPhoneLinks.forEach(function(link) {
    if (!link.id || (link.id !== 'cta-llamar' && link.id !== 'exit-popup-phone')) {
      link.addEventListener('click', function() {
        const linkText = this.textContent.trim().substring(0, 50);
        gtag('event', 'contact_phone', {
          'event_category': 'Conversion',
          'event_label': 'Phone Link - ' + linkText,
          'value': 1
        });
      });
    }
  });

  // Track service page clicks
  const serviceLinks = document.querySelectorAll('a[href*="/servicios/"]');
  serviceLinks.forEach(function(link) {
    link.addEventListener('click', function(e) {
      const serviceName = this.getAttribute('href').split('/').filter(Boolean).pop();
      gtag('event', 'view_service', {
        'event_category': 'Engagement',
        'event_label': serviceName,
        'value': 0
      });
    });
  });

  // Track navigation menu clicks
  const navLinks = document.querySelectorAll('.nav-link');
  navLinks.forEach(function(link) {
    link.addEventListener('click', function() {
      const linkText = this.textContent.trim();
      gtag('event', 'navigation_click', {
        'event_category': 'Navigation',
        'event_label': linkText,
        'value': 0
      });
    });
  });

  // Track exit popup shown
  const exitPopup = document.getElementById('exit-intent-popup');
  if (exitPopup) {
    const observer = new MutationObserver(function(mutations) {
      mutations.forEach(function(mutation) {
        if (mutation.target.style.display !== 'none') {
          gtag('event', 'exit_popup_shown', {
            'event_category': 'Engagement',
            'event_label': 'Exit Intent Triggered',
            'value': 0
          });
        }
      });
    });
    observer.observe(exitPopup, { attributes: true, attributeFilter: ['style'] });
  }

  // Track scroll depth (25%, 50%, 75%, 100%)
  let scrollMarkers = {25: false, 50: false, 75: false, 100: false};
  window.addEventListener('scroll', function() {
    const scrollPercent = Math.round((window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100);

    Object.keys(scrollMarkers).forEach(function(marker) {
      if (scrollPercent >= marker && !scrollMarkers[marker]) {
        scrollMarkers[marker] = true;
        gtag('event', 'scroll_depth', {
          'event_category': 'Engagement',
          'event_label': marker + '%',
          'value': parseInt(marker)
        });
      }
    });
  });

});
