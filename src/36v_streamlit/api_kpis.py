import streamlit as st


def kpi(title, icon, value):
    st.markdown(
        f"""
    <div class="kpi-card">
        <div class="kpi-title">{icon} {title}</div>
        <div class="kpi-value">{value:,}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def plot_kpis(df):
    total_countries = len(df)
    total_population = df["pop"].sum()
    avg_population = int(df["pop"].mean())
    largest_gpd = df["gdpPercap"].max()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        kpi("Total Countries", "🌍", total_countries)

    with c2:
        kpi("Total Population", "👥", total_population)

    with c3:
        kpi("Avg Population", "📊", avg_population)

    with c4:
        kpi("Largest GPD", "🌐", largest_gpd)
