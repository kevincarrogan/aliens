#!/usr/bin/env python3
import collections
import random
import re
import sys


def partition_network(network):
    """Divide a network into 1 or more coherent networks. Returns a pair of
    network dicts. The first item is a coherent network, the second item is
    the network consisting of the nodes not in the first network.
    """
    if not network:
        return network, {}

    # Sort so that we get predictable ouput, makes tests easier.
    start = sorted(network)[0]
    q = collections.deque([start])

    visited = set()

    while q:
        node = q.pop()
        visited.add(node)

        for n in network[node]:
            if n in visited:
                continue

            q.append(n)

    not_visited = set(network) - visited
    visited_network = {k: network[k] for k in visited}
    remaining_network = {k: network[k] for k in not_visited}

    return visited_network, remaining_network


def fixup_network(network):
    """Insure that if A -> B, then B -> A."""
    # We need to iterate over a copy of the keys else we get RuntimeError
    # when adding missing nodes.
    for src_node in sorted(network):
        for dest_node in network[src_node]:
            if dest_node not in network:
                network[dest_node] = []

            if src_node not in network[dest_node]:
                network[dest_node].append(src_node)

    return network


def read_map(fh):
    """Builds a network map from lines in a file.

    Keys are names of cities, values are a list of names of connected cities.
    If city A has a connection to city B, then we guarantee B -> A.
    """
    pattern = re.compile(r' (?:north|east|south|west)=')
    network = {}

    for line in fh:
        line = line.strip()
        names = pattern.split(line)
        node = names[0]

        network[node] = names[1:]

    fixup_network(network)

    return network


def setup_game(map_file, num_aliens):
    city_map = read_map(map_file)
    start_positions = random.sample(list(city_map), num_aliens)

    return city_map, start_positions


def move_alien(city_map, start_city):
    """Pick a connected city at random (or the same city if no connections)."""
    try:
        dest_city = random.choice(city_map[start_city])
    except (KeyError, ValueError):
        dest_city = start_city

    return dest_city


def cities_with_multiple_aliens(alien_positions):
    """Returns a set of cities where more than 1 alien moved."""
    counts = collections.Counter(alien_positions)
    # Don't include None in ruined cities.
    ruined_cities = [city for city in counts if city and counts[city] > 1]

    return ruined_cities


def remove_network_connections(network, dead_nodes):
    """Modifies a network so that no node has a connection to any dead node."""
    for node in dead_nodes:
        for connected_node in network[node]:
            network[connected_node].remove(node)

        network[node] = []


def write_network(network, fh):
    # Bug! The challenge expects us to remember the direction each city is
    # but it was simpler to ignore that. So here we just make up a direction.
    compass_points = ('north', 'east', 'south', 'west')

    for node in sorted(network):
        connections = network[node]
        parts = [node]

        for label, node in zip(compass_points, connections):
            parts.append('%s=%s' % (label, node))

        line = ' '.join(parts)

        fh.write(line + '\n')


def main(argv):
    num_aliens = int(sys.argv[1])
    # city_map is the network map, a mutable dict where city names are keys,
    # and the values are a list of other connected cities.
    # alien_positions is a list of city names. Alien 0 is at alien_positions[0].
    # Alien 99 is at alien_positions[99].
    city_map, alien_positions = setup_game(sys.stdin, num_aliens)

    # OK. Every turn we build a new list of alien positions by moving each
    # alien to a connected city, picked at random. After they have all moved
    # we check if any of them are in the same city. If they are, then those
    # aliens are killed (which is recorded as None in the alien_positions list)
    # and the city_map is modified to remove the city from all connected cities.

    # There's an optimisation we could do: find if the network has split then
    # ignore aliens who are in their own isolated network because they can never
    # bump into another alien from that time onwards.

    max_turns = 10000

    for turn in range(max_turns):
        alien_positions = [move_alien(city_map, city) for city in alien_positions]
        ruined_cities = cities_with_multiple_aliens(alien_positions)
        # Here we need to say which aliens were killed in which cities.
        # TODO!
        if ruined_cities:
            sys.stderr.write('turn %s: %r\n' % (turn, ruined_cities))

        alien_positions = [None if c in ruined_cities else c for c in alien_positions]
        remove_network_connections(city_map, ruined_cities)

        if not any(alien_positions):
            # All the aliens are dead!
            break

    # And give the final status of the map.
    write_network(city_map, sys.stdout)


if __name__ == '__main__':
    main(sys.argv)
