# write by number int dari 0 - 379
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(379):
	value = randint(0,379)
	print(value)