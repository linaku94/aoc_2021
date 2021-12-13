import numpy as np
import matplotlib.pyplot as plt

def fold(paper, axes, sizes):
    for i, ax in enumerate(axes):
        if ax == 0:
            bottom = np.flip(paper[sizes[i]+1:,:], axis = ax)
            paper = paper[:sizes[i],:] + bottom
        else:
            right = np.flip(paper[:,sizes[i]+1:], axis = ax)
            paper = paper[:,:sizes[i]] + right
    return paper

dots = []
axes = []
sizes = []
with open('input.txt', 'r') as file:
    for line in file:
        if line[0] == 'f':
            line = line.rstrip()
            line = line.split('fold along ')[1].split('=')
            if line[0] == 'x':
                axes.append(0)
            else:
                axes.append(1)
            sizes.append(int(line[1]))
        elif line != '\n':
            line = line.rstrip()
            line = line.split(',')
            dots.append((int(line[0]), int(line[1])))

paper = np.zeros((sizes[0]*2+1, sizes[1]*2+1), dtype = np.bool)
for ind in dots:
    paper[ind] = True

### part 1:
print(np.count_nonzero(fold(paper, [axes[0]], [sizes[0]])))

## part 2:
paper = fold(paper, axes, sizes)
paper = np.swapaxes(paper, 0, 1)
plt.imshow(paper)
plt.show()
