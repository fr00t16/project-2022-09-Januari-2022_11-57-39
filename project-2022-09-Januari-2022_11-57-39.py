# write by number int dari 0 - 249
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(249):
	value = randint(0,249)
	print(value)