correct=int(input("Corrected pin :"))
n=3
flag=False
while(n>0):
    attempt=int(input("Valid pin :"))
    if(correct==attempt):
        flag=True
        break
if(flag):
    print("ACCESS GRANTED")
else:
    print("Locked")