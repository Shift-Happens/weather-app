import api_weather


def launch_program():
    api_weather.get_localisation()
    api_weather.get_weather()
