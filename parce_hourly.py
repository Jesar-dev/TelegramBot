import requests
import os


def parce_hourly(coordinates):
    """
    coordinates: координаты города или улицы (list[широта, долгота])
    Функция передаёт координаты на сайт openweathermap и парсит информацию
    о погоде по часам на 48 часов.
    Возвращает строку с кратким описанием погоды по часам.
    """
    count = 0
    weather = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={0}\
&lon={1}&exclude=daily&appid={2}&units=metric&lang=ru".format(coordinates[0], coordinates[1],
                                                              os.environ.get('API')))
    weather_json = weather.json()
    hourly_weather = weather_json['hourly']
    result = ""
    first_hour = hourly_weather[0]['dt']
    for hour in hourly_weather:
        if count == 0:
            result += "Сейчас погода: \
            {0}\n".format(hour['weather'][0]['description'])
            count += 1
        else:
            now_hour = (hour['dt'] - first_hour)/3600
            result += "Через {0} час погода: \
            {1}\n".format(int(now_hour), hour['weather'][0]['description'])
    return result
