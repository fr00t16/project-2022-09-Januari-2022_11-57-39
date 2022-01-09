# write by number int dari 0 - 835
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(835):
	value = randint(0,835)
	print(value)