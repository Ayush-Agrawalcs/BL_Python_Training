n=int(input("Enter the number of rows::"))
m=int(input("Enter the number of columns:"))

arr=[]

for i in range(0,n):
    row=[]
    for j in range(0,m):
        value=int(input())
        row.append(value)
    arr.append(row)



def display(arr):
    for i in range(0,n):
        for j in range(0,m):
            print(arr[i][j],end=" ")
        print()
    print()


display(arr)