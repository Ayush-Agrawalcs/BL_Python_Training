n=int(input("Enter the number:"))
i=0
power=1
while(i<=n and n<31):
    print("2^", i, "=", power)
    power = power * 2
    i += 1