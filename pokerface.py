import random
import sys
random.seed(int(sys.argv[1]))
decision = 0
final_round=5
print "Chances of each player per round were:"


# Defining a deck of cards
#1-Spades, 2-Clubs, 3-Diamonds, 4- Hearts
# 1.1- Ace through 1.13-King, 1 - 10

deck_of_cards = [1,2,3,4]
temp_array=[]
t=0

for i in deck_of_cards:
	y=1
	while y<14:
		if y<10:
			t=i+0.1*y
			#print t
			temp_array.append(t)
			y=y+1	
		if y>10:
			t=i+0.01*y
			#print t
			temp_array.append(t)
			y=y+1	
		if y==10:
			y=y+1

#Append temp_array to deck_of_cards and shuffle

deck_of_cards.extend(temp_array)
random.shuffle(deck_of_cards)

#Alternate way of defining deck of cards
deck_of_cards_2 = []

from enum import Enum
class Suit(Enum):
	heart=1
	diamond=2
	spade=3
	club=4
	
class Value(Enum):
	Ace=1
	Two=2
	Three=3
	Four=4
	Five=5
	Six=6
	Seven=7
	Eight=8
	Nine=9
	Ten=10
	Jack=11
	Queen=12
	King=13		
		
for i in Suit:
	for j in Value:
		deck_of_cards_2.append((i,j))


random.shuffle(deck_of_cards_2)
test_deck=deck_of_cards_2
#print deck_of_cards_2

##################

#Dealing three cards to each player in the beginning

hand_player_1=[]
hand_player_2=[]

t=1
for i in deck_of_cards_2:
	hand_player_1.append(i)
	deck_of_cards_2.remove(i)
	t=t+1
	if(t>3):
		break
	else:
		continue
		
t=1
for i in deck_of_cards_2:
	hand_player_2.append(i)
	deck_of_cards_2.remove(i)
	t=t+1
	if(t>3):
		break
	else:
		continue

#Game flow
rounds=0

while rounds<5:

	player=1
	rounds=rounds+1
	
	while player<3:
		chance=random.random()
		# print player
		print chance
		if chance<0.5:
			decision = 1
			final_round=rounds
			loser = player
			break
		player = player + 1
		if decision == 0:
			loser = 0
			
	if decision ==1:
		break
		

print "Did the game end in a win (1)?"
print decision
print "The final round was:"
print final_round
print "The loser was:"
print loser
#print temp_array
print "Deck of cards is:"
print deck_of_cards
print "Alternate deck of cards is:"
print test_deck
print "Player 1's hand"
print hand_player_1
print "Player 2's hand"
print hand_player_2

