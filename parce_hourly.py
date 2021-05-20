import os
import requests


SITE_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={0}\
&lon={1}&exclude=daily&appid={2}&units=metric&lang=ru"


def parce_hourly(coordinates):
    """
    coordinates: координаты города или улицы (list[широта, долгота])
    Функция передаёт координаты на сайт openweathermap и парсит информацию
    о погоде по часам на 48 часов.
    Возвращает строку с кратким описанием погоды по часам.
    """
    count = 0
    weather = requests.get(SITE_URL.format(coordinates[0], coordinates[1],
                                           os.environ.get('API')))
    weather_json = weather.json()
    hourly_weather = weather_json['hourly']
    result = ""
    word_hour = ""
    first_hour = hourly_weather[0]['dt']
    for hour in hourly_weather:
        if count == 0:
            result += "Сейчас погода: \
            {0}\n".format(hour['weather'][0]['description'])
            count += 1
        else:
            now_hour = (hour['dt'] - first_hour)/3600
            if int(now_hour) >= 10 and int(now_hour) <= 19:
                word_hour = "часов"
            elif int(now_hour) % 10 == 1:
                word_hour = "час"
            elif int(now_hour) % 10 in [2, 3, 4]:
                word_hour = "часа"
            else:
                word_hour = "часов"
            result += "Через {0} {1} погода: \
            {2}\n".format(int(now_hour), word_hour, hour['weather'][0]['description'])
    return result
