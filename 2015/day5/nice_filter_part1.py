import re

with open("./input", "r") as f:
	lst = f.read()
lst = lst.split('\n')
lst = [re.match(r"(.*[aeiou]){3,}.*", item) for item in lst]    # at least 3 vowels
lst = [item.group() for item in lst if item is not None]
lst = [re.match(r".*(.)\1{1,}.*", item) for item in lst]        # contains 2 repeating
lst = [item.group() for item in lst if item is not None]
blacklist = ["ab", "cd", "pq", "xy"]                            # blacklist
result = []
for item in lst:
	for black in blacklist:
		if black in item:
			break
	else:
		result.append(item)
print(result)
print(len(result))