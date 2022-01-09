# write by number int dari 0 - 323
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(323):
	value = randint(0,323)
	print(value)