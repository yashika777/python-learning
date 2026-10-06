l=[2,10,4,45,87,98,67,56,69,0,19]
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)    
            
