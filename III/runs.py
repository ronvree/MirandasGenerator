from PIL import Image


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

    def get_image(self, color_dict):
        img = Image.new('RGB', (len(self.init_state), self.iterations), 'white')
        pixels = img.load()
        for y in range(self.iterations):
            for x in range(len(self.init_state)):
                color = color_dict[self.states[y].get(x)]
                if color is not None:
                    pixels[x, y] = color
                else:
                    pixels[x, y] = (0, 0, 0)
        return img


class IterationRun:

    def __init__(self, rules, init_state, iterations):
        self.size = len(init_state)
        self.iterations = iterations
        self.rules = rules
        self.states = [init_state]
        state = init_state

        for iteration in range(iterations):
            for rule in self.rules:
                state = rule.next(state)
                self.states.append(state)

    def get_image(self, color_dict):
        img = Image.new('RGB', (self.size, len(self.states)), 'white')
        pixels = img.load()
        for y in range(len(self.states)):
            for x in range(self.size):
                color = color_dict[self.states[y].get(x)]
                if color is not None:
                    pixels[x, y] = color
                else:
                    pixels[x, y] = (0, 0, 0)
        return img

