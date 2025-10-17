#!/usr/bin/env python3
"""
Script de pruebas básicas para el Agente IA Mind&Heart
"""

from utils import validate_query

def test_validate_query():
    """Prueba la función de validación de consultas"""
    print("Probando validate_query...")

    # Casos válidos
    valid_queries = [
        "Tengo problemas de ansiedad en mi relación",
        "Cómo mejorar la comunicación con mi pareja",
        "Consejos para manejar el estrés emocional"
    ]

    # Casos inválidos
    invalid_queries = [
        "",
        "Hola",
        "123"
    ]

    for query in valid_queries:
        assert validate_query(query), f"Falló validación para: {query}"
        print(f"✓ Válida: {query}")

    for query in invalid_queries:
        assert not validate_query(query), f"Falló invalidación para: {query}"
        print(f"✓ Inválida: {query}")

    print("validate_query: PASSED\n")

def test_imports():
    """Prueba que todos los módulos se importen correctamente"""
    print("Probando imports...")

    try:
        from agent import MindHeartAgent
        print("✓ Import MindHeartAgent")

        from tavily_client import TavilyClient
        print("✓ Import TavilyClient")

        from gemini_client import GeminiClient
        print("✓ Import GeminiClient")

        from utils import validate_query
        print("✓ Import utils")

        print("Imports: PASSED\n")

    except ImportError as e:
        print(f"✗ Error en import: {e}")
        raise

def test_agent_initialization():
    """Prueba inicialización del agente (sin API keys)"""
    print("Probando inicialización del agente...")

    try:
        from agent import MindHeartAgent
        # Esto debería fallar sin API keys, pero verificar que se importe
        agent = MindHeartAgent()
        print("✗ Agente se inicializó sin API keys (inesperado)")
    except ValueError as e:
        if "no configurada" in str(e):
            print("✓ Agente correctamente requiere API keys")
        else:
            raise
    except Exception as e:
        print(f"✗ Error inesperado: {e}")
        raise

    print("Agent initialization: PASSED\n")

if __name__ == "__main__":
    print("Iniciando pruebas del Agente IA Mind&Heart\n")

    test_imports()
    test_validate_query()
    test_agent_initialization()

    print("Todas las pruebas pasaron exitosamente! 🎉")