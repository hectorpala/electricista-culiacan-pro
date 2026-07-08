#!/usr/bin/env node
/**
 * Generador automático de imágenes del sitio (Google Gemini / Imagen).
 *
 * Lee .pipeline/imagenes-pendientes.json y, por cada entrada `enabled`:
 *   - tipo "ia":     genera con la API de Google (gemini-3-pro-image-preview),
 *                    optimiza a WebP en los tamaños pedidos y guarda con la
 *                    convención de nombres del sitio.
 *   - tipo "resize": deriva la imagen de un archivo existente con sharp (sin IA).
 *
 * IDEMPOTENTE: salta lo que ya existe (usa --force para regenerar).
 * No aborta si una imagen falla; reporta al final.
 *
 * Key: se toma de GEMINI_API_KEY o de .pipeline/.gemini-key (gitignored).
 *      Sácala gratis en https://aistudio.google.com/apikey
 *
 * Uso:
 *   node .pipeline/generar-imagenes.mjs            # genera lo pendiente
 *   node .pipeline/generar-imagenes.mjs --force    # regenera todo
 *
 * Requiere: npm i sharp   (la llamada a la API usa fetch nativo de Node 18+)
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import sharp from "sharp";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const MANIFEST = path.join(ROOT, ".pipeline", "imagenes-pendientes.json");
const FORCE = process.argv.includes("--force");
const MODEL = process.env.GEMINI_IMAGE_MODEL || "gemini-3-pro-image-preview";
const ASPECT = "16:9"; // landscape para heroes
const WEBP_Q = 82;

const log = (...a) => console.log(...a);

function loadManifest() {
  const m = JSON.parse(fs.readFileSync(MANIFEST, "utf8"));
  if (!Array.isArray(m.imagenes)) throw new Error("manifiesto sin 'imagenes'");
  return m;
}
function ensureDir(p) {
  fs.mkdirSync(path.dirname(p), { recursive: true });
}

// La key se toma de GEMINI_API_KEY o de .pipeline/.gemini-key (gitignored).
function loadKey() {
  if (process.env.GEMINI_API_KEY) return true;
  const kf = path.join(ROOT, ".pipeline", ".gemini-key");
  if (fs.existsSync(kf)) {
    const k = fs.readFileSync(kf, "utf8").trim();
    if (k) { process.env.GEMINI_API_KEY = k; return true; }
  }
  return false;
}

// ---- tarea RESIZE (sin IA) -------------------------------------------------
async function doResize(img) {
  const out = path.join(ROOT, img.salida);
  const src = path.join(ROOT, img.fuente);
  if (fs.existsSync(out) && !FORCE) return { estado: "saltado", out: img.salida };
  if (!fs.existsSync(src)) return { estado: "error", out: img.salida, motivo: `fuente no existe: ${img.fuente}` };
  ensureDir(out);
  let s = sharp(src);
  if (img.trim) s = s.trim();
  if (img.ancho) s = s.resize({ width: img.ancho, withoutEnlargement: false });
  s = out.toLowerCase().endsWith(".png") ? s.png() : s.webp({ quality: 90 });
  await s.toFile(out);
  return { estado: "generado", out: img.salida };
}

// ---- tarea SVG -> WebP (ilustración vectorial hecha como código, sin IA) ----
async function doSVG(img) {
  const dir = path.join(ROOT, img.dir);
  const sizes = img.tamanos || [800];
  const src = path.join(ROOT, img.fuente);
  const targets = sizes.map((w) => path.join(dir, `${img.base}-${w}w.webp`));
  if (targets.every((t) => fs.existsSync(t)) && !FORCE)
    return { estado: "saltado", out: `${img.base} (${sizes.join("/")}w)` };
  if (!fs.existsSync(src)) return { estado: "error", out: img.base, motivo: `SVG no existe: ${img.fuente}` };
  fs.mkdirSync(dir, { recursive: true });
  const svg = fs.readFileSync(src);
  for (const w of sizes) {
    const out = path.join(dir, `${img.base}-${w}w.webp`);
    await sharp(svg, { density: 200 }).resize({ width: w }).webp({ quality: WEBP_Q }).toFile(out);
  }
  return { estado: "generado", out: `${img.base} (${sizes.join("/")}w)` };
}

// ---- llamada a Google Gemini (genera 1 imagen, devuelve Buffer PNG) --------
async function geminiGenerate(prompt) {
  const key = process.env.GEMINI_API_KEY;
  // La key va en HEADER, no en query string (en la URL puede filtrarse a logs/proxies).
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent`;
  const body = {
    contents: [{ parts: [{ text: prompt }] }],
    generationConfig: { responseModalities: ["IMAGE"], imageConfig: { aspectRatio: ASPECT } },
  };
  const r = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json", "x-goog-api-key": key },
    body: JSON.stringify(body),
  });
  if (!r.ok) {
    const t = await r.text();
    throw new Error(`HTTP ${r.status} del modelo ${MODEL}: ${t.slice(0, 400)}`);
  }
  const j = await r.json();
  const parts = j?.candidates?.[0]?.content?.parts || [];
  const img = parts.find((p) => p.inlineData?.data || p.inline_data?.data);
  const data = img?.inlineData?.data || img?.inline_data?.data;
  if (!data) throw new Error("respuesta sin imagen: " + JSON.stringify(j).slice(0, 400));
  return Buffer.from(data, "base64");
}

// ---- tarea IA --------------------------------------------------------------
async function doIA(img, estilo) {
  const dir = path.join(ROOT, img.dir);
  const sizes = img.tamanos || [800];
  const targets = sizes.map((w) => path.join(dir, `${img.base}-${w}w.webp`));
  if (targets.every((t) => fs.existsSync(t)) && !FORCE)
    return { estado: "saltado", out: `${img.base} (${sizes.join("/")}w)` };
  if (!process.env.GEMINI_API_KEY)
    return { estado: "pendiente", out: `${img.base} (${sizes.join("/")}w)`, motivo: "falta GEMINI_API_KEY" };

  const prompt = `${estilo}\n\nESCENA: ${img.prompt}\n\nFormato: foto horizontal 16:9 (landscape), sin texto superpuesto.`;
  const buf = await geminiGenerate(prompt);

  fs.mkdirSync(dir, { recursive: true });
  for (const w of sizes) {
    const out = path.join(dir, `${img.base}-${w}w.webp`);
    await sharp(buf).resize({ width: w }).webp({ quality: WEBP_Q }).toFile(out);
  }
  return { estado: "generado", out: `${img.base} (${sizes.join("/")}w)` };
}

// ---- main ------------------------------------------------------------------
async function main() {
  const m = loadManifest();
  const hayKey = loadKey();
  const enabled = m.imagenes.filter((x) => x.enabled);
  log(`Generador de imágenes (modelo ${MODEL}) — ${enabled.length} entradas${FORCE ? " (--force)" : ""}${hayKey ? "" : " (sin GEMINI_API_KEY: solo tareas resize)"}\n`);

  const stats = { generado: 0, saltado: 0, pendiente: 0, error: 0 };
  for (const img of enabled) {
    let r;
    try {
      r = img.tipo === "resize" ? await doResize(img)
        : img.tipo === "svg" ? await doSVG(img)
        : await doIA(img, m.estilo);
    } catch (e) {
      r = { estado: "error", out: img.base || img.salida || "?", motivo: e.message };
    }
    stats[r.estado] = (stats[r.estado] || 0) + 1;
    const icon = { generado: "✅", saltado: "·", pendiente: "⏳", error: "❌" }[r.estado];
    log(`  ${icon} [${r.estado}] ${r.out}${r.motivo ? `  — ${r.motivo}` : ""}`);
  }

  log(`\nResumen: ${stats.generado} generadas · ${stats.saltado} ya existían · ${stats.pendiente} pendientes (sin key) · ${stats.error} errores`);
  if (stats.pendiente > 0)
    log(`\n⏳ Hay imágenes IA pendientes. Pon tu key de Google AI Studio y vuelve a correr:\n   echo 'AIza...' > .pipeline/.gemini-key\n   node .pipeline/generar-imagenes.mjs`);
  if (stats.error > 0) process.exitCode = 1;
}

main();
