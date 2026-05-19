import csv

from models.flight import Flight
from models.airline import Airline
from models.airport import Airport

from dto.flight_dto import FlightDTO

class FlightService:

    def __init__(self, session):

        self.session = session

    def get_all_flights(self):

        return self.session.query(Flight).all()

    def create_flight(
        self,
        flight_number,
        airline_name,
        from_airport,
        to_airport,
        price,
        duration
    ):

        airline = (
            self.session.query(Airline)
            .filter_by(name=airline_name)
            .first()
        )

        if not airline:

            airline = Airline(
                name=airline_name,
                code=airline_name[:2].upper()
            )

            self.session.add(airline)

            self.session.flush()

        dep = (
            self.session.query(Airport)
            .filter_by(code=from_airport)
            .first()
        )

        if not dep:

            dep = Airport(
                code=from_airport,
                city="Unknown",
                country="Unknown"
            )

            self.session.add(dep)

            self.session.flush()

        arr = (
            self.session.query(Airport)
            .filter_by(code=to_airport)
            .first()
        )

        if not arr:

            arr = Airport(
                code=to_airport,
                city="Unknown",
                country="Unknown"
            )

            self.session.add(arr)

            self.session.flush()

        flight = Flight(
            flight_number=flight_number,
            airline_id=airline.id,
            departure_airport_id=dep.id,
            arrival_airport_id=arr.id,
            price=float(price),
            duration=int(duration)
        )

        try:

            self.session.add(flight)

            self.session.commit()

        except Exception as e:

            self.session.rollback()

            print(e)

    def delete_flight(self, flight_id):

        flight = (
            self.session.query(Flight)
            .get(flight_id)
        )

        if flight:

            self.session.delete(flight)

            self.session.commit()

    def update_flight(self, flight_id, data):

        flight = (
            self.session.query(Flight)
            .get(flight_id)
        )

        if flight:

            flight.price = data["price"]

            flight.duration = data["duration"]

            self.session.commit()

    def import_from_csv(self, filename):

        flights = []

        with open(
            filename,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                dto = FlightDTO(
                    flight_number=row["flight_number"],
                    airline=row["airline"],
                    from_airport=row["from_airport"],
                    to_airport=row["to_airport"],
                    price=row["price"],
                    duration=row["duration"]
                )

                flights.append(dto)

        self.save_flights(flights)

    def save_flights(self, flights):

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

    def update_flight_full(
        self,
        flight_id,
        flight_number,
        airline_name,
        from_airport,
        to_airport,
        price,
        duration
    ):

        flight = (
            self.session.query(Flight)
            .get(flight_id)
        )

        if not flight:

            return

        airline = (
            self.session.query(Airline)
            .filter_by(name=airline_name)
            .first()
        )

        if not airline:

            airline = Airline(
                name=airline_name,
                code=airline_name[:2].upper()
            )

            self.session.add(airline)

            self.session.flush()

        dep = (
            self.session.query(Airport)
            .filter_by(code=from_airport)
            .first()
        )

        if not dep:

            dep = Airport(
                code=from_airport,
                city="Unknown",
                country="Unknown"
            )

            self.session.add(dep)

            self.session.flush()

        arr = (
            self.session.query(Airport)
            .filter_by(code=to_airport)
            .first()
        )

        if not arr:

            arr = Airport(
                code=to_airport,
                city="Unknown",
                country="Unknown"
            )

            self.session.add(arr)

            self.session.flush()

        try:

            flight.flight_number = flight_number

            flight.airline_id = airline.id

            flight.departure_airport_id = dep.id

            flight.arrival_airport_id = arr.id

            flight.price = float(price)

            flight.duration = int(duration)

            self.session.commit()

        except Exception as e:

            self.session.rollback()

            print(e)