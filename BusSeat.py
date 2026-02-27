n=int(input("Enter th number :"))
k=40
while(n>0):
    p=int(input("Enter the passenger :"))
    k-=p
    if(k>=0):
        print("CONFIRMED")
    else:
        print("WAITLISTED")
        break
    n-=1