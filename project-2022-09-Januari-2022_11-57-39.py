# write by number int dari 0 - 29
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(29):
	value = randint(0,29)
	print(value)