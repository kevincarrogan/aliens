import random

class Alien(object):
    
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.city.aliens.add(self)

    def move(self):
        adjacent_cities = self.city.adjacent_cities

        if adjacent_cities:
            new_city = random.choice(adjacent_cities)

            self.city.aliens.remove(self)
            self.city = new_city
            self.city.aliens.add(self)

    @property
    def is_trapped(self):
        return len(self.city.adjacent_cities) == 0

    def __repr__(self):
        return '{} ({})'.format(self.name, self.city)
