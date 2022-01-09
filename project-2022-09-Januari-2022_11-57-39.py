# write by number int dari 0 - 781
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(781):
	value = randint(0,781)
	print(value)