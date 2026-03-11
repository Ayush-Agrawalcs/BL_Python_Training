k=['''hello world
welcome to python programming \n''',
"hello\n","kk"]

with open("kk.txt","w") as f:
    f.writelines(k)

with open("kk.txt","r") as f:
    data=f.read()
    print(data)


with open("kk.txt","r") as f:
    data=f.readline()
    print(data)