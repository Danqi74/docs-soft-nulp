from dataclasses import dataclass


@dataclass
class FlightDTO:
    airline: str
    flight_number: str
    from_airport: str
    to_airport: str
    price: float
    duration: int