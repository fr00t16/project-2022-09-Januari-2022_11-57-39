# write by number int dari 0 - 9
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(9):
	value = randint(0,9)
	print(value)