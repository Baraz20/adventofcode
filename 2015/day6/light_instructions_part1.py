import re

with open("./input", "r") as f:
	data = f.read()
instructions = re.findall(r"(.*) (\d+),(\d+) through (\d+),(\d+)", data)
rows, cols = (1000, 1000)
arr = [[0 for i in range(cols)] for j in range(rows)]


def turn_on(r0: int, c0: int, r1: int, c1: int):
	turn(r0, c0, r1, c1, True)


def turn_off(r0: int, c0: int, r1: int, c1: int):
	turn(r0, c0, r1, c1, False)


def turn(r0: int, c0: int, r1: int, c1: int, mode: bool):
	r0 = int(r0)  # I HATE THIS
	r1 = int(r1)
	c0 = int(c0)
	c1 = int(c1)
	for row in range(r0, r1 + 1):
		for col in range(c0, c1 + 1):
			arr[row][col] = int(mode)


def toggle(r0: int, c0: int, r1: int, c1: int):
	r0 = int(r0)  # I HATE THIS
	r1 = int(r1)
	c0 = int(c0)
	c1 = int(c1)
	for row in range(r0, r1 + 1):
		for col in range(c0, c1 + 1):
			arr[row][col] = int(not arr[row][col])


d = {"turn off": turn_off, "turn on": turn_on, "toggle": toggle}

for instruct in instructions:
	func = d[instruct[0]]
	r0 = instruct[1]
	c0 = instruct[2]
	r1 = instruct[3]
	c1 = instruct[4]
	# print(instruct[0],r0, c0, r1, c1)
	func(r0, c0, r1, c1)

counter = 0
for row in arr:
	for num in row:
		if num == 1:
			counter += 1
print(counter)
