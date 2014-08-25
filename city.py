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

    def remove_connections(self):
        for direction in self.directions:
            other_city = getattr(self, direction)
            if other_city:
                for other_direction in self.directions:
                    if getattr(other_city, other_direction) == self:
                        setattr(other_city, other_direction, None)

    def __repr__(self):
        return '<City: {}>'.format(self.name)
