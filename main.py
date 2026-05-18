from utils.csv_generator import generate_csv
from di import Container
from presentation.cli import CLI


if __name__ == "__main__":
    generate_csv("flights.csv", 1000)

    container = Container()
    service = container.flight_service()

    app = CLI(service)
    app.run()