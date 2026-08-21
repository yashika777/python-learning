def duplicate(l):
    list=[]
    for i in l:
        if i not in list:
            list.append(i)
    return list
print(duplicate([1,2,45,9,2,89,7,45,1]))
