# write by number int dari 0 - 504
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(504):
	value = randint(0,504)
	print(value)