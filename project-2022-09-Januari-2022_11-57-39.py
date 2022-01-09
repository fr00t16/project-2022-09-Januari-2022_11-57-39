# write by number int dari 0 - 590
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(590):
	value = randint(0,590)
	print(value)