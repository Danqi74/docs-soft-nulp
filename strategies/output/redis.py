from strategies.output.strategy import OutputStrategy
import redis
import json

class RedisOutput(OutputStrategy):
    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379, db=0)

    def output(self, data):
        for i, item in enumerate(data):
            key = f"air_samples:{i}"
            self.client.set(key, json.dumps(item.__dict__))