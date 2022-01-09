# write by number int dari 0 - 179
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(179):
	value = randint(0,179)
	print(value)