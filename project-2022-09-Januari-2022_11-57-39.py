# write by number int dari 0 - 625
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(625):
	value = randint(0,625)
	print(value)