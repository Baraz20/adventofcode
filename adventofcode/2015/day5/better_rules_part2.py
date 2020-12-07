import re

with open("./input", "r") as f:
	data = f.read()
data = data.split('\n')
data = [re.match(r".*([a-zA-Z])[a-zA-Z]\1.*", item) for item in data]
data = [item.group() for item in data if item is not None]
data = [re.match(r".*([a-zA-Z]{2}).*\1.*",item) for item in data]
data = [item.group() for item in data if item is not None]
print(len(data))