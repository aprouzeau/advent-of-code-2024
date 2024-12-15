

filename = "input8.txt"
# filename = "day8_input_test.txt"
# filename = "day8_input_test2"

part1 = False

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
    
    # Create a 2D array from the lines
    level = [list(line.strip()) for line in lines if line.strip()]
    
    return level

def computeCentralSym(x0, y0, x, y):
    x1 = (2*x0 - x)*i
    y1 = (2*y0 - y)*i

    return (x1, y1)


def computeCentralSym2(x0, y0, x, y, lenX, lenY):
    withinBound = True
    listResult = []
    i = 1
    while withinBound:
        # print(x0)
        # print(x)
        x1 = (i+1)*x0  - i*x
        y1 = (i+1)*y0  - i*y
        # print("Symetry of "+str(x)+" by "+str(x0)+" is "+str(x1))
        if x1 >= 0 and x1 < lenX and y1 >= 0 and y1 < lenY:
            listResult.append((x1, y1))
            # print("adding "+str((x1, y1)))
        else:
            withinBound = False
        i += 1

    return listResult

dictAntenna = {}
l = load_level(filename)
read_level(l)

for i in range(len(l)):
    for j in range(len(l[0])):
        if l[i][j] !='.':
            if not l[i][j] in dictAntenna:
                dictAntenna[l[i][j]] = []
            dictAntenna[l[i][j]].append((i, j))
# print(dictAntenna)

antinode = []

for key in dictAntenna:
    if len(dictAntenna[key]) > 1:
        antinode.extend(dictAntenna[key])
    for a in dictAntenna[key]:
        newList = dictAntenna[key].copy()
        # print(a)
        # print(newList)
        newList.remove(a)
        for element in newList:
            if part1:
                sym = computeCentralSym(a[0], a[1], element[0], element[1])
                if sym[0] >= 0 and sym[0]< len(l) and sym[1] >= 0 and sym[1] < len(l[0]):
                    antinode.append(sym)
            else:
                antinode.extend(computeCentralSym2(a[0], a[1], element[0], element[1], len(l), len(l[0])))

# print(antinode)
print(len(set(antinode)))



