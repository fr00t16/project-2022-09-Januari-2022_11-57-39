# write by number int dari 0 - 489
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(489):
	value = randint(0,489)
	print(value)