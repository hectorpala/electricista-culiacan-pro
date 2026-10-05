// Coordinador: aspecto de a.btn-primary CON y SIN el CSS externo (bloqueando styles.7f293647.css).
// uso: node _pp-nocss.cjs contacto/ blog/   (rutas relativas servidas en :8097)
const puppeteer = require('/Users/openclaw/Sitios Web/Electricista Culiacán/node_modules/puppeteer');
const BASE = 'http://127.0.0.1:8097/';
(async () => {
  const browser = await puppeteer.launch({ headless: 'shell' });
  for (const rel of process.argv.slice(2)) {
    for (const block of [true, false]) {
      const page = await browser.newPage();
      await page.setViewport({ width: 375, height: 740 });
      await page.setRequestInterception(true);
      page.on('request', r => (block && r.url().includes('styles.7f293647.css')) ? r.abort() : r.continue());
      const errs = []; page.on('pageerror', e => errs.push(String(e).slice(0, 80)));
      await page.goto(BASE + rel, { waitUntil: block ? 'domcontentloaded' : 'networkidle0', timeout: 30000 });
      const rows = await page.evaluate(() => [...document.querySelectorAll('a.btn-primary')].map(a => {
        const cs = getComputedStyle(a); const r = a.getBoundingClientRect();
        return { txt: a.textContent.trim().replace(/\s+/g, ' ').slice(0, 32), h: Math.round(r.height), w: Math.round(r.width), color: cs.color, bg: cs.backgroundColor, bgi: cs.backgroundImage.slice(0, 48), pad: cs.padding, radius: cs.borderRadius };
      }));
      console.log(JSON.stringify({ rel, cssBlocked: block, errs: errs.length, rows }));
      await page.close();
    }
  }
  await browser.close();
})();
