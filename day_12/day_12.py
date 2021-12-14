import numpy as np
import copy
import random
import itertools
def routes(cons):
    # paths = np.load('partial_paths.txt.npy')
    # paths = list(paths)
    paths = []
    for i in range(5000000):
        connections = copy.deepcopy(cons)
        for key in connections.keys():
            random.shuffle(connections[key])
        step = 'start'
        visited = []
        path = ''
        while step != 'end':
            try:
                step = connections[step][0]
            except:
                break
            if step.islower():
                for key in connections.keys():
                    if step in connections[key]:
                        connections[key].remove(step)
            visited.append(step)
            path = path + step
        if path not in paths and 'end' in path:
            paths.append(path)
    return(paths)
        
connections = {}
with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        line = line.split('-')
        if line[0] in connections.keys():
            connections[line[0]].append(line[1])
        else:
            connections[line[0]] = [line[1]]
        if line[1] in connections.keys():
            connections[line[1]].append(line[0])
        else:
            connections[line[1]] = [line[0]]

for val in connections.values():
    if 'start' in val:
        val.remove('start')
del connections['end']
print(connections)

paths = routes(connections)
print(len(paths))

# paths = np.array(paths)
# np.save('partial_paths.txt', paths)
