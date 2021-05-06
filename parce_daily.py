import requests


API = "bbc64ccde0250d64248213a494d3ad7c"


def parce_daily(coordinates):
    weather = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={0}\
&lon={1}&appid={2}&units=metric&lang=ru".format(coordinates[0], coordinates[1], API))
    weather_json = weather.json()
    temp_morning = weather_json['daily'][0]['temp']['morn']
    temp_day = weather_json['daily'][0]['temp']['day']
    temp_eve = weather_json['daily'][0]['temp']['eve']
    temp_night = weather_json['daily'][0]['temp']['night']
    temp_min = weather_json['daily'][0]['temp']['min']
    temp_max = weather_json['daily'][0]['temp']['max']
    wind_speed = weather_json['daily'][0]['wind_speed']
    try:
        rain = weather_json['daily'][0]['rain']
    except Exception:
        rain = "к сожалению информация о осадках не найдена("
    cloudy = weather_json['daily'][0]['clouds']
    description = weather_json['daily'][0]['weather'][0]['description']
    result_weather = "Температура утром: {0}℃\n\
    Температура днём: {1}℃\n\
    Температура вечером: {2}℃\n\
    Температура ночью: {3}℃\n\
    Минимальная температура: {4}℃\n\
    Максимальная температура: {5}℃\n\
    Скорость ветра: {6}м/c\n\
    Осадки: {7}м\n\
    Облачность: {8}%\n\
    Краткое описание погоды: {9}".format(temp_morning, temp_day, temp_eve,
                                         temp_night,
                                         temp_min,
                                         temp_max,
                                         wind_speed,
                                         rain, cloudy,
                                         description)
    return result_weather
