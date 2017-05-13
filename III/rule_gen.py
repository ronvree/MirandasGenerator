import copy

from III.pattern import RangedPattern, red_heart_pattern
from III.rule import SubstitutionSystem, Rule
from III.runs import AutomatonRun
from III.state import RangedState


class SubstitutionSystemGeneratorV1:

    def __init__(self, pattern):
        if pattern.get_number_of_layers() > 0:
            substitutions = SubstitutionSystem()
            new_pattern = copy.deepcopy(pattern)

            value_subs = dict()
            value_counter = pattern.get_number_of_values()

            for layer_index in range(pattern.get_number_of_layers() - 1):

                for i in range(2 * layer_index + 1):
                    n1 = new_pattern.get(layer_index + 1, i)
                    n2 = new_pattern.get(layer_index + 1, i + 1)
                    n3 = new_pattern.get(layer_index + 1, i + 2)
                    v = new_pattern.get(layer_index, i)

                    if (n1, n2, n3) in substitutions.mapped_neighbourhoods() and substitutions.get((n1, n2, n3)) != v:
                        if n3 in value_subs.keys():
                            value_subs[n3].add(value_counter)
                        else:
                            value_subs[n3] = {value_counter}
                        n3 = value_counter
                        value_counter += 1
                        new_pattern.set(layer_index + 1, i + 2, n3)
                        substitutions.set((n1, n2, n3), v)
                    else:
                        substitutions.set((n1, n2, n3), v)

            self.substitutions = substitutions
            self.pattern = new_pattern
            self.value_mapping = value_subs

        else:
            self.substitutions = SubstitutionSystem()
            self.pattern = RangedPattern(0)
            self.value_mapping = dict()


pattern = red_heart_pattern()

algorithm = SubstitutionSystemGeneratorV1(pattern)
substitutions = algorithm.substitutions
new_pattern = algorithm.pattern
val_sub = algorithm.value_mapping

print(pattern)
print(new_pattern)
print(val_sub)

print(substitutions)


nr_of_values = new_pattern.get_number_of_values()
rule = Rule(nr_of_values)
rule.randomize()
for n in substitutions.mapped_neighbourhoods():
    rule.set(n, substitutions.get(n))

init_state = RangedState(100, nr_of_values)
init_state.randomize()


for i in range(11):
    init_state.set(i, new_pattern.get(5, i))

color_dict = dict()
color_dict[0] = (200, 200, 200)
color_dict[1] = (0, 0, 0)
color_dict[2] = (255, 0, 0)
color_dict[3] = (0, 255, 0)
color_dict[4] = (0, 0, 255)
color_dict[5] = (255, 255, 0)

for v in val_sub.keys():
    subs = val_sub[v]
    for sub in subs:
        color_dict[sub] = color_dict[v]

run = AutomatonRun(rule, init_state, 100)
run.get_image(color_dict).save("test.png")


