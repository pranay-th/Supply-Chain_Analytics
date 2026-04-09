# Delivery time variance histograms
import streamlit as st
import plotly.express as px
from processing.analytics import get_delivery_variance

def render_delivery_variance(df):
    st.subheader("Delivery Variance")
    delivery_date_data = get_delivery_variance(df)

    bins = st.slider("Number of bins", min_value=5, max_value=50, value=20)

    fig = px.histogram(
        delivery_date_data,
        x='delivery_time_days',
        nbins=bins,
        title='Distribution of Delivery time'
    )