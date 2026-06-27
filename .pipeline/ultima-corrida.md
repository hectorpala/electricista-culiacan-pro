# Auto Agente Electricista — parte del 2026-06-27
**Resultado:** encontré 9, arreglé 9 · 1 necesita tu decisión · publicado

Hola Héctor, esto es lo que hice hoy solo.
Encontré 9 cosas: arreglé 9 · 0 que no pude arreglar · 1 necesita tu decisión.

## ✅ Arreglé (9)

**4 blogs con imagen incorrecta en el esquema para Google (datos invisibles al visitante pero importantes para el SEO):**
Los 4 blogs de abajo le decían a Google que la imagen del negocio era un archivo con el nombre equivocado (`electricista-culiacan-hero-800w.webp` en lugar del correcto `hero-electricista-culiacan-800w.webp`). En el navegador se ve igual, pero los robots de Google usaban el nombre viejo que no corresponde a ningún archivo real del sitio.
- https://electricistaculiacanpro.mx/blog/ahorro-energia-iluminacion-led/
- https://electricistaculiacanpro.mx/blog/cuando-llamar-electricista-emergencia/
- https://electricistaculiacanpro.mx/blog/mantenimiento-tablero-electrico-preventivo/
- https://electricistaculiacanpro.mx/blog/seguridad-electrica-temporada-lluvias/

**2 blogs con JavaScript doble que podía romper el menú en móvil:**
Dos blogs (cómo prevenir cortocircuitos y señales de instalación obsoleta) cargaban DOS versiones del mismo código JavaScript: una vez dentro de la página y otra vez como archivo externo. Eso puede hacer que el menú de hamburguesa se comporte de forma rara al abrirlo/cerrarlo en móvil. Quité el archivo externo (el que sobraba), ya que la versión interna es la correcta.
- https://electricistaculiacanpro.mx/blog/como-prevenir-cortocircuitos-casa/
- https://electricistaculiacanpro.mx/blog/senales-instalacion-electrica-obsoleta/

**2 blogs con precio de servicio propio visible (que no deberíamos publicar):**
Dos artículos del blog citaban explícitamente precios que cobramos — algo que según tu política de negocio jamás debe aparecer en el texto visible de la página (los precios van en cotización, no publicados en internet). Lo cambié por "Solicita tu cotización sin costo".
- Blog cortocircuitos decía en el FAQ "cuesta desde $500 MXN" → https://electricistaculiacanpro.mx/blog/como-prevenir-cortocircuitos-casa/
- Blog mantenimiento tablero decía "desde $600 hasta $1,500 MXN" → https://electricistaculiacanpro.mx/blog/mantenimiento-tablero-electrico-preventivo/

**1 página de servicio con título y descripción mejorada para Google:**
La página de "Instalación de Contactos" aparece en posición 5 de Google cuando alguien busca "contactos culiacán", pero nadie hace clic (0 de 15 personas que te ven). Reescribí el título para que sea más directo y también mencione el cambio de contactos, no solo la instalación.
- Antes: "Instalación de Contactos Eléctricos en Culiacán | 24 Horas"
- Ahora: "Contactos Eléctricos Culiacán | Instalación y Cambio · 24/7"
- → https://electricistaculiacanpro.mx/servicios/instalacion-contactos/

## ⚠️ Encontré pero NO pude arreglar solo (0)

Todo lo que encontré lo pude arreglar.

## 🌱 Mejoré / agregué (0)

Sin páginas nuevas hoy. Tus datos de Google confirman que el sitio ya cubre bien la demanda actual. En vez de inventar páginas que podrían dañar tu posicionamiento, me enfoqué en mejorar las páginas existentes.

**Nota de Google Search Console:** tus clics bajaron 15% este mes (102 → 87 clics). La buena noticia: la palabra clave principal "electricista culiacán" subió de posición 8.2 a posición 4.7 — el cambio de título de la portada que hicimos el 22 de junio SÍ está funcionando. Los clics deberían subir en las próximas 2-4 semanas. Sugiero revisarlo el 15 de julio.

## 🧠 Aprendí hoy (para no volver a fallar)
- Si un blog tiene su propio código JavaScript interno, no cargar también el archivo externo adicional — se duplicarían instrucciones y el menú podría romperse en móvil.
- La imagen del negocio que ve Google (en los datos estructurados invisibles) debe usar el nombre exacto del archivo; si el nombre no coincide, Google no puede mostrarla aunque haya un archivo parecido.
- Los precios de nuestro servicio en el cuerpo de un artículo del blog también violan la política "nunca precio visible" — no solo las páginas de servicio. Ahora el sistema detecta esto automáticamente en todos los archivos.
(ya van ~52 reglas aprendidas en total)

## ⏳ Necesito que tú decidas (1)

**La página `/servicios/` no existe y da error 404:** Cada página de servicio tiene una "miga de pan" (el camino de navegación arriba que dice "Inicio > Servicios > [nombre del servicio]"). El enlace del segundo nivel ("Servicios") va a una página que no existe — da error 404. Esto afecta a TODAS las páginas de servicio del sitio.

Dos opciones:
1. **Crear una página hub en `/servicios/`** que liste todos tus servicios con fotos y enlaces (yo la puedo hacer, solo dime que sí).
2. **Quitar el enlace de "Servicios"** en la miga de pan para que no sea clicable (solución más rápida, menos valor SEO).

Avísame cuál prefieres y lo hago en la próxima corrida.

**Pendiente anterior que sigue en cola:** hay 33 páginas más con precios en el texto (testimonios de clientes que dicen cuánto ahorraron, rangos de mercado educativos, y páginas como "¿Cuánto cuesta un electricista?" donde los precios SON el contenido). Necesito saber si quieres excepciones para esas páginas o si las reescribo sin números.

## 📦 ¿Se publicó?
Sí, todo revisado y en vivo. Le avisé a Google para que lo muestre en las próximas horas (7 páginas enviadas para re-indexación automática).
