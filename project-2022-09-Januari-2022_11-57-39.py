# write by number int dari 0 - 51
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(51):
	value = randint(0,51)
	print(value)