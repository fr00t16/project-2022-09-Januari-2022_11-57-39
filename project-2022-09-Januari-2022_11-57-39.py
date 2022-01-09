# write by number int dari 0 - 576
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(576):
	value = randint(0,576)
	print(value)