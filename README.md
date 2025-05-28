# Order Management API

This is a simple backend application built with **FastAPI** and **SQLAlchemy** to manage product orders. It provides RESTful endpoints to create, read, update, and delete orders.

## Features

- Create new product orders
- Retrieve one or all orders
- Update existing orders
- Delete orders
- SQLite for development and PostgreSQL ready
- Fully tested with `pytest` and `httpx`

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy (async)
- PostgreSQL / SQLite
- Pytest
- httpx

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd order_system

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Running the Application

```bash
# Start the FastAPI server
uvicorn app.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

Swagger UI documentation: `http://127.0.0.1:8000/docs`

## Running Tests

```bash
# Run all tests
PYTHONPATH=./ ./run_tests.sh
```

You should see output similar to:

```
tests/test_orders.py .... [100%]
4 passed in 0.45s
```

## Project Structure

```
order_system/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── db_base
│   ├── logger
│   ├── task
│   ├── cekery_worker
│   ├── routes/
│   │   └── orders.py
│   └── database.py
├── tests/
│   └── test_orders.py
├── run_tests.sh
└── requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🚀 Getting Started with Docker

To run the application and the background worker using Docker and Docker Compose:

### 1. Build and start services

```bash
docker-compose up --build
```

This will start:
- The **FastAPI** application (served via Uvicorn)
- A **Redis** server (used as the broker for Celery)
- A **Celery** worker for background task processing

### 2. Access the API

Once the services are up, the API will be accessible at:

```
http://localhost:8000
```

And the automatically generated documentation will be available at:

```
http://localhost:8000/docs
```

### 3. Run tests (optional)

To run the test suite locally (not via Docker):

```bash
PYTHONPATH=./ ./run_tests.sh
```

Make sure to install development dependencies if you're running tests outside of Docker.
