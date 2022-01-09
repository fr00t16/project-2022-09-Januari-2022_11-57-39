# write by number int dari 0 - 44
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(44):
	value = randint(0,44)
	print(value)