# app/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from app.db_base import Base
from app import models, schemas
import os

DATABASE_URL = "postgresql+asyncpg://postgres:KHWmnSnQZMuqihZMfuxKiZwmdMhgxaFu@metro.proxy.rlwy.net:12098/railway"

SessionLocal = None  # Será inicializado más adelante

def init_session(engine):
    global SessionLocal
    SessionLocal = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )


if os.getenv("TESTING") != "1":
    # Evita errores si TESTING está seteado antes de este import
    from app.database import DATABASE_URL
    engine = create_async_engine(DATABASE_URL, echo=True)
    init_session(engine)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def create_order(order: schemas.OrderCreate):
    async with SessionLocal() as session:
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


async def update_order(order_id: int, order_update: schemas.OrderCreate):
    async with SessionLocal() as session:
        result = await session.execute(select(models.Order).where(models.Order.id == order_id))
        db_order = result.scalar_one_or_none()
        if not db_order:
            return None

        db_order.product_name = order_update.product_name
        db_order.quantity = order_update.quantity
        await session.commit()
        await session.refresh(db_order)
        return db_order


async def delete_order(order_id: int):
    async with SessionLocal() as session:
        result = await session.execute(select(models.Order).where(models.Order.id == order_id))
        db_order = result.scalar_one_or_none()
        if not db_order:
            return False

        await session.delete(db_order)
        await session.commit()
        return True


def get_test_sessionmaker(database_url: str):
    engine = create_async_engine(database_url, echo=True)
    TestingSessionLocal = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )
    return TestingSessionLocal, engine
