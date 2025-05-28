# app/tasks.py

import asyncio
from app.celery_worker import celery_app
from app import crud


@celery_app.task
def process_order(order_id: int):
    print(f"⏳ Processing order {order_id}")
    asyncio.run(simulate_processing(order_id))


async def simulate_processing(order_id: int):
    import time
    time.sleep(5)  # Simulación de trabajo pesado
    await crud.update_order_status(order_id, "completed")
    print(f"✅ Order {order_id} completed")
