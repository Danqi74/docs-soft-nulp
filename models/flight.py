from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True)

    flight_number = Column(String)

    airline_id = Column(Integer, ForeignKey("airlines.id"))

    departure_airport_id = Column(Integer, ForeignKey("airports.id"))

    arrival_airport_id = Column(Integer, ForeignKey("airports.id"))

    price = Column(Float)

    duration = Column(Integer)

    airline = relationship("Airline")

    departure_airport = relationship(
        "Airport",
        foreign_keys=[departure_airport_id]
    )

    arrival_airport = relationship(
        "Airport",
        foreign_keys=[arrival_airport_id]
    )