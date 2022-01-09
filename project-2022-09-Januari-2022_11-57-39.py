# write by number int dari 0 - 849
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(849):
	value = randint(0,849)
	print(value)