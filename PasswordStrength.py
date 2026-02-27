y=input("Enter the password :")
digit=False
upper=False
for char in y:
    if(char.isdigit()):
        digit=True
    elif(char.isupper()):
        upper=True

if(len(y)>=8 and upper and digit):
    print("Strong")
else:
    print("Weak")

