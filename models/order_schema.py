# Defines validation rules for order records
from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class Order(BaseModel):
    order_id:str
    warehouse:str
    region: Optional[str]
    product: str
    order_qty: int
    order_date: str
    delivery_date: str
    delivery_time_days: Optional[float]
    status: str

    @field_validator("order_qty")
    @classmethod
    def validate_order_qty(cls, v):
        if v <= 0:
            raise ValueError("order_qty must be greater than 0")
        return v

    @field_validator("order_date")
    @classmethod
    def validate_order_date(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid Date format: {v}")
        return v

    @field_validator("delivery_date")
    @classmethod
    def validate_delivery_date(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Invalid Date format: {v}")
        return v