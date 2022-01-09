# write by number int dari 0 - 367
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(367):
	value = randint(0,367)
	print(value)