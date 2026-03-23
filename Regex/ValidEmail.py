import re

email="^[a-zA-z0-9]+@[gmail]+\\.[com]+$"
k=input("Enter Email address")
mat=re.match(email,k)
if(mat):
    print("Valid Email")
else:
    print("Email. is not valid")