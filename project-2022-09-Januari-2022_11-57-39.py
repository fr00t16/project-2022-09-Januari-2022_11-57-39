# write by number int dari 0 - 139
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(139):
	value = randint(0,139)
	print(value)