from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_and_get_order():
    # Crear orden
    response = client.post(
        "/orders", json={"product_name": "Teclado", "quantity": 5})
    assert response.status_code == 200
    data = response.json()
    assert data["product_name"] == "Teclado"
    assert data["status"] == "pending"
    order_id = data["id"]

    # Obtener orden
    response = client.get(f"/orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == order_id
    assert data["quantity"] == 5
