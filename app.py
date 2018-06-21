#!/bin/python

# A map of cities.
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
