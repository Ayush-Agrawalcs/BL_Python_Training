import random
n=int(input("Enter the no."))
dict={}
while n>0:
    k=random.randint(1,6)
    dict[k]=dict.get(k,0)+1
    n-=1

print(dict)