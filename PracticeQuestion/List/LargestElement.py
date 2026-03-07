n=int(input("Enter the value of n:"))
list=[]
for i in range(0,n):
    value=int(input("Enter the value:"))
    list.append(value)

max=list[0]
for i in range(0,len(list)):
    if(list[i]>max):
        max=list[i]

print(max)