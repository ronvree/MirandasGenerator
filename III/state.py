import random


class State:

    def __init__(self, size):
        self.size = size
        self.cells = size * [0]

    def __str__(self):
        return ' '.join([str(cell) for cell in self.cells])

    def __len__(self):
        return self.size

    def get(self, i):
        return self.cells[i]

    def set(self, i, value):
        self.cells[i] = value


class RangedState(State):   # TODO -- check for values under 0?

    def __init__(self, size, number_of_values):
        super().__init__(size)
        self.number_of_values = number_of_values
        self.values = range(0, number_of_values)

    def randomize(self):
        for i in range(self.size):
            self.cells[i] = random.choice(self.values)

    def set(self, i, value):
        if value < self.number_of_values:
            self.cells[i] = value
        else:
            raise ValueRangeException(value, self.number_of_values - 1)

    def get_number_of_values(self):
        return self.number_of_values


class ElementaryState(RangedState):

    def __init__(self, size):
        super().__init__(size, 2)


class ValueRangeException(Exception):

    def __init__(self, value, max_value):
        self.value = value
        self.max = max_value

    def __str__(self):
        return "Can't set cell to {}. Max allowed value is {}!".format(self.value, self.max)

