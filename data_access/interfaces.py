from abc import ABC, abstractmethod
from typing import List
from entities import FlightDTO


class IFlightRepository(ABC):

    @abstractmethod
    def save_flights(self, flights: List[FlightDTO]):
        pass

    @abstractmethod
    def load_from_csv(self, path: str) -> List[FlightDTO]:
        pass