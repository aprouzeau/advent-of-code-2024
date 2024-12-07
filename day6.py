from enum import Enum

# filename = "input6.txt"
filename = "day6_input_test.txt"

# Enum for directions
class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    RIGHT = (1, 0)
    LEFT = (-1, 0)

class Guard:
    def __init__(self, pos, orientation, level):
        self.pos = pos
        self.orientation = orientation
        self.inMap = True
        self.map = level
        self.map[pos[1]][pos[0]] = 'x'
        self.obstPos = []
        self.fullWalk = []
        self.fullWalk.append(((pos[0], pos[1]), self.getChar()))

    def walkStraight(self, level):
        canWalk = True
        LeaveMap = False
        while canWalk:
            dx, dy = self.orientation.value
            nx, ny = self.pos[0] + dx, self.pos[1] + dy
            if nx >= 0 and nx < len(level[0]) and ny >= 0 and ny < len(level):
                if level[ny][nx] == '#':
                    canWalk = False
                else:
                    # if self.map[ny][nx] == 'x':
                    if True:
                        # print("Been there")
                        # print((nx, ny))
                        orienTempo = self.orientation
                        self.turnRight()
                        dax, day = self.orientation.value
                        notBlocked = True
                        notLoop = True
                        leftMap = False
                        nax, nay = nx, ny
                        while notLoop:
                            if nax+dax >= 0 and nax+dax< len(level[0]) and nay+day>= 0 and nay+day< len(level):
                                if level[nay+day][nax+dax] == '#':
                                    self.turnRight()
                                    notBlocked = False
                                else:
                                    dax, day = self.orientation.value
                                    nax, nay = nax + dax, nay + day
                                    test = ((nax, nay), self.getChar())
                                    if test in self.fullWalk:
                                        notLoop = False
                            else:
                                leftMap = True
                                notBlocked = False
                                notLoop = False
                        if not leftMap:
                            # if self.map[nay][nax] == self.getChar():
                            test = ((nax, nay), self.getChar())
                            if test in self.fullWalk:
                                # print("Been there already")
                                self.obstPos.append((nx+dx, ny+dy))
                        self.orientation = orienTempo
                    self.map[ny][nx] = self.getChar()
                    self.fullWalk.append(((nx, ny), self.getChar()))
                    self.pos = (nx, ny)
            else:
                LeaveMap = True
                canWalk = False
        if LeaveMap:
            self.inMap = False
    def turnRight(self):
        newOrien = Direction.UP
        match self.orientation:
            case Direction.UP:
                newOrien = Direction.RIGHT
            case Direction.RIGHT:
                newOrien = Direction.DOWN
            case Direction.DOWN:
                newOrien = Direction.LEFT
            case Direction.LEFT:
                newOrien = Direction.UP
        self.orientation = newOrien

    def getChar(self):
        match self.orientation:
            case Direction.UP:
                return '^'
            case Direction.RIGHT:
                return '>'
            case Direction.DOWN:
                return 'v'
            case Direction.LEFT:
                return '<'

    def walkUntilLeave(self, level):
        countIt = 0
        while self.inMap:
            self.walkStraight(level)
            self.turnRight()
            # print(countIt)
            countIt += 1
        countX = 0
        for i in range(len(level)):
            countX += level[i].count('x')
        return countX




def load_level(file_path):
    with open(file_path, 'r') as file:
        # Read the file, strip newlines, and split into lines
        lines = file.readlines()
    
    # Create a 2D array from the lines
    level = [list(line.strip()) for line in lines if line.strip()]
    
    return level

def read_level(level):
    for i in range(len(level)):
        line = ''
        for j in range(len(level[0])):
            line += level[i][j]
        print(line)

def createGuard(level):
    pos = (0, 0)
    orientation = Direction.UP
    for i in range(len(level)):
        for j in range(len(level[0])):
            if level[i][j] == '^':
                pos = (j, i)
    g = Guard(pos, orientation, level)
    return g


l = load_level(filename)
# read_level(l)
guard =  createGuard(l)
# print(guard.pos)
# print(guard.orientation)
# read_level(guard.map)



# print(guard.walkUntilLeave(l))

guard.walkStraight(l)
guard.turnRight()
read_level(guard.map)
print(guard.obstPos)

# guard.walkStraight(l)
# guard.turnRight()
# read_level(guard.map)
# print(guard.obstPos)

# guard.walkStraight(l)
# guard.turnRight()
# read_level(guard.map)

# print(guard.obstPos)

# guard.walkStraight(l)
# guard.turnRight()
# read_level(guard.map)

print(guard.obstPos)
print(len(set(guard.obstPos)))
print(guard.fullWalk)
# print(guard.pos)
# print(guard.orientation)
# read_level(guard.map)
