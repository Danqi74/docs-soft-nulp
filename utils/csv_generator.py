import csv
import random


def generate_csv(path="flights.csv", rows=1000):
    airlines = ["WizzAir", "Ryanair", "Lufthansa", "UIA"]
    airports = ["LWO", "KBP", "FRA", "WAW", "BER"]

    with open(path, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "airline", "flight_number",
            "from_airport", "to_airport",
            "price", "duration"
        ])

        for i in range(rows):
            writer.writerow([
                random.choice(airlines),
                f"FL{i}",
                random.choice(airports),
                random.choice(airports),
                round(random.uniform(50, 500), 2),
                random.randint(60, 300)
            ])

if __name__ == "__main__":
    generate_csv()