import json
from strategies.output.console import ConsoleOutput
from strategies.output.file import FileOutput
from strategies.output.kafka import KafkaOutput
from strategies.output.redis import RedisOutput

def get_strategy():
    with open("config.json") as f:
        config = json.load(f)

    output_type = config["output"]

    if output_type == "console":
        return ConsoleOutput()
    elif output_type == "file":
        return FileOutput()
    elif output_type == "kafka":
        return KafkaOutput()
    elif output_type == "redis":
        return RedisOutput()
    else:
        raise ValueError("Unknown output type")