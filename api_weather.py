import requests
import json
import datetime


def get_localisation():
    e = requests.get("http://ip-api.com/json/?").json()
    latitude = e["latitude"]
    longitude = e['longitude']
    return latitude, longitude


def get_weather():
    latitude, longitude = get_localisation()
    weather = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&\
    hourly=temperature_2m").json()
    current_time_unformated = datetime.now
    current_time = current_time_unformated.strftime('%Y-%m-%dT%H:00')

    print(latitude, longitude)
    print(current_time)
    print(weather['hourly']['time'][0], weather['hourly']["temperature_2m"][0])
    print(weather)


def output_weather_data_as_a_string():
    pass


get_weather()