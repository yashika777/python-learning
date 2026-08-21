def second_largest(l):
    largest=0
    secondlargest=0
    for i in l:
        if i>largest:
            secondlargest=largest
            largest=i
        if (i!=largest and i>secondlargest):
            secondlargest=i
    print(largest)
    print(secondlargest)
second_largest([10,80,79,567,2345,77542,8776543,456,46,887])