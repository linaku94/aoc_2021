import numpy as np 

def fuel(init_state):
    cost = [np.sum(np.abs(init_state-i)) for i in range(len(init_state))]
    return min(cost)

### brute force it just because I can!
def more_fuel(init_state):
    fuel_cost = np.zeros_like(init_state, dtype = np.int)
    for i in range(len(init_state)):
        fuel_cost[i] += np.sum([np.sum(np.arange(1, np.abs(init_state[k]-i)+1)) for k in range(len(init_state))])
    return min(fuel_cost)

def calc_fuel(init_state):
    mean = int(np.mean(init_state))
    cost = [(np.sum(np.arange(1,np.abs(init_state[i]-mean)+1))) for i in range(len(init_state))]
    return np.sum(cost)

with open('input.txt', 'r') as file:
    init_state = np.loadtxt(file, delimiter = ',', dtype = np.int)

print(fuel(init_state))
print(calc_fuel(init_state))
