# write by number int dari 0 - 959
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(959):
	value = randint(0,959)
	print(value)