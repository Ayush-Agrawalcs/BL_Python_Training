amount=int(input("Enter the amount:"))
discount=0
if amount>=5000:
    discount=amount-amount*0.20
elif amount>=3000:
    discount=amount-amount*0.10
elif amount>=1000:
    discount=amount-amount*0.05
else:    
    discount=amount

print(discount)