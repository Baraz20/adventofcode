import re

with open("./input", "r") as f:
	inp = f.read()
maths = re.findall(r"(\d+)x(\d+)x(\d+)", inp)
maths = [sorted(map(int, item)) for item in maths]
total = 0
for num in maths:
	total += 2 * (num[0] + num[1])
	total += num[0] *num[1] *num[2]
print(total)
