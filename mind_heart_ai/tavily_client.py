import os
import requests
from typing import List, Dict

class TavilyClient:
    def __init__(self):
        self.api_key = os.getenv("TAVILY_API_KEY")
        self.base_url = "https://api.tavily.com/search"

    def search(self, query: str) -> List[Dict]:
        if not self.api_key:
            raise ValueError("TAVILY_API_KEY no configurada")

        params = {
            "api_key": self.api_key,
            "query": query,
            "include_answer": "false",
            "search_depth": "advanced"
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            # Extraer resultados relevantes
            results = []
            for result in data.get("results", [])[:5]:  # Limitar a 5 resultados
                results.append({
                    "title": result.get("title", ""),
                    "content": result.get("content", ""),
                    "url": result.get("url", "")
                })

            return results

        except requests.RequestException as e:
            raise Exception(f"Error en búsqueda Tavily: {str(e)}")