import random

stake=int(input("Enter the stake:"))
goal=int(input("Enter the goal:"))
trial=int(input("Enter the trials: "))

total_wins = 0
total_bets = 0
for i in range(trial):
    cash=stake
    bet=0
    while cash>0 and cash<goal:
        bet+=1
        if random.random()<0.5:
            cash+=1
        else:
            cash-=1
    
    if cash == goal:
        total_wins += 1
    total_bets += bet

win=(total_wins/trial)*100
lose=100-win
average=total_bets/trial

print(f"Total wins: {total_wins}")
print(f"Win percentage: {win:.2f}%")
print(f"Loss percentage: {lose:.2f}%")
print(f"Average number of bets per trial: {average:.2f}")