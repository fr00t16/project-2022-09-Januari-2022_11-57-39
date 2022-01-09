# write by number int dari 0 - 833
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(833):
	value = randint(0,833)
	print(value)