class FlightDTO:

    def __init__(
        self,
        flight_number,
        airline,
        from_airport,
        to_airport,
        price,
        duration
    ):

        self.flight_number = flight_number

        self.airline = airline

        self.from_airport = from_airport

        self.to_airport = to_airport

        self.price = float(price)

        self.duration = int(duration)