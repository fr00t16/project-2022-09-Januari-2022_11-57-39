# write by number int dari 0 - 444
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(444):
	value = randint(0,444)
	print(value)