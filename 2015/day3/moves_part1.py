with open("./input", "r") as f:
	inp = f.read()
x = 0
y = 0
result = set((x, y))
for move in inp:
	if move == '^':
		y += 1
	elif move == 'v':
		y -= 1
	elif move == '>':
		x += 1
	elif move == '<':
		x -= 1
	result.add((x, y))

print(result)
print(len(result) - 1)
