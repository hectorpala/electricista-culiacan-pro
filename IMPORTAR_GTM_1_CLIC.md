# IMPORTAR CONFIGURACION GTM EN 1 CLIC

**Tiempo total: 3 minutos**

---

## ANTES DE EMPEZAR (30 segundos)

### **Obtener tu ID de Medicion GA4:**

1. Ve a: https://analytics.google.com
2. Haz clic en **"Administrar"** (⚙️ esquina inferior izquierda)
3. En la columna "Propiedad", haz clic en **"Flujos de datos"**
4. Haz clic en tu flujo de datos web (electricistaculiacanpro.mx)
5. **Copia el "ID de medicion"** (formato: `G-XXXXXXXXXX`)

**✅ ANOTA TU ID AQUI:** `G-________________`

---

## PASO 1: EDITAR EL ARCHIVO JSON (1 minuto)

1. Abre el archivo: **`gtm-config-import.json`** con un editor de texto
2. Presiona `Ctrl+F` (o `Cmd+F` en Mac)
3. Busca: `G-XXXXXXXXXX`
4. Reemplaza con: **TU ID de medicion** que copiaste arriba
5. **Guarda el archivo** (`Ctrl+S` o `Cmd+S`)

**Ejemplo:**
```json
"value": "G-XXXXXXXXXX"     ← ANTES
"value": "G-ABC123XYZ789"   ← DESPUES (con tu ID real)
```

---

## PASO 2: IMPORTAR A GOOGLE TAG MANAGER (1 minuto)

### **2.1 Abrir GTM:**
1. Ve a: https://tagmanager.google.com
2. Busca el contenedor: **GTM-XXXXXXXX**
3. Haz clic para abrirlo

### **2.2 Importar Archivo:**
1. En el menu superior, haz clic en **"Administrar"**
2. En la seccion "Contenedor", haz clic en **"Importar contenedor"**
3. Haz clic en **"Elegir archivo del contenedor"**
4. Selecciona el archivo: **`gtm-config-import.json`** (el que editaste)
5. Haz clic en **"Continuar"**

### **2.3 Configurar Importacion:**
1. En "Elegir espacio de trabajo":
   - Selecciona: **"Nuevo"**
   - Nombre: `Tracking SEO Electricista`
2. En "Elegir una opcion de importacion":
   - Selecciona: **"Combinar"** (segundo radio button)
   - Marca: ☑️ **"Sobrescribir etiquetas, activadores y variables conflictivos"**
3. Haz clic en **"Confirmar"**

**✅ RESULTADO:** Veras un mensaje de exito con el resumen de importacion

---

## PASO 3: PUBLICAR (30 segundos)

1. Haz clic en **"Enviar"** (esquina superior derecha)

2. Escribe:
   - **Nombre de la version:** `Tracking tarjetas SEO electricista`

3. Haz clic en **"Publicar"**

---

## ✅ LISTO! AHORA VERIFICA

### **Verificacion en Google Analytics** (1 minuto)

1. Ve a: https://analytics.google.com

2. En el menu izquierdo: **Informes → Tiempo real**

3. Abre en otra pestana: https://electricistaculiacanpro.mx

4. Desplazate hasta "Mas opciones de electricidad"

5. Haz clic en cualquier tarjeta (ej: "Electricista cerca de mi")

6. Vuelve a Google Analytics (pestana Tiempo real)

7. En "Evento por nombre de evento" deberias ver:
   ```
   click_seo_card
   ```

**Si lo ves → FUNCIONA PERFECTAMENTE! 🎉**

---

## QUE PASARA AHORA

Automaticamente se rastreara:

1. **Cada clic en tarjetas SEO**
   - Nombre de la tarjeta
   - Posicion (1-5)
   - URL destino

2. **Profundidad de scroll**
   - 25%, 50%, 75%, 90%

3. **En 1-2 semanas podras ver:**
   - Que tarjeta es mas popular?
   - Usuarios leen todo el homepage?
   - Mejora el CTR homepage → landings?

---

## SI ALGO SALE MAL

### **No veo eventos en GA4 Tiempo real**

**Espera 1-2 minutos y recarga la pagina**

Si sigues sin verlos:

1. Verifica que publicaste en GTM (paso 3)
2. Borra cache del navegador
3. Abre el sitio en modo incognito
4. Haz clic en una tarjeta de nuevo

### **Error al importar**

**Asegurate de:**
- Seleccionar "Combinar" (no "Sobrescribir")
- Marcar la casilla "Sobrescribir etiquetas..."

---

## PROXIMOS PASOS (ESTA SEMANA)

1. **Hoy:** Verifica que funciona (eventos en GA4)
2. **Esta semana:** Documenta metricas actuales (baseline)
3. **Proximas semanas:** Monitorea que tarjeta es mas popular
4. **Mes 2:** Analiza resultados y optimiza

---

## RESUMEN

```
✅ Archivo configurado con tu ID GA4
✅ Listo para importar a GTM
✅ Solo 3 pasos: Abrir GTM → Importar → Publicar
✅ Verificar en GA4 Tiempo real

Total: ~3 minutos
```

---

**Ahora solo importa el archivo y listo!** 🚀
