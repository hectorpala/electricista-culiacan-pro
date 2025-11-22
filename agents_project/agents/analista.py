from crewai import Agent
from langchain_openai import ChatOpenAI

class AnalistaAgent:
    """
    Agente especializado en análisis de datos y generación de insights
    """

    def __init__(self, llm):
        self.llm = llm

    def crear_agente(self):
        return Agent(
            role='Analista de Datos',
            goal='Analizar información y extraer insights valiosos y accionables',
            backstory="""Eres un analista de datos experto con habilidades excepcionales
            para identificar patrones, tendencias y oportunidades en los datos. Puedes
            tomar grandes cantidades de información y convertirla en conclusiones claras
            y recomendaciones prácticas. Tu análisis siempre es profundo, objetivo y
            orientado a la acción.""",
            verbose=True,
            allow_delegation=True,
            llm=self.llm
        )
