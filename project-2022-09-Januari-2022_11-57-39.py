# write by number int dari 0 - 82
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(82):
	value = randint(0,82)
	print(value)