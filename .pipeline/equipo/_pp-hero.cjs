// Barrido del coordinador: posición del primer wa.me y tel: visibles por página, a 375 y 1280.
// Uso: node _pp-hero.cjs <ruta-relativa/> [...]
const puppeteer = require('/Users/openclaw/Sitios Web/Electricista Culiacán/node_modules/puppeteer');
const BASE = 'http://127.0.0.1:8097/';
(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const out = [];
  for (const rel of process.argv.slice(2)) {
    const row = { rel };
    for (const w of [375, 1280]) {
      const page = await browser.newPage();
      const errs = [];
      page.on('pageerror', e => errs.push(String(e).slice(0, 80)));
      await page.setViewport({ width: w, height: w === 375 ? 740 : 800 });
      await page.goto(BASE + rel.replace('index.html', ''), { waitUntil: 'networkidle0', timeout: 30000 });
      const m = await page.evaluate(() => {
        const vis = el => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.display !== 'none' && cs.visibility !== 'hidden'; };
        const first = sel => { for (const a of document.querySelectorAll(sel)) { if (vis(a) && !a.closest('.floating-btn,.floating-cta,[class*=floating]')) { const r = a.getBoundingClientRect(); return { top: Math.round(r.top + scrollY), h: Math.round(r.height), w: Math.round(r.width), color: getComputedStyle(a).color }; } } return null; };
        return { wa: first('a[href*="wa.me"]'), tel: first('a[href^="tel:"]'), scrollW: document.documentElement.scrollWidth, title: document.title.slice(0, 60) };
      });
      row[w] = { ...m, errs: errs.length };
      await page.close();
    }
    out.push(row);
    console.log(JSON.stringify(row));
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
