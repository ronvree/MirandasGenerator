import random


class State:
    def __init__(self, width, height, values, seed=0):
        self.width = width
        self.height = height
        self.values = values
        self.cells = [[0] * self.height for _ in self.width]

        # TODO -- read seed

    # TODO -- __str__(self)

    def randomize(self):
        for x in range(self.width):
            for y in range(self.height):
                self.cells[x][y] = random.choice(self.values)

    def get(self, x, y):
        return self.cells[x][y]

    def set(self, x, y, value):  # TODO -- Error if value is not in self.values
        self.cells[x][y] = value


class Rule:
    def __init__(self, values, seed, neighbourhood='wolfram'):
        self.values = values
        self.substitution_system = dict()  # TODO

        if neighbourhood is 'wolfram':
            neighbourhood_size = 5

            # wut




        # TODO -- other neighbourhoods



        # TODO


class Shirt:
    def __init__(self):
        Shirt()
        # TODO
