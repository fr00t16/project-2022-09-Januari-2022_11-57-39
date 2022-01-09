# write by number int dari 0 - 554
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(554):
	value = randint(0,554)
	print(value)