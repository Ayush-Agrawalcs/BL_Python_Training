char=input("Enter the sentence :")
count=0
for j in char:
    if(j=='a' or j=='e' or j=='i' or j=='o' or j=='u' or j=='A' or j=='E' or j=='I' or j=='O' or j=='U'):
        count+=1
print(count)