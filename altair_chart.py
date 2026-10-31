import altair as alt
import streamlit as st


def plot_altair_insights(df_filtered, region_name):
    df_plot = df_filtered.copy()
    df_plot["pop_explife"] = df_plot["pop"] / df_plot["lifeExp"].replace(0, 1)

    # Size = Area
    chart = (
        alt.Chart(df_plot)
        .mark_circle(opacity=0.7, stroke="white", strokeWidth=1)
        .encode(
            x=alt.X(
                "pop:Q", title="Total Population", axis=alt.Axis(format="~s")
            ),  # Readable numbers like 1M, 10M
            y=alt.Y(
                "lifeExp:Q",
                title="Expectativa de vida",
                scale=alt.Scale(zero=False),
            ),
            size=alt.Size(
                "lifeExp:Q", title="Land Area", scale=alt.Scale(range=[100, 3000])
            ),
            color=alt.Color(
                "pop_explife:Q", scale=alt.Scale(scheme="magma"), title="pop explife"
            ),
            tooltip=[
                alt.Tooltip("country", title="Country"),
                alt.Tooltip("pop", title="Population", format=","),
                alt.Tooltip("lifeExp", title="Area (km²)", format=","),
                alt.Tooltip("pop_explife", title="pop explife", format=".2f"),
            ],
        )
        .properties(
            width="container",
            height=500,
            title=f"Insight: Population vs. Density in {region_name} (Linear Scale)",
        )
        .interactive()
    )

    st.altair_chart(chart, width="stretch")
