import math

def check_safeness(listToCheck, verbose):
	sign = math.copysign(1, listToCheck[1] -  listToCheck[0])
	previous = listToCheck[0]
	i = 1
	nonSafeBool = False
	if verbose:
		print(listToCheck)
	# print(sign)
	while i < len(listToCheck) and not nonSafeBool:
	# for i in range(1, len(l)):
		diff = listToCheck[i] - previous
		diffAbs = abs(listToCheck[i] - previous)
		diffSign = math.copysign(1, diff)
		# print(diffSign)
		if diffAbs == 0 or diffAbs > 3:
			# nonSafe += 1
			nonSafeBool = True
			if verbose:
				print("problem diff")
		elif sign != diffSign:
			# nonSafe += 1
			nonSafeBool = True
			if verbose:
				print("problem sign")
		previous = listToCheck[i]
		i += 1
	return nonSafeBool

filename = "input2.txt"
# filename = "day2_input_test.txt"
# filename = "day2_input_test_small"

list1 = []
verbose = True

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
safe = 0
# total = -6
# print(math.copysign(1, total))

for l in list1:
	nonSafeBool = check_safeness(l, verbose)
	# print(l)
	if not nonSafeBool:
		safe += 1
	if nonSafeBool:
		#print("Not Safe")
		countSafe = 0
		# nonSafe += 1
		for j in range(len(l)):
			if verbose:
				print(j)
			l2 = l.copy()
			l2.pop(j)
			nonSafeTempo = check_safeness(l2, verbose)
			if not nonSafeTempo:
				countSafe += 1
		if countSafe > 0:
			safe += 1




	#print(l)
# safe = total - nonSafe
print(total)
print(safe)