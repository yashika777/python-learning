def duplicate(l):
    i=0
    while i<len(l):
        j=i+1
        while j<len(l):
            if l[i]==l[j]:
                l.pop(j)
            else:
                j+=1
        i+=1
    return l
print(duplicate([1,2,45,9,2,89,7,45,1]))
