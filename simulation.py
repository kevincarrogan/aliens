import random

from city import City
from alien import Alien

class Simulation(object):

    def __init__(self, city_network, num_aliens):
        self.cities = set()
        self.aliens = set()
        self.runs = 0

        self.create_cities(city_network)
        self.create_aliens(num_aliens)

    def create_cities(self, city_network):
        generated_cities = {}
        for city_name, directions in city_network.iteritems():
            city = City(city_name)
            generated_cities[city_name] = city
            for direction, other_city_name in directions.iteritems():
                if other_city_name not in generated_cities:
                    generated_cities[other_city_name] = (City(other_city_name))
                other_city = generated_cities[other_city_name]
                setattr(city, direction, other_city)

        self.cities = set(generated_cities.values())

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

