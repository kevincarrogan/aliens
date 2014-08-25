class Simulation(object):

    def __init__(self, cities, aliens):
        self.cities = cities
        self.aliens = aliens
        self.runs = 0

    def run(self):
        while self.runs < 10000:
            self.move_aliens()

            self.runs += 1
        print 'Finished running'

    def move_aliens(self):
        for alien in self.aliens:
            alien.move()
