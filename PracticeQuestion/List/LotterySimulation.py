import random
i=0
set=set()
while(i<6):
    lottery=random.randint(1,50)
    if(lottery not in set):
        set.add(lottery)
        i+=1

print(set)

