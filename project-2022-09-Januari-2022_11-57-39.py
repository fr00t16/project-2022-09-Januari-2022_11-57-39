# write by number int dari 0 - 419
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(419):
	value = randint(0,419)
	print(value)