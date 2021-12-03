import copy 

def count_bits(numbers, k):
    c0 = 0
    for num in numbers:
        if int(num[k]) == 0:
            c0+=1
    return(c0, len(numbers)-c0)


def power(c0, c1):
    gamma = ''
    epsilon = ''
    for i, bit in enumerate(c0):
        if bit > c1[i]:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        else:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
    print(int(gamma, 2) * int(epsilon, 2))

def oxygen(numbers):
    for k in range(len(numbers[0])):
        c0, c1 = count_bits(numbers, k)
        if c0 > c1:
            for num in copy.deepcopy(numbers):
                if int(num[k]) == 1:
                    numbers.remove(num)
        else:
            for num in copy.deepcopy(numbers):
                if int(num[k]) == 0:
                    numbers.remove(num)
        if len(numbers) == 1:
            break
    return(int(numbers[0],2))

def co2(numbers):
    for k in range(len(numbers[0])):
        c0, c1 = count_bits(numbers, k)
        if c0 > c1:
            for num in copy.deepcopy(numbers):
                if int(num[k]) == 0:
                    numbers.remove(num)
        else:
            for num in copy.deepcopy(numbers):
                if int(num[k]) == 1:
                    numbers.remove(num)
        if len(numbers) == 1:
            break
    return(int(numbers[0],2))

numbers = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        numbers.append(line)

c0 = []
c1 = []
for i in range(len(numbers[0])):
    a,b = count_bits(numbers, i)
    c0.append(a)
    c1.append(b)

power(c0, c1)

print(co2(copy.deepcopy(numbers))*oxygen(numbers))