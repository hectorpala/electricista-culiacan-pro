# Automatización de Landing Pages

Crea una landing page completa automáticamente desde cero.

## 📝 Uso

```
/automatizaciondelanding "Nombre del Servicio"
```

**Ejemplos:**
- `/automatizaciondelanding "Instalación de Minisplit"`
- `/automatizaciondelanding "Reparación de Apagadores"`
- `/automatizaciondelanding "Mantenimiento de Clima"`

---

## 🎯 Lo que hace automáticamente

1. ✅ Genera el slug del servicio (ej: "instalacion-minisplit")
2. ✅ Crea contenido SEO optimizado (title, description, keywords)
3. ✅ Genera 4 benefits personalizados para el servicio
4. ✅ Copia el template v2.0.0 base
5. ✅ Aplica todo el contenido al HTML
6. ✅ Valida y crea imágenes faltantes
7. ✅ Verifica que el HTML sea válido
8. ✅ Abre el resultado en el navegador

**Tiempo estimado: 30-45 segundos**

---

## 🚀 Ejecución

Cuando ejecutes este comando, verás:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 AUTOMATIZACIÓN DE LANDING INICIADA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Servicio: {nombre del servicio}
🔗 Slug: {slug generado}

[PASO 1/7] Generando slug...
[PASO 2/7] Generando contenido SEO...
[PASO 3/7] Creando config.json...
[PASO 4/7] Copiando template v2.0.0...
[PASO 5/7] Aplicando contenido...
[PASO 6/7] Validando imágenes...
[PASO 7/7] Validando HTML...

🎉 LANDING CREADA EXITOSAMENTE
📂 Ubicación: servicios/{slug}/index.html
```

---

## ⚠️ Requisitos

Antes de ejecutar, asegúrate de tener:

1. ✅ Template base en: `servicios/reparacion-cortos-circuitos/`
2. ✅ Script ejecutable: `scripts/crear-landing-auto.sh`
3. ✅ Imagen hero en: `assets/images/optimizadas/{slug}-culiacan-800w.webp`

---

## 🔧 Flujo interno

Este comando ejecuta el script `scripts/crear-landing-auto.sh` que:
1. Llama al generador de SEO
2. Crea el config.json
3. Invoca el agentconstructor
4. Valida imágenes y HTML
5. Abre el navegador

---

## 💡 Notas

- El slug se genera automáticamente desde el nombre del servicio
- La imagen hero debe llamarse: `{slug}-culiacan-800w.webp`
- Si falta la imagen 1200w, se crea automáticamente desde la 800w
- El resultado se guarda en: `servicios/{slug}/`
