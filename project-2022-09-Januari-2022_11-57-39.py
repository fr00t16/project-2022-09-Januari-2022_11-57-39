# write by number int dari 0 - 375
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(375):
	value = randint(0,375)
	print(value)