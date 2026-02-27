a=int(input("Enter the starting number:"))
b=int(input("Enter the eding number: "))
countp=0
for i in range(a,b+1):
    count=0
    for j in range(2,i):
        if i%j==0:
            count=count+1
            break
    if count==0:
        print(i)
        countp=countp+1
print(countp)