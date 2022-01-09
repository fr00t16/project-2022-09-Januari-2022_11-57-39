# write by number int dari 0 - 506
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(506):
	value = randint(0,506)
	print(value)