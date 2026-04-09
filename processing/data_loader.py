# Load CSV/JSON into Pandas DataFrame
import pandas as pd
from config.settings import RAW_DATA_FILE

def load_orders():
    data=pd.read_csv(RAW_DATA_FILE)

    return data

def summarize_data(data):
    info=data.info()
    analytic=data.describe(include='all')

    print(info)
    print(analytic)
    
    return 
