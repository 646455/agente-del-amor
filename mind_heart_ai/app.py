import streamlit as st
from dotenv import load_dotenv
from agent import MindHeartAgent
import json
import os
from datetime import datetime

# Cargar variables de entorno
load_dotenv()

# Configuración de la página
st.set_page_config(
    page_title="Mind & Heart AI - Psicología y Relaciones",
    page_icon="💙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar estado de la sesión ANTES de cualquier uso
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'current_category' not in st.session_state:
    st.session_state.current_category = "General"
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False
if 'saved_conversations' not in st.session_state:
    st.session_state.saved_conversations = []
if 'welcome_shown' not in st.session_state:
    st.session_state.welcome_shown = False

# Cargar conversaciones guardadas desde archivo
def load_saved_conversations():
    try:
        if os.path.exists('conversaciones_guardadas.json'):
            with open('conversaciones_guardadas.json', 'r', encoding='utf-8') as f:
                return json.load(f)
    except:
        pass
    return []

# Guardar conversaciones en archivo
def save_conversations_to_file():
    try:
        with open('conversaciones_guardadas.json', 'w', encoding='utf-8') as f:
            json.dump(st.session_state.saved_conversations, f, ensure_ascii=False, indent=2)
    except Exception as e:
        st.error(f"Error al guardar conversaciones: {str(e)}")

# Cargar conversaciones al inicio
if not st.session_state.saved_conversations:
    st.session_state.saved_conversations = load_saved_conversations()

# Estilos CSS personalizados
if st.session_state.dark_mode:
    st.markdown("""
    <style>
        .main {
            background-color: #1e1e1e;
            color: #ffffff;
        }
        .main-header {
            background: linear-gradient(135deg, #333333 0%, #555555 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }
        .chat-message {
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        }
        .user-message {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin-left: 2rem;
        }
        .assistant-message {
            background: #333333;
            border-left: 4px solid #667eea;
            margin-right: 2rem;
            color: #ffffff;
        }
        .category-button {
            background: #667eea;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            margin: 0.25rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .category-button:hover {
            background: #5a6fd8;
            transform: translateY(-2px);
        }
        .mood-indicator {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: bold;
        }
        .mood-positive { background: #d4edda; color: #155724; }
        .mood-neutral { background: #fff3cd; color: #856404; }
        .mood-negative { background: #f8d7da; color: #721c24; }
        .stTextArea textarea {
            background-color: #333333;
            color: #ffffff;
            border: 1px solid #555555;
        }
        .stButton button {
            background-color: #667eea;
            color: white;
        }
        .stButton button:hover {
            background-color: #5a6fd8;
        }
        h1, h2, h3, p {
            color: #ffffff;
        }
        .sidebar .sidebar-content {
            background-color: #2d2d2d;
        }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .chat-message {
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .user-message {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin-left: 2rem;
        }
        .assistant-message {
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            margin-right: 2rem;
        }
        .category-button {
            background: #667eea;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            margin: 0.25rem;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .category-button:hover {
            background: #5a6fd8;
            transform: translateY(-2px);
        }
        .mood-indicator {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            border-radius: 15px;
            font-size: 0.8rem;
            font-weight: bold;
        }
        .mood-positive { background: #d4edda; color: #155724; }
        .mood-neutral { background: #fff3cd; color: #856404; }
        .mood-negative { background: #f8d7da; color: #721c24; }
    </style>
    """, unsafe_allow_html=True)

# Función para aplicar tema
def apply_theme():
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
            [data-testid="stAppViewContainer"] {
                background-color: #1e1e1e !important;
                color: #ffffff !important;
            }
            [data-testid="stSidebar"] {
                background-color: #2d2d2d !important;
            }
            .main-header {
                background: linear-gradient(135deg, #333333 0%, #555555 100%) !important;
                color: white !important;
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                margin-bottom: 2rem;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            }
            .chat-message {
                padding: 1rem;
                border-radius: 10px;
                margin: 0.5rem 0;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
            }
            .user-message {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
                color: white !important;
                margin-left: 2rem;
            }
            .assistant-message {
                background: #333333 !important;
                border-left: 4px solid #667eea;
                margin-right: 2rem;
                color: #ffffff !important;
            }
            .stTextArea textarea {
                background-color: #333333 !important;
                color: #ffffff !important;
                border: 1px solid #555555 !important;
            }
            .stButton button {
                background-color: #667eea !important;
                color: white !important;
            }
            .stButton button:hover {
                background-color: #5a6fd8 !important;
            }
            h1, h2, h3, p, div, span {
                color: #ffffff !important;
            }
            .stMarkdown p, .stMarkdown div, .stMarkdown span {
                color: #ffffff !important;
            }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
            .main-header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 2rem;
                border-radius: 15px;
                text-align: center;
                margin-bottom: 2rem;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
            .chat-message {
                padding: 1rem;
                border-radius: 10px;
                margin: 0.5rem 0;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }
            .user-message {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                margin-left: 2rem;
            }
            .assistant-message {
                background: #f8f9fa;
                border-left: 4px solid #667eea;
                margin-right: 2rem;
            }
        </style>
        """, unsafe_allow_html=True)

# Aplicar tema
apply_theme()

# Sidebar con funcionalidades adicionales
with st.sidebar:
    # Logo en el sidebar
    try:
        st.image("mind_heart_ai/logo.png", width=100, use_container_width=True)
    except:
        st.markdown("🧠")  # Fallback si no hay imagen

    st.title("🎯 Mind & Heart AI")
    st.markdown("---")

    # Selector de modo oscuro/claro
    if st.button("🌙 Modo Oscuro" if not st.session_state.dark_mode else "☀️ Modo Claro"):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()

    # Categorías de consultas
    st.subheader("📂 Categorías")
    categories = ["General", "Comunicación", "Conflicto", "Ansiedad", "Autoestima", "Familia", "Amistad", "Trabajo"]
    for cat in categories:
        if st.button(f"📌 {cat}", key=f"cat_{cat}"):
            st.session_state.current_category = cat

    st.markdown(f"**Categoría actual:** {st.session_state.current_category}")

    # Historial de conversaciones guardadas
    st.subheader("📚 Conversaciones Guardadas")
    if st.session_state.saved_conversations:
        for i, conv in enumerate(st.session_state.saved_conversations):
            col1, col2 = st.columns([3, 1])
            with col1:
                if st.button(f"📄 {conv.get('title', f'Conversación {i+1}')} ({len(conv.get('messages', []))} msgs)", key=f"load_conv_{i}"):
                    st.session_state.chat_history = conv.get('messages', [])
                    st.session_state.current_category = conv.get('category', 'General')
                    st.success(f"✅ Conversación '{conv.get('title', f'Conversación {i+1}')}' cargada")
            with col2:
                if st.button("🗑️", key=f"delete_conv_{i}"):
                    st.session_state.saved_conversations.pop(i)
                    save_conversations_to_file()
                    st.success("🗑️ Conversación eliminada")
                    st.rerun()

    # Historial de la sesión actual
    st.subheader("💬 Sesión Actual")
    if st.session_state.chat_history:
        for i, chat in enumerate(st.session_state.chat_history[-5:]):  # Últimas 5
            if chat['role'] == 'user':
                if st.button(f"💬 {chat['content'][:30]}...", key=f"history_{i}"):
                    st.session_state.selected_chat = chat
                    st.rerun()

    # Estadísticas
    st.subheader("📊 Estadísticas")
    total_consultas = len(st.session_state.chat_history)
    st.metric("Consultas realizadas", total_consultas)

    # Recursos recomendados
    st.subheader("📖 Recursos")
    st.markdown("""
    - [APA - Psicología](https://www.apa.org)
    - [Mayo Clinic](https://www.mayoclinic.org)
    - [Psychology Today](https://www.psychologytoday.com)
    """)

# Header principal
st.markdown("""
<div class="main-header">
    <h1>💙 Mind & Heart AI</h1>
    <p>Tu compañero inteligente en psicología y relaciones de pareja</p>
    <p style="font-size: 0.9em; opacity: 0.9;">Consulta con un experto virtual sobre temas de salud mental y relaciones</p>
</div>
""", unsafe_allow_html=True)

# Categorías rápidas
st.subheader("🏷️ Categorías Populares")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("💬 Comunicación", use_container_width=True):
        st.session_state.current_category = "Comunicación"
with col2:
    if st.button("❤️ Amor", use_container_width=True):
        st.session_state.current_category = "Amor"
with col3:
    if st.button("😰 Ansiedad", use_container_width=True):
        st.session_state.current_category = "Ansiedad"
with col4:
    if st.button("👨‍👩‍👧 Familia", use_container_width=True):
        st.session_state.current_category = "Familia"

# Área de chat principal
st.subheader(f"💭 Consulta - {st.session_state.current_category}")

# Mensaje de bienvenida si es la primera vez
if not st.session_state.welcome_shown and not st.session_state.chat_history:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #e3f2fd 0%, #f3e5f5 100%); padding: 2rem; border-radius: 15px; margin: 1rem 0; border-left: 4px solid #667eea;">
        <h3 style="color: #1976d2; margin-top: 0;">👋 ¡Hola! Bienvenido a Mind & Heart AI</h3>
        <p style="color: #424242; font-size: 1.1em; margin-bottom: 1rem;">
            Soy tu compañero inteligente especializado en psicología y relaciones de pareja.
            Estoy aquí para escucharte, apoyarte y guiarte con consejos profesionales basados en evidencia científica.
        </p>
        <p style="color: #666; font-style: italic;">
            💙 Recuerda: Este es un espacio seguro para expresarte libremente. Todas tus conversaciones son confidenciales.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🚀 Comenzar conversación", type="primary"):
        st.session_state.welcome_shown = True
        st.rerun()

# Mostrar historial de chat
for message in st.session_state.chat_history[-10:]:  # Últimos 10 mensajes
    if message['role'] == 'user':
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>👤 Tú:</strong> {message['content']}
            <br><small style="opacity: 0.7;">{message['timestamp']}</small>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Análisis de sentimiento simple
        sentiment = "neutral"
        if any(word in message['content'].lower() for word in ['feliz', 'bien', 'mejor', 'gracias']):
            sentiment = "positive"
        elif any(word in message['content'].lower() for word in ['triste', 'mal', 'problema', 'dolor']):
            sentiment = "negative"

        st.markdown(f"""
        <div class="chat-message assistant-message">
            <strong>🤖 Mind & Heart:</strong> {message['content']}
            <br><small style="opacity: 0.7;">{message['timestamp']}
            <span class="mood-indicator mood-{sentiment}">Sentimiento: {sentiment.title()}</span></small>
        </div>
        """, unsafe_allow_html=True)

# Input de consulta
query = st.text_area(
    "Describe tu consulta:",
    placeholder=f"Ej: Tengo problemas de {st.session_state.current_category.lower()} con mi pareja...",
    height=100,
    key="query_input"
)

col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    submit_button = st.button("🚀 Obtener Respuesta", type="primary", use_container_width=True)
with col2:
    if st.button("🗑️ Limpiar Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()
with col3:
    if st.button("💾 Guardar Conversación", use_container_width=True):
        if st.session_state.chat_history:
            # Pedir título para la conversación
            title = st.text_input("Título de la conversación:", value=f"Consulta - {st.session_state.current_category}", key="save_title")
            if st.button("✅ Confirmar Guardado", key="confirm_save"):
                conversation_data = {
                    'title': title,
                    'category': st.session_state.current_category,
                    'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'messages': st.session_state.chat_history.copy()
                }
                st.session_state.saved_conversations.append(conversation_data)
                save_conversations_to_file()
                st.success(f"✅ Conversación '{title}' guardada permanentemente")
                st.rerun()
        else:
            st.warning("⚠️ No hay mensajes para guardar")

if submit_button and query.strip():
    # Agregar mensaje del usuario al historial
    user_message = {
        'role': 'user',
        'content': query,
        'timestamp': datetime.now().strftime("%H:%M:%S"),
        'category': st.session_state.current_category
    }
    st.session_state.chat_history.append(user_message)

    with st.spinner("🤔 Procesando tu consulta..."):
        try:
            # Inicializar agente
            agent = MindHeartAgent()

            # Personalizar prompt según categoría
            category_prompts = {
                "Comunicación": "Enfócate en técnicas de comunicación efectiva y resolución de conflictos.",
                "Ansiedad": "Considera aspectos de manejo de ansiedad y estrés en relaciones.",
                "Autoestima": "Trabaja en el desarrollo de la autoestima y confianza personal.",
                "Familia": "Incluye dinámicas familiares y roles en el sistema familiar.",
                "Amistad": "Considera aspectos de relaciones platónicas y sociales.",
                "Trabajo": "Enfócate en balance trabajo-vida personal y relaciones laborales."
            }

            category_instruction = category_prompts.get(st.session_state.current_category, "")

            response = agent.process_query(query, category_instruction)

            # Agregar respuesta al historial
            assistant_message = {
                'role': 'assistant',
                'content': response,
                'timestamp': datetime.now().strftime("%H:%M:%S"),
                'category': st.session_state.current_category
            }
            st.session_state.chat_history.append(assistant_message)

            st.rerun()

        except Exception as e:
            st.error(f"❌ Error al procesar la consulta: {str(e)}")
            st.info("💡 Asegúrate de configurar las API keys correctamente en el archivo .env")

elif submit_button and not query.strip():
    st.warning("⚠️ Por favor, ingresa una consulta válida.")

# Información adicional
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ### 📋 Consejos de Uso
    - Sé específico en tu consulta
    - Incluye contexto sobre la situación
    - Menciona cómo te sientes
    - Pregunta sobre estrategias prácticas
    """)

with col2:
    st.markdown("""
    ### ⚠️ Nota Importante
    Este agente proporciona información general basada en conocimientos psicológicos. **Para situaciones graves o de crisis, consulta con un profesional de la salud mental calificado.**

    *Recuerda: La IA no reemplaza el asesoramiento profesional*
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>💙 Mind & Heart AI - Cuidando tu bienestar emocional</p>
    <p style="font-size: 0.8em;">Desarrollado con ❤️ para ayudar en temas de psicología y relaciones</p>
</div>
""", unsafe_allow_html=True)