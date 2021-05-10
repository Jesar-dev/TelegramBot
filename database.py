import shelve


def check_database(town):
    """
    town: город или адрес в формате str
    Функция получает на вход строку с городом и проверяет
    есть ли в базе данных данный город
    Возвращает True если есть и False в ином случае
    """
    with shelve.open('cities.db') as db:
        if town in db.keys():
            return True
        else:
            return False


def add_to_database(town, coordinates):
    """
    town: город или адрес в формате str
    coordinates: координаты в формате list[широта, долгота]
    Функция получает на вход город и координаты и добавляет их
    в базу данных.
    """
    with shelve.open('cities.db') as db:
        db[town] = coordinates


def get_coordinates_from_database(town):
    """
    town: город или адрес в формате str
    Функция получает на вход город или адрес в формате str
    и возвращает координаты из базы данных
    """
    with shelve.open('cities.db') as db:
        return db[town]
