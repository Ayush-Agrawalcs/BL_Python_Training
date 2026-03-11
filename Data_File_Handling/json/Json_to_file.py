import json
student={
    "name": "Ayush55",
    "age": 22,
    "city": "Delhi",
    "education": {
        "degree": "B.Tech",
        "major": "Computer Science",
        "university": "XYZ University"
    },
}

try:
    data=json.load(open('dt.json','r'))
except:
    data=[]
data.append(student)
json.dump(data,open('dt.json','w'))

print(data)

k='''hello world
welcome to python programming'''

with open("kk.txt","w") as f:
    f.writelines(k)

