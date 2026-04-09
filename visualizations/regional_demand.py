# Regional demand trends
import streamlit as st
import plotly.express as plt
from processing.analytics import regional_demand

def render_regional_demand(df):
    st.subheader("Regional demand")
    regional_data = get_regional_demand(df)

    fig = px.bar(
        regional_data,
        x='region',
        y='total_quantity',
        title='Demand by Region'
    )

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(regional_data)
    