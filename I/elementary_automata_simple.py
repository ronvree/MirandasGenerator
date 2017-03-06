import random


def cell_str(cell):
    return 'O' if cell else ' '


class State:

    def __init__(self, size):
        self.cells = size * [False]

    def __str__(self):
        return ' '.join([cell_str(cell) for cell in self.cells])

    def __len__(self):
        return len(self.cells)

    def randomize(self):
        for i in range(len(self.cells)):
            self.cells[i] = bool(random.getrandbits(1))

    def get(self, i):
        return self.cells[i]

    def set(self, i, val):
        self.cells[i] = val


class Rule:

    def __init__(self, n=0):
        self.substitution_system = dict()
        for x in [False, True]:
            for y in [False, True]:
                for z in [False, True]:
                    self.substitution_system[(x, y, z)] = bool(n % 2)
                    n >>= 1

    def __str__(self):
        return '\n'.join([str(' '.join([cell_str(c) for c in s])) + " -> " + cell_str(self.substitution_system[s]) for s in self.substitution_system])

    def randomize(self):
        for s in self.substitution_system:
            self.substitution_system[s] = bool(random.getrandbits(1))

    def next(self, state):
        n = len(state)
        next_state = State(n)
        for i in range(n):
            pattern = (state.get(i), state.get((i + 1) % n), state.get((i + 2) % n))
            next_state.set((i + 1) % n, self.substitution_system.get(pattern))
        return next_state

    def get(self, x, y, z):
        return self.substitution_system[(x, y, z)]

    def set(self, x, y, z, o):
        self.substitution_system[(x, y, z)] = o

