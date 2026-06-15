#!/usr/bin/env node
/**
 * Generador automático de imágenes del sitio.
 *
 * Lee .pipeline/imagenes-pendientes.json y, por cada entrada `enabled`:
 *   - tipo "ia":     genera con la API de OpenAI (gpt-image-1), optimiza a WebP
 *                    en los tamaños pedidos y guarda con la convención del sitio.
 *   - tipo "resize": deriva la imagen de un archivo existente con sharp (sin IA).
 *
 * IDEMPOTENTE: salta lo que ya existe (usa --force para regenerar).
 * No aborta si una imagen falla; reporta al final.
 *
 * Uso:
 *   export OPENAI_API_KEY="sk-..."        # solo para las tareas tipo "ia"
 *   node .pipeline/generar-imagenes.mjs            # genera lo pendiente
 *   node .pipeline/generar-imagenes.mjs --force    # regenera todo
 *
 * Requiere: npm i openai sharp
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import sharp from "sharp";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const MANIFEST = path.join(ROOT, ".pipeline", "imagenes-pendientes.json");
const FORCE = process.argv.includes("--force");
const QUALITY = process.env.IMG_QUALITY || "high"; // gpt-image-1: low|medium|high
const GEN_SIZE = "1536x1024"; // landscape para heroes
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

// ---- tarea IA (OpenAI gpt-image-1) -----------------------------------------
let _openai = null;
async function getOpenAI() {
  if (_openai) return _openai;
  const { default: OpenAI } = await import("openai");
  _openai = new OpenAI(); // usa OPENAI_API_KEY del entorno
  return _openai;
}

async function doIA(img, estilo) {
  const dir = path.join(ROOT, img.dir);
  const sizes = img.tamanos || [800];
  const targets = sizes.map((w) => path.join(dir, `${img.base}-${w}w.webp`));
  if (targets.every((t) => fs.existsSync(t)) && !FORCE)
    return { estado: "saltado", out: `${img.base} (${sizes.join("/")}w)` };

  if (!process.env.OPENAI_API_KEY)
    return { estado: "pendiente", out: `${img.base} (${sizes.join("/")}w)`, motivo: "falta OPENAI_API_KEY" };

  const prompt = `${estilo}\n\nESCENA: ${img.prompt}`;
  const openai = await getOpenAI();
  const res = await openai.images.generate({
    model: "gpt-image-1",
    prompt,
    size: GEN_SIZE,
    quality: QUALITY,
    n: 1,
  });
  const b64 = res.data?.[0]?.b64_json;
  if (!b64) throw new Error("la API no devolvió imagen (b64_json vacío)");
  const buf = Buffer.from(b64, "base64");

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
  const enabled = m.imagenes.filter((x) => x.enabled);
  log(`Generador de imágenes — ${enabled.length} entradas habilitadas${FORCE ? " (--force)" : ""}\n`);

  const stats = { generado: 0, saltado: 0, pendiente: 0, error: 0 };
  for (const img of enabled) {
    let r;
    try {
      r = img.tipo === "resize" ? await doResize(img) : await doIA(img, m.estilo);
    } catch (e) {
      r = { estado: "error", out: img.base || img.salida || "?", motivo: e.message };
    }
    stats[r.estado] = (stats[r.estado] || 0) + 1;
    const icon = { generado: "✅", saltado: "·", pendiente: "⏳", error: "❌" }[r.estado];
    log(`  ${icon} [${r.estado}] ${r.out}${r.motivo ? `  — ${r.motivo}` : ""}`);
  }

  log(`\nResumen: ${stats.generado} generadas · ${stats.saltado} ya existían · ${stats.pendiente} pendientes (sin key) · ${stats.error} errores`);
  if (stats.pendiente > 0)
    log(`\n⏳ Hay imágenes IA pendientes. Exporta tu key y vuelve a correr:\n   export OPENAI_API_KEY="sk-..."\n   node .pipeline/generar-imagenes.mjs`);
  if (stats.error > 0) process.exitCode = 1;
}

main();
