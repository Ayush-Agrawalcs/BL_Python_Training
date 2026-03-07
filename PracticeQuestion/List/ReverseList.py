n=int(input("Enter the value of n:"))
list=[]
for i in range (0,n+1):
    value=int(input("Enter the value:"))
    list.append(value)

  #uning Built-in function
# list.reverse()
# print(list)

for i in range(0,len(list)-1):
    tem=list[i]
    list[i]=list[len(list)-1-i]
    list[len(list)-1-i]=tem

print(list)