import math
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
c=int(input("Enter the value ofn c:"))

delta=y*y+4*x*c
if(delta>0):
    root1=(-y + math.sqrt(delta)/2*x)
    root2=(-y/math.sqrt(delta)/2*x)
    print("Root1:", root1)
    print("Root2:",root2)
elif (delta == 0):
    root = -b / (2 * a)
    print("Both roots are equal: " + root);
        
else: 
    print("Roots are imaginary (no real roots).")
        
