n=int(input("Enter the value of n:"))
list=[]
for i in range (0,n+1):
    value=int(input("Enter the value:"))
    list.append(value)

duplicate=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if list[i]==list[j] not in duplicate:
            duplicate.append(list[i])

print(duplicate)
            

