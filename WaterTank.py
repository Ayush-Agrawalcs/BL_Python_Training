n=int(input("Enter the digit:"))
balance=1000
count=0
while(n>0):
    inflow=int(input("Enter the inflow:"))
    if(balance>0):
        balance-=inflow
        count+=1
    n-=1
print(count)