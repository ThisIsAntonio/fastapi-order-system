from fastapi import APIRouter, HTTPException
from app import schemas, database, crud
from app.logger import logger
from app import tasks

router = APIRouter()


@router.post("/orders", response_model=schemas.OrderResponse)
async def create_order(order: schemas.OrderCreate):
    if order.quantity <= 0:
        logger.warning("Attempted to create order with non-positive quantity")
        raise HTTPException(
            status_code=400, detail="Quantity must be greater than zero")

    try:
        db_order = await database.create_order(order)
        logger.info(
            f"Order created: {db_order.product_name} x{db_order.quantity}")
        tasks.process_order.delay(db_order.id)  # Sent to Celery task queue

        return db_order
    except Exception as e:
        logger.error(f"Failed to create order: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/orders", response_model=list[schemas.OrderResponse])
async def get_orders():
    return await database.get_orders()


@router.get("/orders/{order_id}", response_model=schemas.OrderResponse)
async def get_order(order_id: int):
    order = await crud.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}
