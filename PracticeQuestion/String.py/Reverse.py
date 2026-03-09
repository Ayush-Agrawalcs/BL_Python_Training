p="aaabbcc"
dict={}
for i in p:
    dict[i]=dict.get(i,0)+1

p=""
for k,v in dict.items():
    p+=k
    p+=str(v)

print(p)
