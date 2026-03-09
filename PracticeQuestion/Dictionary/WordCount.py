sentence = "python is easy python is powerful"
word=sentence.split()
dict={}
for i in word:
    dict[i]=dict.get(i,0)+1

print(dict)