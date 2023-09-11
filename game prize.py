from numpy import random
import numpy as np
ar1=np.array ([12,13,88,100])
computer=random.choice(ar1)
print(ar1)
print("CHOOSE ANY LUCKY NUMBER TO WIN PRIZE")
player=int(input())
if(player==computer):
    print("LUCKY NUMBER",computer)
    print("YOUR CHOOSEN NUMBER",player)
    print("WOW,YOU WONE THE BUMPER PRIZE")
else:
    print("LUCKY NUMBER",computer)
    print("YOUR CHOOSEN NUMBER",player)
    print("YOU ARE LOST THE GAME TRY NEXT TIME")
    
