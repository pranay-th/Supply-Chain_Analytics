# Product-level heatmaps
import streamlit as st
import plotly.express as px
from processing.analytics import get_product_analysis

def render_product_analysis(df):
    st.subheader("Product Analysis")
    product_data = get_product_analysis(df)

    fig = px.imshow(
        product_data,
        title="Product Demand Heatmap"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(product_data)