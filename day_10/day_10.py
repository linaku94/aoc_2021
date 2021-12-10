import numpy as np

modes = {'(' : 'open',
        '[' : 'open',
        '{' : 'open',
        '<' : 'open',
        ')' : 'close',
        ']' : 'close',
        '}' : 'close',
        '>' : 'close'}

types = {'(' : 0,
        '[' : 1,
        '{' : 2,
        '<' : 3,
        ')' : 0,
        ']' : 1,
        '}' : 2,
        '>' : 3}

points = {'(' : 1,
        '[' : 2,
        '{' : 3,
        '<' : 4,
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137}

def check_line(line, modes, types, points):
    i = 0
    while True:
        if len(line) == 0 or i>=len(line)-1:
            # print('correct line')
            return 0, line
        
        elif modes[line[i]] != modes[line[i+1]]:
            if types[line[i]] == types[line[i+1]]:
                line = line.replace(line[i:i+2], '')
                i = 0
            else:
                # print('line corrupted')
                return points[line[i+1]], None

        else:
            i+=1

def complete_line(line, points):
    score = 0
    for i in range(1,len(line)+1):
        score*=5
        score+= points[line[-i]]
    return score

with open('input.txt', 'r') as file:
    lines = []
    for line in file:
        line = line.rstrip()
        lines.append(line)

score_1 = 0
score_2 = []
for line in lines:
    s, new_line = check_line(line, modes, types, points)
    score_1+=s
    if new_line is not None:
        score_2.append(complete_line(new_line, points))

print('first part ', score_1)
score_2 = int(np.median(score_2))
print('second part ', score_2)