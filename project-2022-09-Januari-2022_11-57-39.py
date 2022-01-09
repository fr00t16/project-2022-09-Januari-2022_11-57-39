# write by number int dari 0 - 295
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(295):
	value = randint(0,295)
	print(value)