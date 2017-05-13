import copy
import os
from PIL import Image

from I.elementary.automata_simple import Rule, State


class AutomatonRun:

    def __init__(self, rule, init_state, iterations):
        self.rule = rule
        self.init_state = init_state
        self.iterations = iterations
        self.states = list()
        self.states.append(init_state)
        state = init_state
        for i in range(iterations):
            state = rule.next(state)
            self.states.append(state)

    def get_image(self):
        img = Image.new('RGB', (len(self.init_state), self.iterations), 'white')
        pixels = img.load()
        for y in range(self.iterations):
            for x in range(len(self.init_state)):
                if self.states[y].get(x):
                    pixels[x, y] = (0, 0, 0)
                else:
                    pixels[x, y] = (255, 255, 255)
        return img


def generate_all_patterns(size):
    init_state = State(size)
    init_state.set(int((len(init_state) - 1) / 2), True)

    for rule_index in range(pow(2, 8)):
        run = AutomatonRun(Rule(rule_index), copy.deepcopy(init_state), int(size / 2))
        run.get_image().save(os.getcwd() + "\patterns\pattern{}.png".format(rule_index))


def show_pattern_of_rule(index):
    size = 1000
    iterations = int(size / 2)
    init_state = State(size)
    init_state.set(int((len(init_state) - 1) / 2), True)
    run = AutomatonRun(Rule(index), init_state, iterations)
    run.get_image().show()

