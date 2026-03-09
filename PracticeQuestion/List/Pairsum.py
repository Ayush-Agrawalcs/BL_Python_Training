List = [1,4,5,3,2]
Target = 6
for i in range(0,len(List)):
    for j in range(i+1,len(List)):
        if(List[i]+List[j]==Target):
            print(List[i],List[j])