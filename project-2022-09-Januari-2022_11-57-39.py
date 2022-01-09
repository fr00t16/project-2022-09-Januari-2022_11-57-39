# write by number int dari 0 - 110
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(110):
	value = randint(0,110)
	print(value)