import random # Random number guessing game. -Billy-


x = random.randint(1, 20) 

print "Guess a number between 1 and 20"

while True:
	y = int(raw_input("> "))

	if x == y:
		print "You Won!"
		exit()
	elif x > y:
		print "To Low"
	else:
		print "To high"
