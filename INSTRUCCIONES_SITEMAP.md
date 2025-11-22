# Instrucciones para Actualizar el Sitemap

## Proposito

El script `update-sitemap.sh` automatiza la actualizacion del sitemap con fechas reales de modificacion de archivos y configuraciones de `changefreq` optimizadas para SEO.

## Cuando Usar el Script

Ejecuta el script cada vez que:
- ✅ Actualices contenido en cualquier pagina (homepage, servicios, blog)
- ✅ Agregues nuevos articulos de blog
- ✅ Modifiques paginas de servicios
- ✅ Hagas cambios importantes en el sitio
- ✅ Antes de hacer deploy a produccion

## Como Usar

```bash
# Desde la raiz del proyecto
./update-sitemap.sh
```

## Que Hace el Script

1. **Lee la fecha de modificacion real** de cada archivo HTML
2. **Asigna `changefreq` inteligente** segun el tipo de pagina:
   - `weekly`: Homepage, Blog index (contenido dinamico)
   - `monthly`: Servicios, Articulos de blog (contenido estable)
   - `yearly`: Contacto (raramente cambia)
3. **Mantiene las prioridades** correctas para SEO
4. **Genera sitemap valido** en `sitemaps/main_sitemap.xml`

## Configuracion de Changefreq

| Tipo de Pagina | Changefreq | Razon |
|----------------|------------|-------|
| Homepage | weekly | Se actualiza frecuentemente con nuevo contenido |
| Blog Index | weekly | Se agrega nuevo contenido regularmente |
| Paginas de Servicio | monthly | Contenido estable, cambios ocasionales |
| Articulos de Blog | monthly | Contenido evergreen, raramente se modifica |
| Pagina de Contacto | yearly | Informacion estatica |

## Agregar Nuevas URLs

Si agregas nuevas paginas al sitio:

1. Abre `update-sitemap.sh`
2. Agrega una nueva linea en la seccion "Procesar todas las URLs":

```bash
process_url "https://electricistaculiacanpro.mx/nueva-pagina/" "0.X"
```

3. Ajusta la prioridad (0.1 a 1.0) segun la importancia de la pagina

## Prioridades Recomendadas

- **1.0**: Homepage
- **0.9**: Servicios principales, paginas de alta conversion
- **0.8**: Servicios secundarios, categorias importantes
- **0.7**: Articulos de blog, paginas de soporte
- **0.6**: Contenido complementario

## Actualizar Meta Tag x-build

Despues de ejecutar el script, actualiza el meta tag en `index.html`:

```html
<meta name="x-build" content="YYYY-MM-DDTHH:MM:SSZ" />
```

## Verificar el Sitemap

Despues de ejecutar el script:

1. Revisa `sitemaps/main_sitemap.xml`
2. Verifica que las fechas sean actuales
3. Confirma que todas las URLs esten presentes
4. Valida en: https://www.xml-sitemaps.com/validate-xml-sitemap.html

## Importante

- El script **NO** hace commit automatico
- **Revisa** los cambios antes de hacer commit
- **Ejecuta** antes de cada deploy importante
- **Manten sincronizado** el meta tag x-build con las fechas del sitemap

## Beneficios SEO

✅ **Senales de frescura**: Google ve fechas actualizadas reales
✅ **Crawl budget optimizado**: `changefreq` ayuda a Google a priorizar
✅ **Indexacion rapida**: Nuevas paginas se descubren mas rapido
✅ **Consistencia**: Meta tags alineados con sitemap
