# write by number int dari 0 - 251
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(251):
	value = randint(0,251)
	print(value)