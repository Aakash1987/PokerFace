#Pseudo Code for Poker Face v1

#Defining a deck of cards from 1.1 to 4.13 - Not needed for v1

Deck_of_cards = [1,2,3,4]
temp_array=[]
y=1
t=0
for i in Deck_of_Cards
	for y<14
		t=i+0.1*y
		Add t to temp_array
		y=y+1
		
Append temp_array to deck_of_cards

#Shuffle the deck of cards - Not needed for v1
random.shuffle(deck_of_cards)


#Define game structure

rounds = 1
chance = random.random()

for rounds<5
	{
	player=1
	rounds=rounds+1
	
	for player<3
		{
		if chance<0.5, decision=0 else decision=1
	
		if decision=0, then {rounds=5, winner=player, player = 3}
		else continue
		player=player+1
		}
	}
	

Print: Winner is player number
Print: winner