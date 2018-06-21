#!/bin/python

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

# A dictionary of aliens.
# The key is the name of the alien and the value is the city the alien is currently
# located in.
aliens = {
    'alien 1': 'Foo',
    'alien 2': 'Bar',
    'alien 3': 'Baz',
}
