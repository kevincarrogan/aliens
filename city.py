class City(object):

    def __init__(self, name):
        self.name = name
        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def __repr__(self):
        return self.name
