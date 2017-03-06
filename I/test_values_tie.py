from I.elementary_automata_values import Rule, State
from PIL import Image
import random as rnd

# values = range(4)
# size = 301
# mid = int(size/2)
#
# r = Rule(values)
# r.randomize()
#
# s = State(size, values)
# s.set(int((len(s) - 1) / 2), 1)

# Print data
# print(r)
# print()
# print(s)

# Keep track of states
# states = list()
# iterations = mid
# for i in range(iterations):
#     states.append(s)
#     s = r.next(s)


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

        slope = int(length/6)
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

tie = Tie(200, 3)
tie.save("tie.png")














#
# width = 31
#
# bottom_part_length = int(width/2)
#
# for i in range(bottom_part_length):
#     for j in range(mid - i):
#         states[i].set(j, 0)
#     for j in range(mid + i, size):
#         states[i].set(j, 0)
#
# offset = bottom_part_length
# counter = 0
# for i in range(bottom_part_length, iterations):
#     for j in range(mid - offset):
#         states[i].set(j, 0)
#     for j in range(mid + offset, size):
#         states[i].set(j, 0)
#     if counter % int(iterations/16) == 0:
#         offset -= 1
#     counter += 1
#
# states.reverse()
#
# # Visualize states
#
# white = (255, 255, 255)
#
# color_map = [0] * (max(values) + 1)  # TODO jezus wat lelijk
# rgb = range(255)
# for value in values:
#     color_map[value] = (rnd.choice(rgb), rnd.choice(rgb), rnd.choice(rgb))
#
#
# # color_map[0] = (255, 255, 255)
# # color_map[1] = (255, 0, 0)
# # color_map[2] = (0, 255, 0)
# # color_map[3] = (0, 0, 255)
#
# img = Image.new('RGB', (size, iterations), 'black')
# pixels = img.load()
# for state in range(iterations):
#     for i in range(size):
#         pixels[i, state] = color_map[states[state].get(i)]
#
# img.save("tie.png")
