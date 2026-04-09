# Core analytics functions (group-by, aggregations, metrics)
import pandas as pd

def get_status_distribution(df):
    status_counts = df['status'].value_counts()
    status_counts = status_counts.reset_index()
    return status_counts

def get_warehouse_performance(df):
    result = df.groupby['warehouse'].agg(
        total_orders=("order_id", "count"),
        total_quantity=("order_qty","sum"),
        avg_delivery_time=("delivery_time_days", "mean")
    )
    return result.reset_index()

def regional_demand(df):
    result = df["order_month"] = df["order_date"].dt.to_period("M")

    return result

def get_delivery_variance(df):
    result = df['delivery_time_days'].describe()

    return result

def add_delay_flag(df, threshold_days=7):
    df = df.copy()
    df['is_delayed'] = (
        (df['status'] == 'Delayed') |
        ((df['status'] == 'Pending') & (df['delivery_time_days'] > threshold_days))
    )
    return df

def get_delay_tracking(df):
    df = add_delay_flag(df)
    return df[df['is_delayed']]

def get_product_analysis(df):
    result=pd.pivot_table(df,
    index="product",
    columns="warehouse",
    values="order_qty",
    aggfunc="sum"
)
    return result