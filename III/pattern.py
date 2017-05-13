import random


class Pattern:
    def __init__(self, number_of_layers):
        self.layers = [[]] * number_of_layers
        for i in range(number_of_layers):
            self.layers[i] = [0] * (i * 2 + 1)

    def __str__(self):
        layer_indices = list(range(len(self.layers)))
        layer_indices.reverse()
        result = ""
        for i in layer_indices:
            result += ("   " * (len(self.layers) - i - 1)) + str(self.layers[i]) + "\n"
        return result

    def get_number_of_layers(self):
        return len(self.layers)

    def get(self, layer, index):
        return self.layers[layer][index]

    def set(self, layer, index, value):
        self.layers[layer][index] = value


class RangedPattern(Pattern):
    def __init__(self, number_of_layers):
        super().__init__(number_of_layers)
        self.number_of_values = 1
        self.values = [0]

    def randomize(self):
        for layer in self.layers:
            for i in range(len(layer)):
                layer[i] = random.choice(self.values)

    def get_number_of_values(self):
        return self.number_of_values

    def set(self, layer, index, value):
        if value >= self.number_of_values:
            self.number_of_values = value + 1
            self.values = range(self.number_of_values)
        super().set(layer, index, value)


'''
    Pre-defined patterns
'''


def elementary_heart_pattern():
    pattern = RangedPattern(6)
    # Layer 0
    pattern.set(0, 0, 1)
    # Layer 1
    pattern.set(1, 0, 1)
    pattern.set(1, 2, 1)
    # Layer 2
    pattern.set(2, 0, 1)
    pattern.set(2, 4, 1)
    # Layer 3
    pattern.set(3, 0, 1)
    pattern.set(3, 6, 1)
    # Layer 4
    pattern.set(4, 0, 1)
    pattern.set(4, 8, 1)
    pattern.set(4, 1, 1)
    pattern.set(4, 7, 1)
    pattern.set(4, 4, 1)
    # Layer 5
    for i in range(11):
        pattern.set(5, i, 1)
    return pattern


def red_heart_pattern():
    nr_of_layers = 6
    pattern = RangedPattern(nr_of_layers)
    for layer in range(nr_of_layers):
        for i in range(layer * 2 + 1):
            if i == 0 or i == (layer * 2):
                pattern.set(layer, i, 1)
            else:
                pattern.set(layer, i, 2)
    for i in range(11):
        pattern.set(5, i, 1)
    pattern.set(4, 4, 1)
    pattern.set(4, 1, 1)
    pattern.set(4, 7, 1)
    return pattern

