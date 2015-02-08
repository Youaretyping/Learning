# Billy's Random Deck Database 
import random

suits = random.choice(('Clubs', 'Diamonds', 'Hearts', 'Spades'))
ranks = random.choice(('2', '3', '4', '5', '6', '7', '8', '9', 
							 'Jacks', 'Queens', 'Kings', 'Ace'))

print "%s of %s" % (ranks, suits)

