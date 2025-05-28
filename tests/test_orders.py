import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_create_and_get_order():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        # Crear orden
        response = await client.post("/orders", json={"product_name": "Teclado", "quantity": 5})
        assert response.status_code == 200
        data = response.json()
        assert data["product_name"] == "Teclado"
        assert data["status"] == "pending"
        order_id = data["id"]

        # Obtener orden
        response = await client.get(f"/orders/{order_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == order_id
        assert data["quantity"] == 5
