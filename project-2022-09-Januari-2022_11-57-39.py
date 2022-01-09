# write by number int dari 0 - 315
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(315):
	value = randint(0,315)
	print(value)