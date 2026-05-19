import csv
import json
from models.air_sample import AirSample

class CsvReader:
    def read(self):
        with open("config.json") as f:
            config = json.load(f)
        
        data = []
        with open(config["input_path"], newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                v = AirSample(
                    row.get("Parameter Code"),
                    row.get("Observation Count"),
                    row.get("1st Max Value"),
                    row.get("Date of Last Change"),
                    row.get("Location 1")
                )
                data.append(v)
        return data