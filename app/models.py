# app/models.py

from sqlalchemy import Column, Integer, String
from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    quantity = Column(Integer)
    status = Column(String, default="pending")
