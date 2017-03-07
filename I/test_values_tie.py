from I.elementary_automata_values import Rule, State
from PIL import Image
import random as rnd


class Tie:

    def __init__(self, length, nr_of_colors=4, rule=None):

        # Set tie instance variables
        self.length = length
        self.values = range(nr_of_colors)
        if rule is None:
            self.rule = Rule(self.values)
            self.rule.randomize()
        else:
            self.rule = rule

        # Set constants
        iterations = length
        width = 1 + length * 2
        mid = int(width/2)

        # Set initial state
        s = State(width, self.values)
        s.set(mid, rnd.choice(self.values[1:]))
        s.randomize()

        # Generate pattern
        self.states = list()
        for iteration in range(iterations):
            self.states.append(s)
            s = self.rule.next(s)

        # Determine colors
        color_map = [0] * len(self.values)
        rgb = range(255)
        for value in self.values:
            color_map[value] = (rnd.choice(rgb), rnd.choice(rgb), rnd.choice(rgb))

        # Draw tie
        self.img = Image.new('RGB', (width, iterations), 'grey')
        pixels = self.img.load()

        self.states.reverse()

        slope = int(length/10)
        bottom_part_length = int(length / slope)

        bottom_layers = range(length - bottom_part_length, length)
        top_layers = range(length - bottom_part_length)

        offset = bottom_part_length
        for layer in bottom_layers:
            for i in range(mid - offset, mid + offset):
                pixels[i, layer] = color_map[self.states[layer].get(i)]
            offset -= 1

        counter, offset = 0,  0
        for layer in top_layers:
            for i in range(mid - offset, mid + offset):
                pixels[i, layer] = color_map[self.states[layer].get(i)]
            if counter % slope == 0:
                offset += 1
            counter += 1

    def save(self, file_name):
        self.img.save(file_name)


# Make tie

ties = 20

for i in range(ties):
    tie = Tie(200, 4)
    tie.save("ties_demo/tie" + str(i) + ".png")

