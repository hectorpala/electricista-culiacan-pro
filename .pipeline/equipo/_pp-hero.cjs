// Coordinador: mide wa.me y tel dentro de header.hero a 375x812 y 1280x800, pageerror y (opcional) buscador de colonias.
// uso: node _pp-hero.js <url1> [url2 ...]   (añade ?search para probar el buscador)
const puppeteer = require('/Users/openclaw/Sitios Web/Electricista Culiacán/node_modules/puppeteer');
(async () => {
  const urls = process.argv.slice(2);
  const browser = await puppeteer.launch({ headless: 'shell', args: ['--no-sandbox'] });
  for (const raw of urls) {
    const testSearch = raw.endsWith('?search');
    const url = raw.replace('?search', '');
    for (const vp of [{ w: 375, h: 812, m: true }, { w: 1280, h: 800, m: false }]) {
      const page = await browser.newPage();
      const errs = [];
      page.on('pageerror', e => errs.push(String(e.message).slice(0, 80)));
      await page.setViewport({ width: vp.w, height: vp.h, isMobile: vp.m, deviceScaleFactor: 1 });
      await page.goto(url, { waitUntil: 'networkidle0', timeout: 30000 });
      const r = await page.evaluate(() => {
        const hero = document.querySelector('header.hero');
        const box = e => { if (!e) return null; const b = e.getBoundingClientRect(); return { top: Math.round(b.top + scrollY), h: Math.round(b.height), bottom: Math.round(b.bottom + scrollY), vis: b.height > 0 && getComputedStyle(e).display !== 'none' }; };
        const wa = hero && hero.querySelector('a[href^="https://wa.me"]');
        const tel = hero && hero.querySelector('a[href="tel:+526673922273"]');
        return { hero: box(hero), wa: box(wa), tel: box(tel), telColor: tel ? getComputedStyle(tel).color : null, docH: document.documentElement.scrollHeight };
      });
      let search = null;
      if (testSearch && vp.m) {
        const count = async () => page.evaluate(() => [...document.querySelectorAll('a[href*="/electricista-colonias-culiacan/"]')].filter(a => a.getBoundingClientRect().height > 0).length);
        const before = await count();
        await page.type('#searchInput', 'tres');
        await new Promise(r => setTimeout(r, 600));
        const after = await count();
        const tresRios = await page.evaluate(() => !!document.querySelector('a[href*="/tres-rios/"]') && document.querySelector('a[href*="/tres-rios/"]').getBoundingClientRect().height > 0);
        search = { before, after, tresRiosVisible: tresRios };
      }
      console.log(JSON.stringify({ url: url.replace('http://127.0.0.1:8097', ''), vp: vp.w, ...r, errs, search }));
      await page.close();
    }
  }
  await browser.close();
})();
