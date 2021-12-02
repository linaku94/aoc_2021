import time
from day_1 import depth_increases, window_sum

# runs = int(input('number of runs: '))
runs = 1000

filename = 'input.txt'

depths = []
with open(filename, 'r') as file:
    for line in file:
        depths.append(int(line.rstrip()))

start = time.monotonic()
for i in range(runs):
    depth_increases(window_sum(depths))

print((time.monotonic()-start)/ runs)
