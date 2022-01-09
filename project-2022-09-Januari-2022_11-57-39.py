# write by number int dari 0 - 889
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(889):
	value = randint(0,889)
	print(value)