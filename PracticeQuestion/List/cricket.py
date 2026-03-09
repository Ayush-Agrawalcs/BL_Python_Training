import random

def toss():
    l=random.randint(0,1)
    return l

p1=0
p2=0
k=toss()
for i in range(0,7):
    p1+=random.randint(0,6)

for i in range(0,7):
    p2+=random.randint(0,6)

if(p1>p2):
    print("player1 win")
elif p1==p2:
    print("Match draw")
else:
    print("player2 win")

