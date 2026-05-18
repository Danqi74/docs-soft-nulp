from sqlalchemy.orm import Session
from models import Airline, Airport, Flight
from entities import FlightDTO
from typing import List
import csv
from .interfaces import IFlightRepository


class FlightRepository(IFlightRepository):

    def __init__(self, session: Session):
        self.session = session

    def load_from_csv(self, path: str) -> List[FlightDTO]:
        result = []
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                result.append(
                    FlightDTO(
                        airline=row["airline"],
                        flight_number=row["flight_number"],
                        from_airport=row["from_airport"],
                        to_airport=row["to_airport"],
                        price=float(row["price"]),
                        duration=int(row["duration"])
                    )
                )
        return result

    def save_flights(self, flights: List[FlightDTO]):

        for f in flights:

            airline = (
                self.session.query(Airline)
                .filter_by(name=f.airline)
                .first()
            )

            if not airline:
                airline = Airline(
                    name=f.airline,
                    code=f.airline[:2].upper()
                )

                self.session.add(airline)
                self.session.flush()

            dep = (
                self.session.query(Airport)
                .filter_by(code=f.from_airport)
                .first()
            )

            if not dep:
                dep = Airport(
                    code=f.from_airport,
                    city="Unknown",
                    country="Unknown"
                )

                self.session.add(dep)
                self.session.flush()

            arr = (
                self.session.query(Airport)
                .filter_by(code=f.to_airport)
                .first()
            )

            if not arr:
                arr = Airport(
                    code=f.to_airport,
                    city="Unknown",
                    country="Unknown"
                )

                self.session.add(arr)
                self.session.flush()

            flight = Flight(
                flight_number=f.flight_number,
                airline_id=airline.id,
                departure_airport_id=dep.id,
                arrival_airport_id=arr.id,
                price=f.price,
                duration=f.duration
            )

            self.session.add(flight)

        self.session.commit()