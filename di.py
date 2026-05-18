from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base
from data_access.flight_repository import FlightRepository
from business.flight_service import FlightService


class Container:

    def __init__(self):

        engine = create_engine("sqlite:///flights.db")

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)

        self.session = Session()

    def flight_service(self):

        repo = FlightRepository(self.session)

        return FlightService(repo)