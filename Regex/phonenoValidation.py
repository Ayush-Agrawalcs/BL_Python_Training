import re
phoneno=input("Enter the Phone no:")
mat=re.match("[0-9]{10}",phoneno)
if mat:
    print("Valid Phone no.")
else:
    print("It is not valid")