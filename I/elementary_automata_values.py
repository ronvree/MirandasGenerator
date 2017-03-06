import random


def cell_str(cell):
    str_dict = dict()
    str_dict[0] = ' '
    str_dict[1] = '@'
    str_dict[2] = '%'
    str_dict[3] = '#'
    return str_dict[cell]


class State:

    def __init__(self, size, values):
        self.cells = size * [0]
        self.values = values

    def __str__(self):
        return ' '.join([cell_str(cell) for cell in self.cells])

    def __len__(self):
        return len(self.cells)

    def randomize(self):
        for i in range(len(self.cells)):
            self.cells[i] = random.choice(self.values)

    def get(self, i):
        return self.cells[i]

    def set(self, i, val):
        self.cells[i] = val


class Rule:

    def __init__(self, values, n=0):
        self.substitution_system = dict()
        self.values = values
        for x in self.values:
            for y in self.values:
                for z in self.values:
                    self.substitution_system[(x, y, z)] = 0

    def __str__(self):
        return '\n'.join([str(' '.join([cell_str(c) for c in s])) + " -> "
                          + cell_str(self.substitution_system[s]) for s in self.substitution_system])

    def randomize(self):
        for s in self.substitution_system:
            self.substitution_system[s] = random.choice(self.values)

    def next(self, state):
        n = len(state)
        next_state = State(n, self.values)
        for i in range(n):
            pattern = (state.get(i), state.get((i + 1) % n), state.get((i + 2) % n))
            next_state.set((i + 1) % n, self.substitution_system.get(pattern))
        return next_state

    def get(self, x, y, z):
        return self.substitution_system[(x, y, z)]

    def set(self, x, y, z, o):
        self.substitution_system[(x, y, z)] = o
