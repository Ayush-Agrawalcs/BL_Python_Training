import re
password="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%_-])[A-Za-z0-9@#$%_-]{8,20}$"
pa=input("Enter the password")
mt=re.match(password,pa)
print("yes" if mt else "No")