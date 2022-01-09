# write by number int dari 0 - 522
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(522):
	value = randint(0,522)
	print(value)