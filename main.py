import requests
import os

from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "you sid from twilio here"
auth_token = "you auth token from twilio here"

api_key = "you api key from openweather here"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_params = {
    "lat": 34.225727,
    "lon": -77.944710,
    "exclude":"current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, weather_params )
response.raise_for_status()


will_rain = False
weather_data = response.json()["hourly"][0:12]

for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
           will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(body="Umbrella Alert! It might rain today",from_='from no. here',to='to no. here')
    print(message.status)