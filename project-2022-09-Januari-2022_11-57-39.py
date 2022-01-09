# write by number int dari 0 - 598
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(598):
	value = randint(0,598)
	print(value)