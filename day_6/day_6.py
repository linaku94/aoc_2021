import numpy as np

def fish(states, days):
    for i in range(days):
        off = states[0]
        for i in range(len(states)-1):
            states[i] = states[i+1]
        states[-1] = off
        states[-3] += off
    return(np.sum(states))


with open('input.txt', 'r') as file:
    init_state = np.loadtxt(file, delimiter = ',', dtype = np.int)

states = np.zeros((9), dtype = np.int)
for i in range(9):
    states[i] = np.count_nonzero(init_state == i)
days = 256

print(fish(states, days))