from celery import Celery
import httpx
import redis

app = Celery('second_example', broker='pyamqp://guest@localhost//')

index = 1


@app.task
def go_to_url():
    global index
    with httpx.Client() as web_client:
        url = 'https://www.boredapi.com/api/activity'
        response = web_client.get(url)
        result = response.json()['activity']
        with redis.Redis(host='localhost', port=6380, db=0) as redis_client:
            redis_client.set(index, result)
    index += 1


@app.task
def get_from_storage():
    with redis.Redis(host='localhost', port=6380, db=0) as redis_client:
        result = redis_client.get(index)
        print(result)



app.conf.beat_schedule = {
    'add-every-2-seconds': {
        'task': 'third_example.go_to_url',
        'schedule': 5,

    },
    'check-every-5-second': {
        'task': 'third_example.get_from_storage',
        'schedule': 5,


    }
}

app.conf.timezone = 'UTC'
