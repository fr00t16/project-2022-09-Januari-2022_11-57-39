# write by number int dari 0 - 233
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(233):
	value = randint(0,233)
	print(value)