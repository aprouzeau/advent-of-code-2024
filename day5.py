filename = "input5.txt"
# filename = "day5_input_test.txt"


def checkOneRule(rule, updateList):
	number1 = rule[0]
	number2 = rule[1]
	# print(rule)
	# print(updateList)
	if number1 not in updateList or number2 not in updateList:
		return True
	else:
		if updateList.index(number1) < updateList.index(number2):
			return True
		else:
			return False 

def switch(rule, updateList):
	number1 = rule[0]
	number2 = rule[1]
	id1 = updateList.index(number1)
	id2 = updateList.index(number2)
	# tempoId = 0
	newList = updateList.copy()
	newList[id1] = updateList[id2]
	newList[id2] = updateList[id1]
	return newList

def checkAllRules(dico, updateList):
	listRuleToCheck = []
	for x in updateList:
		for t in dico[x]:
			if t not in listRuleToCheck:
				listRuleToCheck.append(t)
	# print(listRuleToCheck)
	correct = True
	for r in listRuleToCheck:
		if not checkOneRule(r, updateList):
			correct = False
	return correct


def checkAllRulesNumber(dico, updateList):
	listRuleToCheck = []
	RuleBreak = 0
	for x in updateList:
		for t in dico[x]:
			if t not in listRuleToCheck:
				listRuleToCheck.append(t)
	# print(listRuleToCheck)
	# correct = True
	for r in listRuleToCheck:
		if not checkOneRule(r, updateList):
			RuleBreak += 1
	return RuleBreak

def modifList(dico, updateList):
	listRuleToCheck = []
	RuleBreak = 0
	newUpdateList = updateList.copy()
	for x in updateList:
		for t in dico[x]:
			if t not in listRuleToCheck:
				listRuleToCheck.append(t)
	# print(listRuleToCheck)
	# correct = True
	for r in listRuleToCheck:
		if not checkOneRule(r, newUpdateList):
			newUpdateList = switch(r, newUpdateList)
	return newUpdateList

def star1(dico, listOfList):
	sumMiddle = 0
	for l in listOfList:
		if checkAllRules(dico, l):
			middleIndex = (len(l) - 1)/2
			sumMiddle += l[int(middleIndex)]
	return sumMiddle

# Start trying to permute number when rule is violated: works on example but fail on real input
def star2(dico, listOfList):
	sumMiddle = 0
	for l in listOfList:
		if not checkAllRules(dico, l):
			newl = modifList(dico, l)
			middleIndex = (len(newl) - 1)/2
			sumMiddle += newl[int(middleIndex)]
	return sumMiddle


def numberRuleBreakPerUpdate(dico, listOfList):
	for l in listOfList:
		numberBreak = checkAllRulesNumber(dico, l)
		if numberBreak > 0:
			print(numberBreak)


dictRule = {}
# listRule = []
listUpdate = []

with open(filename) as file:
	lines = file.readlines()
	for line in lines:
		if '|' in line:
			ruleStr = line.split('|')
			number1 = int(ruleStr[0])
			number2 = int(ruleStr[1])
			if number1 not in dictRule:
				dictRule[number1] = []
			if number2 not in dictRule:
				dictRule[number2] = []
			dictRule[number1].append((number1, number2))
			dictRule[number2].append((number1, number2))
			# listRule.append((int(ruleStr[0]), int(ruleStr[1])))
		elif ',' in line:
			updateStr = line.split(',')
			listUpdate.append([int(x) for x in updateStr])


print(star1(dictRule, listUpdate))
# numberRuleBreakPerUpdate(dictRule, listUpdate)


print(star2(dictRule, listUpdate))

# print(dictRule)
# print(listUpdate)

# checkAllRules(dictRule, listUpdate[0])

# print(listRule[0])
# print(listUpdate[0])

# print(checkOneRule(listRule[15], listUpdate[3]))
