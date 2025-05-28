# app/celery_worker.py

from celery import Celery

celery_app = Celery(
    "order_tasks",
    broker="redis://localhost:6379/0",
)

celery_app.conf.task_routes = {
    "app.tasks.process_order": {"queue": "orders"}
}
