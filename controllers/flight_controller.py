from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from services.flight_service import FlightService

from database import session

from models.flight import Flight

flight_bp = Blueprint(
    "flight_bp",
    __name__
)

service = FlightService(session)

@flight_bp.route("/flights")
def flights():

    flights = service.get_all_flights()

    return render_template(
        "flights.html",
        flights=flights
    )

@flight_bp.route("/add", methods=["GET", "POST"])
def add_flight():

    if request.method == "POST":

        service.create_flight(
            flight_number=request.form["flight_number"],
            airline_name=request.form["airline"],
            from_airport=request.form["from_airport"],
            to_airport=request.form["to_airport"],
            price=request.form["price"],
            duration=request.form["duration"]
        )

        return redirect("/flights")

    return render_template("add_flight.html")

@flight_bp.route("/delete/<int:id>")
def delete_flight(id):

    service.delete_flight(id)
    return redirect("/flights")

@flight_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_flight(id):

    flight = session.query(Flight).get(id)

    if not flight:
        return "Flight not found"

    if request.method == "POST":

        flight_number = request.form["flight_number"]
        airline = request.form["airline"]
        from_airport = request.form["from_airport"]
        to_airport = request.form["to_airport"]
        price = request.form["price"]
        duration = request.form["duration"]

        if (
            not flight_number or
            not airline or
            not from_airport or
            not to_airport or
            not price or
            not duration
        ): return "All fields are required"

        service.update_flight_full(
            flight_id=id,
            flight_number=flight_number,
            airline_name=airline,
            from_airport=from_airport,
            to_airport=to_airport,
            price=price,
            duration=duration
        )

        return redirect("/flights")

    return render_template(
        "edit_flight.html",
        flight=flight
    )