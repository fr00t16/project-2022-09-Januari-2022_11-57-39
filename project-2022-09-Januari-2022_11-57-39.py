# write by number int dari 0 - 190
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(190):
	value = randint(0,190)
	print(value)