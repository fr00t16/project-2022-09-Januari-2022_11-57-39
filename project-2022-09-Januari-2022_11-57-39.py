# write by number int dari 0 - 653
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(653):
	value = randint(0,653)
	print(value)