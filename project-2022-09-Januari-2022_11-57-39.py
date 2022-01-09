# write by number int dari 0 - 161
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(161):
	value = randint(0,161)
	print(value)