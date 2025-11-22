# Configuracion de Analytics para Medir Impacto

## Eventos Implementados

El sitio ahora envia automaticamente eventos a Google Analytics via DataLayer para medir el impacto de las optimizaciones.

---

## Eventos Configurados

### 1. **Clics en Tarjetas SEO** (`click_seo_card`)

**Que mide:** Cada clic en las tarjetas de "Mas opciones de electricidad"

**Parametros enviados:**
```javascript
{
  'event': 'click_seo_card',
  'card_name': 'electricista_cerca_de_mi',    // Nombre de la tarjeta
  'card_position': '1',                         // Posicion en el grid (1-5)
  'card_url': './servicios/...',               // URL destino
  'page_location': '/index.html'               // Pagina origen
}
```

**Tarjetas trackeadas:**
1. `electricista_cerca_de_mi` (Posicion 1)
2. `electricista_24_7` (Posicion 2)
3. `electricista_a_domicilio` (Posicion 3)
4. `electricista_precios` (Posicion 4)
5. `electricista_colonias` (Posicion 5)

---

### 2. **Profundidad de Scroll** (`scroll_depth`)

**Que mide:** Engagement del usuario con el contenido

**Triggers:**
- 25% de scroll
- 50% de scroll
- 75% de scroll
- 90% de scroll

**Parametros enviados:**
```javascript
{
  'event': 'scroll_depth',
  'scroll_percentage': 50,          // Porcentaje alcanzado
  'page_location': '/index.html'    // Pagina actual
}
```

---

## Configuracion en Google Tag Manager

### Paso 1: Crear Variables Personalizadas

1. Ve a **Variables** → **Nueva**
2. Crea las siguientes variables de capa de datos:

| Variable | Nombre de Variable | Tipo |
|----------|-------------------|------|
| `card_name` | DL - Card Name | Variable de capa de datos |
| `card_position` | DL - Card Position | Variable de capa de datos |
| `card_url` | DL - Card URL | Variable de capa de datos |
| `scroll_percentage` | DL - Scroll Percentage | Variable de capa de datos |

---

### Paso 2: Crear Activadores (Triggers)

#### Activador: Clic en Tarjeta SEO
- **Nombre:** Click - SEO Card
- **Tipo:** Evento personalizado
- **Nombre del evento:** `click_seo_card`

#### Activador: Scroll Depth
- **Nombre:** Scroll Depth Milestone
- **Tipo:** Evento personalizado
- **Nombre del evento:** `scroll_depth`

---

### Paso 3: Crear Etiquetas de Google Analytics 4

#### Etiqueta 1: Evento Click SEO Card

**Configuracion:**
- **Tipo de etiqueta:** Google Analytics: Evento GA4
- **ID de medicion:** Tu GA4 Measurement ID
- **Nombre del evento:** `click_seo_card`
- **Parametros del evento:**
  - `card_name`: `{{DL - Card Name}}`
  - `card_position`: `{{DL - Card Position}}`
  - `card_url`: `{{DL - Card URL}}`
- **Activacion:** Click - SEO Card

#### Etiqueta 2: Evento Scroll Depth

**Configuracion:**
- **Tipo de etiqueta:** Google Analytics: Evento GA4
- **ID de medicion:** Tu GA4 Measurement ID
- **Nombre del evento:** `scroll_depth`
- **Parametros del evento:**
  - `scroll_percentage`: `{{DL - Scroll Percentage}}`
- **Activacion:** Scroll Depth Milestone

---

## Reportes Sugeridos en Google Analytics 4

### 1. **Analisis de Tarjetas SEO mas Clickeadas**

**Exploracion personalizada:**
```
Dimensiones:
- card_name
- card_position

Metricas:
- Recuento de eventos (click_seo_card)
- Usuarios unicos

Segmento:
- Pagina = "/" (homepage)
```

**Que mide:**
- Que tarjeta atrae mas clics?
- La posicion afecta el CTR?
- Que servicio genera mas interes?

---

### 2. **Embudo de Conversion**

**Configurar en Analisis > Exploracion de rutas:**
```
Paso 1: Visualizacion homepage (/)
Paso 2: Evento click_seo_card
Paso 3: Visualizacion de pagina (/servicios/...)
Paso 4: Evento de contacto (WhatsApp/telefono)
```

