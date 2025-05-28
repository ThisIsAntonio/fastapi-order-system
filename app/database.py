# app/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from app import models
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from app.db_base import Base
from app import models, schemas

DATABASE_URL = "postgresql+asyncpg://postgres:KHWmnSnQZMuqihZMfuxKiZwmdMhgxaFu@metro.proxy.rlwy.net:12098/railway"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def create_order(order: schemas.OrderCreate):
    async with SessionLocal() as session:
        async with session.begin():
            new_order = models.Order(
                product_name=order.product_name,
                quantity=order.quantity,
                status="pending"
            )
            session.add(new_order)
        await session.commit()
        await session.refresh(new_order)
        return new_order


async def get_orders():
    async with SessionLocal() as session:
        result = await session.execute(
            select(models.Order).order_by(models.Order.id)
        )
        return result.scalars().all()
