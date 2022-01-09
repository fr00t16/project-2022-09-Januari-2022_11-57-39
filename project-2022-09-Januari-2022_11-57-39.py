# write by number int dari 0 - 615
# for test apps form this project 
from random import seed
from random import randint
seed(1)
for _ in range(615):
	value = randint(0,615)
	print(value)