# write by number int dari 0 - 885
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(885):
	value = randint(0,885)
	print(value)