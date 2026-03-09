list=[1,2,4,6]
list.sort()
se=set(list)
list1=[]
i=1
while i<max(se):
    if(i not in se):
        list1.append(i)
    i+=1

print(list1)
