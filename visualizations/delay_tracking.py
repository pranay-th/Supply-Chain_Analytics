# On-time vs delayed scatter plots
import streamlit as st
import plotly.express as px
from processing.analytics import get_delay_tracking

def render_delay_tracking(df):
    st.subheader("Delay Tracking")
    delay_data = get_delay_tracking(df)

    fig = px.scatter(
        delay_data,
        x='order_date',
        y='delivery_time_days',      # delivery_time_date → delivery_time_days (correct column name)
        color='status',              # colour → color (plotly uses American spelling)
        title='Ontime vs Delayed orders'
    )

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(delay_data)