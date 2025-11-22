from crewai import Agent
from langchain_openai import ChatOpenAI

class EscritorAgent:
    """
    Agente especializado en creación de contenido y redacción
    """

    def __init__(self, llm):
        self.llm = llm

    def crear_agente(self):
        return Agent(
            role='Escritor Profesional',
            goal='Crear contenido de alta calidad, atractivo y bien estructurado',
            backstory="""Eres un escritor profesional con años de experiencia creando
            contenido para diferentes audiencias. Tienes la habilidad de tomar información
            compleja y convertirla en narrativas claras y convincentes. Tu escritura es
            siempre precisa, atractiva y adaptada al público objetivo.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
