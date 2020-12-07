with open("./input", "r") as f:
	inp = f.read()
data1 = inp[::2]
data2 = inp[1::2]
result = set()


def move_dammit(data):
	x = 0
	y = 0
	result.add((x, y))
	for move in data:
		if move == '^':
			y += 1
		elif move == 'v':
			y -= 1
		elif move == '>':
			x += 1
		elif move == '<':
			x -= 1
		result.add((x, y))


move_dammit(data1)
move_dammit(data2)
print(len(result))
