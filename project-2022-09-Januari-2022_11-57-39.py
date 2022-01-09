# write by number int dari 0 - 867
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(867):
	value = randint(0,867)
	print(value)