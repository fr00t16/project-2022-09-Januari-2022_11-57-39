# write by number int dari 0 - 665
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(665):
	value = randint(0,665)
	print(value)