import numpy as np

data_res = []
data_in = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        line = line.split(' | ')
        data_res.append(line[1].split(' '))
        data_in.append(line[0].split(' '))

nums = np.zeros((len(data_in), 10), dtype = np.int)
for i, entry in enumerate(data_in):
    nums[i,:] = [len(s) for s in entry]
sum = np.sum([np.count_nonzero([nums == i]) for i in [2,4,3,7]])
print(sum)

def decode(data, read):
    sets = []
    for data_point in data:
        s = set([d for d in data_point])
        if len(data_point) == 2:
            one = s
        elif len(data_point) == 3:
            seven = s
        elif len(data_point) == 4:
            four = s
        elif len(data_point) == 7:
            eight = s
        else:
            sets.append(s)
    
    for s in sets:
        if len(s) == 6:
            if four <= s:
                nine = s
                sets.remove(s)
    for s in sets:
        if len(s) == 6:
            if seven <= s:
                zero = s
                sets.remove(s)

    for s in sets:
        if len(s) == 6:
            six = s
            sets.remove(s)


    for s in sets:
        if s <= six:
            five = s
            sets.remove(s)
    
    for s in sets:
        if s <= nine:
            three = s
            sets.remove(s)

    two = sets[0]
    sets.remove(two)
    
    sum = ''
    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
    for data_point in read:
        s = set([d for d in data_point])
        for i, number in enumerate(numbers):
            if s == number:
                sum = sum + str(i)

    return(int(sum))

sum = 0
for i, data in enumerate(data_in):
    sum += decode(data, data_res[i])

print(sum)

