n=int(input("Enter the value of n:"))
list=[]
for i in range (0,n+1):
    value=int(input("Enter the value:"))
    list.append(value)
even=0
odd=0
for i in list:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("Even no count.:",even)
print("Odd no. count :",odd)
