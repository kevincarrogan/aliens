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
        'East': 'Bar',
    },
}


def random_city(cities):
    return random.choice(cities.keys())


def generate_aliens(number_to_generate):
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
aliens = generate_aliens(10)
