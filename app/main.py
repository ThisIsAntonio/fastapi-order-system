from fastapi import FastAPI, HTTPException
from app import schemas, crud, database
import asyncio

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.init_db()


@app.post("/orders", response_model=schemas.OrderResponse)
async def create_order(order: schemas.OrderCreate):
    db_order = await crud.create_order(order)
    return db_order


@app.get("/orders/{order_id}", response_model=schemas.OrderResponse)
async def get_order(order_id: int):
    order = await crud.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}
