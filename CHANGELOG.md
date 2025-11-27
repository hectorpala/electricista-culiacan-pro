# Changelog - Electricista Culiacán Pro

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [2024-11-27]

### Agregado
- Sistema de comandos Claude (.claude/commands/) para automatización de workflow
- Comando `/landing-creator` para crear landing pages con SEO optimizado
- Comando `/validar` para validar páginas antes de commit
- Comando `/deploy-quick` para deployment automático a GitHub Pages
- Comando `/seo-optimizer` para análisis y optimización SEO
- Comando `/daily-summary` para resúmenes diarios de trabajo
- Comando `/weekly-report` para reportes semanales ejecutivos
- Skill `@validador-pagina` para validación interactiva de páginas
- CHANGELOG.md para tracking automático de cambios

### Mejorado
- Documentación de reglas críticas (REGLA #0 a #0.5) en landing-creator.md
- Validación obligatoria de mobile + desktop antes de commit
- Critical CSS completo en todas las landing pages

### Corregido
- **Colores corporativos:** Cambiados de azul a naranja (#E36414, #F97316) en index.html
  - Variables CSS `:root` actualizadas
  - Gradientes de botones corregidos
  - Links y elementos interactivos actualizados
  - Estilos inline corregidos
  - **Razón:** Mantener identidad visual idéntica a Plomero Culiacán Pro (empresa hermana)

### Documentado
- **Branding compartido:** Electricista Culiacán Pro y Plomero Culiacán Pro son empresas hermanas
- **Identidad visual idéntica:** Ambas empresas usan los mismos colores (#E36414, #F97316)
- **Aclaración en landing-creator.md:** Solo cambia contenido textual, NO diseño/colores
- **Aclaración en validador-pagina.md:** El validador NO cambia colores (ya son correctos)
- **Razón corporativa:** Mantener consistencia visual entre empresas del mismo grupo

### Notas
- Sistema copiado y adaptado desde proyecto plomero culiacan pro
- Todos los comandos adaptados a contexto de servicios eléctricos
- URLs actualizadas a electricistaculiacanpro.mx

---

## Formato de Changelog

Cada entrada debe seguir este formato:

### Agregado
- Nuevas funcionalidades, landing pages, secciones completas

### Mejorado
- Optimizaciones de performance (LCP, CLS, bundle size)
- Mejoras SEO (keywords, schemas, meta tags)
- Refinamientos de diseño sin cambiar funcionalidad

### Corregido
- Corrección de bugs, errores, problemas visuales
- Fixes de schemas JSON-LD, breadcrumbs, paths

### Eliminado
- Funcionalidades removidas, archivos obsoletos
