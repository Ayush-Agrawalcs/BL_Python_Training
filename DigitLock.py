n=int(input("Enput the number :"))
while(n>10):
    temp=n
    sum=0
    while(temp>0):
        rem=temp%10
        sum=sum+rem
        temp=temp//10
    n=n-sum
print(n)

