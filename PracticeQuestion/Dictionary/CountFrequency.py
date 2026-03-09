list=[1,1,2,3,4,1,2,3]
dict={}
for i in list:
    dict[i]=dict.get(i,0)+1
    

print(dict)