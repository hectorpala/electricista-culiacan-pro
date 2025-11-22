from crewai import Task

class TareaContenidoElectricista:
    """
    Tarea especializada para generar contenido SEO de Electricista Culiacán Pro
    """

    @staticmethod
    def generar_pagina_seo(agent, keyword, zona):
        return Task(
            description=f"""Genera una página optimizada para SEO para "Electricista Culiacán Pro".

**ENTRADA:**
- Keyword principal: "{keyword}"
- Zona/Colonia: "{zona}"

**INSTRUCCIONES OBLIGATORIAS:**

1. **SLUG**:
   - Minúsculas, sin acentos, con guiones
   - 3-6 palabras incluyendo ciudad o zona
   - Ejemplo: "electricista-urgente-culiacan-centro"

2. **URL**:
   - /servicios/[slug]/
   - Ejemplo: "/servicios/electricista-urgente-culiacan-centro/"

3. **META_TITLE** (60-65 caracteres):
   - Incluir keyword + zona + beneficio
   - Ejemplo: "Electricista Urgente en Culiacán Centro | Llegada 30-60 min"

4. **META_DESCRIPTION** (150-160 caracteres):
   - Urgencia + cobertura + contacto
   - Mencionar certificación, 24/7, garantía
   - Incluir WhatsApp/teléfono implícito

5. **H1**:
   - Keyword exacta + promesa clara
   - Ejemplo: "Electricista Urgente 24/7 en Culiacán Centro – Emergencias en 30-60 min"

6. **INTRO** (2-3 líneas):
   - Describir problemas eléctricos comunes
   - Mencionar zonas específicas
   - Llamado a la acción suave

7. **SERVICIOS** (lista de 4-6 items):
   - Servicios eléctricos específicos
   - Relacionados con la keyword
   - Ejemplos: "Reparación de cortocircuitos", "Instalación de contactos", "Mantenimiento de tableros"

8. **BENEFICIOS** (lista de 4-5 items):
   - Llegada 30-60 min
   - Certificación CFE
   - Garantía por escrito
   - Facturación SAT
   - WhatsApp 24/7

9. **CTA** (una frase de acción):
   - Urgente y directa
   - Ejemplo: "¿Cortocircuito ahora? Escríbenos por WhatsApp y llegamos en 30-60 min a {zona}"

10. **FAQ** (mínimo 3, idealmente 8):
    - Preguntas sobre tiempos, costos, cobertura, garantías, certificaciones
    - Respuestas específicas para Culiacán
    - Mencionar colonias y servicios concretos
    - Formato: lista de objetos con "pregunta" y "respuesta"

11. **SCHEMA_FAQ** (opcional pero recomendado):
    - JSON-LD FAQPage válido
    - Mismo contenido que FAQ pero en formato Schema.org

**COLONIAS DE REFERENCIA CULIACÁN:**
Zona Norte: Las Quintas, Tres Ríos, Country Tres Ríos, Campestre, Hacienda del Valle
Zona Centro: Centro, Guadalupe, Chapultepec, Santa Fe, Zona Dorada
Zona Sur: Villa Universidad, Montebello, Villa Bonita, Lomas del Boulevard
Zona Oriente: Colinas de San Miguel, Nuevo Culiacán, Infonavit Humaya

**SERVICIOS ELÉCTRICOS PRINCIPALES:**
- Instalación eléctrica completa
- Reparación de cortocircuitos
- Instalación de contactos y apagadores
- Instalación de iluminación LED
- Mantenimiento de tableros eléctricos
- Emergencias eléctricas 24/7
- Instalación de tierra física
- Cambio de breakers

**TERMINOLOGÍA TÉCNICA CORRECTA:**
✅ SÍ: electricista, electricidad, cortocircuitos, cableado, contactos, tableros, iluminación, breaker, tierra física, CFE, centro de carga
❌ NO: plomero, plomería, fugas, drenaje (esto es de plomeros, NO de electricistas)

**TONO Y VOZ:**
- Profesional pero cercano
- Español de México natural
- Generar urgencia sin ser agresivo
- Enfatizar confianza: certificación, garantía, rapidez
- Mencionar colonias específicas (no solo "Culiacán")

**FORMATO DE SALIDA:**
DEVUELVE ÚNICAMENTE JSON VÁLIDO con esta estructura exacta:

{{
  "slug": "string (sin acentos, minúsculas, guiones)",
  "url": "/servicios/slug/",
  "meta_title": "string (60-65 chars)",
  "meta_description": "string (150-160 chars)",
  "h1": "string",
  "intro": "string (2-3 líneas)",
  "servicios": ["item1", "item2", "item3", "item4"],
  "beneficios": ["item1", "item2", "item3", "item4"],
  "cta": "string",
  "faq": [
    {{"pregunta": "string", "respuesta": "string"}},
    {{"pregunta": "string", "respuesta": "string"}},
    {{"pregunta": "string", "respuesta": "string"}}
  ],
  "schema_faq": {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "pregunta",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "respuesta"
        }}
      }}
    ]
  }}
}}

**CRÍTICO:**
- NO agregues texto fuera del JSON
- NO uses comillas triples para envolver el JSON
- Asegúrate de que el JSON sea válido y parseable
- Usa escape correcto para comillas dentro de strings
""",
            agent=agent,
            expected_output="JSON válido con toda la estructura de la página SEO, sin texto adicional"
        )
