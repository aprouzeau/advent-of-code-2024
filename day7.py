from itertools import product
import time

filename = "input7.txt"
# filename = "day7_input_test.txt"

class Equation:
	def __init__(self, result, listNumber):
		self.result = result
		self.listNumber = listNumber
		self.numberSign = len(listNumber) - 1
		self.combi = [''.join(combination) for combination in product(['+', '*', '|'], repeat=self.numberSign)]
	# def print(self):
	# 	print('Equation')
	# 	print(self.result)
	# 	print(self.listNumber)
	def __str__(self):
		return str(self.result)+' : '+str(self.listNumber)+'->'+str(self.combi)
	def testEq(self):
		foundOneTrue = False
		for c in self.combi:
			cl = list(c)
			# evalStr = str(self.listNumber[0])
			evalInt = self.listNumber[0]
			for i in range(len(cl)):
				match cl[i]:
					case '+':
						evalInt += self.listNumber[i+1]
					case '*':
						evalInt *= self.listNumber[i+1]
					case '|':
						evalStr = str(evalInt) + str(self.listNumber[i+1])
						evalInt = int(evalStr)
				# evalStr += cl[i] + str(self.listNumber[i+1])
			# resultEq = eval(evalStr)
			if evalInt == self.result:
				foundOneTrue = True
		return foundOneTrue



def readInput(filename):
	listEquation = []
	with open(filename) as file:
		lines = file.readlines()
		for line in lines:
			xs = line.split(':')
			result = int(xs[0])
			rest = xs[1].strip()
			elementsStr = rest.split(' ')
			element = [int(item) for item in elementsStr]
			eq = Equation(result, element)
			# print(eq)
			listEquation.append(eq)
	return listEquation

listEq = readInput(filename)
sumTrue = 0
start = time.time()
for eq in listEq:
	if eq.testEq():
		# print(eq)
		sumTrue += eq.result
end = time.time()

print(sumTrue)

print("Time: "+str(end-start))

