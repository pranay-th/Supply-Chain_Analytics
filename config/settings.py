# File paths, constants, Streamlit settings
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent
DATA_DIR=BASE_DIR / "data"
RAW_DATA_FILE=DATA_DIR / "aws_supply_chain_orders_raw.csv"