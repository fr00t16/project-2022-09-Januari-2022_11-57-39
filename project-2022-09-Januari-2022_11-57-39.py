# write by number int dari 0 - 440
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(440):
	value = randint(0,440)
	print(value)