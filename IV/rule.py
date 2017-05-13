import random

from III.state import RangedState


class Rule:

    def __init__(self, number_of_values, relative_nbh_indices, index=0):
        self.system = dict()

        self.number_of_values = number_of_values
        self.values = range(number_of_values)
        self.relative_nbh_indices = relative_nbh_indices

        base = number_of_values

        perms = self.help_fill_perms(len(relative_nbh_indices))

        for i in range(len(perms)):
            self.set(tuple(perms[i]), int((index % pow(base, i + 1)) / pow(base, i)))

    def help_fill_perms(self, i):
        if i:
            res = []
            for p in self.help_fill_perms(i - 1):
                for v in self.values:
                    n_p = list(p)
                    n_p.append(v)
                    res.append(n_p)
            return res
        else:
            return [[]]

    def __str__(self):
        return '\n'.join([str(' '.join([str(c) for c in s])) + " -> "
                          + str(self.system[s]) for s in self.system])

    def randomize(self):
        for s in self.mapped_neighbourhoods():
            self.set(s, random.choice(self.values))

    def next(self, state):
        n = len(state)
        next_state = RangedState(n, self.number_of_values)
        for i in range(n):
            nbh = tuple([state.get((i + j) % n) for j in self.relative_nbh_indices])
            next_state.set((i + 1) % n, self.get(nbh))
        return next_state

    def mapped_neighbourhoods(self):
        return self.system.keys()

    def get(self, neighbourhood):
        return self.system[neighbourhood]

    def set(self, neighbourhood, value):
        self.system[neighbourhood] = value
