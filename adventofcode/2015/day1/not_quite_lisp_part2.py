with open("./input", "r") as f:
	inp = f.read()

counter = 0
index = -1  # because index before entering
for ch in inp:
	print(counter)
	index += 1
	if counter < 0:
		break
	if ch == '(':
		counter += 1
	elif ch == ')':
		counter -= 1
print(index)
