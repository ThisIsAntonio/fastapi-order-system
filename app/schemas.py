# app/schemas.py

from pydantic import BaseModel


class OrderCreate(BaseModel):
    product_name: str
    quantity: int


class OrderResponse(OrderCreate):
    id: int
    status: str

    class Config:
        orm_mode = True
        from_attributes = True
