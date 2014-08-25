class Alien(object):
    
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __repr__(self):
        return '{} ({})'.format(self.name, self.city)
