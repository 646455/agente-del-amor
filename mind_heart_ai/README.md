# Agente IA Experto en Psicología y Relaciones de Pareja

Una aplicación web inteligente que combina las APIs de Gemini y Tavily para proporcionar consejos expertos en psicología y relaciones de pareja.

## 🚀 Características

- **Consultas Inteligentes**: Procesa preguntas sobre psicología y relaciones
- **Búsqueda Contextual**: Utiliza Tavily para encontrar información relevante actualizada
- **Respuestas Expertas**: Genera consejos basados en evidencia con Gemini
- **Interfaz Amigable**: Desarrollada con Streamlit para fácil uso
- **Validación Segura**: Filtra consultas irrelevantes y promueve el bienestar

## 🛠️ Tecnologías

- **Python 3.8+**
- **Streamlit** - Framework web
- **Google Gemini API** - Generación de respuestas IA
- **Tavily API** - Búsqueda web inteligente
- **python-dotenv** - Gestión de variables de entorno

## 📋 Requisitos Previos

1. **API Keys**:
   - [Google AI Studio](https://aistudio.google.com/) para Gemini API
   - [Tavily](https://tavily.com/) para búsqueda web

2. **Python**:
   - Versión 3.8 o superior

## 🔧 Instalación

1. **Clona o descarga el proyecto**:
   ```bash
   git clone <repository-url>
   cd mind_heart_ai
   ```

2. **Instala dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura variables de entorno**:
   - Copia `.env.example` a `.env`
   - Completa tus API keys:
   ```env
   GEMINI_API_KEY=tu_clave_de_gemini_aqui
   TAVILY_API_KEY=tu_clave_de_tavily_aqui
   ```

## 🚀 Uso Local

Ejecuta la aplicación:
```bash
streamlit run app.py
```

La aplicación estará disponible en `http://localhost:8501`

## 🌐 Despliegue en Streamlit Cloud

1. **Sube el código a GitHub** (repositorio público)

2. **Ve a [Streamlit Cloud](https://share.streamlit.io/)**

3. **Conecta tu repositorio**:
   - Selecciona el repositorio
   - Archivo principal: `mind_heart_ai/app.py`
   - Rama: `main`

4. **Configura secrets**:
   - En Streamlit Cloud, ve a Settings > Secrets
   - Agrega:
   ```toml
   GEMINI_API_KEY = "tu_clave_de_gemini"
   TAVILY_API_KEY = "tu_clave_de_tavily"
   ```

5. **Despliega** y obtén la URL pública

## 📁 Estructura del Proyecto

```
mind_heart_ai/
├── app.py              # Aplicación principal de Streamlit
├── agent.py            # Lógica del agente IA
├── tavily_client.py    # Cliente para API de Tavily
├── gemini_client.py    # Cliente para API de Gemini
├── utils.py            # Utilidades y validaciones
├── test.py             # Script de pruebas
├── requirements.txt    # Dependencias Python
├── .env.example        # Ejemplo de variables de entorno
└── README.md           # Esta documentación
```

## 🧪 Pruebas

Ejecuta las pruebas básicas:
```bash
python test.py
```

## ⚠️ Consideraciones Éticas

- **No reemplaza terapia profesional**: Las respuestas son informativas, no diagnósticas
- **Privacidad**: No almacena datos personales de usuarios
- **Bienestar**: Promueve buscar ayuda profesional cuando sea necesario

## 📄 Licencia

Este proyecto es de código abierto. Consulta el archivo de licencia para más detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores.

## 📞 Soporte

Para soporte técnico o preguntas sobre el proyecto, por favor contacta al desarrollador.