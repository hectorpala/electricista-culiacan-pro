from crewai import Task

class Tareas:
    """
    Define las tareas que los agentes ejecutarán
    """

    @staticmethod
    def tarea_investigacion(agent, tema):
        return Task(
            description=f"""Investiga a fondo sobre: {tema}

            Debes:
            1. Buscar información actualizada y confiable
            2. Identificar las tendencias principales
            3. Recopilar datos y estadísticas relevantes
            4. Verificar la credibilidad de las fuentes

            Proporciona un resumen completo con todos los hallazgos importantes.""",
            agent=agent,
            expected_output="Un informe detallado de investigación con fuentes verificadas"
        )

    @staticmethod
    def tarea_analisis(agent, datos):
        return Task(
            description=f"""Analiza la siguiente información: {datos}

            Debes:
            1. Identificar patrones y tendencias clave
            2. Extraer insights valiosos
            3. Generar conclusiones basadas en datos
            4. Proporcionar recomendaciones accionables

            El análisis debe ser profundo y objetivo.""",
            agent=agent,
            expected_output="Un análisis completo con insights y recomendaciones"
        )

    @staticmethod
    def tarea_escritura(agent, tema, informacion):
        return Task(
            description=f"""Crea un artículo/contenido sobre: {tema}

            Basándote en: {informacion}

            El contenido debe:
            1. Ser claro y fácil de entender
            2. Estar bien estructurado con introducción, desarrollo y conclusión
            3. Incluir los puntos clave de manera atractiva
            4. Tener un tono profesional pero accesible
            5. Ser original y libre de plagio

            Formato: Markdown""",
            agent=agent,
            expected_output="Un artículo completo y bien redactado en formato markdown"
        )
