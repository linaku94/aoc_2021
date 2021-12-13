import numpy as np

def light(matrix, i,k):
    add = np.ones((3,3))
    add[1,1] = 0
    matrix[i-1:i+2, k-1:k+2] += add
    return(matrix)

def propagate_lights(matrix, days):
    num_flashes = 0
    for day in range(days):
        matrix +=1
        test = matrix[1:-1, 1:-1] >=10
        flashed = []
        while test.any():
            for i in range(1,11):
                for k in range(1,11):
                    if matrix[i,k] >= 10 and (i,k) not in flashed:
                        light(matrix, i,k)
                        flashed.append((i,k))
                        num_flashes+=1
            for tup in flashed:
                matrix[tup] = 0
            test = matrix[1:-1, 1:-1] >=10
        center = matrix[1:-1,1:-1] == 0
        if center.all():
            print('synchronized')
            return num_flashes, day+1
    return num_flashes

matrix = np.zeros((12,12))
with open('input.txt', 'r') as file:
    for i,line in enumerate(file):
        line = line.rstrip()
        for k, number in enumerate(line):
            matrix[i+1,k+1] = str(number)

print(propagate_lights(matrix, 1000))