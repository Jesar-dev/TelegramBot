import shelve


def check_database(town):
    with shelve.open('cities.db') as db:
        if town in db.keys():
            return True
        else:
            return False


def add_to_database(town, coordinates):
    with shelve.open('cities.db') as db:
        db[town] = coordinates


def get_coordinates_from_database(town):
    with shelve.open('cities.db') as db:
        return db[town]
