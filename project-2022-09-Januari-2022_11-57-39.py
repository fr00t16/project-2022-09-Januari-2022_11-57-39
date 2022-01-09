# write by number int dari 0 - 721
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(721):
	value = randint(0,721)
	print(value)