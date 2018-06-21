#!/usr/bin/env python3
import io
import unittest

import invasion


class PartitionNetworkTestCase(unittest.TestCase):
    def test_single_network(self):
        n = {
            'a': ['b'],
            'b': ['a'],
        }

        network, remaining = invasion.partition_network(n)

        self.assertEqual(network, n)
        self.assertEqual(remaining, {})

    def test_two_networks(self):
        n = {
            'a': ['b'],
            'b': ['a'],
            'c': [],
        }

        network, remaining = invasion.partition_network(n)

        self.assertEqual(network, {'a': ['b'], 'b': ['a']})
        self.assertEqual(remaining, {'c': []})


class ReadMapTestCase(unittest.TestCase):
    def test_read_map(self):
        map_file = io.StringIO(
            'A north=B east=C south=D west=E\n'
            'B north=A east=C south=D west=E\n'
            'C north=A east=B south=D west=E\n'
            'D north=A east=B south=C west=E\n'
            'E north=A east=B south=C west=D\n')

        network = invasion.read_map(map_file)
        expected = {
            'A': ['B', 'C', 'D', 'E'],
            'B': ['A', 'C', 'D', 'E'],
            'C': ['A', 'B', 'D', 'E'],
            'D': ['A', 'B', 'C', 'E'],
            'E': ['A', 'B', 'C', 'D'],
        }

        self.assertEqual(network, expected)

    def test_long_city_names(self):
        map_file = io.StringIO(
            'San Francisco south=San Jose\n')

        network = invasion.read_map(map_file)
        expected = {
            'San Francisco': ['San Jose'],
            'San Jose': ['San Francisco'],
        }

        self.assertEqual(network, expected)


class CitiesWithMultipleAliensTestCase(unittest.TestCase):
    def test_ruined_cities(self):
        positions = 'ABCDEEEEA'
        result = invasion.cities_with_multiple_aliens(positions)

        self.assertEqual(result, ['A', 'E'])


if __name__ == '__main__':
    unittest.main()
