import re


def readRegex(stxt):
	x = re.findall("mul\(\d{1,3},\d{1,3}\)", stxt)
	# print(x)
	sumX = 0
	for s in x:
		ns = re.findall("\d{1,3}", s)
		mulx = 1
		for n in ns:
			mulx *= int(n)
		sumX += mulx
	return sumX


filename = "input3.txt"
# filename = "day_3_input_test.txt"

sumTotal = 0

# txt = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
txt = ""
with open(filename) as file:
	txt = file.read()

partDont = txt.split("don't")
print(partDont)

sumTotal += readRegex(partDont[0])

for i in range(1,len(partDont)):
	parts = partDont[i].split("do")
	for j in range(1, len(parts)):
		sumTotal += readRegex(parts[j])

print(sumTotal)