import random

from I.ties.tie import Tie


class TestTie(Tie):

    def get_shirt_image(self, colors, seed):  # TODO -- less hacky
        shirt = Tie(self.length, self.width, colors, seed)
        img = shirt.get_pattern_image()
        pixels = img.load()

        self.states.reverse()

        slope = int(self.length / 10)
        mid = int(img.width / 2)
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


def random_rgb_color():
    return random.choice(range(256)), random.choice(range(256)), random.choice(range(256))


def random_rgb_colors(n):
    return [random_rgb_color() for _ in range(n)]


number_of_colors = 3
seed_bits = 2048

colors = random_rgb_colors(number_of_colors)

init_state_seed = int(random.getrandbits(seed_bits))
rule_seed = int(random.getrandbits(seed_bits))

shirt_init_state_seed = int(random.getrandbits(seed_bits))
shirt_rule_seed = int(random.getrandbits(seed_bits))


print(init_state_seed)
print(rule_seed)
print()
print(shirt_init_state_seed)
print(shirt_rule_seed)


# tie = Tie(200, 50, colors, 'random')
tie = TestTie(200, 50, colors, (init_state_seed, rule_seed))

image = tie.get_shirt_image(random_rgb_colors(number_of_colors),
                            (shirt_init_state_seed, shirt_rule_seed))

image.save("result.png")
