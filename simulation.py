class Simulation(object):

    def __init__(self, cities, aliens):
        self.cities = cities
        self.aliens = aliens
        self.runs = 0

    def run(self):
        print 'Running simulation'
