import copy
import random

from III.pattern import RangedPattern, red_heart_pattern
from III.rule import SubstitutionSystem, Rule
from III.runs import AutomatonRun
from III.state import RangedState


class SubstitutionSystemGeneratorV2:

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
                            value_subs[n3].add((n1, n2, value_counter))
                        else:
                            value_subs[n3] = {(n1, n2, value_counter)}
                        n3 = value_counter
                        value_counter += 1
                        new_pattern.set(layer_index + 1, i + 2, n3)
                        substitutions.set((n1, n2, n3), v)
                    else:
                        substitutions.set((n1, n2, n3), v)

            self.substitutions = substitutions
            self.pattern = new_pattern
            self.value_mapping = value_subs

            # Get all unmapped neighbourhoods grouped by leftmost element
            pos_nbhs_by_left_val = dict()
            vals = range(value_counter)
            for v in vals:
                pos_nbhs_by_left_val[v] = set()
            for i in vals:
                for j in vals:
                    for k in vals:
                        pos_nbhs_by_left_val[i].add((i, j, k))
                pos_nbhs_by_left_val[i] -= substitutions.mapped_neighbourhoods()

            # Pick one arbitrary nbh
            nbh = None
            for i in pos_nbhs_by_left_val.keys():
                if len(pos_nbhs_by_left_val.get(i)) > 0:
                    nbh = random.choice(list(pos_nbhs_by_left_val.get(i)))
                    break
            # If there are no unused neighbourhoods, we're done
            if nbh is None:
                return

            # Iterate through the top layer and map neighbourhoods
            nbhs_left = 0
            for key in pos_nbhs_by_left_val.keys():
                nbhs_left += len(pos_nbhs_by_left_val[key])

            orig_nbhs_left = nbhs_left

            # while nbhs_left > (new_pattern.get_number_of_layers() - 1) * 2 + 1:
            #     for i in range((new_pattern.get_number_of_layers() - 1) * 2 + 1):
            #         v = new_pattern.get(new_pattern.get_number_of_layers() - 1, i)
            #         (x, y, z) = nbh
            #         substitutions.set(nbh, v)
            #         pos_nbhs_by_left_val[x].remove(nbh)
            #         nbh = random.choice(list(pos_nbhs_by_left_val[z]))
            #
            #     nbhs_left = 0
            #     for key in pos_nbhs_by_left_val.keys():
            #         nbhs_left += len(pos_nbhs_by_left_val[key])

            while nbhs_left > orig_nbhs_left/1.5:
                for i in range((new_pattern.get_number_of_layers() - 1) * 2 + 1):
                    v = new_pattern.get(new_pattern.get_number_of_layers() - 1, i)
                    (x, y, z) = nbh
                    substitutions.set(nbh, v)
                    pos_nbhs_by_left_val[x].remove(nbh)
                    nbh = random.choice(list(pos_nbhs_by_left_val[z]))

                nbhs_left = 0
                for key in pos_nbhs_by_left_val.keys():
                    nbhs_left += len(pos_nbhs_by_left_val[key])

            for v in pos_nbhs_by_left_val.keys():
                for nbh in pos_nbhs_by_left_val[v]:
                    substitutions.set(nbh, random.choice(vals))


        else:
            self.substitutions = SubstitutionSystem()
            self.pattern = RangedPattern(0)
            self.value_mapping = dict()


pattern = red_heart_pattern()

algorithm = SubstitutionSystemGeneratorV2(pattern)
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

init_state = RangedState(400, nr_of_values)
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
    for (a, b, c) in subs:
        color_dict[c] = color_dict[v]

run = AutomatonRun(rule, init_state, 400)
run.get_image(color_dict).save("test.png")
