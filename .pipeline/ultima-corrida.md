# Auto Agente Electricista — parte del 2026-08-04
**Resultado:** encontré 22, arreglé 8 · 4 para ti · publicado

Hola Héctor, esto es lo que hice hoy solo.
Encontré 22 cosas: arreglé 8 · 4 necesitan tu decisión · 10 no pude arreglar solo (quedaron anotadas para las próximas corridas).

## ✅ Arreglé (8)
- La página de tu blog (el listado con todos los artículos) tenía 5 tarjetas que prometían un tema y llevaban a otro completamente distinto — por ejemplo, una decía "Bajones de luz" pero al hacer clic te llevaba al artículo de "¿Cuándo llamar a un electricista de emergencia?". Corregí las 5 para que el título, la foto y el enlace coincidan con el artículo real, y le agregué un párrafo de introducción para que la página no se viera tan vacía → https://electricistaculiacanpro.mx/blog/
- El código que le da seguridad a tu sitio (se llama "política de seguridad de contenido") estaba bloqueando sin querer a Microsoft Clarity, la herramienta que graba cómo la gente usa tu página para saber si algo se traba. Lo desbloqueé — mi primer intento no funcionó del todo bien, mi propio verificador lo detectó y lo corregí antes de publicar nada → https://electricistaculiacanpro.mx/
- La página de iluminación LED prometía "Ahorra 80%" en el título que aparece en Google, pero adentro de la página decía "hasta 80%" (una promesa fija en vez de "hasta cierto porcentaje"). Unifiqué todo a "hasta 80%" para no prometer de más → https://electricistaculiacanpro.mx/servicios/iluminacion-led/
- En el artículo de cómo prevenir cortocircuitos, un texto naranja sobre fondo azul claro era difícil de leer para personas con baja visión. Lo oscurecí un poco para que se lea bien → https://electricistaculiacanpro.mx/blog/como-prevenir-cortocircuitos-casa/
- El buscador de colonias había perdido el "marco" que le aparece a los botones cuando alguien navega con el teclado (en vez del mouse) — sin eso, una persona que depende del teclado no sabe en qué casilla está parada. Se lo devolví → https://electricistaculiacanpro.mx/servicios/electricista-colonias-culiacan/
- Una página vieja de una colonia (con un error de dedo en el nombre desde hace tiempo) se había quedado sin ningún enlace que llevara a ella, flotando sola en el sitio. Puse un reenvío automático hacia la página correcta para que nadie caiga en una página huérfana.
- Borré 2 archivos de tipografía duplicados que ya no usaba nadie (ocupaban espacio sin ningún beneficio) y actualicé 3 documentos internos que todavía los mencionaban, para que no se vuelvan a copiar por error en el futuro.
- Uno de mis propios robots de revisión estaba marcando una "alerta falsa" en el blog (un color declarado en el código pero nunca usado de verdad en la página). Le enseñé a distinguir cuándo algo declarado se usa de verdad, para que deje de generar ruido.

