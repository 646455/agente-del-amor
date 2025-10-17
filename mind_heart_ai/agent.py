import os
from tavily_client import TavilyClient
from gemini_client import GeminiClient
from utils import validate_query

class MindHeartAgent:
    def __init__(self):
        self.tavily_client = TavilyClient()
        self.gemini_client = GeminiClient()

    def process_query(self, query: str, category_instruction: str = "") -> str:
        # Validar consulta
        if not validate_query(query):
            return "Lo siento, tu consulta parece estar fuera del alcance de psicología y relaciones de pareja. Por favor, reformula tu pregunta."

        try:
            search_results = []
            try:
                # Intentar buscar información relevante con Tavily
                search_results = self.tavily_client.search(query)
            except Exception as tavily_error:
                # Si Tavily falla, continuar sin búsqueda (usar solo conocimiento de Gemini)
                print(f"Tavily no disponible: {tavily_error}. Continuando con Gemini solo.")

            # Construir prompt para Gemini
            prompt = self._build_prompt(query, search_results, category_instruction)

            # Generar respuesta con Gemini
            response = self.gemini_client.generate_response(prompt)

            return response

        except Exception as e:
            return f"Error al procesar la consulta: {str(e)}. Verifica que las API keys estén configuradas correctamente."

    def _build_prompt(self, query: str, search_results: list, category_instruction: str = "") -> str:
        if search_results:
            context = "\n".join([f"- {result['title']}: {result['content'][:200]}..." for result in search_results[:3]])
            context_text = f"Información relevante encontrada en fuentes confiables:\n{context}"
        else:
            context_text = "No se pudo acceder a información externa actualizada."

        prompt = f"""
Eres un psicólogo experto y consejero en relaciones de pareja con más de 20 años de experiencia.
Una persona te consulta sobre el tema de "{query}"

{context_text}

{category_instruction}

Proporciona una respuesta empática, basada en evidencia y profesional que incluya:
1. Validación de los sentimientos del consultante
2. Consejos prácticos y accionables específicos para su situación
3. Estrategias de comunicación efectiva
4. Recomendaciones para buscar ayuda profesional si es necesario
5. Recursos adicionales o lecturas recomendadas si aplica

IMPORTANTE: Adapta tu respuesta al contexto cultural hispano parlante, considerando valores familiares, comunicación emocional y dinámicas sociales propias de la cultura latina.

Responde en español, de manera clara, cálida y concisa. Usa un tono profesional pero cercano y empático.
"""

        return prompt