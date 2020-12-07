import re

with open("./input", "r") as f:
	data = f.read()

lights = [[False] * 1000] * 1000


def turn_on(start_x, start_y, end_x, end_y):
	global lights
	for i in range(start_x, end_x + 1):
		for j in range(start_y, end_y + 1):
			lights[i][j] = True


def turn_off(start_x, start_y, end_x, end_y):
	global lights
	for i in range(start_x, end_x + 1):
		for j in range(start_y, end_y + 1):
			lights[i][j] = False


def toggle(start_x, start_y, end_x, end_y):
	global lights
	for i in range(start_x, end_x + 1):
		for j in range(start_y, end_y + 1):
			lights[i][j] = not lights[i][j]


instructions = {'turn on': turn_on, 'turn off': turn_off, 'toggle': toggle}

for instruction in re.findall(r'(.*) (\d+),(\d+) through (\d+),(\d+)', data):
	coords = [int(x) for x in list(instruction)[1:]]
	instructions[instruction[0]](*coords)

c = 0
for line in lights:
	for i in line:
		if i:
			c += 1

print(c)
