import numpy as np


def lines(x,y, diagonals = False):
    coordinates = np.zeros((1000,1000), dtype = np.int)
    for i, test in enumerate(x[:,0]):
        if x[i,0] == x[i,1]:
            coordinates[x[i,0], y[i,:].min():y[i,:].max()+1] += 1
        elif y[i,0] == y[i,1]:
            coordinates[x[i,:].min():x[i,:].max()+1, y[i,0]] += 1
        elif diagonals:
            X = np.arange(x[i,:].min(),x[i,:].max()+1)
            Y = np.arange(y[i,:].min(),y[i,:].max()+1)
            if x[i,0] > x[i,1]:
                X = np.flip(X)
            if y[i,0] > y[i,1]:
                Y = np.flip(Y)
            for i, x_cor in enumerate(X):
                coordinates[x_cor, Y[i]] +=1
    return coordinates


x_cor = np.zeros((500,2), dtype = np.int)
y_cor = np.zeros_like(x_cor, dtype = np.int)
with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.rstrip()
        P = line.split(' -> ')
        A = P[0].split(',')
        B = P[1].split(',')
        x_cor[i,0] = int(A[0])
        x_cor[i,1] = int(B[0])
        y_cor[i,0] = int(A[1])
        y_cor[i,1] = int(B[1])

coordinates = lines(x_cor, y_cor, diagonals = True)
print(np.sum(coordinates>=2))
