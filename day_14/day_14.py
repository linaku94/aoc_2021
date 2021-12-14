import copy 

def polymerization(old_state, rules, steps):
    for step in range(steps):
        state = copy.deepcopy(old_state)
        for key in state.keys():
            state[key] = 0
        for key in old_state.keys():
            pols = list(key)
            np0 = pols[0]+rules[key]
            np1 = rules[key] + pols[1]
            state[np0] += old_state[key]
            state[np1] += old_state[key]
        old_state = copy.deepcopy(state)
    return state

def elements(state):
    elements = {}
    for key in state.keys():
        vals = list(key)
        for val in vals:
            if val in elements:
                elements[val] += state[key]
            else:
                elements[val] = state[key]
    for key in elements.keys():
        if elements[key]%2 == 0:
            elements[key] = int(elements[key]/2)
        else:
            elements[key] = int((elements[key]+1)/2)
    return elements

with open('input.txt', 'r') as file:
    lines = file.readlines()
    polymer = lines[0].rstrip()
    state = {}
    rules = {}
    for line in lines[2:]:
        line = line.rstrip()
        values = line.split(' -> ')
        rules[values[0]] = values[1]
        if values[0] in polymer:
            state[values[0]] = 1
        else:
            state[values[0]] = 0

state = polymerization(state, rules, 40)
result = elements(state)
print(max(result.values())-min(result.values()))
