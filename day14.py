import re
import time


filename = "input14.txt"
# filename = "day14_input_test.txt"

# sizeW = 11
# sizeH = 7

part1 = False


sizeW = 101
sizeH = 103

def find_group_robot(level):
	R = len(level)
	C = len(level[0])

def read_level(level):
	print("-------------")
	for i in range(len(level)):
		line = ''
		for j in range(len(level[0])):
			line += level[i][j]
		print(line)   
	print("-------------")

def fill_level(level, listR):
	for r in listR:
		level[r.pos[1]][r.pos[0]] = '*'

def clean_level(level):
	for i in range(len(level)):
		for j in range(len(level[0])):
			level[i][j] = ' '

bathroom = []
for j in range(sizeH):
	l = []
	for i in range(sizeW):
		l.append(' ')
	bathroom.append(l)


class Robot:
	def __init__(self, pos, speed, sizeW, sizeH):
		self.pos = pos
		self.speed = speed
		self.sizeH = sizeH
		self.sizeW = sizeW
	def __str__(self):
		return str(self.pos)+" -> "+str(self.speed)
	def walkOneSecond(self):
		newPosX = self.pos[0] + self.speed[0]
		if newPosX < 0:
			diffX = self.sizeW + newPosX
			newPosX = diffX
		if newPosX >= self.sizeW:
			diffX = newPosX - self.sizeW
			newPosX = diffX
		newPosY = self.pos[1] + self.speed[1]
		if newPosY < 0:
			diffY = self.sizeH + newPosY
			newPosY = diffY
		if newPosY >= self.sizeH:
			diffY = newPosY - self.sizeH
			newPosY = diffY
		self.pos = (newPosX, newPosY)

pattern = r"p=(-?\d+),(-?\d+)\s*v=(-?\d+),(-?\d+)"
robotList = []

with open(filename) as file:
	lines = file.readlines()
	for line in lines:
		match = re.search(pattern, line)
		if match:
		    p1 = int(match.group(1))
		    p2 = int(match.group(2))
		    v1 = int(match.group(3))
		    v2 = int(match.group(4))
		    robotList.append(Robot((p1, p2), (v1, v2), sizeW, sizeH))

# for r in robotList:
# 	print(r)
# 	r.walkOneSecond()
# 	print(r.pos)

read_level(bathroom)
fill_level(bathroom, robotList)
read_level(bathroom)
clean_level(bathroom)
read_level(bathroom)


# robot = Robot((2, 4), (2, -3), sizeW, sizeH)
# print(robot)
if part1:
	for i in range(100):
		for r in robotList:
			r.walkOneSecond()

		# print(robot.pos)

	quadranHL = 0
	quadranHR = 0
	quadranBL = 0
	quadranBR = 0

	columnMilieu = int(sizeW/2)
	lineMilieu = int(sizeH/2)

	print(columnMilieu)
	print(lineMilieu)

	for r in robotList:
		if r.pos[0] < columnMilieu and r.pos[1] < lineMilieu:
			quadranHL += 1
		if r.pos[0] > columnMilieu and r.pos[1] < lineMilieu:
			quadranHR += 1
		if r.pos[0] < columnMilieu and r.pos[1] > lineMilieu:
			quadranBL += 1
		if r.pos[0] > columnMilieu and r.pos[1] > lineMilieu:
			quadranBR += 1

	mulResult = quadranHL * quadranHR * quadranBL * quadranBR
	print(mulResult)
else:
	for i in range(7083):
		for r in robotList:
			r.walkOneSecond()
	fill_level(bathroom, robotList)
	read_level(bathroom)
	# numberOfSeconds = 1
	# while True:
	# 	print("Number of seconds: "+str(numberOfSeconds))
	# 	for r in robotList:
	# 		r.walkOneSecond()
	# 	fill_level(bathroom, robotList)
	# 	read_level(bathroom)
	# 	clean_level(bathroom)
	# 	numberOfSeconds += 1
	# 	time.sleep(1)	




