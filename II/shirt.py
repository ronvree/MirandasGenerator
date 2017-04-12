import random

from PIL import Image


class State:
    def __init__(self, width, height, values, seed=0):
        self.width = width
        self.height = height
        self.values = values
        self.cells = [[0] * self.height for _ in range(self.width)]

        if seed is 'random':
            self.randomize()

        # TODO -- read seed

    # TODO -- __str__(self)

    def randomize(self):
        for x in range(self.width):
            for y in range(self.height):
                self.cells[x][y] = random.choice(self.values)

    def get_image(self, colors):
        img = Image.new('RGB', (self.width, self.height), 'grey')
        pixels = img.load()
        for x in range(self.width):
            for y in range(self.height):
                pixels[x, y] = colors[self.get(x, y)]
        return img

    def get(self, x, y):
        return self.cells[x][y]

    def set(self, x, y, value):  # TODO -- Error if value is not in self.values
        self.cells[x][y] = value


class Rule:
    def __init__(self, values, seed, neighbourhood='wolfram'):
        self.values = values
        self.substitution_system = dict()  # TODO

        if neighbourhood is 'wolfram':
            base = len(values)
            self.neighbourhood = [(1, 0), (0, 1), (0, -1), (-1, 0), (0, 0)]

            # Nice
            i = 0
            for v in values:
                for w in values:
                    for x in values:
                        for y in values:
                            for z in values:
                                self.substitution_system[(v, w, x, y, z)] = int(
                                    (seed % pow(base, i + 1)) / pow(base, i))
                                i += 1

                                # TODO -- other neighbourhoods

    def randomize(self):
        for s in self.substitution_system:
            self.substitution_system[s] = random.choice(self.values)

    def next(self, state):
        next_state = State(state.width, state.height, self.values)
        for x in range(state.width):
            for y in range(state.height):
                neighbourhood = tuple([state.get((x + n[0]) % state.width,
                                                 (y + n[1]) % state.height) for n in self.neighbourhood])
                next_state.set(x, y, self.substitution_system.get(neighbourhood))
        return next_state


class Shirt:
    def __init__(self, width, height, values, seed, iterations=100, neighbourhood='wolfram'):
        self.width = width
        self.height = height
        self.values = values
        self.state = State(width, height, values, seed[0])
        self.rule = Rule(values, seed[1], neighbourhood)

        for i in range(iterations):
            self.state = self.rule.next(self.state)

    def get_image(self): # TODO -- shape shirt
        img = Image.new('RGB', (self.width, self.height), 'grey')
        pixels = img.load()
        for x in range(self.width):
            for y in range(self.height):
                pixels[x, y] = self.state.get(x,y)
        return img

########################

def random_rgb_color():
    return random.choice(range(256)), random.choice(range(256)), random.choice(range(256))


def random_rgb_colors(n):
    return [random_rgb_color() for _ in range(n)]


nr_of_colors = 2
iterations = 50
colors = random_rgb_colors(nr_of_colors)
# colors = [(255,255,255),(0,0,0)]

s = State(100, 100, range(nr_of_colors))
s.set(49, 49, 1)
# s.randomize()
r = Rule(range(nr_of_colors), 0)
r.randomize()

for _ in range(iterations):
    s = r.next(s)

img = s.get_image(colors)

img.save("result.png")

