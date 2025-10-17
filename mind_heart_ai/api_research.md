# Investigación de APIs para Agente IA en Psicología y Relaciones de Pareja

## API de Gemini (Google AI)

### Descripción
Gemini es la API de Google para modelos de inteligencia artificial generativa, parte de Google AI Studio. Es ideal para generar respuestas expertas en psicología y relaciones de pareja, ya que puede procesar consultas complejas y proporcionar consejos basados en conocimiento general y patrones aprendidos.

### Endpoints Principales
- **Generación de Texto**: `https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent`
  - Método: POST
  - Parámetros: prompt, configuración de modelo (temperatura, max_tokens, etc.)
- **Chat Interactivo**: Soporta sesiones de conversación continuas.

### Autenticación
- Requiere API Key de Google AI Studio.
- Se pasa en el header: `Authorization: Bearer {API_KEY}` o como parámetro de query `key={API_KEY}`.

### Límites de Uso
- Cuotas diarias: Dependiendo del plan (gratuito: limitado, pago: más alto).
- Costos: Basado en tokens procesados (aprox. $0.00025 por 1K tokens para Gemini 1.5).
- Límites de rate: 60 requests por minuto para cuentas gratuitas.

### Integración en Python
Usar la librería oficial `google-generativeai`:
```python
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Consulta sobre psicología")
```

## API de Tavily

### Descripción
Tavily es una API para búsqueda web inteligente, optimizada para obtener información relevante y actualizada. Útil para enriquecer respuestas del agente con datos frescos sobre psicología, estudios recientes o consejos en relaciones de pareja.

### Endpoints Principales
- **Búsqueda**: `https://api.tavily.com/search`
  - Método: GET
  - Parámetros: query (consulta), api_key, include_images (opcional), etc.

### Autenticación
- Requiere API Key obtenida de Tavily.
- Se pasa como parámetro: `api_key={API_KEY}`.

### Límites de Uso
- Cuotas: Dependiendo del plan (gratuito: 1000 búsquedas/mes, pago: ilimitado).
- Costos: $0.005 por búsqueda para plan básico.
- Límites de rate: 10 requests por segundo.

### Integración en Python
Usar requests o la librería `tavily-python` si existe:
```python
import requests
response = requests.get("https://api.tavily.com/search", params={
    "query": "psicología de relaciones de pareja",
    "api_key": "YOUR_API_KEY"
})
results = response.json()
```

## Consideraciones para el Proyecto
- **Seguridad**: Almacenar API keys de forma segura (variables de entorno, no en código).
- **Combinación**: Usar Tavily para buscar información contextual, luego Gemini para sintetizar y generar respuestas expertas.
- **Costos**: Monitorear uso para evitar exceder límites.
- **Actualizaciones**: Ambas APIs evolucionan; verificar documentación oficial periódicamente.