# 📦 Order Management API

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Test Workflow](https://github.com/ThisIsAntonio/fastapi-order-system/actions/workflows/test.yml/badge.svg)]


A lightweight backend application built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL** for managing product orders with full support for async I/O, Docker, and background processing via Celery and Redis.

---

## ✨ Features

- 📥 Create new product orders
- 📋 Retrieve individual or all orders
- ✏️ Update existing orders
- ❌ Delete orders
- 🔁 Asynchronous processing using Celery + Redis
- 🧪 Full test coverage with `pytest` and `httpx`
- 🐳 Docker and Docker Compose support

---

## 🛠️ Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy (Async)
- PostgreSQL (Production) / SQLite (Testing)
- Redis & Celery (Background Tasks)
- Pytest & HTTPX
- Docker & Docker Compose

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ThisIsAntonio/fastapi-order-system
cd fastapi-order-system
```

### 2. Create a Virtual Environment

#### 🔷 Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 🔶 Windows

```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Environment Configuration

This project uses a `.env` file to store environment variables such as the database URL.

Create a `.env` file in the root directory with the following structure:

```env
DATABASE_URL=postgresql+asyncpg://<username>:<password>@<host>:<port>/<database>
```

Example:

```env
DATABASE_URL=postgresql+asyncpg://postgres:mysecret@localhost:5432/orders_db
```

Make sure this file is **not committed** to version control.

---

## 💡 Running the App Locally

```bash
uvicorn app.main:app --reload
```

Visit the API docs:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Running Tests

### 🐧 Linux / macOS

```bash
PYTHONPATH=./ ./run_tests.sh
```

### 🪟 Windows

```cmd
set PYTHONPATH=.
pytest tests/
```

---

## 🐳 Docker Setup

### 1. Start All Services

```bash
docker-compose up --build
```

This launches:

- `redis`: Task broker
- `celery_worker`: Background job processor
- `FastAPI` app via Uvicorn (modify Dockerfile as needed)

### 2. Access the API

- [http://localhost:8000](http://localhost:8000)
- [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 Project Structure

```
fastapi-order-system/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes/
│   │   └── orders.py
│   ├── database.py
│   ├── celery_worker.py
│   └── tasks/
├── tests/
│   └── test_orders.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run_tests.sh
└── README.md
```

---

## 👨‍💻 Author

**Marcos Astudillo**  
[![🌍 Portfolio](https://img.shields.io/badge/Website-marcosastudillo.com-blueviolet?style=for-the-badge&logo=google-chrome)](https://www.marcosastudillo.com)
[![💼 LinkedIn](https://img.shields.io/badge/LinkedIn-Marcos%20Astudillo-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/marcos-antonio-astudillo-carrasco)
[![🐱 GitHub](https://img.shields.io/badge/GitHub-ThisIsAntonio-181717?style=for-the-badge&logo=github)](https://github.com/ThisIsAntonio)


---

## 📄 License

This project is licensed under the [`MIT LICENSE`](LICENSE) © 2025 Marcos Astudillo