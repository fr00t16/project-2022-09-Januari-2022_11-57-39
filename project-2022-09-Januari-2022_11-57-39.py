# write by number int dari 0 - 555
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(555):
	value = randint(0,555)
	print(value)