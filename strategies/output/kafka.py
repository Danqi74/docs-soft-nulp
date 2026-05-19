from strategies.output.strategy import OutputStrategy
from kafka import KafkaProducer
import json

class KafkaOutput(OutputStrategy):
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = "air_samples"

    def output(self, data):
        for item in data:
            self.producer.send(self.topic, item.__dict__)
        self.producer.flush()