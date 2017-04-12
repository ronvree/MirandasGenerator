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

r = Rule(90)

size = 140
s = State(size)
s.set(int((len(s) - 1)/2), True)

run = AutomatonRun(r, s, int(size/2))

print(r)
run.get_image().save("test.png")

