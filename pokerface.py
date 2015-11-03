import random
import sys
random.seed(int(sys.argv[1]))
rounds=1
decision = 0
while rounds<5:
	rounds=rounds+1
	chance=random.random()
	if chance<0.5:
		decision = 1
		final_round=rounds
		break

print decision
