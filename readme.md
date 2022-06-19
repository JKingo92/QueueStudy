## How to Run
First initialize RabbitMQ server using docker:

```docker run --rm -p 5672:5672 -p 8080:15672 rabbitmq:3-management```

You can look at the RMQ dashboard on http://localhost:8080/ using guest:guest

After it, you have to set up celery consumer(worker) using:


```celery -A celerytask worker --pool=solo -l info```

Then, runing 

```python task.py```

You can get your result using Celery/RMQ architecture in your localhost