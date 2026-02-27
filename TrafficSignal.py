z=int(input("Enter a Time"))
z=z%90
if(z<=30):
    print("Red")
elif(z>30 and z<=45):
    print("Yellow")
else:
    print("Green")