# write by number int dari 0 - 754
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(754):
	value = randint(0,754)
	print(value)