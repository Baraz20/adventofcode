import hashlib as hl
import re

with open("./input", "r") as f:
	key = f.read()

counter = 0
coin = ""
target = 5
while coin[0:target] != "0"*target:
	counter += 1
	new_key = key + str(counter)
	coin = hl.md5(new_key.encode()).hexdigest()
print(coin, key, counter)
