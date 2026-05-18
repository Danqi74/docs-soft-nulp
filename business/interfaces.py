from abc import ABC, abstractmethod


class IFlightService(ABC):

    @abstractmethod
    def import_flights(self, csv_path: str):
        pass