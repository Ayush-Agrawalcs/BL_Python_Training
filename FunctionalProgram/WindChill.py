import math
t=float(input("Enter the value x:"))
c=float(input("Enter the value of y:"))


def clacu_windchill(t,v):
    return 35.75 +0.6215*t+(0.4275-37.75)*math.pow(v,0.16)

wind=clacu_windchill(t,c)
print(wind)

