# write by number int dari 0 - 129
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(129):
	value = randint(0,129)
	print(value)