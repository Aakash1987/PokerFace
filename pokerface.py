#Pseudo Code for Poker Face v1

#Defining a deck of cards from 1.1 to 4.13 - Not needed for v1
##
##Deck_of_cards = [1,2,3,4]
##temp_array=[]
##y=1
##t=0
##for i in Deck_of_Cards
##	for y<14
##		t=i+0.1*y
##		temp_array.insert(0,t)
##		y=y+1
##		
###Append temp_array to deck_of_cards
##deck_of_cards.extend(temp_array)
##
###Shuffle the deck of cards - Not needed for v1
##random.shuffle(deck_of_cards)
##
###Deal two cards to each player
##player_1 = player_2=[]
##
##player_1 = random.sample(deck_of_cards,2)
##for x in player_1
##	deck_of_cards.remove(x)
##
##player_2 = random.sample(deck_of_cards,2)
##for x in player_2
##	deck_of_cards.remove(x)
##
###Define game structure
##
##rounds = 1
## 
##
##for rounds<5
##	{
##	chance = random.random() #selects a random number between 0 and 1 uniformly distributed
##	player=1
##	rounds=rounds+1
##	
##	for player<3
##		{
##		if player=1, 
##			{
##			player_1 = player_1 + random.sample(deck_of_cards,2)
##			for x in player_1
##				deck_of_cards.remove(x)
##			}
##		else if player = 2, 
##			{
##			player_2 = player_2 + random.sample(deck_of_cards,2)
##			for x in player_2
##				deck_of_cards.remove(x)
##			}
##		else 
##			print: "Error"
##			exit
##		
##		if chance<0.5
##			decision=0 
##		else 
##			decision=1 #Not using player hands at all in this version
##	
##		if decision=0
##			{
##			rounds=5, 
##			winner=player, 
##			player = 3
##			}
##			
##		player=player+1
##		}
##	}
##	
##
##Print: "Winner is player number"
##Print: winner
##Print: "Final hands are"
##Print player_1
##Print player_2
##
