tu= (1,2,3,2,1,4,1)
dict={}
for i in tu:
    dict[i]=dict.get(i,0)+1

print(dict)