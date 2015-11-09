import random
import sys
random.seed(int(sys.argv[1]))
rounds=0
decision = 0
final_round=5
	

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


print decision
print final_round
print loser
