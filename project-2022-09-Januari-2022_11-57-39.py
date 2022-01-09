# write by number int dari 0 - 260
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(260):
	value = randint(0,260)
	print(value)