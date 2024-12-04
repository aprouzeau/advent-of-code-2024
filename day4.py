from enum import Enum

filename = "input4.txt"
# filename = "day4_input_test.txt"

# Enum for directions
class Direction1(Enum):
    UP_RIGHT = (1, -1)
    DOWN_RIGHT = (1, 1)
    UP_LEFT = (-1, -1)
    DOWN_LEFT = (-1, 1)
    UP = (0, -1)
    DOWN = (0, 1)
    RIGHT = (1, 0)
    LEFT = (-1, 0)

# Enum for directions
class Direction2(Enum):
    UP_RIGHT = (1, -1)
    DOWN_RIGHT = (1, 1)
    UP_LEFT = (-1, -1)
    DOWN_LEFT = (-1, 1)



def load_level(file_path):
    with open(file_path, 'r') as file:
        # Read the file, strip newlines, and split into lines
        lines = file.readlines()
    
    # Create a 2D array from the lines
    level = [list(line.strip()) for line in lines if line.strip()]
    
    return level

def checkword1(ix, jx, level):
	nbXmas = 0
	for direction in Direction1:
		dx, dy = direction.value
		nx, ny = jx + dx, ix + dy
		n2x, n2y = jx + 2*dx, ix + 2*dy
		n3x, n3y = jx + 3*dx, ix + 3*dy
		if n3x >= 0 and n3x < len(level[0]) and n3y >= 0 and n3y < len(level):
			if level[ny][nx] == 'M' and level[n2y][n2x] == 'A' and level[n3y][n3x] == 'S':
				nbXmas += 1
	return nbXmas

def checkword2(ix, jx, level):
	nbXmas = 0
	isTrue = False
	for direction in Direction2:
		dx, dy = direction.value
		nx, ny = jx + dx, ix + dy
		n2x, n2y = jx + -1*dx, ix + dy
		n3x, n3y = jx + -1*dx, ix + -1*dy
		n4x, n4y = jx + dx, ix + -1*dy
		if ix > 0 and ix < len(level[0])-1 and jx > 0 and jx < len(level)-1:
			if level[ny][nx] == 'S' and level[n2y][n2x] == 'M' and level[n3y][n3x] == 'M' and level[n4y][n4x] == 'S':
				#nbXmas += 1
				isTrue = True
				# print(ix, jx)
			elif level[ny][nx] == 'S' and level[n2y][n2x] == 'S' and level[n3y][n3x] == 'M' and level[n4y][n4x] == 'M':
				isTrue = True
				# print(ix, jx)
	if isTrue:
		nbXmas = 1
	return nbXmas


def part1(level):
	countWord = 0
	for i in range(len(level)):
		line = ''
		for j in range(len(level[0])):
			line += level[i][j]
			nbWord = 0
			match level[i][j]:
				case 'X':
					nbWord = checkword1(i, j, level)
					countWord += nbWord
					#print('X')
				# case 'S':
				# 	nbWord = checkword(i, j, l, 'A', 'M', 'X')
				# 	countWord += nbWord
					#print('S')
	return countWord

def part2(level):
	countWord = 0
	for i in range(len(level)):
		line = ''
		for j in range(len(level[0])):
			line += level[i][j]
			nbWord = 0
			match level[i][j]:
				case 'A':
					nbWord = checkword2(i, j, level)
					countWord += nbWord
					#print('X')
				# case 'S':
				# 	nbWord = checkword(i, j, l, 'A', 'M', 'X')
				# 	countWord += nbWord
					#print('S')
	return countWord




l = load_level(filename)
countWord = 0
print(part1(l))
print(part2(l))
