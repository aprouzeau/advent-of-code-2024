import numpy as np
from math import isclose
import re

def solveClawEq(xA, yA, xB, yB, xP, yP):
	a = np.array([[xA, xB],[yA,yB]])
	b = np.array([xP, yP])
	result = np.linalg.solve(a,b)
	det = xA*yB - xB*yA
	if det == 0:
		print("det nulle")
	return result

listEq = []

eq = []

filename = "input13.txt"
# filename = "day13_input_test.txt"
# filename = "aoc13.txt"


with open(filename) as file:
	lines = file.readlines()
	for line in lines:
		if "Button A" in line:
			# print("Button 1")
			eq = []
			matchX = re.search(r'X\+(\d+)', line)
			eq.append(int(matchX.group(1)))
			matchY = re.search(r'Y\+(\d+)', line)
			eq.append(int(matchY.group(1)))
		if "Button B" in line:
			matchX = re.search(r'X\+(\d+)', line)
			eq.append(int(matchX.group(1)))
			matchY = re.search(r'Y\+(\d+)', line)
			eq.append(int(matchY.group(1)))
		if "Prize" in line:
			matchX = re.search(r'X\=(\d+)', line)
			eq.append(int(matchX.group(1)))
			matchY = re.search(r'Y\=(\d+)', line)
			eq.append(int(matchY.group(1)))
			listEq.append(eq)

# print(listEq)
print(len(listEq))
sum = 0
# tolerance = 0.000000OOO1
for l in listEq:
	result = solveClawEq(l[0], l[1], l[2], l[3], l[4], l[5])
	# print(l)
	if isclose(result[0], int(result[0])) and isclose(result[1], int(result[1])):
		sum += result[0]*3 + result[1]
		# print("True")
	# else:
		# print("False")

print(sum)

		



# result1 = solveClawEq(94, 34, 22, 67, 8400, 5400)
# print(result1[0])
# print(result1[0].is_integer())
# print(result1[1])
# print(result1[1].is_integer())
# print(isclose(result1[1], int(result1[1])))

# result1 = solveClawEq(26, 66, 67, 21, 12748, 12176)

# print(result1[0])
# print(result1[0].is_integer())
# print(result1[1])
# print(result1[1].is_integer())
# print(isclose(result1[1], int(result1[1])))
# print(solveClawEq(17, 86, 84, 37, 7870, 6450))
# print(solveClawEq(69, 23, 27, 71, 18641, 10279))