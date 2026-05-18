from business.interfaces import IFlightService
from data_access.interfaces import IFlightRepository


class FlightService(IFlightService):

    def __init__(self, repo: IFlightRepository):
        self.repo = repo

    def import_flights(self, csv_path: str):
        flights = self.repo.load_from_csv(csv_path)
        self.repo.save_flights(flights)