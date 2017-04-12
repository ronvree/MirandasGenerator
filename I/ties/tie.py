import random
from PIL import Image


class State:

    def __init__(self, size, values, seed=0):
        self.values = values
        self.cells = size * [0]
        if seed == 'random':
            self.randomize()
        elif seed != 0:
            base = len(self.values)
            for i in range(size):
                self.cells[size - i - 1] = int((seed % pow(base, i+1))/pow(base, i))

    def __str__(self):
        return ' '.join([str(cell) for cell in self.cells])

    def __len__(self):
        return len(self.cells)

    def randomize(self):
        for i in range(len(self.cells)):
            self.cells[i] = random.choice(self.values)

    def get(self, i):
        return self.cells[i]

    def set(self, i, val):  # TODO -- error if val is not in self.values
        self.cells[i] = val


class Rule:

    def __init__(self, values, seed):
        self.substitution_system = dict()
        self.values = values
        base = len(values)
        if seed == 'random':
            i = 0
            for x in self.values:
                for y in self.values:
                    for z in self.values:
                        self.substitution_system[(x, y, z)] = 0
                        i += 1
            self.randomize()
        else:
            i = 0
            for x in self.values:
                for y in self.values:
                    for z in self.values:
                        self.substitution_system[(x, y, z)] = int((seed % pow(base, i + 1)) / pow(base, i))
                        i += 1

    def __str__(self):
        return '\n'.join([str(' '.join([str(c) for c in s])) + " -> "
                          + str(self.substitution_system[s]) for s in self.substitution_system])

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


class Tie:

    def __init__(self, length, width, colors, seed):
        self.length = length
        self.width = width
        self.colors = colors

        self.init_state_size, mid = length * 2 + 1,  length
        color_values = range(len(colors))

        if seed == 'random':
            self.init_state = State(self.init_state_size, color_values, seed)
            self.rule = Rule(color_values, seed)
        else:
            self.init_state = State(self.init_state_size, color_values, seed[0])
            self.rule = Rule(color_values, seed[1])

        self.states = list()
        s = self.init_state
        for iteration in range(length):
            self.states.append(s)
            s = self.rule.next(s)

    def get_pattern_image(self):
        img = Image.new('RGB', (self.init_state_size, self.length), 'grey')
        pixels = img.load()
        for state in range(self.length):
            for i in range(self.init_state_size):
                pixels[i, state] = self.colors[self.states[state].get(i)]
        return img

    def get_image(self):
        img = Image.new('RGB', (self.width, self.length), 'grey')
        pixels = img.load()

        self.states.reverse()

        slope = int(self.length / 10)
        mid = int(self.width / 2)
        bottom_part_length = int(self.length / slope)

        bottom_layers = range(self.length - bottom_part_length, self.length)
        top_layers = range(self.length - bottom_part_length)

        offset = bottom_part_length
        for layer in bottom_layers:
            for i in range(mid - offset, mid + offset):
                pixels[i, layer] = self.colors[self.states[layer].get(i)]
            offset -= 1

        counter, offset = 0, 0
        for layer in top_layers:
            for i in range(mid - offset, mid + offset):
                pixels[i, layer] = self.colors[self.states[layer].get(i)]
            if counter % slope == 0:
                offset += 1
            counter += 1

        self.states.reverse()

        return img

    def set_colors(self, colors):
        if len(colors) == len(self.colors):
            self.colors = colors
        else:
            print("Number of colors does not match!")
            raise Exception()

