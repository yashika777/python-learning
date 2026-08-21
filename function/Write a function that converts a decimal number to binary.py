def binary(n):
    l=[]
    while n>0:
        l.append(n%2)
        n=n//2
    reverse=[]
    for i in l[::-1]:
        reverse.append(i)
    print(reverse)
binary(10)
    