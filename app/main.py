
from fastapi import FastAPI
from app import database
from app.logger import logger
from app.routes import orders
from contextlib import asynccontextmanager

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.init_db()
    yield
    
app = FastAPI(lifespan=lifespan)


app.include_router(orders.router)
