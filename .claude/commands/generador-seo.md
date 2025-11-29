# Generador de Contenido SEO para Servicios Eléctricos

Genera contenido SEO optimizado para un servicio de electricista en Culiacán.

## 📋 Input

Recibes:
- **Nombre del servicio**: Ej. "Instalación de Minisplit"
- **Slug**: Ej. "instalacion-minisplit"

## 🎯 Output esperado

Debes generar contenido optimizado para SEO específico para servicios de electricista en Culiacán, Sinaloa, México.

### 1. **Title** (50-60 caracteres)
- Debe incluir el servicio + "Culiacán"
- Incluir un beneficio clave o valor agregado
- Entre 50-60 caracteres EXACTOS
- Ejemplo: `Instalación Minisplit Culiacán | Clima Profesional`

### 2. **Meta Description** (120-155 caracteres)
- Emoji inicial ⚡
- Descripción del servicio
- Beneficio principal
- Call to action con teléfono 667 392 2273
- Entre 120-155 caracteres EXACTOS
- Ejemplo: `⚡ Instalación minisplit en Culiacán. Inverter y estándar. Instalación certificada 24/7. ¡Llama: 667 392 2273!`

### 3. **Keywords** (6-8 keywords separadas por comas)
- Formato: keyword1 culiacan, keyword2 culiacan, electricista culiacan...
- Incluir variaciones long-tail
- Todas en minúsculas, sin acentos
- Ejemplo: `instalacion minisplit culiacan, minisplit culiacan, aire acondicionado culiacan, electricista clima culiacan`

### 4. **H1** (título principal)
- Debe incluir el servicio + "Culiacán"
- Incluir beneficio clave
- Formato: "Servicio en Culiacán | Beneficio"
- Ejemplo: `Instalación de Minisplit en Culiacán | Clima Profesional Certificado`

### 5. **Subtitle** (hero subtitle - 1-2 líneas)
- Descripción del servicio
- Mencionar tipos o variantes del servicio
- Incluir garantía y profesionalismo
- 30-50 palabras
- Ejemplo: `Instalación profesional de minisplit inverter y estándar en Culiacán. Todas las marcas. Instalación rápida, limpia y certificada. Garantía por escrito de 6 meses.`

### 6. **WhatsApp Text**
- Texto corto para el mensaje de WhatsApp
- Solo el nombre del servicio en minúsculas
- Ejemplo: `instalación de minisplit`

### 7. **Breadcrumb**
- Nombre corto para el breadcrumb
- Capitalizado
- Ejemplo: `Instalación Minisplit`

### 8. **Service Type** (para Schema.org)
- Nombre formal del servicio
- Capitalizado
- Ejemplo: `Instalación de Minisplit`

### 9. **Schema Description**
- Descripción detallada para Schema.org
- 2-3 frases
- Mencionar tipos, beneficios y características
- 40-60 palabras
- Ejemplo: `Instalación profesional de minisplit inverter y estándar en hogares y negocios. Todas las marcas reconocidas. Servicio rápido, limpio y certificado con garantía de 6 meses.`

### 10. **Benefits** (4 benefits específicos del servicio)

Cada benefit debe tener:
- **title**: Título del beneficio (5-8 palabras)
- **description**: Descripción detallada (40-60 palabras) con datos concretos, cifras, o detalles técnicos

**Criterios para los benefits:**
1. **Específicos del servicio**: No genéricos, deben ser únicos para este servicio
2. **Con datos concretos**: Incluir números, porcentajes, tiempos, garantías
3. **Orientados a soluciones**: Resolver problemas específicos del cliente
4. **Profesionales**: Mostrar expertise y certificación

**Ejemplo de benefits para "Instalación de Minisplit":**

```json
{
  "title": "Instalación certificada en 3 horas",
  "description": "Instalamos tu minisplit en 3 horas promedio. Electricistas certificados con 10+ años de experiencia. Incluye pruebas de funcionamiento, vacuum, carga de gas y limpieza del área. Sin daños a muros ni sorpresas."
}
```

---

## 📝 Formato de Output

Debes responder EXACTAMENTE en este formato JSON:

```json
{
  "seo": {
    "title": "Título aquí (50-60 chars)",
    "description": "Descripción aquí (120-155 chars)",
    "keywords": "keyword1, keyword2, keyword3..."
  },
  "content": {
    "h1": "H1 aquí",
    "subtitle": "Subtitle aquí (30-50 palabras)",
    "whatsapp_text": "texto whatsapp",
    "breadcrumb": "Breadcrumb",
    "service_type": "Service Type"
  },
  "schema": {
    "description": "Descripción Schema.org (40-60 palabras)"
  },
  "benefits": [
    {
      "title": "Benefit 1 title",
      "description": "Benefit 1 description (40-60 palabras)"
    },
    {
      "title": "Benefit 2 title",
      "description": "Benefit 2 description (40-60 palabras)"
    },
    {
      "title": "Benefit 3 title",
      "description": "Benefit 3 description (40-60 palabras)"
    },
    {
      "title": "Benefit 4 title",
      "description": "Benefit 4 description (40-60 palabras)"
    }
  ]
}
```

---

## ⚡ Contexto del negocio

**Negocio**: Electricista Culiacán Pro
**Ubicación**: Culiacán, Sinaloa, México
**Zonas de servicio**: Las Quintas, Tres Ríos, Chapultepec, Montebello, Centro
**Teléfono**: 667 392 2273
**Rating**: 4.8★ en Google
**Clientes**: 150+ clientes satisfechos

**Valores clave a comunicar:**
- Servicio profesional y certificado
- Respuesta rápida (24/7 para emergencias)
- Garantía por escrito
- Precios justos y transparentes
- Experiencia comprobada

---

## 🎯 Reglas importantes

1. **SIEMPRE incluir "Culiacán"** en title, description, h1, keywords
2. **Teléfono siempre es 667 392 2273**
3. **No usar emojis** excepto ⚡ en la meta description
4. **Benefits deben ser únicos** para cada servicio (no genéricos)
5. **Contar caracteres exactos** en title (50-60) y description (120-155)
6. **Keywords sin acentos** y en minúsculas
7. **Tone profesional** pero cercano
8. **Enfoque en soluciones** no en problemas
9. **Incluir garantía** cuando sea relevante
10. **Mencionar certificación** cuando aplique

---

## 💡 Ejemplos de servicios y sus características únicas

### Instalación de Minisplit
- Focus: Clima, ahorro energía, marcas, instalación técnica
- Benefits: Instalación rápida, vacuum, carga gas, marcas reconocidas

### Reparación de Apagadores
- Focus: Seguridad, contactos quemados, chispas, prevención incendios
- Benefits: Diagnóstico gratis, repuestos originales, mismo día

### Instalación Tierra Física
- Focus: Seguridad, protección equipos, normatividad, mediciones
- Benefits: Medición con telurómetro, cumplimiento NOM, equipos sensibles

### Iluminación LED
- Focus: Ahorro energía (80%), temperatura color, vida útil
- Benefits: ROI 6-12 meses, duración 25 años, asesoría temperatura

### Mantenimiento Tableros
- Focus: Prevención, seguridad, breakers, termografía
- Benefits: Inspección termográfica, detección puntos calientes, prevención

---

**IMPORTANTE**: Adapta los benefits según el tipo de servicio. Cada servicio debe tener benefits ÚNICOS y específicos.
