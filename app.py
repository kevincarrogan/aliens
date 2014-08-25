#!/usr/bin/python
import sys
import argparse
import random

from city import City
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
            direction_args[point] = other_city
        cities[city_name] = ((City(city_name), direction_args))

    for _, (city, directions) in cities.iteritems():
        for direction, other_city_name in directions.iteritems():
            other_city = cities[other_city_name]
            setattr(city, direction, other_city[0])

    cities = set(
        city[0]
        for city in cities.values()
    )

    num_aliens = args.num_aliens

    simulation = Simulation(cities, num_aliens)
    simulation.run()
