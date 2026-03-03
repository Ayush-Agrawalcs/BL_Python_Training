import random
n=int(input("Entern the no. of times you want to flip the coin:"))
head=0
tail=0
while(n>0):
    flip=random.randint(0,1)
    if(flip==1):
        head+=1
    else:
        tail+=1
    n-=1

heada=head*100/(head+tail)
taila=tail*100/(head+tail)
print("Number of winning heads:",heada,"%")
print("Number of winning tails:",taila)
