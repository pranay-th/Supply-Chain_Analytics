# Streamlit entry point for dashboards
import streamlit as st

from config.settings import APP_TITLE, RAW_DATA_FILE
from processing.data_loader import load_orders
from processing.data_cleaner import clean_orders
from visualizations.status_dashboard import render_status_dashboard
from visualizations.warehouse_performance import render_warehouse_performance
from visualizations.regional_demand import render_regional_demand
from visualizations.delivery_variance import render_delivery_variance
from visualizations.delay_tracking import render_delay_tracking
from visualizations.product_analysis import render_product_analysis


def main():
    st.set_page_config(page_title=APP_TITLE, layout="wide")
    st.title(APP_TITLE)

    df = load_orders()       # load_orders takes no args — RAW_DATA_FILE is used internally
    cleaned_df = clean_orders(df)

    if isinstance(cleaned_df, tuple):
        cleaned_df, invalid_df = cleaned_df
    else:
        invalid_df = None

    page = st.sidebar.selectbox(
        "Choose Dashboard",
        [
            "Status Distribution",
            "Warehouse Performance",
            "Regional Demand",
            "Delivery Variance",
            "Delay Tracking",
            "Product Analysis",
        ],
    )

    if invalid_df is not None and not invalid_df.empty:
        with st.expander("Invalid Rows"):
            st.dataframe(invalid_df)

    if page == "Status Distribution":
        render_status_dashboard(cleaned_df)
    elif page == "Warehouse Performance":
        render_warehouse_performance(cleaned_df)
    elif page == "Regional Demand":
        render_regional_demand(cleaned_df)
    elif page == "Delivery Variance":
        render_delivery_variance(cleaned_df)
    elif page == "Delay Tracking":
        render_delay_tracking(cleaned_df)
    elif page == "Product Analysis":
        render_product_analysis(cleaned_df)


if __name__ == "__main__":
    main()