def gcd(n,m):
    s=set()
    for i in range(1,n):
        if n%i==0:
            s.add(i)
    l=set()
    for j in range(1,m):
        if m%j==0:
            l.add(j)
    common=l&s
    greatest=0
    for k in common:
        if k>greatest:
            greatest=k
    return greatest
print(gcd(12,16))



            
