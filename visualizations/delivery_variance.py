# Delivery time variance histograms
import streamlit as st
import plotly.express as px
from processing.analytics import get_delivery_variance

def render_delivery_variance(df):
    st.subheader("Delivery Variance")
    get_delivery_variance(df)  # still available if needed elsewhere

    bins = st.slider("Number of bins", min_value=5, max_value=50, value=20)

    fig = px.histogram(
        df,                          # pass full df so histogram has the column, not a Series
        x='delivery_time_days',
        nbins=bins,
        title='Distribution of Delivery time'
    )
    st.plotly_chart(fig, use_container_width=True)  # was missing
