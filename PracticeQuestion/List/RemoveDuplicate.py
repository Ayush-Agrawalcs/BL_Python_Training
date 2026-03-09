import random
p1=0
p2=0
count=0
def add(p,k):
    p+=k
    if(p>100):
        p=100
    return p

def subtract(p,k):
    p-=k
    if(p<0):
        p=0
    return p

while p1<100 and p2<100:
    k=random.randint(1,6)
    l=random.randint(1,3) 
    if l==2:
        if count%2==0:
            p1=add(p1,k)
        else:
            p2=add(p2,k)
    if l==3:
        if count%2==0:
            p1=subtract(p1,k)
        else:
            p2=subtract(p2,k)
        
    count+=1

    
if(p1==100):
    print("player1 wins")
else:
    print("player2 wins")

print("tottla dice roll",count)