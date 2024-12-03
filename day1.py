filename = "input1.txt"
# filename = "day1_input_test.txt"

list1 = []
list2 = []

part2 = True

with open(filename) as file:
    lines = file.readlines()
    for line in lines:
        line_str = line.rstrip('\n')
        x = line_str.split('   ')
        list1.append(int(x[0]))
        list2.append(int(x[1]))


if(not part2):
    list1.sort()
    list2.sort()

    sizeL = len(list1)

    # print(list1)
    # print(list2)

    dist = 0

    for i in range(sizeL):
        dist += abs(list1.pop(0) - list2.pop(0))

    print(dist)
else:
    dist = 0
    for n in list1:
        occ = list2.count(n)
        dist += n*occ
    print(dist)



