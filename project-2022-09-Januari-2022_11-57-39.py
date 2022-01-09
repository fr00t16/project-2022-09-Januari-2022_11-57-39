# write by number int dari 0 - 499
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(499):
	value = randint(0,499)
	print(value)