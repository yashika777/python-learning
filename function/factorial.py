def fact(n):
    j=1
    for i in range(1,n+1):
        j*=i
    return j
enter=int(input('enter value:'))
print(fact(enter))
