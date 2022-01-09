# write by number int dari 0 - 559
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(559):
	value = randint(0,559)
	print(value)