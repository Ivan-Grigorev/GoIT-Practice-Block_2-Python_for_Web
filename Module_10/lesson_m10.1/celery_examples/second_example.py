from celery import Celery
import requests

app = Celery('second_example', broker='pyamqp://guest@localhost//')


@app.task
def check():
    response = requests.get('https://catfact.ninja/fact')
    result = response.json()
    print(result['fact'])


app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'second_example.check',
        'schedule': 5.0,

    },
}
app.conf.timezone = 'UTC'
