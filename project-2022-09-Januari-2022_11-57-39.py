# write by number int dari 0 - 97
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(97):
	value = randint(0,97)
	print(value)