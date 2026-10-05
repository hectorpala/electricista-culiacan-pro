/* medicion.js — eventos de GA4 (vía dataLayer → GTM-5Z2QRZ5Q → G-7CML8QYBGQ) para TODAS las
   páginas, incluidos los blogs que no cargan main.min.js. Misma medición que el sitio
   hermano (1/2-oct-2026): generate_lead {metodo, ubicacion, form_name}, faq_open {pregunta},
   web_vital {metrica, valor, rating} y la bandera ?interno=1 para no contar al dueño. */
/* Visitas del dueño fuera de GA4: abrir una vez cualquier página con ?interno=1 marca ESTE
   navegador (?interno=0 lo desmarca). ga-disable-<ID> es el apagador oficial de Google y GTM lo
   respeta. Va primero porque GTM carga hasta la interacción o 1.5 s después del load. */
(function() {
try {
var q = location.search.match(/[?&]interno=([01])(?:&|$)/);
if (q) { if (q[1] === '1') localStorage.setItem('ecp_interno', '1'); else localStorage.removeItem('ecp_interno'); }
if (localStorage.getItem('ecp_interno') === '1') {
window['ga-disable-G-7CML8QYBGQ'] = true;
}
} catch (e) {}
})();
/* Lead tracking UNIVERSAL: cualquier clic a WhatsApp o telefono, en CUALQUIER pagina
   (hero, flotantes, inline, paginas de servicio). Empuja generate_lead a dataLayer en el
   momento del clic (queda en la cola aunque GTM cargue diferido). Listener delegado en captura. */
