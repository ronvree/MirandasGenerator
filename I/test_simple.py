from I.elementary_automata_simple import Rule, State

r = Rule(30)
print(r)

print()

size = 140
s = State(size)
s.set(int((len(s) - 1)/2), True)
print(s)

for i in range(int(size/2)):
    s = r.next(s)
    print(s)
