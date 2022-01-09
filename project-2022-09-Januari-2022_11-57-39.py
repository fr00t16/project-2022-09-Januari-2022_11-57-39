# write by number int dari 0 - 330
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(330):
	value = randint(0,330)
	print(value)