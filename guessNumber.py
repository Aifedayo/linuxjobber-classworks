from random import randint

guess = 0
var = randint(1,100)

while guess != var:
	guess = int(input("Guess a number from 1 to 100: "))
	
	