# write by number int dari 0 - 613
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(613):
	value = randint(0,613)
	print(value)