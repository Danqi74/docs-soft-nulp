from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Airline(Base):
    __tablename__ = "airlines"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)

    flights = relationship("Flight", back_populates="airline")


class Airport(Base):
    __tablename__ = "airports"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    city = Column(String)
    country = Column(String)


class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True)
    flight_number = Column(String)

    airline_id = Column(Integer, ForeignKey("airlines.id"))
    departure_airport_id = Column(Integer, ForeignKey("airports.id"))
    arrival_airport_id = Column(Integer, ForeignKey("airports.id"))

    price = Column(Float)
    duration = Column(Integer)

    airline = relationship("Airline", back_populates="flights")