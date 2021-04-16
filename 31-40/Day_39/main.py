from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from twilio.rest import Client
from os import environ

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "GYE"

account_sid = environ.get("ACCOUNT_SID")
auth_token = environ.get("AUTH_TOKEN")

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to"
                 f"{flight.destination_city}-{flight.destination_airport}, from {flight.out_date}"
                 f"to {flight.return_date}.",
            to=environ.get("TO_C"),
            )
        print(message.sid)
