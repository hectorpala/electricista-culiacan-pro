// Service Worker - Electricista Culiacán Pro
// Version: 4.0.0 - Cache optimizado para GitHub Pages
// GitHub Pages tiene cache de 10min, SW compensa con cache local largo

const CACHE_VERSION = 'v6';
const CACHE_NAME = `electricista-culiacan-${CACHE_VERSION}`;

// Assets críticos para precache (LCP/FCP)
const PRECACHE_ASSETS = [
  '/',
  '/index.html',
  '/styles.min.css',
  '/main.min.js',
  '/assets/css/critical.min.css',
  '/assets/fonts/inter-400.woff2',
  '/assets/fonts/inter-600.woff2',
  '/assets/images/optimizadas/hero-mobile-320w.webp',
  '/assets/images/optimizadas/hero-mobile-480w.webp',
  '/assets/images/optimizadas/hero-mobile-640w.webp',
  '/assets/images/optimizadas/hero-electricista-culiacan-800w.webp',
  '/assets/images/optimizadas/logo-128w.webp',
  '/assets/images/optimizadas/logo-256w.webp',
  '/manifest.json'
];

// Patrones para cache dinámico por tipo
const CACHE_PATTERNS = {
  images: /\.(webp|png|jpg|jpeg|svg|ico)$/i,
  fonts: /\.(woff2|woff|ttf)$/i,
  styles: /\.css(\?.*)?$/i,
  scripts: /\.js(\?.*)?$/i
};

// Install - precache assets críticos
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(PRECACHE_ASSETS))
      .then(() => self.skipWaiting())
  );
});

// Activate - limpiar caches viejos
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k.startsWith('electricista-') && k !== CACHE_NAME)
            .map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

// Fetch - Stale-While-Revalidate para assets, Network-First para HTML
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // Solo GET requests del mismo origen
  if (request.method !== 'GET' || !url.origin.includes('electricistaculiacanpro')) return;

  // HTML pages: Network first, fallback to cache
  if (request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(networkFirst(request));
    return;
  }

  // Assets estáticos: Stale-While-Revalidate (rápido + actualizado)
  if (isStaticAsset(url.pathname)) {
    event.respondWith(staleWhileRevalidate(request));
    return;
  }

  // Default: cache first
  event.respondWith(cacheFirst(request));
});

// Estrategia: Cache First
async function cacheFirst(request) {
  const cached = await caches.match(request);
  if (cached) return cached;

  try {
    const response = await fetch(request);
    if (response.ok) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, response.clone());
    }
    return response;
  } catch {
    return new Response('Offline', { status: 503 });
  }
}

// Estrategia: Network First (para HTML)
async function networkFirst(request) {
  try {
    const response = await fetch(request);
    if (response.ok) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, response.clone());
    }
    return response;
  } catch {
    const cached = await caches.match(request);
    return cached || new Response('Offline', { status: 503 });
  }
}

// Estrategia: Stale-While-Revalidate (para assets)
async function staleWhileRevalidate(request) {
  const cache = await caches.open(CACHE_NAME);
  const cached = await cache.match(request);

  // Actualizar en background
  const fetchPromise = fetch(request).then(response => {
    if (response.ok) cache.put(request, response.clone());
    return response;
  }).catch(() => null);

  // Retornar cache inmediatamente si existe
  return cached || fetchPromise;
}

// Detectar si es asset estático
function isStaticAsset(pathname) {
  return Object.values(CACHE_PATTERNS).some(pattern => pattern.test(pathname));
}
