def polymerization(old_state, rules_split, steps):
    for step in range(steps):
        new_state = {x: 0 for x in old_state.keys()}
        for key in old_state.keys():
            np0 = key[0]+rules_split[key]
            np1 = rules_split[key] + key[1]
            new_state[np0] += old_state[key]
            new_state[np1] += old_state[key]
        old_state = new_state
    elems = {i: 0 for i in set("".join([i for i in new_state.keys()]))}
    for key in new_state.keys():
        for val in key:
            elems[val] += new_state[key]
    elems = {key: value // 2 for key, value in elems.items()}
    return elems


with open('input.txt', 'r') as file:
    lines = file.readlines()
    polymer = lines[0].rstrip()
    state = {}
    rules = {}
    for line in lines[2:]:
        values = line.rstrip().split(" -> ")
        rules[values[0]] = values[1]
        state[values[0]] = 1 if values[0] in polymer else 0

result = polymerization(state, rules, 40)
print(max(result.values())-min(result.values()) + 1)