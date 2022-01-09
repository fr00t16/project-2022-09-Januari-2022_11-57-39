# write by number int dari 0 - 768
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(768):
	value = randint(0,768)
	print(value)