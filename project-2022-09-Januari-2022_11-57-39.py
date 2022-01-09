# write by number int dari 0 - 461
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(461):
	value = randint(0,461)
	print(value)