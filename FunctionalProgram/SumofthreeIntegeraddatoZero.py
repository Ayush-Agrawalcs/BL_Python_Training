n=int(input("Enter the input"))
arr=[]
for i in range(0,n+1):
    arr.append(int(input()))
count=0


def cubic_runningtime(arr):
    for i in range(0,n):
        for j in range(0,i+1):
            for k in range(0,j+1):
                if(arr[i]+arr[j]+arr[k]==0):
                    print(arr[i] ,arr[j] ,arr[k])
                    count+=1
print(count)

cubic_runningtime(arr)