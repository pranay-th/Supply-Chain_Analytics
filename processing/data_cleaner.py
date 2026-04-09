# Handle missing values, duplicates, type conversions
import pandas as pd
from models.order_schema import Order

def validate_rows(df):
    valid_rows=[]
    invalid_rows=[]

    for record in df.to_dict(orient="records"):
        try:
            validated=Order(**record)
            valid_rows.append(validated.model_dump())
        except Exception:
            invalid_rows.append(record)

    valid_df=pd.DataFrame(valid_rows)    # dedented out of the for loop
    invalid_df=pd.DataFrame(invalid_rows)

    return valid_df,invalid_df
    
def remove_duplicates(df):
    df=df.drop_duplicates(subset=['order_id'])
    return df

def normalize_missing_values(df):
    # fill string/object columns with "Unknown", numeric columns with 0
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(0)

    return df

def convert_date_columns(df):
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["delivery_date"] = pd.to_datetime(df["delivery_date"], errors="coerce")  # to_date_time → to_datetime

    return df

def convert_numeric_columns(df):
    df["order_qty"] = pd.to_numeric(df["order_qty"], errors='coerce')
    df["delivery_time_days"] = pd.to_numeric(df["delivery_time_days"], errors='coerce')  # delivery_time_day → delivery_time_days

    return df

def clean_orders(df):
    valid_df, invalid_df = validate_rows(df)
    df = valid_df
    df = remove_duplicates(df)
    df = normalize_missing_values(df)
    df = convert_date_columns(df)
    df = convert_numeric_columns(df)
    return df, invalid_df
