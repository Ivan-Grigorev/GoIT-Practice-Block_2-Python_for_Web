from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y

# celery -A first_example worker --loglevel=INFO
# docker run -d -p 5672:5672 rabbitmq
