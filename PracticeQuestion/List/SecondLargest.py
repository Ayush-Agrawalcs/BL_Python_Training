list1=[10,5,8,20,3,20,30]
a=set(list1)
list=list(a)
max=list[0]
max1=list[1]
for i in range(2,len(list)):
    if(list[i]>max):
        max1=max
        max=list[i]
    elif(list[i]>max1 and list[i]!=max1):
        max1=list[i]

print(max1)