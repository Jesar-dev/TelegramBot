import os
import requests


SITE_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={0}\
&lon={1}&appid={2}&units=metric&lang=ru"


def parce_daily(coordinates):
    """
    coordinates: координаты города или улицы (list[широта, долгота])
    Функция передаёт координаты на сайт openweathermap и парсит информацию
    о погоде на 7 дней.
    Возвращает строку с данными о погоде на 7 дней.
    """
    weather = requests.get(SITE_URL.format(coordinates[0], coordinates[1],
                                           os.environ.get('API')))
    weather_json = weather.json()
    result_weather = ""
    count = 0
    for day in weather_json['daily']:
        temp_morning = day['temp']['morn']
        temp_day = day['temp']['day']
        temp_eve = day['temp']['eve']
        temp_night = day['temp']['night']
        temp_min = day['temp']['min']
        temp_max = day['temp']['max']
        wind_speed = day['wind_speed']
        try:
            rain = day['rain']
        except Exception:
            rain = 0
        cloudy = day['clouds']
        description = day['weather'][0]['description']
        if count == 0:
            current_day = "Сегодня"
        elif count == 1:
            current_day = "Завтра"
        elif count < 5:
            current_day = "Через {0} дня".format(count)
        else:
            current_day = "Через {0} дней".format(count)
        count += 1
        result_weather += "{0}\n\
Температура утром: {1}℃\n\
Температура днём: {2}℃\n\
Температура вечером: {3}℃\n\
Температура ночью: {4}℃\n\
Минимальная температура: {5}℃\n\
Максимальная температура: {6}℃\n\
Скорость ветра: {7}м/c\n\
Осадки: {8}см\n\
Облачность: {9}%\n\
Краткое описание погоды: {10}\n\n".format(current_day, temp_morning, temp_day, temp_eve,
                                          temp_night,
                                          temp_min,
                                          temp_max,
                                          wind_speed,
                                          rain, cloudy,
                                          description)
    return result_weather
