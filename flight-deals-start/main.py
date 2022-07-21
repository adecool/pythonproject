from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
import smtplib

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    print(city_names)
    codes = flight_search.get_destination_codes(city_names)
    data_manager.update_destination_codes(codes)
    sheet_data = data_manager.get_destination_data()

today = datetime.now() + timedelta(1)
six_month_from_today = datetime.now() + timedelta(6 * 30)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today,
        to_time=six_month_from_today
    )

    if flight.price < destination["lowestPrice"]:
        with smtplib.SMTP("smtp.gmail.com") as server:
            server.starttls()
            server.login('gen2proff@gmail.com', 'gen2;soul')
            notification = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

            server.sendmail('gen2proff@gmail.com','gen2proff@yahoo.com',msg=notification.encode('utf-8'))