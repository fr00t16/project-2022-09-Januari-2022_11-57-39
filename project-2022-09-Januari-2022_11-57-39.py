# write by number int dari 0 - 400
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(400):
	value = randint(0,400)
	print(value)