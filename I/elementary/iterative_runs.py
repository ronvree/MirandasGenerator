import os
from PIL import Image

from I.elementary.automata_simple import Rule, State


class IterationRun:

    def __init__(self, rule_indices, size, iterations):
        self.size = size
        self.iterations = iterations
        self.rules = [Rule(i) for i in rule_indices]
        state = State(size)
        state.set(int((size - 1) / 2), True)
        self.states = [state]

        for iteration in range(iterations):
            for rule in self.rules:
                state = rule.next(state)
                self.states.append(state)

    def get_image(self):
        img = Image.new('RGB', (self.size, len(self.states)), 'white')
        pixels = img.load()
        for y in range(len(self.states)):
            for x in range(self.size):
                if self.states[y].get(x):
                    pixels[x, y] = (0, 0, 0)
                else:
                    pixels[x, y] = (255, 255, 255)
        return img


def generate_2nd_degree_iteration_runs(size, indices):
    for i in indices:
        for j in indices:
            print("{}_{}".format(i, j))
            run = IterationRun([i, j], size, int(size/2))
            run.get_image().save(os.getcwd() + "\patterns_iter_2\pattern_{}_{}.png".format(i, j))


def generate_3rd_degree_iteration_runs(size, indices):
    for i in indices:
        for j in indices:
            for k in indices:
                print("{}_{}_{}".format(i, j, k))
                run = IterationRun([i, j, k], size, int(size/2))
                run.get_image().save(os.getcwd() + "\patterns_iter_3\pattern_{}_{}_{}.png".format(i, j, k))

generate_3rd_degree_iteration_runs(200, [110, 73, 30, 101, 16, 22, 161, 60, 105])

# indices = [22, 110]
# indices = [110, 73, 30, 101]
# size = 1000
# IterationRun(indices, size, int(size/2)).get_image().show()