## ⚠️ Encontré pero NO pude arreglar solo (10)
- Los botones flotantes de WhatsApp y Llamar tapan los enlaces de "Términos/Contacto/Privacidad" al final de casi 650 páginas cuando alguien llega hasta abajo en el celular — necesita un ajuste de espacio que toca muchas páginas a la vez, lo dejé anotado para hacerlo con cuidado.
- En unas 40 páginas, cierto texto naranja (preguntas frecuentes, testimonios, la tabla de precios) tiene poco contraste contra el fondo — se lee, pero cuesta trabajo a personas con baja visión. Es un cambio grande, lo dejé para una corrida dedicada.
- En 33 páginas, durante el primer instante de carga (antes de que termine de cargar el diseño), un botón de "Más información" y otro de WhatsApp se ven casi invisibles por una fracción de segundo. No afecta después de que carga todo, pero lo voy a corregir.
- El botón "Cerrar" de la ventana emergente de salida no recibe el foco automáticamente cuando alguien navega solo con el teclado — tendría que tabular a ciegas para encontrarlo.
- En 46 páginas, los menús de navegación no tienen "nombre" para los lectores de pantalla que usan las personas ciegas, así que anuncian "navegación, navegación" sin decir cuál es cuál.
- En las 642 páginas de colonias, la foto del encabezado a veces se descarga dos veces por un detalle técnico de tamaños — no se nota a simple vista, pero desperdicia datos del celular del visitante.
- Encontré archivos viejos (una copia sin comprimir del código, y hasta 2 copias completas de tu página principal) que siguen visibles públicamente aunque nadie los usa — no son peligrosos, pero es basura digital que vale la pena limpiar.
- Unos iconos de la app están duplicados (mismo dibujo, archivos repetidos) y el ícono más grande pesa casi 100KB cuando podría pesar la cuarta parte.
- 6 enlaces del sitio siguen apuntando a colonias que Google decidió no mostrar en sus resultados — no rompen nada, pero es tráfico que Google ignora de todos modos.
- En 4 artículos del blog, un dato técnico interno (el "costo estimado" que le mando a Google en un formato especial) está mal escrito como texto en vez de número — Google simplemente lo ignora, no se ve en la página.

## 🌱 Mejoré / agregué (0)
Sin páginas nuevas hoy: revisé Google Search Console con datos reales y no encontré ningún hueco de búsqueda que no estés cubriendo ya (fuera de temas que decidiste no ofrecer, como eléctrico automotriz). No inventé páginas porque eso dañaría tu posicionamiento.

## 🧠 Aprendí hoy (para no volver a fallar)
- Cuando una página tiene "tarjetas" que enlazan a otros artículos del blog, voy a comparar siempre el título de la tarjeta contra el título real del artículo al que lleva — hoy encontré 5 que no coincidían y llevaban meses así.
- Al desbloquear una herramienta externa (como Microsoft Clarity) en el "candado de seguridad" del sitio, voy a revisar primero a qué direcciones exactas se conecta esa herramienta, en vez de asumir que es solo una — hoy mi primer intento se quedó corto y mi propio verificador lo cachó antes de publicar.
- Uno de mis robots de revisión daba una alarma falsa por un color declarado pero nunca usado de verdad en una página. Ya le enseñé a distinguir "está escrito" de "se usa de verdad".
- Confirmé con datos duros de Google (7 semanas de medición, como acordamos) que diferenciar más colonias pequeñas no está funcionando: ninguna de las 8 que se probaron quedó indexada. Ya frené esa estrategia hasta que tú decidas el siguiente paso.
(ya van 131 reglas aprendidas en total)

## ⏳ Necesito que tú decidas (4)
- El enlace de tu ficha de Google (Google Maps/Google Business) que tiene el sitio está roto — en vez de llevar a tu ficha, lleva a la página principal de Google. Necesito que me pases el enlace correcto de "Compartir" de tu ficha para arreglarlo — no puedo adivinarlo.
- Encontré 5 lugares distintos del sitio con precios diferentes para el mismo servicio (por ejemplo, el diagnóstico aparece como $200 en un lado y $300 en otro). No toco precios sin tu autorización: necesito que me digas cuál es la tabla correcta y de ahí actualizo todo lo demás.
- Hay un "mapa de tu sitio" viejo registrado en el panel de Google que ya no existe (da error 404) y lleva casi 2 meses ensuciando el reporte de Google. No es algo que se arregle con código — hay que entrar al panel de Search Console y borrarlo manualmente ahí; si quieres te explico paso a paso.
- Como acordamos hace semanas, si a las 3-4 semanas las colonias nuevas no se indexaban en Google, había que parar de crearlas. Ya pasaron 7 semanas y confirmé con datos: ninguna de las 8 que probamos quedó indexada. Ya detuve la creación de más colonias nuevas — solo necesito que confirmes si quieres que además "apague" (sin borrar) las páginas de colonias que Google decidió no mostrar, o que las deje como están mientras se sigue midiendo.

## 📦 ¿Se publicó?
Sí, todo revisado y en vivo; le avisé a Google para que lo muestre.