(function() {
  // Dónde está el botón: permite comparar qué CTA convierte (flotante vs hero vs cuerpo...).
  function ubicacion(el) {
    if (el.closest('.floating-btn, .floating-whatsapp, .floating-call')) return 'flotante';
    if (el.closest('[class*="exit-intent"], [id*="exit-intent"]')) return 'exit_intent';
    if (el.closest('nav')) return 'menu';
    if (el.closest('header, .hero, #inicio')) return 'hero';
    if (el.closest('footer')) return 'footer';
    if (el.closest('article')) return 'articulo';
    var sec = el.closest('section[id]');
    return sec ? sec.id : 'cuerpo';
  }
  // BUZÓN (4-oct-2026): si el cliente toca WhatsApp/Llamar antes de que GA4 termine de cargar
  // (~2 s en 4G), el celular se cambia de app y el aviso por GTM se pierde. En ese caso el aviso
  // va DIRECTO a GA4 con sendBeacon, que el navegador entrega aunque la página quede pausada.
  // Si GA4 ya cargó, va por dataLayer → GTM como siempre. Nunca por los dos: no se cuenta doble.
  // Los avisos del buzón llevan ubicacion '<lugar>_rapido' para saber cuántos se rescatan.
  var GA4 = 'G-7CML8QYBGQ';
  function ga4Listo() {
    var g = window.google_tag_manager;
    return !!(g && g[GA4]);
  }
  function galleta(nombre) {
    var m = document.cookie.match('(?:^|; )' + nombre + '=([^;]*)');
    return m ? m[1] : '';
  }
  function buzon(datos) {
    try {
      if (window['ga-disable-' + GA4] || !navigator.sendBeacon) return false;
      var ga = galleta('_ga').split('.');
      var cid = ga.length >= 4 ? ga[2] + '.' + ga[3] : '';
      var nuevo = !cid;
      var ahora = Math.floor(Date.now() / 1000);
      if (nuevo) {
        cid = Math.floor(Math.random() * 2147483647) + '.' + ahora;
        // Misma galleta que usa GA4: si la página sigue viva y GA4 carga, reconoce al visitante.
        document.cookie = '_ga=GA1.1.' + cid + '; max-age=63072000; path=/; domain=' +
          location.hostname.replace(/^www\./, '') + '; SameSite=Lax';
      }
      var ses = galleta('_ga_' + GA4.slice(2)).match(/^GS\d\.\d\.s?(\d+)/);
      var q = {
        v: '2', tid: GA4, cid: cid, sid: ses ? ses[1] : String(ahora), sct: '1', seg: '1',
        _p: String(Math.floor(Math.random() * 1e9)), en: 'generate_lead',
        dl: location.href, dr: document.referrer, dt: document.title,
        ul: (navigator.language || '').toLowerCase(),
        'ep.metodo': datos.metodo, 'ep.ubicacion': datos.ubicacion + '_rapido', 'ep.page': datos.page
      };
      if (datos.form_name) q['ep.form_name'] = datos.form_name;
      if (!ses) { q._ss = '1'; q._nsi = '1'; }
      if (nuevo) q._fv = '1';
      var url = 'https://www.google-analytics.com/g/collect?' + Object.keys(q).map(function(k) {
        return encodeURIComponent(k) + '=' + encodeURIComponent(q[k] == null ? '' : q[k]);
      }).join('&');
      return navigator.sendBeacon(url);
    } catch (err) { return false; }
  }
  function lead(datos) {
    try {
      datos.page = location.pathname;
      if (!ga4Listo() && buzon(datos)) return;
      window.dataLayer = window.dataLayer || [];
      datos.event = 'generate_lead';
      window.dataLayer.push(datos);
    } catch (err) {}
  }
  document.addEventListener('click', function(e) {
    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var metodo = (href.indexOf('wa.me') !== -1 || href.indexOf('api.whatsapp') !== -1) ? 'whatsapp'
               : (href.indexOf('tel:') === 0) ? 'llamada' : null;
    if (!metodo) return;
    lead({ metodo: metodo, ubicacion: ubicacion(a) });
  }, true);
  // Formularios: el evento submit solo llega si pasó la validación del navegador.
  document.addEventListener('submit', function(e) {
    var f = e.target;
    if (!f || f.tagName !== 'FORM') return;
    lead({ metodo: 'formulario', ubicacion: ubicacion(f),
           form_name: f.getAttribute('name') || f.id || 'sin_nombre' });
  }, true);
})();
/* FAQ: qué preguntas abre la gente (= dudas reales que conviene responder arriba). */
(function() {
  function push(texto) {
    try {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({ event: 'faq_open', pregunta: (texto || '').trim().slice(0, 100) });
    } catch (err) {}
  }
  document.addEventListener('toggle', function(e) {
    var d = e.target;
    if (!d || d.tagName !== 'DETAILS' || !d.open) return;
    var s = d.querySelector('summary');
    push(s && s.textContent);
  }, true);
  document.addEventListener('click', function(e) {
    var b = e.target && e.target.closest ? e.target.closest('.faq-question') : null;
    if (!b || b.tagName === 'SUMMARY' || b.getAttribute('aria-expanded') === 'true') return;
    push(b.textContent);
  }, true);
})();
/* Core Web Vitals de visitantes REALES (LCP, CLS, INP), enviados una vez al ocultar la página. */
(function() {
  if (!('PerformanceObserver' in window)) return;
  var lcp = 0, cls = 0, inp = 0, enviado = false;
  var ventana = 0, ini = 0, ult = 0; // CLS = peor ventana (≤5 s, huecos <1 s), como Google
  function obs(tipo, fn, extra) {
    try {
      var o = { type: tipo, buffered: true };
      for (var k in extra) o[k] = extra[k];
      new PerformanceObserver(function(l) { l.getEntries().forEach(fn); }).observe(o);
    } catch (err) {}
  }
  obs('largest-contentful-paint', function(en) { lcp = en.startTime; });
  obs('layout-shift', function(en) {
    if (en.hadRecentInput) return;
    if (ventana && en.startTime - ult < 1000 && en.startTime - ini < 5000) ventana += en.value;
    else { ventana = en.value; ini = en.startTime; }
    ult = en.startTime;
    if (ventana > cls) cls = ventana;
  });
  obs('event', function(en) { if (en.interactionId && en.duration > inp) inp = en.duration; },
      { durationThreshold: 40 });
  function nota(v, bueno, malo) { return v <= bueno ? 'bueno' : v <= malo ? 'mejorable' : 'malo'; }
  function enviar(forzar) {
    if (enviado || (!forzar && document.visibilityState !== 'hidden')) return;
    enviado = true;
    var dl = window.dataLayer = window.dataLayer || [];
    if (lcp) dl.push({ event: 'web_vital', metrica: 'LCP', valor: Math.round(lcp), rating: nota(lcp, 2500, 4000) });
    dl.push({ event: 'web_vital', metrica: 'CLS', valor: Math.round(cls * 1000) / 1000, rating: nota(cls, 0.1, 0.25) });
    if (inp) dl.push({ event: 'web_vital', metrica: 'INP', valor: Math.round(inp), rating: nota(inp, 200, 500) });
  }
  document.addEventListener('visibilitychange', enviar);
  window.addEventListener('pagehide', function() { enviar(true); });
})();
