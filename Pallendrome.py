p=int(input("Enter the pallendrome :"))
k=p
sum=0
while(k>0):
    rem=k%10
    sum=sum*10+rem
    k=k//10
print(sum)
if(sum==p):
    print("PALINDROME")
else:
    print("Not PALINDROME")