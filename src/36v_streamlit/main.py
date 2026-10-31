import sys
from datetime import date
from pathlib import Path

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).parent))

from api_kpis import plot_kpis
from altair_chart import plot_altair_insights


st.set_page_config(page_title="Cibertec-36V", layout="wide", page_icon="📊")

st.markdown(
    """
    <style>
    /* ============= Tab DATA · Catppuccin Latte (light) ============= */
    .st-key-data_chart,
    .st-key-data_altair {
        padding: 0.75rem;
        border-radius: 16px;
        border: 1px solid #ccd0da;                     /* Surface0 */
        background: #eff1f5;                           /* Base     */
        box-shadow: 0 8px 24px rgba(76, 79, 105, 0.12); /* Text    */
        transition: border-color 0.25s ease,
                    box-shadow 0.25s ease,
                    transform 0.25s ease;
    }

    .st-key-data_chart:hover,
    .st-key-data_altair:hover {
        transform: translateY(-3px);
        border-color: #1e66f5;                         /* Blue     */
        box-shadow: 0 14px 34px rgba(30, 102, 245, 0.15),
                    0 8px 24px rgba(76, 79, 105, 0.12);
    }

    .st-key-data_chart [data-testid="stImage"] img {
        display: block;
        width: 100%;
        height: auto;
        border-radius: 10px;
    }

    /* ================== KPI cards · Catppuccin Latte ================== */
    .kpi-card {
        padding: 1rem 1.15rem 1.05rem;
        border-radius: 14px;
        border: 1px solid #ccd0da;                      /* Surface0 */
        background: #eff1f5;                            /* Base     */
        box-shadow: 0 4px 14px rgba(76, 79, 105, 0.08);
        transition: border-color 0.25s ease, box-shadow 0.25s ease;
    }

    .kpi-card:hover {
        border-color: #1e66f5;                          /* Blue */
        box-shadow: 0 8px 22px rgba(30, 102, 245, 0.14);
    }

    .kpi-title {
        display: flex;
        align-items: center;
        gap: 0.4rem;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #6c6f85;                                 /* Subtext0 */
        margin-bottom: 0.35rem;
    }

    .kpi-value {
        font-size: clamp(1.6rem, 2.2vw, 2rem);
        font-weight: 700;
        line-height: 1.1;
        letter-spacing: -0.02em;
        color: #4c4f69;                                 /* Text */
        font-variant-numeric: tabular-nums;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🚀 Basic - class: Streamlit para Data Analytics")

st.divider()

tab_intro, tab_media, tab_info, tab_data, tab_graficos = st.tabs(
    ["📝 Intro", "🖼️ Media", "ℹ️ Info", "DATA", "GRAFICOS"]
)

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
    print(lenguajes)

    btn_generar = st.button("🚀 Generar Resumen", use_container_width=True)

with tab_info:
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
        st.info(
            "👈 Configura todos los parámetros en el Sidebar para ver el resultado."
        )

with tab_data:
    st.header("🧪 Análisis Avanzado")
    uploaded_file = st.file_uploader("Sube tu propio dataset (CSV)", type="csv")

    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.success("¡Dataset listo para análisis!")

        plot_kpis(data)

        st.subheader("📈 Comparativa de Esperanza de Vida")
        paises_disponibles = sorted(data["country"].unique())

        paises_sel = st.multiselect(
            "Selecciona los países a comparar:",
            options=paises_disponibles,
            default=["Mexico", "Spain"],
        )

        if paises_sel:
            fig, ax = plt.subplots(figsize=(10, 5), dpi=150)

            with st.expander("📊 Ver tabla comparativa de selección"):
                df_comp = data[data["country"].isin(paises_sel)]
                st.dataframe(df_comp.sort_values(["year", "country"]), width="stretch")

            paleta = [
                "#1e66f5",  # Blue
                "#40a02b",  # Green
                "#df8e1d",  # Yellow
                "#fe640b",  # Peach
                "#ea76cb",  # Pink
                "#8839ef",  # Mauve
                "#179299",  # Teal
                "#d20f39",  # Red
            ]

            for i, pais in enumerate(paises_sel):
                df_pais = data[data["country"] == pais]
                color = paleta[i % len(paleta)]
                ax.plot(
                    df_pais["year"],
                    df_pais["lifeExp"],
                    color=color,
                    marker="o",
                    markersize=5,
                    markeredgecolor="#eff1f5",
                    markeredgewidth=1.2,
                    linewidth=2.4,
                    label=pais,  # Etiqueta para la leyenda
                )

            ax.set_title(
                "Evolución de la Esperanza de Vida",
                fontsize=15,
                fontweight="bold",
                color="#4c4f69",  # Text
                loc="left",
                pad=18,
            )
            ax.set_xlabel("Año", fontsize=11, color="#6c6f85")  # Subtext0
            ax.set_ylabel("Años de Vida", fontsize=11, color="#6c6f85")

            ax.grid(True, linestyle="--", linewidth=0.7, alpha=0.8, color="#ccd0da")
            ax.set_axisbelow(True)
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["left"].set_color("#ccd0da")
            ax.spines["bottom"].set_color("#ccd0da")
            ax.tick_params(colors="#6c6f85", labelsize=10)  # Subtext0

            leg = ax.legend(
                title="Países",
                frameon=False,
                loc="upper left",
                fontsize=10,
                labelcolor="#4c4f69",
            )
            leg.get_title().set_color("#6c6f85")

            fig.patch.set_facecolor("#eff1f5")
            ax.set_facecolor("#eff1f5")
            fig.tight_layout()

            with st.container(key="data_chart"):
                st.pyplot(fig, clear_figure=True)

        st.divider()
        st.subheader("🌍 Insights por continente")

        if "continent" in data.columns:
            col_a, col_b = st.columns(2)

            with col_a:
                continentes = sorted(data["continent"].dropna().unique())
                continente_sel = st.selectbox("Continente:", continentes)

            with col_b:
                anios = sorted(data["year"].dropna().unique(), reverse=True)
                anio_sel = st.selectbox("Año:", anios)

            df_filtrado = data[
                (data["continent"] == continente_sel) & (data["year"] == anio_sel)
            ]

            with st.container(key="data_altair"):
                plot_altair_insights(df_filtrado, continente_sel)
        else:
            st.warning("El dataset no tiene columna 'continent'.")
