import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API_KEY")
MY_LAT = os.environ.get("MY_LAT")
MY_LON = os.environ.get("MY_LON")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
all_weather_id = []
will_rain = False

for position in range(12):
    all_weather_id.append(weather_data["hourly"][:12][position]["weather"][0]["id"])

for weather_id in all_weather_id:
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring an umbrella.",
                from_=os.environ.get("FROM_C"),
                to=os.environ.get("TO_C"),
                )
    print(message.status)
