import requests, json
import datetime


def get_localisation():
    e = requests.get("http://ip-api.com/json/?").json()
    lat = e["lat"] 
    lon = e['lon']
    return lat,lon

def get_weather():
    lat,lon = get_localisation()
    print(lat, lon)
    pogoda = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m").json()
    # print(pogoda)
    current_time = datetime.now().strftime('%Y-%m-%dT%H:00')
    print(current_time)
    print(pogoda['hourly']['time'][0],pogoda['hourly']["temperature_2m"][0])

    
get_weather()
