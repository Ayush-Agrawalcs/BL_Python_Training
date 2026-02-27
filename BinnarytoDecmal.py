n=input("Enter a binary number: ")
decimal=0
power=0
for digit in n[::-1]:
    decimal+=int(digit)*2**power
    power+=1
print("The decimal equivalent of", n, "is", decimal)