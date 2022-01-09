# write by number int dari 0 - 254
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(254):
	value = randint(0,254)
	print(value)