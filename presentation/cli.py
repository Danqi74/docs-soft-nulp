from presentation.interfaces import IPresentation
from business.interfaces import IFlightService


class CLI(IPresentation):

    def __init__(self, service: IFlightService):
        self.service = service

    def run(self):
        print("1. Import flights from CSV")
        choice = input("> ")

        if choice == "1":
            path = input("CSV path: ")
            self.service.import_flights(path)
            print("Import completed")