import os
import requests


SITE_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={0}&lon={1}\
&exclude=daily&appid={2}&units=metric&lang=ru"


def parce_current(coordinates):
    """
    coordinates: координаты города или улицы (list[широта, долгота])
    Функция передаёт координаты на сайт openweathermap и парсит информацию
    о погоде в данный момент.
    Возвращает строку с данными о погоде в данный момент.
    """
    weather = requests.get(SITE_URL.format(coordinates[0], coordinates[1],
                                           os.environ.get('API')))
    weather_json = weather.json()
    temp = weather_json['current']['temp']
    feels = weather_json['current']['feels_like']
    pressure = weather_json['current']['pressure']
    clouds = weather_json['current']['clouds']
    humidity = weather_json['current']['humidity']
    description = weather_json['current']['weather'][0]['description']
    wind_speed = weather_json['current']['wind_speed']
    result_weather = "Температура на улице: {0}\n\
Чувствуется как: {1}\n\
Давление воздуха: {2}\n\
Облачность: {3}%\n\
Влажность: {4}%\n\
Скорость ветра: {5}м/c\n\
Краткое описание погоды: {6}".format(temp, feels, pressure, clouds, humidity, wind_speed, description)
    return result_weather
