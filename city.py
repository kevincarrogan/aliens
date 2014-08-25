class City(object):

    directions = ['north', 'east', 'south', 'west']

    def __init__(self, name):
        self.name = name
        self.north = None
        self.east = None
        self.south = None
        self.west = None
        self.aliens = set()

    @property
    def adjacent_cities(self):
        return [
            getattr(self, direction)
            for direction in self.directions
            if getattr(self, direction)
        ]

    def __repr__(self):
        return self.name
