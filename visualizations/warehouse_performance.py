# Warehouse performance charts
import streamlit as st
import plotly.express as px                          # plt → px (wrong alias)
from processing.analytics import get_warehouse_performance


def render_warehouse_performance(df):
    st.subheader("Warehouse Performance")
    warehouse_data = get_warehouse_performance(df)

    metric = st.selectbox(
    "Select Metric",
    ["total_orders", "total_quantity", "avg_delivery_time"]
    )

    fig = px.bar(
    warehouse_data,
    x="warehouse",
    y=metric,
    title="Total Quantity by Warehouse"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(warehouse_data)

