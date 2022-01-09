# write by number int dari 0 - 64
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(64):
	value = randint(0,64)
	print(value)