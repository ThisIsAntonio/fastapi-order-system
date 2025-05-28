# app/schemas.py

from pydantic import BaseModel, ConfigDict
from typing import Optional

class OrderCreate(BaseModel):
    product_name: str
    quantity: int


class OrderResponse(OrderCreate):
    id: int
    status: str

    model_config = ConfigDict(from_attributes=True)
