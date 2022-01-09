# write by number int dari 0 - 101
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(101):
	value = randint(0,101)
	print(value)