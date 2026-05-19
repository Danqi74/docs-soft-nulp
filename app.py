from flask import Flask

from database import Base
from database import engine

from controllers.flight_controller import flight_bp

from services.flight_service import FlightService

from database import session

app = Flask(__name__)

Base.metadata.create_all(engine)

app.register_blueprint(flight_bp)

service = FlightService(session)

service.import_from_csv("flights.csv")

if __name__ == "__main__":

    app.run(debug=True)