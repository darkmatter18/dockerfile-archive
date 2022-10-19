import time
import redis 
from flask import Flask

app = Flask(__name__)
cache = redis.Redis('host', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as e:
            if retries == 0:
                raise e
            retrues -= 1
            time.sleep(0.5)

@app.route('/')
def hola():
    count = get_hit_count()
    return f"I have been visited {count} times."