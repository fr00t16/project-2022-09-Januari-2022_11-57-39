# write by number int dari 0 - 31
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(31):
	value = randint(0,31)
	print(value)