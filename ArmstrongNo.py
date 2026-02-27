p=int(input("Enter the number:"))
k=p
count=0
while(k>0):
    count+=1
    k//=10

print(count)

k=p
sum=0
while(k>0):
    rem=k%10
    remp=rem**count         
    sum=sum+remp
    k//=10

print(sum)