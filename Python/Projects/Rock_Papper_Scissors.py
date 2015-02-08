# Rock Papper Scissors Game -Billy-

import sys #  Imports the sys library.
import random # Imports the random libraries.


print "You have now entered a epic battle, your only weapons are Rock, Paper and Scissors!" 


def makeYourChoice(): # Tells the player what to input for each choice.
	print "Press R for Rock"
	print "Press P for Paper"       
	print "Press S for Scissors"	# Player's choices.
	print "Press Q to Quit"

	userChoice = raw_input("What do you want to choose?").lower() # Prompts the player to enter in a choice.

	if userChoice == "r": 
		return "Rock"

	if userChoice == "p":
		return "Paper"	
							# Player's choices.
	if userChoice == "s":
		return "Scissors"

	if userChoice == "q":
		sys.exit(0)

	else: # else kicks in if no choice is made
		makeYourChoice()

#print makeYourChoice()		


def computerRandom(): # This allows the computer to make its choice.
	options = ["Rock", "Paper", "Scissors"] # Computers need choices, too.
	randomChoice = random.randint (0,2) # This calls on the random library we set up on the top.
	return options [randomChoice] # RandomChoice randomly maps whats on the options list.


def comparison (humanChoice, computerChoice):

	if humanChoice == computerChoice:
		return "Draw"

	if humanChoice == "Rock" and computerChoice == "Paper":
		return "Computer Wins"

	if humanChoice == "Paper" and computerChoice == "Scissors":
		return "Computer Wins"

	if humanChoice == "Scissors" and computerChoice == "Rock":
		return "Computer Wins"
	else:
		return "Human Wins"
a = 0

while True:
	
	a += 1

	if a == 5:
		exit()

	humanChoice = makeYourChoice()
	computerChoice = computerRandom()

	print "You chose", humanChoice
	print "The computer chose", computerChoice

	result = comparison (humanChoice, computerChoice)

	if result == "Draw":
		print "It's a draw"

	elif result == "Computer Wins":
		print "Bahahah, you lost!"

	else: print "Yay! You won!"

	print " "
	
