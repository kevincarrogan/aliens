#!/bin/python
import random

# A dictionary of cities.
# The key being the name of the city and the corresponding dictionary value
# being a dictionary of each city name in that direction.
cities = {
    'Foo': {
        'north': 'Bar',
        'west': 'Baz',
        'south': 'Qu-ux',
    },
    'Bar': {
        'north': 'Foo',
        'west': 'Bee',
    },
    'Baz': {
        'east': 'Foo',
    },
    'Qu-ux': {
        'north': 'Foo',
    },
    'Bee': {
        'east': 'Bar',
    },
}


def random_city(cities):
    return random.choice(cities.keys())


def generate_aliens(cities, number_to_generate):
    aliens = {}
    for i in range(number_to_generate):
        name = 'alien {}'.format(i)
        city = random_city(cities)
        aliens[name] = city
    return aliens


# A dictionary of aliens.
# The key is the name of the alien and the value is the city the alien is currently
# located in.
# aliens = {
#    'alien 1': 'Foo',
#    'alien 2': 'Bar',
#    'alien 3': 'Baz',
# }
aliens = generate_aliens(cities, 10)


def random_connected_city(cities, current_city):
    available_choices = cities[current_city]
    if len(available_choices):
        return random.choice(available_choices.values())
    else:
        # The alien is stuck with nowhere to go
        return current_city


def wander_aliens(cities, aliens):
    new_aliens = {}
    for name, current_city in aliens.items():
        new_aliens[name] = random_connected_city(cities, current_city)
    return new_aliens


aliens = wander_aliens(cities, aliens)


def get_aliens_in_city(aliens, city):
    found_aliens = []
    for alien, current_city in aliens.items():
        if current_city == city:
            found_aliens.append(alien)

    return found_aliens


def destroy(cities, aliens):
    new_cities = {}
    new_aliens = {}

    destroyed_cities = set()
    destroyed_aliens = set()

    for city in cities.keys():
        aliens_in_city = get_aliens_in_city(aliens, city)
        if len(aliens_in_city) > 1:
            destroyed_cities.add(city)
            for alien in aliens_in_city:
                destroyed_aliens.add(alien)
            print '{} has been destroyed by {}!'.format(
                city,
                ' and '.join(aliens_in_city),
            )

    for city, connections in cities.items():
        if city not in destroyed_cities:
            new_connections = {}
            for direction, connected_city in connections.items():
                if connected_city not in destroyed_cities:
                    new_connections[direction] = connected_city
            new_cities[city] = new_connections

    for alien, city in aliens.items():
        if alien not in destroyed_aliens:
            new_aliens[alien] = city

    return new_cities, new_aliens

cities, aliens = destroy(cities, aliens)
