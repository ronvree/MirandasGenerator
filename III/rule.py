import random

from III.state import RangedState


class SubstitutionSystem:

    def __init__(self):
        self.system = dict()

    def __str__(self):
        return '\n'.join([str(' '.join([str(c) for c in s])) + " -> "
                          + str(self.system[s]) for s in self.system])

    def mapped_neighbourhoods(self):
        return self.system.keys()

    def get(self, neighbourhood):
        return self.system[neighbourhood]

    def set(self, neighbourhood, value):
        self.system[neighbourhood] = value


class Rule(SubstitutionSystem):

    def __init__(self, number_of_values, index=0):
        super().__init__()
        self.number_of_values = number_of_values
        self.values = range(number_of_values)
        base = number_of_values
        i = 0
        for x in self.values:
            for y in self.values:
                for z in self.values:
                    self.set((x, y, z), int((index % pow(base, i + 1)) / pow(base, i)))
                    i += 1

    def randomize(self):
        for s in self.mapped_neighbourhoods():
            self.set(s, random.choice(self.values))

    def next(self, state):
        n = len(state)
        next_state = RangedState(n, self.number_of_values)
        for i in range(n):
            neighbourhood = (state.get(i), state.get((i + 1) % n), state.get((i + 2) % n))
            next_state.set((i + 1) % n, self.get(neighbourhood))
        return next_state

