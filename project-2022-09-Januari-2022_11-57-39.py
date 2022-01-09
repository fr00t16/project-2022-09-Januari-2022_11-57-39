# write by number int dari 0 - 111
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(111):
	value = randint(0,111)
	print(value)