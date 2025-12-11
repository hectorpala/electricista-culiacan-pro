# Automatizacion de Landing de Colonias

Crea landing pages para colonias de Culiacan automaticamente.

## Uso

```
/automatizacioncolonia "Nombre de la Colonia"
```

**Ejemplos:**
- `/automatizacioncolonia "Las Quintas"`
- `/automatizacioncolonia "Tres Rios"`
- `/automatizacioncolonia "Villa Universidad"`

---

## Lo que hace automaticamente

1. Genera el slug de la colonia (ej: "las-quintas")
2. Crea el directorio en `/colonias/{slug}/`
3. Copia el template base de Centro
4. Reemplaza todas las menciones de "Centro" por el nombre de la colonia
5. Actualiza las URLs canonicas y rutas
6. Valida que el HTML sea correcto

---

## Ejecucion

Cuando ejecutes este comando, ejecuta el script:

```bash
./scripts/crear-colonia.sh "$ARGUMENTS"
```

Luego muestra el resultado al usuario con:
- El slug generado
- La URL final de la colonia
- Confirmacion de que la landing fue creada

---

## Archivo de colonias disponible

El archivo `culiacan_colonias.json` contiene:
- **168 colonias**
- **303 fraccionamientos**

Para ver colonias faltantes, compara las que estan en el JSON vs las carpetas existentes en `/colonias/`.

---

## Creacion masiva

Para crear multiples colonias, puedes llamar el script varias veces:

```bash
./scripts/crear-colonia.sh "Colonia 1"
./scripts/crear-colonia.sh "Colonia 2"
./scripts/crear-colonia.sh "Colonia 3"
```

O pedir al usuario que proporcione una lista de colonias a crear.
