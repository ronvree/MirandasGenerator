import random

from III.runs import AutomatonRun
from III.state import RangedState
from IV.rule import Rule

width = 200
iterations = 200
nr_of_values = 2
relative_nbh = (-1, 1, 0)

init_state = RangedState(width, nr_of_values)
init_state.randomize()

rule = Rule(nr_of_values, relative_nbh)
rule.randomize()

run = AutomatonRun(rule, init_state, iterations)


def random_rgb_color():
    return random.choice(range(256)), random.choice(range(256)), random.choice(range(256))


def random_rgb_colors(n):
    return [random_rgb_color() for _ in range(n)]

color_map = random_rgb_colors(nr_of_values)

img = run.get_image(color_map)

img.save("test.png")
