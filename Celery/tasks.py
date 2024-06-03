from celery import Celery

# Create a new Celery instance and configure it
celery_app = Celery('tasks', broker='pyamqp://guest:guest@localhost:5672', backend='rpc://')

# Define a simple task
@celery_app.task
def add(x, y):
    result = x + y
    print(result)
