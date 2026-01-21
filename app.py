import streamlit as st
import pandas as pd

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="DATA WOLF | Neural B2B", page_icon="🐺", layout="wide")

# CSS MAESTRO: AJUSTE DE VISIBILIDAD Y ENLACE DE VENTAS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300;500&display=swap');

    /* Fondo general con efecto Matrix suave */
    .main {
        background-color: #050505;
        background-image: linear-gradient(rgba(0, 255, 65, 0.03) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(0, 255, 65, 0.03) 1px, transparent 1px);
        background-size: 30px 30px;
    }

    /* BLOQUE CRÍTICO: Fondo para que la información se lea (Recuadro Rojo en tu imagen) */
    .stApp {
        background-color: rgba(10, 10, 10, 0.85); /* Fondo oscuro sólido para legibilidad */
    }

    /* Títulos Neón con mejor contraste */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        color: #00FF41 !important;
        text-shadow: 0 0 12px rgba(0, 255, 65, 0.9);
    }

    /* Texto de información: Cambiado a Blanco Puro para lectura clara */
    .stMarkdown, p, span, li {
        font-family: 'JetBrains Mono', monospace !important;
        color: #FFFFFF !important; /* Blanco para que no se pierda */
        font-weight: 400;
    }

    /* COLUMNA DE OPCIONES (Se mantiene perfecta como pediste) */
    [data-testid="stSidebar"] {
        background-color: #000000;
        border-right: 2px solid #00FF41;
    }

    /* Estilo para el Link de Ventas (Botón Neón) */
    .sales-link {
        display: inline-block;
        padding: 10px 20px;
        color: #00FF41 !important;
        border: 2px solid #00FF41;
        text-decoration: none;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        border-radius: 5px;
        box-shadow: 0 0 10px #00FF41;
        text-align: center;
    }
    .sales-link:hover {
        background-color: #00FF41;
        color: #000000 !important;
        box-shadow: 0 0 25px #00FF41;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (COLUMNA DE OPCIONES - SIN CAMBIOS) ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/00FF41/wolf.png")
    st.markdown("### DATA WOLF PANEL")
    st.markdown(f"**Status:** `ACTIVE_NEURAL_LINK`")
    menu = st.radio("Navegación de Sistemas", ["Centro de Mando", "Manifiesto Wolf", "Free Trial (Leads B2B)", "Contacto Directo"])
    st.markdown("---")
    # Link directo a Ventas por WhatsApp
    st.markdown('<a href="https://wa.me/525562460821" class="sales-link">📞 CONTACTAR VENTAS</a>', unsafe_allow_html=True)

# --- CONTENIDO PRINCIPAL ---

if menu == "Centro de Mando":
    st.title("🐺 DATA WOLF: Inteligencia de Negocios de Verdad")
    st.subheader("Dominio estratégico con alma humana.")
    st.markdown("""
    > **Procesamos el caos con la frialdad del algoritmo para liberar la voluntad del hombre; 
    porque en la era de la IA, el Wolf no solo extrae datos, despierta mercados.**
    """)
    
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🛠️ Automatización\nEliminamos el error humano. Tu empresa corriendo en Python 24/7.")
    with col2:
        st.markdown("### 📊 Scraping Global\nExtracción de datos estratégica. No reportamos, dominamos.")
    with col3:
        st.markdown("### 🎯 Máximo ROI\nLeads filtrados quirúrgicamente para cierres inmediatos.")

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-style: italic; font-size: 0.9em; color: #00FF41;'>\"Y lo he llenado del Espíritu de Dios, en sabiduría y en inteligencia, en ciencia y en todo arte...\" — Éxodo 31:3</p>", unsafe_allow_html=True)

elif menu == "Manifiesto Wolf":
    st.title("🔱 El Manifiesto del Lobo")
    st.markdown("### Misión")
    st.write("Nacimos del fuego y la resistencia. Nuestra misión es redimir el tiempo perdido mediante la automatización de élite en Python e IA, transformando el caos operativo en libertad humana.")
    st.markdown("### Visión")
    st.write("Ser el puente tecnológico global que demuestre que el pasado no define el destino. Aspiramos a digitalizar la eficiencia en cada mercado.")

elif menu == "Free Trial (Leads B2B)":
    st.title("⚡ PRUÉBANOS: SERVICIO SIN COSTO")
    st.info("Solicita una extracción de datos global. Tiempo de respuesta: 1 hora.")
    
    with st.form("leads_gratis"):
        rubro = st.text_input("Tu Rubro Operativo")
        rubro_deseado = st.text_input("Rubro Deseado (Target)")
        zona = st.text_input("Zona Geográfica")
        nombre = st.text_input("Nombre")
        whatsapp = st.text_input("WhatsApp")
        
        if st.form_submit_button("INICIAR EXTRACCIÓN"):
            st.success("SOLICITUD RECIBIDA. El documento con candado se enviará a la brevedad.")

elif menu == "Contacto Directo":
    st.title("🤝 Alianzas de Alto Nivel")
    st.markdown("---")
    st.write("📧 **Correo Seguro:** datawolf_solutions@proton.me")
    st.markdown('<br><a href="https://wa.me/525562460821" class="sales-link">📱 ENVIAR WHATSAPP A VENTAS</a>', unsafe_allow_html=True)
