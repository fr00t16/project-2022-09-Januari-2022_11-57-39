# write by number int dari 0 - 89
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(89):
	value = randint(0,89)
	print(value)