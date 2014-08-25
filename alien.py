class Alien(object):
    
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.city.aliens.append(self)

    def __repr__(self):
        return '{} ({})'.format(self.name, self.city)
