n=int(input("Enter the value of n:"))
list=[]
for i in range (0,n+1):
    value=int(input("Enter the value:"))
    list.append(value)

min=list[0]
for i in range(0,len(list)):
    if(min>list[i]):
        min=list[i]

print(min)