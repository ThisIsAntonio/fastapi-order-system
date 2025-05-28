# app/crud.py

from sqlalchemy.future import select
from app.models import Order
from app.database import SessionLocal


async def create_order(order_data):
    async with SessionLocal() as session:
        new_order = Order(**order_data.dict())
        session.add(new_order)
        await session.commit()
        await session.refresh(new_order)
        return new_order


async def get_order(order_id: int):
    async with SessionLocal() as session:
        result = await session.execute(select(Order).where(Order.id == order_id))
        return result.scalar_one_or_none()


async def update_order_status(order_id: int, new_status: str):
    async with SessionLocal() as session:
        result = await session.execute(select(Order).where(Order.id == order_id))
        order = result.scalar_one_or_none()
        if order:
            order.status = new_status
            await session.commit()
