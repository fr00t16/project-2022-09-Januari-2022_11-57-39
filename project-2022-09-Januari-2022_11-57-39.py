# write by number int dari 0 - 137
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(137):
	value = randint(0,137)
	print(value)