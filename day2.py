import math

filename = "input2.txt"
# filename = "day2_input_test.txt"

list1 = []

with open(filename) as file:
	lines = file.readlines()
	for line in lines:
		line_str = line.rstrip('\n')
		x = line_str.split(' ')
		listX = []
		for n in x:
			listX.append(int(n))
		list1.append(listX)

# print(list1)

nonSafe = 0
total = len(list1)
# total = -6
# print(math.copysign(1, total))

for l in list1:
	sign = math.copysign(1, l[1] -  l[0])
	previous = l[0]
	i = 1
	nonSafeBool = False
	firstLetGo = False
	# print(l)
	# print(sign)
	while i < len(l) and not nonSafeBool:
	# for i in range(1, len(l)):
		diff = l[i] - previous
		diffAbs = abs(l[i] - previous)
		diffSign = math.copysign(1, diff)
		# print(diffSign)
		if diffAbs == 0 or diffAbs > 3:
			if firstLetGo:
				nonSafe += 1
				nonSafeBool = True
			else:
				firstLetGo = True
			# print("problem diff")
		elif sign != diffSign:
			if firstLetGo:
				nonSafe += 1
				nonSafeBool = True
			else:
				firstLetGo = True
			# print("problem sign")
		if not firstLetGo:
			previous = l[i]
		i += 1



	#print(l)
safe = total - nonSafe
print(total)
print(safe)