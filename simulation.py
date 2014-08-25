import random

from alien import Alien

class Simulation(object):

    def __init__(self, cities, num_aliens):
        self.cities = cities
        self.aliens = set()
        self.runs = 0

        self.create_aliens(num_aliens)

    def create_aliens(self, num_aliens):
        for i in range(num_aliens):
            alien_name = 'Alien {}'.format(i + 1)
            start_city = random.choice(list(self.cities))
            self.aliens.add(Alien(alien_name, start_city))

    def run(self):
        while self.runs < 10000 and self.aliens:
            self.move_aliens()
            self.fight_aliens()

            self.runs += 1

    def move_aliens(self):
        for alien in self.aliens:
            alien.move()

    def fight_aliens(self):
        destroyed_cities = []
        for city in self.cities:
            if len(city.aliens) > 1:
                destroyed_cities.append(city)
        for destroyed_city in destroyed_cities:
            destroyed_city.remove_connections()
            self.cities.remove(destroyed_city)
            self.aliens -= destroyed_city.aliens
            alien_names = [alien.name for alien in destroyed_city.aliens]
            destroyers = ' and '.join(alien_names)
            print '{} has been destroyed by {}!'.format(destroyed_city.name, destroyers)

