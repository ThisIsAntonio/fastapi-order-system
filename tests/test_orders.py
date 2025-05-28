import pytest
import os, tempfile
os.environ["TESTING"] = "1"
db_fd, db_path = tempfile.mkstemp()
TEST_DATABASE_URL = f"sqlite+aiosqlite:///{db_path}"

from httpx import AsyncClient
from httpx import ASGITransport
from app.database import get_test_sessionmaker
from app import database

SessionLocal, engine = get_test_sessionmaker(TEST_DATABASE_URL)
database.SessionLocal = SessionLocal
from app.main import app

from unittest.mock import patch


@pytest.fixture(autouse=True)
async def setup_test_db():
    SessionLocal, engine = get_test_sessionmaker(TEST_DATABASE_URL)
    database.SessionLocal = SessionLocal  # override global session in app

    async with engine.begin() as conn:
        await conn.run_sync(database.Base.metadata.drop_all)
        await conn.run_sync(database.Base.metadata.create_all)
    yield
    await engine.dispose()


@pytest.mark.asyncio
async def test_create_and_get_order():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Create order
        response = await client.post("/orders", json={"product_name": "Teclado", "quantity": 5})
        assert response.status_code == 200
        data = response.json()
        assert data["product_name"] == "Teclado"
        assert data["status"] == "pending"
        order_id = data["id"]

        # Get orden
        response = await client.get(f"/orders/{order_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == order_id
        assert data["quantity"] == 5


@pytest.mark.asyncio
async def test_update_order():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Create order to update
        response = await client.post("/orders", json={"product_name": "Mouse", "quantity": 2})
        assert response.status_code == 200
        order_id = response.json()["id"]

        # Update orden
        update_data = {"product_name": "Mouse Gamer", "quantity": 10}
        response = await client.put(f"/orders/{order_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["product_name"] == "Mouse Gamer"
        assert data["quantity"] == 10


@pytest.mark.asyncio
async def test_delete_order():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Create order to delete
        response = await client.post("/orders", json={"product_name": "Monitor", "quantity": 1})
        assert response.status_code == 200
        order_id = response.json()["id"]

        # Delete order
        response = await client.delete(f"/orders/{order_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "Order deleted successfully"

        # Check that the order no longer exists
        response = await client.get(f"/orders/{order_id}")
        assert response.status_code == 404
        

@pytest.mark.asyncio
async def test_get_all_orders():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Create multiple orders
        await client.post("/orders", json={"product_name": "Laptop", "quantity": 2})
        await client.post("/orders", json={"product_name": "Tablet", "quantity": 1})

        # Get all orders
        response = await client.get("/orders")
        assert response.status_code == 200
        data = response.json()

        assert isinstance(data, list)
        assert len(data) >= 2
        assert any(order["product_name"] == "Laptop" for order in data)
        assert any(order["product_name"] == "Tablet" for order in data)

# Clean up the temporary database file after all tests
@pytest.fixture(scope="session", autouse=True)
def cleanup_temp_db():
    yield
    os.close(db_fd)
    os.unlink(db_path)
