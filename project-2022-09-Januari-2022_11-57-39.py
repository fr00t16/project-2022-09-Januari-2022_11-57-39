# write by number int dari 0 - 975
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(975):
	value = randint(0,975)
	print(value)