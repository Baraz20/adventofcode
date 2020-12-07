import re
import itertools as iter

with open("./input", "r") as f:
	inp = f.read()
maths = re.findall(r"(\d+)x(\d+)x(\d+)", inp)
maths = [tuple(map(int, item)) for item in maths]
print(maths)
c_maths = [tuple(iter.combinations(item, 2)) for item in maths]
print(c_maths)
total = 0

for item in c_maths:
	minn = item[0][0] * item[0][1]
	for num in item:
		summ = num[0] * num[1]
		if summ < minn:
			minn = summ
		total += summ*2
	total += minn


print(total)
