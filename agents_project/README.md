# 🔌 Agente de Contenido SEO - Electricista Culiacán Pro

Sistema de agentes autónomos basado en **CrewAI** para generar contenido SEO optimizado para "Electricista Culiacán Pro".

## 📋 Características

- ✅ Genera contenido JSON listo para publicar
- ✅ Optimizado para SEO con meta tags perfectos
- ✅ Incluye FAQs con Schema.org (JSON-LD)
- ✅ Sigue las normas de marca de Electricista Culiacán Pro
- ✅ Menciona colonias específicas de Culiacán
- ✅ Terminología técnica eléctrica correcta
- ✅ Tono profesional en español de México

## 🚀 Instalación

### 1. Requisitos previos
- Python 3.8 o superior
- Cuenta de OpenAI con API key

### 2. Instalar dependencias

```bash
cd agents_project
pip install -r requirements.txt
```

### 3. Configurar API key

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env y agregar tu API key
nano .env
```

Agregar tu API key en `.env`:
```
OPENAI_API_KEY=sk-tu-api-key-aqui
OPENAI_MODEL_NAME=gpt-4-turbo-preview
```

## 💻 Uso

### Comando básico

```bash
python main.py '<keyword>' '<zona>'
```

### Ejemplos

```bash
# Electricista urgente en el Centro
python main.py 'electricista urgente' 'Culiacán Centro'

# Instalación eléctrica en Las Quintas
python main.py 'instalacion electrica' 'Las Quintas'

# Reparación de cortocircuitos en Tres Ríos
python main.py 'reparacion cortocircuitos' 'Tres Ríos'

# Mantenimiento de tableros en Chapultepec
python main.py 'mantenimiento tableros' 'Chapultepec'

# Instalación de contactos en Villa Universidad
python main.py 'instalacion contactos' 'Villa Universidad'
```

## 📁 Estructura del proyecto

```
agents_project/
├── agents/                      # Agentes especializados
│   ├── contenido_electricista.py   # Agente generador de contenido SEO
│   ├── investigador.py             # Agente investigador (ejemplo)
│   ├── escritor.py                 # Agente escritor (ejemplo)
│   └── analista.py                 # Agente analista (ejemplo)
├── tasks/                       # Definiciones de tareas
│   ├── tarea_contenido_electricista.py
│   └── tareas.py
├── tools/                       # Herramientas para agentes
│   └── search_tools.py
├── config/                      # Archivos de configuración
├── output/                      # Archivos JSON generados
├── main.py                      # Script principal
├── requirements.txt             # Dependencias Python
├── .env.example                 # Plantilla de variables de entorno
└── README.md                    # Este archivo
```

## 📊 Formato de salida

El agente genera un JSON con esta estructura:

```json
{
  "slug": "electricista-urgente-culiacan-centro",
  "url": "/servicios/electricista-urgente-culiacan-centro/",
  "meta_title": "Electricista Urgente en Culiacán Centro | Llegada 30-60 min",
  "meta_description": "Electricista certificado 24/7 en Culiacán Centro. Emergencias eléctricas con llegada en 30-60 min. WhatsApp inmediato. Garantía por escrito. Cobertura completa.",
  "h1": "Electricista Urgente 24/7 en Culiacán Centro – Emergencias en 30-60 min",
  "intro": "¿Cortocircuito o apagón en tu casa? Nuestro equipo de electricistas certificados llega en 30-60 min a Culiacán Centro y colonias cercanas. Atención inmediata por WhatsApp.",
  "servicios": [
    "Reparación de cortocircuitos urgentes",
    "Instalación de contactos y apagadores",
    "Mantenimiento de tableros eléctricos",
    "Instalación de iluminación LED"
  ],
  "beneficios": [
    "Llegada garantizada en 30-60 min",
    "Electricistas certificados por CFE",
    "Garantía por escrito en todos los trabajos",
    "Facturación SAT disponible",
    "Atención 24/7 por WhatsApp"
  ],
  "cta": "¿Cortocircuito ahora? Escríbenos por WhatsApp y llegamos en 30-60 min a Culiacán Centro",
  "faq": [
    {
      "pregunta": "¿Cuánto tardan en llegar a Culiacán Centro?",
      "respuesta": "Llegamos en 30-60 minutos a Culiacán Centro y colonias cercanas como Guadalupe, Chapultepec y Santa Fe."
    }
  ],
  "schema_faq": {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [...]
  }
}
```

## 🗺️ Colonias de Culiacán soportadas

### Zona Norte
- Las Quintas
- Tres Ríos
- Country Tres Ríos
- Campestre
- Hacienda del Valle

### Zona Centro
- Centro
- Guadalupe
- Chapultepec
- Santa Fe
- Zona Dorada

### Zona Sur
- Villa Universidad
- Montebello
- Villa Bonita
- Lomas del Boulevard

### Zona Oriente
- Colinas de San Miguel
- Nuevo Culiacán
- Infonavit Humaya

## ⚡ Keywords principales recomendadas

- `electricista urgente`
- `instalacion electrica`
- `reparacion cortocircuitos`
- `instalacion contactos`
- `mantenimiento tableros`
- `instalacion iluminacion`
- `electricista 24 horas`
- `emergencia electrica`
- `cambio breakers`
- `instalacion tierra fisica`

## 🎨 Identidad de marca

**Colores:**
- ✅ Azul: `#1E40AF`, `#3B82F6`
- ✅ Amarillo: `#FCD34D`
- ❌ NO usar naranja (es de plomero)

**Iconos:**
- ✅ ⚡🔌💡⚙️🛡️
- ❌ NO 🔧💧🚿 (son de plomería)

**Terminología:**
- ✅ electricista, electricidad, cortocircuitos, tableros, contactos, breakers, CFE
- ❌ NO plomero, plomería, fugas, drenaje

## 🛠️ Personalización

### Modificar el prompt del agente

Edita `agents/contenido_electricista.py` para ajustar el comportamiento del agente.

### Modificar la tarea

Edita `tasks/tarea_contenido_electricista.py` para cambiar las instrucciones de generación.

### Cambiar modelo de IA

Edita `.env`:
```
OPENAI_MODEL_NAME=gpt-4  # o gpt-3.5-turbo para más velocidad/menor costo
```

## 📝 Notas importantes

1. **API Key de OpenAI es requerida** - El sistema usa modelos GPT
2. **Los archivos se guardan en `/output`** - Revisa ahí los JSONs generados
3. **Valida el JSON** - Siempre verifica que sea parseable antes de usar
4. **Personaliza según necesidad** - El agente aprende de ejemplos

## 🐛 Solución de problemas

### Error: "OPENAI_API_KEY no encontrada"
- Verifica que creaste el archivo `.env`
- Asegúrate de que la API key sea válida

### El JSON no se genera correctamente
- Prueba con un modelo más avanzado (gpt-4)
- Ajusta la temperatura en `main.py`
- Revisa que las instrucciones estén claras

### El agente es muy lento
- Usa `gpt-3.5-turbo` en lugar de `gpt-4`
- Reduce el número de FAQs solicitadas

## 📚 Recursos

- [Documentación CrewAI](https://docs.crewai.com/)
- [OpenAI API](https://platform.openai.com/docs/api-reference)
- [Guía de formato](../formatoparacrearurlelectricidad.md)

## 📄 Licencia

Uso interno - Electricista Culiacán Pro

---

**Versión:** 1.0
**Fecha:** Noviembre 2025
**Mantenedor:** Equipo de desarrollo Electricista Culiacán Pro
