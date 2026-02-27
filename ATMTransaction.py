x=int(input("Enter the amount to withdraw:"))
n=int(input("Enter the number of account:"))
balance=x
while(n!=0):
    y=int(input("Enter your amount:"))
    if(y%100==0 and y<balance):
        balance-=y
        print("Success")
    else:
        print("Failed")
    n-=1
print(balance)