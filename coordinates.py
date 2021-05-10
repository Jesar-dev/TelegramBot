import requests


def parse_coordinates(town):
    """
    town: город или адрес в формате str
    Функция получает на вход город, передаёт данные на сайт
    и парсит координаты города в формате list[широта, долгота]
    Возвращаемое значение: list[широта, долгота]
    """
    r = requests.get("http://search.maps.sputnik.ru/search/addr?q={0}".format(town))
    get_json = r.json()
    coordinates = get_json['result']['address'][0]['features'][0]['geometry']['geometries'][0]['coordinates']
    lat = coordinates[1]
    lon = coordinates[0]
    lat_lon = [lat, lon]
    return lat_lon
