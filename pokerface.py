import random
import sys
random.seed(int(sys.argv[1]))
rounds=0
decision = 0
final_round=5
print "Chances of each player per round were:"

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
