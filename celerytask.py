from celery import Celery

app = Celery("celerytask", broker="amqp://guest@localhost//", backend="rpc")


@app.task(name="sum-of-two-numbers")
def add(x, y):
    return x + y


#  celery -A celerytask worker --pool=solo -l info
