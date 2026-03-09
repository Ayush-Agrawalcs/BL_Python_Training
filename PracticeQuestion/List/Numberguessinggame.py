import random
k=random.randint(1,100)
count=1
while True:
    val=int(input("Choose value between 1 to 100 :"))
    if(val>k):
        print("Too high")
    elif(val<k):
        print("Too Low")
    else:
        print("Matched")
        break
    count+=1

print("Total no. of guess is",count)