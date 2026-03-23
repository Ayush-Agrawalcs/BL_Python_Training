dict={
    "1":("Ayush", "HR",10000),
    "2":("Aman","Developer",200000),
    "3":("Ankur","Analyst",30000),
    "4":("an","qwer",60000)
}

for id,(name,role,sal) in dict.items():
    dict[id]=(name,role,sal+1000)

print(dict)
max=0
a=""
b=""
for id,(name,role,sal) in dict.items():
    if max < sal:
        max=sal
        a=name
        b=role


print(max,a,b)



