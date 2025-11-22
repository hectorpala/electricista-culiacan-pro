#!/usr/bin/env python3
"""
Sistema de Agentes para Electricista Culiacán Pro
Genera contenido SEO optimizado en formato JSON
"""

import os
import sys
import json
from dotenv import load_dotenv
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

# Importar agentes y tareas
from agents.contenido_electricista import ContenidoElectricistaAgent
from tasks.tarea_contenido_electricista import TareaContenidoElectricista


def inicializar_llm():
    """Inicializa el modelo de lenguaje"""
    load_dotenv()

    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Error: OPENAI_API_KEY no encontrada en .env")
        print("💡 Copia .env.example a .env y agrega tu API key")
        sys.exit(1)

    model = os.getenv('OPENAI_MODEL_NAME', 'gpt-4-turbo-preview')

    return ChatOpenAI(
        model=model,
        temperature=0.7,
        api_key=api_key
    )


def generar_contenido_electricista(keyword: str, zona: str):
    """
    Genera contenido SEO para Electricista Culiacán Pro

    Args:
        keyword: Palabra clave principal (ej: "electricista urgente")
        zona: Zona o colonia de Culiacán (ej: "Culiacán Centro", "Las Quintas")

    Returns:
        dict: Contenido generado en formato JSON
    """
    print(f"\n⚡ Generando contenido para: {keyword} + {zona}")
    print("=" * 60)

    # Inicializar LLM
    llm = inicializar_llm()

    # Crear agente
    agente_contenido = ContenidoElectricistaAgent(llm).crear_agente()

    # Crear tarea
    tarea = TareaContenidoElectricista.generar_pagina_seo(
        agent=agente_contenido,
        keyword=keyword,
        zona=zona
    )

    # Crear crew
    crew = Crew(
        agents=[agente_contenido],
        tasks=[tarea],
        process=Process.sequential,
        verbose=True
    )

    # Ejecutar
    print("\n🚀 Iniciando generación de contenido...\n")
    resultado = crew.kickoff()

    return resultado


def guardar_resultado(resultado, keyword, zona):
    """Guarda el resultado en un archivo JSON"""
    # Crear nombre de archivo seguro
    filename = f"{keyword.replace(' ', '-')}_{zona.replace(' ', '-')}.json".lower()
    filepath = os.path.join('output', filename)

    # Crear directorio si no existe
    os.makedirs('output', exist_ok=True)

    # Intentar parsear y guardar
    try:
        # Si resultado es string, intentar parsearlo
        if isinstance(resultado, str):
            datos = json.loads(resultado)
        else:
            datos = resultado

        # Guardar con formato bonito
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

        print(f"\n✅ Archivo guardado: {filepath}")
        return filepath

    except json.JSONDecodeError as e:
        print(f"\n⚠️  El resultado no es JSON válido: {e}")
        print("\n📄 Guardando resultado raw...")

        # Guardar como texto plano
        txt_filepath = filepath.replace('.json', '.txt')
        with open(txt_filepath, 'w', encoding='utf-8') as f:
            f.write(str(resultado))

        print(f"✅ Guardado como: {txt_filepath}")
        return txt_filepath


def main():
    """Función principal"""
    print("""
╔══════════════════════════════════════════════════════════╗
║   🔌 Generador de Contenido SEO                          ║
║   Electricista Culiacán Pro                              ║
╚══════════════════════════════════════════════════════════╝
    """)

    # Verificar argumentos
    if len(sys.argv) < 3:
        print("📋 Uso: python main.py '<keyword>' '<zona>'")
        print("\n💡 Ejemplos:")
        print("   python main.py 'electricista urgente' 'Culiacán Centro'")
        print("   python main.py 'instalacion electrica' 'Las Quintas'")
        print("   python main.py 'reparacion cortocircuitos' 'Tres Ríos'")
        print("\n🗺️  Zonas comunes de Culiacán:")
        print("   - Las Quintas, Tres Ríos, Campestre (Zona Norte)")
        print("   - Centro, Guadalupe, Chapultepec (Zona Centro)")
        print("   - Villa Universidad, Montebello (Zona Sur)")
        sys.exit(1)

    keyword = sys.argv[1]
    zona = sys.argv[2]

    # Generar contenido
    try:
        resultado = generar_contenido_electricista(keyword, zona)

        print("\n" + "=" * 60)
        print("📊 RESULTADO:")
        print("=" * 60)
        print(resultado)

        # Guardar archivo
        archivo = guardar_resultado(resultado, keyword, zona)

        print("\n✨ ¡Contenido generado exitosamente!")

    except Exception as e:
        print(f"\n❌ Error durante la generación: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
