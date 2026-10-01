const puppeteer = require('/Users/openclaw/Sitios Web/Electricista Culiacán/node_modules/puppeteer');
(async () => {
  const b = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  for (const w of [375, 1280]) {
    const p = await b.newPage();
    await p.setViewport({ width: w, height: 800, isMobile: w === 375 });
    await p.goto('http://127.0.0.1:8097/contacto/', { waitUntil: 'domcontentloaded' });
    await new Promise(r => setTimeout(r, 1000));
    const r = await p.evaluate(() => {
      const out = [];
      for (const a of document.querySelectorAll('a[href*="wa.me"]')) {
        const rc = a.getBoundingClientRect(); const cs = getComputedStyle(a);
        out.push({ top: Math.round(rc.top + scrollY), h: Math.round(rc.height), w: Math.round(rc.width), color: cs.color, bg: cs.backgroundImage.slice(0, 40) || cs.backgroundColor, cls: a.className, pos: cs.position, txt: a.textContent.trim().slice(0, 40) });
      }
      const sheets = [...document.querySelectorAll('link[rel=stylesheet],style')].map(s => s.tagName + ':' + (s.href || s.media || 'inline').slice(-40));
      return { out, sheets };
    });
    console.log(w, JSON.stringify(r, null, 0));
    await p.close();
  }
  await b.close();
})();
