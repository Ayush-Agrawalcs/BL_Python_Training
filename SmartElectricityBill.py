unit=int(input("Enter the number of units :"))
sum=0
if(unit<=100):
    sum=100*3
elif(unit<=200):
    sum=100*3+(unit-100)*5
else:
    sum=100*3+100*5+(unit-200)*8

if(unit>300):
    sum=sum+(sum*10)/100
print(sum)