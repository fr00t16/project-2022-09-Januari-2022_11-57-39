# write by number int dari 0 - 159
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(159):
	value = randint(0,159)
	print(value)