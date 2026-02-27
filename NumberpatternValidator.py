k=int(input("Enter the number"))
list=[]
while(k>0):
    list.append(k%10)
    k=k//10
flag=True
for i in list:
    for j in range (i,len(list)):
        if(list[i]<list[j]):
            flag=False
            break
    if(flag==False):
        break
print(flag)