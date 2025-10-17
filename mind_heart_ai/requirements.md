# Requisitos Funcionales del Agente IA Experto en Psicología y Relaciones de Pareja

## Visión General
El agente IA será una aplicación web desarrollada en Python con Streamlit, que actúa como un experto virtual en psicología y relaciones de pareja. Utilizará las APIs de Gemini y Tavily para proporcionar respuestas informadas, basadas en conocimiento experto y datos actualizados.

## Funcionalidades Principales

### 1. Interfaz de Usuario
- **Entrada de Consultas**: Campo de texto para que el usuario ingrese preguntas o descripciones de situaciones relacionadas con psicología o relaciones de pareja.
- **Visualización de Respuestas**: Área dedicada para mostrar las respuestas generadas por el agente, formateadas de manera clara y legible.
- **Historial de Conversaciones**: Opción para ver conversaciones anteriores (funcionalidad avanzada).

### 2. Procesamiento de Consultas
- **Análisis de Entrada**: El agente debe identificar si la consulta es relevante (psicología/relaciones) y rechazar consultas fuera de scope.
- **Búsqueda de Información**: Integrar Tavily para buscar artículos científicos, consejos actualizados o estudios relevantes sobre el tema.
- **Generación de Respuestas**: Usar Gemini para sintetizar la información de Tavily y generar respuestas expertas, empáticas y basadas en evidencia.

### 3. Expertise Específica
- **Psicología**: Consejos sobre salud mental, manejo de emociones, terapia, etc.
- **Relaciones de Pareja**: Comunicación, resolución de conflictos, compatibilidad, intimidad, etc.
- **Ética**: Respuestas deben promover el bienestar, recomendar consultar profesionales cuando sea necesario, y evitar diagnósticos médicos.

### 4. Flujo de Interacción
1. Usuario ingresa consulta en Streamlit.
2. Agente valida la consulta.
3. Si válida, realiza búsqueda con Tavily.
4. Envía resultados de búsqueda + consulta original a Gemini para generar respuesta.
5. Muestra respuesta al usuario.
6. Opcional: Guarda en historial.

### 5. Validaciones y Manejo de Errores
- Validar que la consulta no esté vacía y sea relevante.
- Manejar errores de API (timeouts, límites excedidos).
- Mensajes de error amigables al usuario.

### 6. Funcionalidades Avanzadas
- **Personalización**: Permitir al usuario especificar contexto (e.g., edad, género, tipo de relación).
- **Modo Seguro**: Opción para respuestas más conservadoras o dirigidas a profesionales.
- **Multilenguaje**: Soporte para español (idioma principal) y inglés.

## Requisitos No Funcionales
- **Rendimiento**: Respuestas en menos de 10 segundos.
- **Escalabilidad**: Capaz de manejar múltiples usuarios concurrentes.
- **Seguridad**: No almacenar datos sensibles; usar HTTPS en despliegue.
- **Accesibilidad**: Interfaz simple y accesible.

## Casos de Uso
- **Usuario A**: "Estoy teniendo problemas de comunicación con mi pareja. ¿Qué puedo hacer?"
  - Agente busca info sobre comunicación en relaciones, genera consejos prácticos.
- **Usuario B**: "Siento ansiedad constante. ¿Es normal?"
  - Agente proporciona info general sobre ansiedad, recomienda consultar terapeuta.

## Alcance y Limitaciones
- No reemplaza terapia profesional.
- Basado en datos disponibles; no garantiza precisión médica.
- Limitado a consultas textuales; no soporta voz o imágenes inicialmente.