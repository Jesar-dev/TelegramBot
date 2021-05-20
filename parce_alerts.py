import os
import requests


SITE_URL = "https://api.openweathermap.org/data/2.5/onecall?lat={0}\
&lon={1}&appid={2}&units=metric&lang=ru"


def parce_alerts(coordinates):
    """
    coordinates: координаты города или улицы (list[широта, долгота])
    Функция передаёт координаты на сайт openweathermap и парсит информацию
    о штормовых предупреждениях.
    Возвращает строку с данными о штормовых предупреждениях (если они есть).
    """
    check_alerts = False
    weather = requests.get(SITE_URL.format(coordinates[0], coordinates[1],
                                           os.environ.get('API')))
    weather_json = weather.json()
    try:
        alerts = weather_json['alerts']
        for alert in alerts:
            if len(alert['description']) != 0:
                check_alerts = True
                main_alert = alert['description']
    except Exception:
        check_alerts = False
    if not check_alerts:
        main_alert = "На завтра нет особых оповещений!"
    return main_alert
