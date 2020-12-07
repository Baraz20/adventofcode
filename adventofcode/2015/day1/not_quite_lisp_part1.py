with open("./input", "r") as f:
	inp = f.read()
counter: int = 0
for ch in inp:
	if ch == "(":
		counter += 1
	elif ch == ")":     # could have used else
		counter -= 1

print(counter)
