import math
x=int(input("Enter the first value: "))
y=int(input("Enter the second value: "))

def calc_Euclidean(x,y):
    return math.sqrt(x*x + y*y)

sum=calc_Euclidean(x,y)
print("The distance is:",sum)


