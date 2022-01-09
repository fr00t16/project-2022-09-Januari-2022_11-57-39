# write by number int dari 0 - 421
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(421):
	value = randint(0,421)
	print(value)