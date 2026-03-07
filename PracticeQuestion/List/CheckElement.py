n=int(input("Enter the value of n:"))
list=[]
for i in range (0,n+1):
    value=int(input("Enter the value:"))
    list.append(value)

target=int(input("Enter the target value"))
for i in list:
    if(target==i):
        print(i)