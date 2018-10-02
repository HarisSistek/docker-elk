# initialize using environment variables
# or configure to use ELASTIC_APM in your application's settings
import elasticapm
from elasticapm.contrib.flask import ElasticAPM

import time

import redis
from flask import Flask


app = Flask(__name__)
app.config['ELASTIC_APM'] = {
    # Set required service name. Allowed characters:
    # a-z, A-Z, 0-9, -, _, and space
    'SERVICE_NAME': 'PYTHON_FLASK_TEST_APP',

    # Set custom APM Server URL (default: http://localhost:8200)
    'SERVER_URL': 'http://apm-server:8200',

    'DEBUG': True,
}

apm = ElasticAPM(app, logging=True)
cache = redis.Redis(host='redis', port=6379)

@elasticapm.capture_span()
def get_hit_count():
    with elasticapm.capture_span('span-get-redis-hit-count'):
        retries = 5
        while True:
            try:
                return cache.incr('hits')
            except redis.exceptions.ConnectionError as exc:
                if retries == 0:
                    raise exc
                retries -= 1
                time.sleep(0.5)

@elasticapm.capture_span()
def sleep_function1():
    with elasticapm.capture_span('span-sleep-loop'):
        time.sleep(2)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World: Redis count is: {}\n'.format(count)

@app.route('/span')
def span():
    sleep_function1()
    return 'span is done'

@app.route('/crash')
def crash():
    try:
        1 / 0
    except:
        apm.capture_exception()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=11000, debug=True)
