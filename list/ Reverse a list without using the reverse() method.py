l=[10,20,30,40,5,67,89,19,28,18]
i=0
j=len(l)-1
while j>i:
    l[i],l[j]=l[j],l[i]
    i+=1
    j-=1
print(l)
    
