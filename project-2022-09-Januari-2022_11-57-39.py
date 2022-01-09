# write by number int dari 0 - 524
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(524):
	value = randint(0,524)
	print(value)