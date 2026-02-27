salary=int(input("Enter the salary: "))
late_days=int(input("Enter the number of late days: "))
absent_days=int(input("Enter the number of absent days:"))
sal=salary
if(late_days>5):
    sal=sal-(sal*5)/100
elif(late_days>10):
    sal=sal-(sal*10)/100
if(absent_days>2):
     sal=sal-(sal*5)/100

print("Final Salary:",sal)
