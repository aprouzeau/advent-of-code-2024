from enum import Enum


# Enum for directions
class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)

filename = "input15.txt"
# filename = "day15_input_test.txt"
# filename = "day15_input_test2.txt"

part1 = True

def read_level(level):
    print("-------------")
    for i in range(len(level)):
        line = ''
        for j in range(len(level[0])):
            line += level[i][j]
        print(line)   
    print("-------------")

def load_level(file_path):
    with open(file_path, 'r') as file:
        # Read the file, strip newlines, and split into lines
        lines = file.readlines()
    game = {}
    level = []
    command = []
    positionRobot = (0, 0)
    # Create a 2D array from the lines
    count_i = 0
    for line in lines:
        if line[0] == '#':
            level.append(list(line.strip()))
            if '@' in line:
                position_j = line.rfind('@')
                positionRobot = (count_i, position_j)
                # print("Found the robot: "+str(position_j)+" - "+str(count_i))
        else:
            command.extend(list(line.strip()))
        count_i += 1
    # level = [list(line.strip()) for line in lines if line.strip()]
    game['level'] = level
    game['command'] = command
    game['positionRobot'] = positionRobot
    return game

def check_move(game, position, direction):
    di, dj = direction.value
    ni, nj = position[0] + di, position[1] + dj
    if game['level'][ni][nj] == '#':
        return False
    elif game['level'][ni][nj] == '.':
        game['level'][ni][nj] = game['level'][position[0]][position[1]]
        game['level'][position[0]][position[1]] = '.'
        if game['level'][ni][nj] == '@':
            game['positionRobot'] = (ni, nj)
        return True
    elif game['level'][ni][nj] == 'O':
        if check_move(game, (ni, nj), direction):
            game['level'][ni][nj] = game['level'][position[0]][position[1]]
            game['level'][position[0]][position[1]] = '.'
            if game['level'][ni][nj] == '@':
                game['positionRobot'] = (ni, nj)
            return True
        else:
            return False

def getDir(com):
    match com:
        case '^':
            return Direction.UP
        case '>':
            return Direction.RIGHT
        case 'v':
            return Direction.DOWN
        case '<':
            return Direction.LEFT

def countPoint(level):
    sumPoint = 0
    for i in range(len(level)):
        for j in range(len(level[0])):
            if level[i][j] == 'O':
                sumPoint += i*100 + j
    return sumPoint




g = load_level(filename)
read_level(g['level'])
# print(check_move(g, (1, 4), Direction.DOWN))
# read_level(g['level'])
for c in g['command']:
    # print(g['positionRobot'])
    check_move(g, g['positionRobot'], getDir(c))
    # print(c)
    # read_level(g['level'])
print(countPoint(g['level']))
