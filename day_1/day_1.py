def depth_increases(depths):            ### check if depth increases
    counter = 0
    for i, d in enumerate(depths[1:]):
        if d > depths[i]:
            counter +=1
    return counter

def window_sum(depths):                ### sum windows
    new_depths = []
    for i, d in enumerate(depths[:-2]):
        new_depths.append(sum(depths[i:i+3]))
    return new_depths

filename = 'input.txt'

depths = []
with open(filename, 'r') as file:
    for line in file:
        depths.append(int(line.rstrip()))

### first part
print(f'first part: {depth_increases(depths)}')

## second part
print(f'second part: {depth_increases(window_sum(depths))}')
