# write by number int dari 0 - 569
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(569):
	value = randint(0,569)
	print(value)