# write by number int dari 0 - 606
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(606):
	value = randint(0,606)
	print(value)