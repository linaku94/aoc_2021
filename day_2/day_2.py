import time

def navigate(command, number, depth, horizontal):
    if command == 'forward':
        horizontal += number
    elif command == 'up':
        depth -= number
    elif command == 'down':
        depth += number
    return(depth, horizontal)


def navigate_2(command, number, aim, depth, horizontal):
    if command == 'forward':
        horizontal += number
        depth += aim*number
    elif command == 'up':
        aim -= number
    elif command == 'down':
        aim += number
    return(aim, depth, horizontal)

horizontal = 0
depth = 0
aim = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.rstrip()
        command = line.split(' ')[0]
        number = int(line.split(' ')[1])
        # depth, horizontal = navigate(command, number, depth, horizontal)
        aim, depth, horizontal = navigate_2(command, number, aim, depth, horizontal)
print(horizontal*depth)
