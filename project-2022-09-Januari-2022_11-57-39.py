# write by number int dari 0 - 279
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(279):
	value = randint(0,279)
	print(value)