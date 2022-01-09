# write by number int dari 0 - 175
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(175):
	value = randint(0,175)
	print(value)