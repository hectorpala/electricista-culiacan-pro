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
