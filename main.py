from datetime import date

import pandas as pd
import streamlit as st


st.set_page_config(page_title="Cibertec-36V", layout="wide", page_icon="📊")

st.markdown(
    """
    <style>
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🚀 Basic - class: Streamlit para Data Analytics")

st.divider()

tab_intro, tab_media = st.tabs(["📝 Intro", "🖼️ Media"])

with tab_intro:
    col_t1, col_t2 = st.columns([2, 1])
    with col_t1:
        st.header("Componentes de Texto")
        st.write(
            "Streamlit permite usar Markdown, lo que facilita crear reportes dinámicos."
        )
        st.code(
            """
# Función para normalizar nombres de columnas
def clean_data(df):
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    return df.dropna()

df_clean = clean_data(raw_data)
""",
            language="python",
            line_numbers=True,
        )
        st.json({"proyecto": "Streamlit Lab", "estado": "Activo", "version": 1.0})
        st.success("✅ **Éxito:** El dataset se cargó correctamente.")
        st.info("ℹ️ **Información:** Este gráfico muestra la tendencia anual.")
        st.warning("⚠️ **Advertencia:** Faltan valores nulos en la columna 'Edad'.")
        st.error("🚨 **Error:** No se pudo conectar a la base de datos.")

    with col_t2:
        st.subheader("Metricas")
        st.metric(label="Versión", value="1.2", delta="Estable")
        st.metric(label="Registros Activos", value="1,250", delta="+12% vs ayer")
        st.metric(
            label="Tiempo de Carga", value="0.8s", delta="-0.2s", delta_color="inverse"
        )

with tab_media:
    st.subheader("Recursos Externos")
    with st.expander(
        "🎵 Reproducir Audio de Muestra (Análisis de Señal)", expanded=True
    ):
        st.audio(
            "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
            format="audio/mp3",
        )
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.image(
            "https://images.unsplash.com/photo-1518770660439-4636190af475",
            caption="Hardware Analysis",
            use_container_width=True,
        )
    with c2:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

with st.sidebar:
    st.header("⌨️ Configuración")
    user_name = st.text_input(label="Analista:", placeholder="Nombre")
    edad = st.number_input(label="Edad", min_value=18, max_value=100, value=18)
    nivel_py = st.select_slider(
        "Nivel Python", ["Novato", "Intermedio", "Avanzado", "Ninja"], value="Avanzado"
    )
    lenguajes = st.multiselect(
        "Lenguajes que dominas:",
        ["Python", "R", "SQL", "Julia", "Scala", "C++", "Rust", "Go"],
        default=["Python"],  # Opción preseleccionada
    )
    nivel = st.select_slider(
        "Nivel Técnico",
        ["Universidad", "Maestria", "Doctorado", "Ninja"],
        value="Universidad",
    )
    civil_state = st.selectbox(
        "Estado Civil:", options=["Casado", "Divorciado", "Soltero"]
    )
    color_fav = st.radio("Color Favorito", ["Rojo", "Verde", "Azul"], horizontal=True)
    fecha_analisis = st.date_input("Fecha del Análisis", date.today())
    notas = st.text_area(
        "Notas Adicionales", placeholder="Escribe observaciones aquí..."
    )
    acepto = st.checkbox("Certificar información", value=True)

    btn_generar = st.button("🚀 Generar Resumen", use_container_width=True)

st.header("🕹️ Centro de Control de Usuario")
if btn_generar:
    if not user_name:
        st.error("⚠️ Debes ingresar un nombre en el panel lateral.")
    else:
        st.balloons()

        with st.expander("📄 EXPEDIENTE DEL ANALISTA", expanded=True):
            st.markdown(f"### ANALISTA: {user_name.upper()}")

            # Fila 1: Datos Técnicos
            c1, c2, c3 = st.columns(3)
            c3.write(f"**Edad:** {edad} años")
            c2.write(f"**Stack:** {lenguajes}")
            c1.write(f"**Nivel:** {nivel}")

            # Fila 2: Fechas y Archivos
            d1, d2, d3 = st.columns(3)
            d1.write(f"**Fecha:** {fecha_analisis.strftime('%d/%m/%Y')}")
            d2.write(f"**Estado Civil:** {civil_state}")
            d3.write(f"**Color Elegido:** {color_fav}")

            st.divider()

            if notas:
                st.markdown("**Observaciones:**")
                st.info(notas)

            st.success("Informe generado y certificado exitosamente.")

else:
    st.info("👈 Configura todos los parámetros en el Sidebar para ver el resultado.")
