import numpy as np 

def fuel(init_state):
    fuel_cost = np.zeros_like(init_state, dtype = np.int)
    for i in range(len(init_state)):
        fuel_cost[i] = np.sum(np.abs(init_state-i))
    # return [fuel_cost == min(fuel_cost)]
    return min(fuel_cost)

def more_fuel(init_state):
    fuel_cost = np.zeros_like(init_state, dtype = np.int)
    for i in range(len(init_state)):
        for k, state in enumerate(init_state):
            fuel_cost[i] += np.sum(np.arange(1, np.abs(state-i)+1))
    # return(np.where(fuel_cost == min(fuel_cost)))
    return min(fuel_cost)

with open('input.txt', 'r') as file:
    init_state = np.loadtxt(file, delimiter = ',', dtype = np.int)

test_state = np.array([16,1,2,0,4,2,7,1,2,14], dtype = np.int)

print(more_fuel(test_state))
