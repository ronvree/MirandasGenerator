from I.elementary_automata_values import Rule, State
from PIL import Image
import random as rnd

values = range(4)
size = 400

r = Rule(values)
r.randomize()

s = State(size, values)
s.set(int((len(s) - 1) / 2), 1)

# Print data
print(r)
print()
print(s)

# Keep track of states
states = list()
iterations = int(size / 2)
for i in range(iterations):
    states.append(s)
    s = r.next(s)
    # print(s)

# Visualize states

color_map = list()
rgb_range = range(256)
for i in values:
    color_map.append((rnd.choice(rgb_range), rnd.choice(rgb_range), rnd.choice(rgb_range)))

img = Image.new('RGB', (size, iterations), 'black')
pixels = img.load()
for state in range(iterations):
    for i in range(size):
        pixels[i, state] = color_map[states[state].get(i)]

# img.show()
img.save("result.png")
