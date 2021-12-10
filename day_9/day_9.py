import numpy as np
from scipy.ndimage import label

def neighbours(m, i, k):
    return(np.array([m[i-1,k], m[i+1,k], m[i,k-1], m[i,k+1]], dtype = np.int))


def risk_level(matrix):
    dim = matrix.shape[0]
    matrix = np.pad(matrix,1, constant_values = 9)
    sum = 0
    for i in range(1,dim+1):
        for k in range(1, dim+1):
            num = matrix[i,k]
            check = num < neighbours(matrix, i,k)
            if check.all():
                sum += num+1
    return sum


matrix = np.zeros((100,100), dtype=np.int)
with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.rstrip()
        for k, num in enumerate(line):
            matrix[i,k] = int(num)

### first part
print(f'risk level: {risk_level(matrix)}')

### second part 
mask = matrix != 9
mask, nums = label(mask)
basins = np.array([np.count_nonzero(mask == i+1) for i in range(nums)])
result = np.sort(basins)[-3:]
print(f'largest basins {np.prod(result)}')  