**Que mide:**
- Tasa de conversion de homepage → landing → contacto
- Donde abandonan los usuarios
- Tiempo promedio por paso

---

### 3. **Engagement por Profundidad de Scroll**

**Exploracion personalizada:**
```
Dimensiones:
- scroll_percentage
- Pagina

Metricas:
- Recuento de eventos
- Usuarios unicos
```

**Que mide:**
- Cuantos usuarios llegan al 90% del contenido?
- La seccion "Mas opciones" se visualiza?
- Engagement general del homepage

---

## KPIs a Monitorear (Primeras 2-4 Semanas)

### Antes vs Despues de las Tarjetas Clickeables

| Metrica | Baseline | Objetivo | Donde Verlo |
|---------|----------|----------|-------------|
| CTR Homepage → Landings | ? | +20% | GA4 > Exploracion |
| Tiempo promedio en homepage | ? | +15% | GA4 > Paginas y pantallas |
| Profundidad de scroll (90%) | ? | +25% | Evento scroll_depth |
| Clics en tarjetas SEO | 0 | >100/semana | Evento click_seo_card |
| Tasa de rebote | ? | -10% | GA4 > Paginas y pantallas |

---

## Google Search Console

### Metricas a Revisar Semanalmente

1. **CTR de Busqueda Organica**
   - Ruta: `Rendimiento > Paginas`
   - Filtrar por: `/index.html` (homepage)
   - Comparar: ultimos 7 dias vs 7 dias anteriores

2. **Impresiones de Keywords Locales**
   - Keywords: "electricista en Culiacan", "electricista cerca de mi", "electricidad 24/7"
   - Ver tendencia semanal

3. **Posicion Promedio**
   - Objetivo: mejorar posiciones para keywords long-tail
   - Ejemplo: "electricista en Las Quintas Culiacan"

---

## Analisis Recomendado (Semana 1-4)

### Semana 1-2: Baseline
- Recopilar datos sin cambios
- Establecer metricas de referencia
- Documentar CTR actual

### Semana 3-4: Post-Optimizacion
- Comparar con baseline
- Identificar tarjeta mas popular
- Ajustar copy si es necesario

### Analisis Mensual
```
1. Que tarjeta tiene mayor CTR?
   → Priorizar ese tipo de contenido

2. Usuarios llegan a scroll 90%?
   → Si no, acortar homepage

3. Tiempo en pagina aumento?
   → Contenido esta funcionando

4. Cual es el embudo mas exitoso?
   → Homepage → Que tarjeta? → Contacto
```

---

## Alertas Configurables en GA4

**Crear alertas personalizadas:**

1. **Alerta: Caida en Clics de Tarjetas**
   - Si `click_seo_card` < 10/dia
   - Notificar por email

2. **Alerta: Tasa de Rebote Alta**
   - Si tasa de rebote > 70%
   - Revisar contenido o velocidad

3. **Alerta: Scroll Depth Bajo**
   - Si scroll 50% < 30% de usuarios
   - Optimizar contenido above-the-fold

---

## Checklist de Implementacion

- [x] Eventos implementados en codigo
- [ ] Variables creadas en GTM
- [ ] Activadores configurados en GTM
- [ ] Etiquetas GA4 creadas
- [ ] Modo Preview GTM verificado
- [ ] Eventos publicados en produccion
- [ ] Dashboard GA4 configurado
- [ ] Baseline documentado (primera semana)
- [ ] Revision semanal agendada
- [ ] Search Console conectado

---

## Recursos Utiles

- **GTM Container ID:** `GTM-XXXXXXXX`
- **Dominio:** `electricistaculiacanpro.mx`
- **Documentacion GA4:** https://support.google.com/analytics/answer/9216061

---

## Proximos Pasos

1. **Inmediato:** Publicar cambios con eventos de tracking
2. **Hoy:** Configurar GTM segun esta guia
3. **Esta semana:** Documentar baseline
4. **Proximas 4 semanas:** Monitorear KPIs semanalmente
5. **Mes 2:** Analizar resultados y optimizar

---

**Ultima actualizacion:** 2025-11-22
**Version:** 1.0
