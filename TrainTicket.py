fair=int(input("Distance :"))
age=int(input("Age :"))

dis=fair*2
if(age>60):
    dis=dis-(dis*0.3)
elif(age<12):
    dis=dis-(dis*0.5)

print(dis)