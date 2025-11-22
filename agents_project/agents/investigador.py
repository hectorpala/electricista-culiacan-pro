from crewai import Agent
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools

class InvestigadorAgent:
    """
    Agente especializado en investigación y recopilación de información
    """

    def __init__(self, llm):
        self.llm = llm

    def crear_agente(self):
        return Agent(
            role='Investigador Experto',
            goal='Investigar y recopilar información precisa y relevante sobre cualquier tema',
            backstory="""Eres un investigador experimentado con habilidades excepcionales
            para encontrar información precisa y confiable. Tienes acceso a múltiples fuentes
            y sabes cómo validar la información que encuentras. Tu objetivo es proporcionar
            datos verificados y útiles para el equipo.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[SearchTools.search_internet()]
        )
