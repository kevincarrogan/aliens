#!/usr/bin/python
import sys

from city import City

if __name__ == '__main__':
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
        cities[city_name] = City(city_name, **direction_args)
