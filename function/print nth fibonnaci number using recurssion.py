def fibonnaci(n):
    a=0
    b=1
    if (n==1 ):
        return a
    elif (n==2):
        return b
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
n=int(input('enter position'))
print(fibonnaci(n))


 