import streamlit as st
import plotly.express as px
from processing.analytics import get_status_distribution

def render_status_dashboard(df):
    st.subheader("Order Status Distribution")
    status_data=get_status_distribution(df)

    fig1 = px.bar(
        status_data,
        x="status",
        y="count",
        title="Order Status Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(status_data)

    fig2 = px.pie(
    status_data,
    names="status",
    values="count",
    title="Order Status Distribution"
    )
    st.plotly_char(fig, use_container_width=True)
    
