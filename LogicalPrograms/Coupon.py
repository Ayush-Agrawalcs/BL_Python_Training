import random

n = int(input("Enter the n distinct integer: "))
set = set()  # Using your variable name
count = 0

def coupon(n, count):
    global set  # refer to the outer 'set'
    while count < n:
        k = random.randint(1, 1000)
        if k in set:
            print("Duplicate found:", k)
            count += 1
        else:
            set.add(k)
            
    return count

count = coupon(n, count)
print("No duplicates found. Total unique numbers:", len(set))
print("duplicate numbers:", count)