#!/usr/bin/python
import sys
import argparse
import random

from city import City
from alien import Alien
from simulation import Simulation

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simulate an alien invasion.')
    parser.add_argument('num_aliens', type=int, help='Number of aliens')
    args = parser.parse_args()

    cities = {}
    for line in sys.stdin:
        line = line.strip()
        city_data = line.split(' ')
        city_name = city_data[0]
        directions = city_data[1:]
        direction_args = {}
        for direction in directions:
            point, other_city = direction.split('=')
            direction_args = {
                point: other_city
            }
        cities[city_name] = (City(city_name), direction_args)

    for _, (city, directions) in cities.iteritems():
        for direction, other_city_name in directions.iteritems():
            other_city = cities[other_city_name]
            setattr(city, direction, other_city)

    aliens = []
    num_aliens = args.num_aliens
    for i in range(num_aliens):
        alien_name = 'Alien {}'.format(i + 1)
        start_city = random.choice(cities.values())
        aliens.append(Alien(alien_name, start_city[0]))

    simulation = Simulation(cities, aliens)
    simulation.run()
