# write by number int dari 0 - 880
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(880):
	value = randint(0,880)
	print(value)